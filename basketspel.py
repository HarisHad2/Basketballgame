import pygame
pygame.init()

PI = 3.141592653

WHITE = ( 255, 255, 255)
ORANGECOURT = ( 248, 193, 120)
BLACK = ( 0, 0, 0)
SHIRTNUMBER = (243, 255, 0)
<<<<<<< HEAD

# Player position
x_player = 180
y_player = 430

x_playerspeed = 0
y_playerspeed = 0

# Screen
size = (900,600)
=======
RED = (255, 0, 0)

# Player position
playerImg = pygame.image.load("basketball-player (21).png")
x_player = 150
y_player = 300
v = 5 
m = 1
b = 5
mb = 1

# Ball
ballImg = pygame.image.load("basketball2.png")
x_ball = 255
y_ball = 275
ballPosX = 0



#background
background = pygame.image.load("rip24.png")

def player(x,y):
    screen.blit(playerImg, (x, y))

def ball(x,y):
    screen.blit(ballImg, (x, y))

isjump = False




# Screen
size = (900,700)
>>>>>>> f5ead737956c42088394f7f7957e4f9251957d77
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Basketball Game")

done = False
jumping = False
<<<<<<< HEAD
gravity = 1.2
=======

>>>>>>> f5ead737956c42088394f7f7957e4f9251957d77
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    keys = pygame.key.get_pressed() 
        
    if isjump == False:           
        if keys[pygame.K_SPACE]:                             
            isjump = True

    if isjump :     
        F =(1 / 9)*m*(v**4)               
        y_player -= F 
        v = v-0.5             
        
        if v<0:      
            m =-1  

        if v == -2.5:
            ballPosX = 15
            

        if v == -5.5:             
            isjump = False           
            v = 5
            m = 1

    if isjump:
        if v > -2.5:
            BF =(1 / 9)*mb*(b**4)
            y_ball -= BF     
            b = b-0.5   

        if b<0:      
            m =-1  

        if b == -2.5:
            ballPosX = 15
            

        if b == -5.5:             
            isjump = False           
            b = 5
            mb = 1
                

    # --- Game logic

    x_ball += ballPosX
    

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if jumping == False:                   
                    jumping = True
                    y_playerspeed = -3
                    if y_player < 200:
                        y_playerspeed = 3

                

    # --- Game logic

    # The jump
    if jumping == True:
        y_player = y_player + gravity
    y_player = y_player + y_playerspeed

    screen.fill(WHITE)

<<<<<<< HEAD
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

    
=======
    #background image
    screen.blit(background,(18, -140))

    # Pitch
    pygame.draw.rect(screen, ORANGECOURT, [0, 400, 900, 300])
    pygame.draw.ellipse(screen, BLACK, [250, 420, 1200, 260], 20)
    pygame.draw.rect(screen, BLACK, [575, 480, 500, 125])
    pygame.draw.rect(screen, ORANGECOURT, [590, 495, 400, 95])
    pygame.draw.arc(screen, BLACK, [455,495,250,100],  PI/2,     PI, 2)
    pygame.draw.arc(screen, BLACK,  [455,495,250,100],    PI, 3*PI/2, 2)
    
    # Player
    player(x_player, y_player)
    ball(x_ball, y_ball)
    
    #stolpen
    pygame.draw.rect(screen, BLACK, [850,45,15,500],)

    #korgen
    pygame.draw.rect(screen, RED, [750,140,100,8])
>>>>>>> f5ead737956c42088394f7f7957e4f9251957d77

    pygame.display.flip()

    clock.tick(60) 
<<<<<<< HEAD

    
=======
>>>>>>> f5ead737956c42088394f7f7957e4f9251957d77
