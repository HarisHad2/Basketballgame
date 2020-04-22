import pygame
pygame.init()

PI = 3.141592653

WHITE = ( 255, 255, 255)
ORANGECOURT = ( 248, 193, 120)
BLACK = ( 0, 0, 0)
SHIRTNUMBER = (243, 255, 0)

# Player position
x_player = 180
y_player = 430

x_playerspeed = 0
y_playerspeed = 0

# Screen
size = (900,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Basketball Game")

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                y_playerspeed = -3
                if y_player <= 200:
                    y_playerspeed = 3

    # --- Game logic

    # The jump
    y_player = y_player + y_playerspeed

    screen.fill(WHITE)

    # Pitch
    pygame.draw.rect(screen, ORANGECOURT, [0, 300, 900, 300])
    pygame.draw.ellipse(screen, BLACK, [250, 320, 1200, 260], 20)
    pygame.draw.rect(screen, BLACK, [575, 380, 500, 125])
    pygame.draw.rect(screen, ORANGECOURT, [590, 395, 400, 95])
    pygame.draw.arc(screen, BLACK, [455,395,250,100],  PI/2,     PI, 2)
    pygame.draw.arc(screen, BLACK,  [455,395,250,100],    PI, 3*PI/2, 2)
    
    # Player
    pygame.draw.rect(screen, BLACK, [x_player, y_player, 50, 50])
    font = pygame.font.SysFont('Calibri', 25, True, False)
    number = font.render("04", True, SHIRTNUMBER)
    screen.blit(number, [190, y_player + 10])

    

    pygame.display.flip()

    clock.tick(60) 