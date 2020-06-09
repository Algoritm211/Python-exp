import pygame


WIDTH = 560
HEIGHT = 1080
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('First game')
clock = pygame.time.Clock()

done = True
while done:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False


    screen.fill(BLUE)
    pygame.display.flip()


pygame.quit()
