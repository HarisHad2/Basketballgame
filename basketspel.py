import pygame
from pygame import mixer

pygame.init()

PI = 3.141592653

WHITE = ( 255, 255, 255)
ORANGECOURT = ( 248, 193, 120)
BLACK = ( 0, 0, 0)
SHIRTNUMBER = (243, 255, 0)
RED = (255, 0, 0)

# background sound
mixer.music.load("Jock Jams - Are You ready For This.mp3")
mixer.music.play(-1)

# Player 
playerImg = pygame.image.load("basketball-player (21).png")
x_player = 150
y_player = 300

# Net
netImg = pygame.image.load("net-115x115.png")
netX = 750
netY = 210

# Blocker
blockerImg = pygame.image.load("basketball-player (2).png")
x_blocker = 345
y_blocker = 328


# Jump for shooter
isJump = False
jumpCount = 10

# Jump for blocker
bisJump = False
bjumpCount = 10

# Ball
ballImg = pygame.image.load("basketball2.png")
x_ball = 255
y_ball = 275
ballPosX = 0
ballPosY = 0



#background
background = pygame.image.load("rip24.png")

def player(x,y):
    screen.blit(playerImg, (x, y))

def ball(x,y):
    screen.blit(ballImg, (x, y))

def net():
    screen.blit(netImg, (netX, netY))

def blocker(x,y):
    screen.blit(blockerImg, (x, y))

# Score
score = 0 
Font = pygame.font.SysFont("monospace", 35)

# Screen
size = (900,700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Basketball Game")

done = False


clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    keys = pygame.key.get_pressed() 
        
            
    if not(isJump): 

        if keys[pygame.K_SPACE]:
            isJump = True
            
    else:
        if jumpCount >= -10:           
            y_player -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
            if jumpCount > -1:
                y_ball -= (jumpCount * abs(jumpCount)) * 0.5
            if jumpCount == -1:            
                ballPosX = 30            
                ballPosY = 1
                
        else: 
            jumpCount = 10
            isJump = False  

    #print(x_ball)
    #print(y_ball)    

    if x_ball == 765:
        ballPosX = 0
        ballPosY = 0
        x_ball = 255
        y_ball = 275
        score += 1

    #if (x_ball >= x_blocker and (x_ball + 64) < x_blocker) or (x_blocker >= x_ball and (x_blocker + 30) < x_ball):
        #if (y_ball >= y_blocker and (y_ball - 64) < y_blocker) or (y_blocker >= y_ball and (y_blocker + 100) < y_ball):
    #if y_ball == y_blocker and x_ball == x_blocker:
    #if (x_ball == x_blocker) and (y_ball >= y_blocker and y_ball < y_blocker):
         
     #   x_ball = 255
     #   y_ball = 275
    #    ballPosX = 0
     #   ballPosY = 0

    if not(bisJump): 

        if keys[pygame.K_UP]:
            bisJump = True
            
    else:
        if bjumpCount >= -10:           
            y_blocker -= (bjumpCount * abs(bjumpCount)) * 0.5
            bjumpCount -= 1     
            #print(x_blocker)  
            #print(y_blocker)

        else: 
            bjumpCount = 10
            bisJump = False            

    

    text = "Score:" + str(score)
    label = Font.render(text, 1, (0,0,0))
        
                

    # --- Game logic

    x_ball += ballPosX
    y_ball += ballPosY

    screen.fill(WHITE)

    #background image
    screen.blit(background,(18, -140))
    
    net()

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
    blocker(x_blocker, y_blocker)
    
    #stolpen
    pygame.draw.rect(screen, BLACK, [850,45,15,500],)

    #korgen
    pygame.draw.rect(screen, RED, [750,210,100,8])

    # Score
    screen.blit(label, (10, 10))
    pygame.display.flip()

    clock.tick(60) 
