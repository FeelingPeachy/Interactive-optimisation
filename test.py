import pygame
import pymunk

def create_structure(space, width, height):
    BROWN = (139, 69, 19, 100)
    rects = [
        [(600, height - 120), (40, 200), BROWN, 100],
        [(900, height - 120), (40, 200), BROWN, 100],
        [(750, height - 240), (340, 40), BROWN, 150],
    ]
    
    shapes = []  # List to hold references to the shapes
    
    for pos, size, colour, mass in rects:
        body = pymunk.Body(mass, pymunk.moment_for_box(mass, size))
        body.position = pos
        shape = pymunk.Poly.create_box(body, size, radius=4)
        shape.color = colour
        shape.elasticity = 0.4
        shape.friction = 0.5
        space.add(body, shape)
        shapes.append(shape)  # Store the shape reference

    return shapes  # Return the list of shapes

def log_forces(space, shapes):
    for shape in shapes:
        # Get the body of the shape and its force
        body = shape.body
        force = body.force
        print(f"Force on shape at position {body.position}: {force}")

def draw_shape_with_border(screen, shape, border_color=(0, 0, 0), border_thickness=3):
    """Draws the filled shape and a solid border around it."""
    vertices = [(shape.body.position.x + v.x, shape.body.position.y + v.y) for v in shape.get_vertices()]

    # Draw the filled shape
    pygame.draw.polygon(screen, shape.color, vertices)
    
    # Draw the solid border around the shape
    pygame.draw.lines(screen, border_color, True, vertices, border_thickness)

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



def main():
    pygame.init()
    width, height = 1000, 800
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    space = pymunk.Space()
    space.gravity = (0, 981)  # Apply gravity
    create_boundaries(space, width, height )

    shapes = create_structure(space, width, height)

    # Simulation loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        space.step(1 / 60.0)  # Step the physics engine

        # Apply an external force for testing (you can modify this)
        for shape in shapes:
            shape.body.apply_force_at_local_point((0, -50), (0, 0))  # Apply upward force

        # Clear the screen
        screen.fill((255, 255, 255))
        
        # Draw the rectangles with solid borders
        for shape in shapes:
            draw_shape_with_border(screen, shape)

        # Log forces every 10 frames
        if pygame.time.get_ticks() % 100 == 0:  # Log every 100 ms (approx 10 frames at 60 FPS)
            log_forces(space, shapes)
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
