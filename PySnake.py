import sys, pygame, snake, food
from time import sleep

size = width, height = 640, 480
scl = 15
if (width%scl)>0:
    width = scl*int(width/scl)
    print("width: ", end="")
    print(width)
if (height%scl)>0:
    height = scl * int(height/scl)
    print("height: ", end="")
    print(height)
player = snake.Snake(width/scl,height/scl)
speed = 1
black = 0, 0, 0
white = 255, 255, 255
alive = True
lastDir = "right"
screen = pygame.display.set_mode(size)

frog = food.Food(int(width/scl),int(height/scl))
#player.grow(12)

def terminate():
    sys.exit()
    
while alive:
    events = pygame.event.get()
    newDir = lastDir
    #kill the game 
    for event in events:
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            terminate()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and lastDir != "down":
                newDir = "up"
            elif event.key == pygame.K_DOWN and lastDir != "up":
                newDir = "down"
            elif event.key == pygame.K_LEFT and lastDir != "right":
                newDir = "left"
            elif event.key == pygame.K_RIGHT and lastDir != "left":
                newDir = "right"
    lastDir=newDir
    player.Move(lastDir)            
    screen.fill(black)
    #pygame.draw.rect(screen, white, (width/2,height/2,20,20),5)
    i=1
    while i < player.length:
        if player.SegPosX[i] == player.SegPosX[0] and player.SegPosY[i] == player.SegPosY[0]:
            print("loser")
            terminate()
        i += 1
    i = 0
    while i < player.length:
        x = player.SegPosX[i]*scl
        y = player.SegPosY[i]*scl
        pygame.draw.rect(screen, white, (x,y,scl,scl), 0)
        pygame.draw.rect(screen, black, (x+1,y+1,scl-2,scl-2), 1)
        #print("it does make it")
        i += 1
    pygame.draw.rect(screen, white, ((frog.x*scl),(frog.y*scl),scl,scl),0)
    pygame.draw.rect(screen, black, (((frog.x*scl)+1),((frog.y*scl)+1),(scl-2),(scl-2)),1)
    if player.SegPosX[0] == frog.x and player.SegPosY[0] == frog.y:
        player.grow(1, lastDir)
        frog.move()
        for i in range(len(player.SegPosX)):
            if i < len(player.SegPosX):
                if frog.x == player.SegPosX[i] and frog.y == player.SegPosY[i]:
                    frog.move()
                    print("collision detected")
                    i = 0
    
    if player.SegPosX[0] < 0 or player.SegPosY[0] < 0 or player.SegPosX[0] > width/scl or player.SegPosY[0] > height/scl:
        print("loser")
        terminate()
    pygame.display.update()
    sleep(0.1)
    
        