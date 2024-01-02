import keyboard
import pygame
import random
import time

starttime = time.time()
screen = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()
plr = pygame.Rect(200,190,20,20)
plr.center = (200,200)
speed = 8
Jump = False
rect = pygame.Rect(400,190,20,20)
rect2 = pygame.Rect(400,190,20,20)
draw = False
draw2 = False
spawn = True
grnd = pygame.Rect(0,0,400,200)
grnd.center = 200,310
sky = pygame.image.load("C:/Users/naser/Downloads/sky.jpg")
run = True
pause = False
Score = 0
bestscore = 0
frame = 0
highframe = 0
timm = 0
high = False
tmr = 0
timer = False

def txtdraw(text,font,color,center):
    img = font.render(text, True, color)
    surface = img.get_rect()
    surface.center = center
    screen.blit(img,surface)

while run == True:
    frame += 1
    screen.blit(sky,(0,0))
    pygame.draw.rect(screen, "Green", grnd)
    grnd.y += 10
    pygame.draw.rect(screen, (150,75,0), grnd)
    grnd.y -= 10
    pygame.init()
    txtfont = pygame.font.SysFont("Burbank big condensed", 60)
    if pause == True:
        fnt2 = pygame.font.SysFont("Burbank big condensed", 70)
        txtdraw("Best Score:" + str(round(bestscore,2)),fnt2,"Black", (200,300))
        txtdraw("Game Over", txtfont, (255,255,255),(200,170))
        if Score > bestscore:
            bestscore = Score
            timer = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    if pause == False:

        fnt2 = pygame.font.SysFont("Burbank big condensed", 30)
        txtdraw("Best Score:" + str(round(bestscore,2)),fnt2,"Black", (300,350))
        endtime = time.time()
        Score = round((endtime) - (starttime), 2)
        txtdraw(str(Score),txtfont,"Black", (200,100))
        if keyboard.is_pressed("space") or keyboard.is_pressed("w") or keyboard.is_pressed("UP"):
            Jump = True
        if Jump == True:
            speed -= .5
            plr.y -= speed
            if plr.y == 190:
                Jump = False
                speed = 8
        player = pygame.draw.rect(screen, (255,255,255), plr)
        rndm = random.randint(1,40)
        if spawn == True:
            if 1 == rndm:
                draw = True
                spawn = False
        if draw == True:
            rectangle = pygame.draw.rect(screen, (255, 255, 255), rect)
            rect.centerx -= 5
            if rect.centerx < 190:
                spawn = True
                if 1 == rndm and draw2 == False:
                    draw2 = True
                if rect.centerx < -20:
                    rect.centerx = 400
                    draw = False

        if draw2 == True:
            rectangle2 = pygame.draw.rect(screen, (255, 0, 0), rect2)
            rect2.centerx -= 5
            spawn = False
            if rect2.centerx < 190:
                spawn = True
            if rect2.centerx < -20:
                rect2.centerx = 400
                draw2 = False
        if Score == bestscore and bestscore != 0 and Score != 0 :
            timer = True
            tmr = time.time()
        if timer == True:
            fnt = pygame.font.SysFont("Burbank big condensed", 30)
            txtdraw("New High Score!",fnt,"Black", (200,50))
            if (time.time()) - tmr > 2:
                timer = False

        if plr.colliderect(rect) == True:
            pause = True
        elif plr.colliderect(rect2) == True:
            pause = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    if keyboard.is_pressed("r"):
        starttime = time.time()
        pause = False
        rect.centerx = 400
        rect2.centerx = 400
    pygame.display.update()
    clock.tick(60)
