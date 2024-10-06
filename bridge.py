import pygame # handle visualisations
import pymunk # handle the physics
import pymunk.pygame_util # to connect the two libs
import math

pygame.init() # init
WIDTH, HEIGHT = 1000, 800 # window size
window = pygame.display.set_mode((WIDTH, HEIGHT)) # window set up


def draw(space, window, draw_options):
    window.fill("white") # clear the window
    space.debug_draw(draw_options)
    pygame.display.update()


def calc_distance(p1,p2):
    return math.sqrt((p2[1] - p1[1])**2 + (p2[0] - p1[0])**2) # calc absolutie distannce

def calc_angle(p1, p2): # gives angle in radians betwen  p1, p2
    return math.atan2(p2[1] - p1[1], p2[0] - p1[0])

# to draw circle need radius and mass
def create_ball(space, radius, mass):
    # not that body is seperate from the image, the body is the underlying "hitbox" where physics is calc, whereas we map the image/shape to the body, so its behaviour may vary slightly
    body = pymunk.Body()
    body.position = (300, 300)# position is calc fromt the center of the obj
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

def run(window, width, height):
    run = True
    clock =pygame.time.Clock() # controlling the game loop speed
    fps = 60
    dt = 1/fps #delta time/chamge in time

    space = pymunk.Space() # we place obj in the space, allowing pymunk to perform simulation of obj in space, that will be drawn
    space.gravity = (0, 981) # gravity in the x dir and y dir.

    ball = create_ball(space, 30, 10 )
    create_boundaries(space, width, height )

    # by default pymunk doesnt draw, only simulates and allows to retrieve info about bodies. to draw need to define draww opotions
    draw_options = pymunk.pygame_util.DrawOptions(window) # now we associaste the window with the spaec

    while run:

        # event loop 
        for event in pygame.event.get(): # loop through all events ie keyboard input ...
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.MOUSEBUTTONDOWN:

                # accessing the body of the shape and applying false (impulse in the x dir) can also do for y at pos of the ball (cennter)
                ball.body.apply_impulse_at_local_point((10000, 0), (0, 0)) #  the 0, 0 is in relation to the dimensions of the shapte itself and impact of impulse varies dependendt on mass
       
       
        draw( space, window, draw_options)
        space.step(dt) # says how fast the simulation should go, so if 60fps, 1/60. so each step in simulation we move forward dt time
        clock.tick(fps) # max game loops per second capped at fps

    pygame.quit()

## note sbout collisions, if velocity is too higih we can miss calculations with vel, as we are checking each frame for collision
# so if too quick, it can go passed the frame before its caclulation
if __name__ == "__main__":
    run(window, WIDTH, HEIGHT)