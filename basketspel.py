import pygame
pygame.init()

PI = 3.141592653

WHITE = ( 255, 255, 255)
ORANGECOURT = ( 248, 193, 120)
BLACK = ( 0, 0, 0)
RED = (255,0,0)

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
    pygame.draw.rect(screen, BLACK, [575, 380, 500, 125])
    pygame.draw.rect(screen, ORANGECOURT, [590, 395, 400, 95])
    pygame.draw.arc(screen, BLACK, [455,395,250,100],  PI/2,     PI, 2)
    pygame.draw.arc(screen, BLACK,  [455,395,250,100],    PI, 3*PI/2, 2)
     

    #stolpen
    pygame.draw.rect(screen, BLACK, [850,45,15,400],)

    #korgen
    pygame.draw.rect(screen, RED, [750,140,100,8])

    

    pygame.display.flip()

    clock.tick(60)


