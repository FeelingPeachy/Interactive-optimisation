import pygame # handle visualisations
import pymunk # handle the physics
import pymunk.pygame_util # to connect the two libs
import math

pygame.init() # init
WIDTH, HEIGHT = 1000, 800 # window size
window = pygame.display.set_mode((WIDTH, HEIGHT)) # window set up


def draw(space, window, draw_options, line):
    window.fill("white") # clear the window
    #print("wwwwwwwwwwwwwwww " , line)
    if line:
        pygame.draw.line(window, "black", line[0], line[1], 3)

    space.debug_draw(draw_options)
    pygame.display.update()


def calc_distance(p1,p2):
    return math.sqrt((p2[1] - p1[1])**2 + (p2[0] - p1[0])**2) # calc absolutie distannce

def calc_angle(p1, p2): # gives angle in radians betwen  p1, p2
    return math.atan2(p2[1] - p1[1], p2[0] - p1[0])

# to draw circle need radius and mass
def create_ball(space, radius, mass, pos):
    # not that body is seperate from the image, the body is the underlying "hitbox" where physics is calc, whereas we map the image/shape to the body, so its behaviour may vary slightly
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = pos# position is calc fromt the center of the obj
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.elasticity = 0.9 # gives it a "bouncy" elastic property
    shape.friction = 0.4
    shape.color = (255, 0, 0, 100)

    # we need to have both as the shape is added to the body. and allows us to see the physics perfomed on the body. otherwise can add just body, but wont see it
    space.add(body, shape) # add the body and shape to the simulation
    return shape


#  to creaete rect, need x,y position of center of rect, and w, h
def create_boundaries(space, w, h):
    rects = [
        [(w / 2, h - 10), (w, 20)],
        [(w / 2, 10), (w, 20)],
        [(10, h / 2), (20, h)], # not that we set the x,y pos to be half of width because doing from center
        [(w - 10, h / 2), (20, h)],
    ]

    for pos, size in rects:

        # if we remove static property, we need to define a mass as now dynamic
        body = pymunk.Body(body_type=pymunk.Body.STATIC) # body doesnt move
        body.position = pos
        shape = pymunk.Poly.create_box(body, size)
        shape.elasticity = 0.4
        shape.friction = 0.5
        space.add(body, shape)
        # keep attention the process, we define pos and dimensions
        # create the body, define type and pos, create shape and attach to body
        # add body to space


def create_swing(space):

    # static point from which we connect a dynamic body that will swing
    rotation_center = pymunk.Body(body_type=pymunk.Body.STATIC)
    rotation_center.position = (300, 270)

    # if we set the body pos to be the same as rotaiton center, they will overlap and wont see the pivot, 
    # but if different pos we will see the joing betwee the rottaion center and the body
    body = pymunk.Body()
    body.position = (300, 300)

    #draw line between body and circle where circle is at te bottom of the line (bidy, pos in body, other pos relative to body)
    line = pymunk.Segment(body, (0, 0), (255,0), 5) # the positions are relative to the body, so 0,0 is the center of the body
    circle = pymunk.Circle(body, 40, (255,0))
    line.friction = 1
    circle.friction = 1
    line.mass = 8
    circle.mass = 30
    circle.elasticity = 0.95

    #create the joint 
    rotation_center_joint = pymunk.PinJoint(body, rotation_center, (0, 0), (0, 0)) # on the body we connect from the center of the body to center of rotation center
    space.add(circle, line, body, rotation_center_joint )
    # notice that we dont add the rotation center_body, thats fine as theres no shape associated with it, its  simply there so we can use in he joint

    return body

def create_structure(space, width, height):
    BROWN = (139, 69, 19, 100)
    rects = [
        [(600, height - 120), (40, 200), BROWN, 100],
        [(900, height - 120), (40, 200), BROWN, 100],
        [(750, height - 240), (340, 40), BROWN, 150],
    ]

    for pos, size, colour, mass in rects:
        body = pymunk.Body()
        body.position = pos
        shape = pymunk.Poly.create_box(body, size, radius=4)
        shape.color = colour
        shape.mass = mass
        shape.elasticity = 0.4
        shape.friction = 0.5
        space.add(body, shape)

def run(window, width, height):
    run = True
    clock =pygame.time.Clock() # controlling the game loop speed
    fps = 60
    dt = 1/fps #delta time/chamge in time

    space = pymunk.Space() # we place obj in the space, allowing pymunk to perform simulation of obj in space, that will be drawn
    space.gravity = (0, 981) # gravity in the x dir and y dir.

    pressed_pos = None
    ball = None

    #ball = create_ball(space, 30, 10 )
    create_boundaries(space, width, height )
    create_structure(space, width, height)
    c = create_swing(space)
    

    # by default pymunk doesnt draw, only simulates and allows to retrieve info about bodies. to draw need to define draww opotions
    draw_options = pymunk.pygame_util.DrawOptions(window) # now we associaste the window with the spaec

    while run:
        line = None
        print(c.force.length)

        if ball and pressed_pos:
            line = [pressed_pos, pygame.mouse.get_pos()] # draw line between mouse and ball

        # event loop 
        for event in pygame.event.get(): # loop through all events ie keyboard input ...
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not ball:
                    pressed_pos = pygame.mouse.get_pos()
                    ball = create_ball(space, 30, 10, pressed_pos)


                # if the ball does exist then we want to launch it at the angle between mouse and ball pos
                elif pressed_pos:
                    ball.body.body_type = pymunk.Body.DYNAMIC # on press the ball becomes dynamic and can be launched
                    angle = calc_angle(*line) # *line breaks it down into its args p1, p2
                    force = calc_distance(*line) * 100
                    fx = math.cos(angle) * force
                    fy = math.sin(angle) * force
                    ball.body.apply_impulse_at_local_point((fx, fy), (0, 0))
                    pressed_pos = None
                    #pass
                
                # if click again remove the ball from screen
                else:
                    
                    space.remove(ball, ball.body) # remove shape and vody
                    ball = None

                # accessing the body of the shape and applying false (impulse in the x dir) can also do for y at pos of the ball (cennter)
                #ball.body.apply_impulse_at_local_point((10000, 0), (0, 0)) #  the 0, 0 is in relation to the dimensions of the shapte itself and impact of impulse varies dependendt on mass
       
       
        draw( space, window, draw_options, line)
        space.step(dt) # says how fast the simulation should go, so if 60fps, 1/60. so each step in simulation we move forward dt time
        clock.tick(fps) # max game loops per second capped at fps

    pygame.quit()

## note sbout collisions, if velocity is too higih we can miss calculations with vel, as we are checking each frame for collision
# so if too quick, it can go passed the frame before its caclulation
if __name__ == "__main__":
    run(window, WIDTH, HEIGHT)