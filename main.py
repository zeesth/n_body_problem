import pygame
from random import randint, random
from motion import Body, WIDTH, HEIGHT

#   Initializing screen with title
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('N Body Simulation')


def main(num):
    #   Creating num objects with random positions and velocities
    run = True
    clock = pygame.time.Clock()
    bodies = []
    
    for i in range(num):
        new_body = Body(random(), random(), (randint(0, 255), randint(0, 255), randint(0, 255)), randint(1e10, 1e30))
        new_body.y_vel = randint(-50000, 50000)
        bodies.append(new_body)

    while run:
        #   Sets tick speed and window color to black
        clock.tick(5)
        SCREEN.fill((0, 0, 20))
        
        for event in pygame.event.get():
            #   Exits program if user closes the window
            if event.type == pygame.QUIT:
                run = False

        #   Initializes motion and draw orbit for each object
        for body in bodies:
            body.movement(bodies)
            body.draw(SCREEN)
            
        #   Updates the window after each motion
        pygame.display.update()
    
    pygame.quit()
    
main(9)