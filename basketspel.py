import pygame
pygame.init()

PI = 3.141592653

WHITE = ( 255, 255, 255)
ORANGECOURT = ( 248, 193, 120)
BLACK = ( 0, 0, 0)

size = (900,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Basketball Game")

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    pygame.draw.rect(screen, ORANGECOURT, [0, 300, 900, 300])
    pygame.draw.ellipse(screen, BLACK, [250, 320, 1200, 260], 20)

    pygame.display.flip()

    clock.tick(60)