##########################
# File Name: portalgametemplate.py
# Description: This program is the template for the summative project
# Author: Jonathan Wei
# Date: 30/12/2018
##########################
from random import randint
import pygame
import time
from os import path

pygame.mixer.pre_init(44100, -16, 1, 512) # load the sound effects faster so there is no delay
pygame.init()
WIDTH = 800
HEIGHT = 600
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont("Times New Roman", 25)
font2 = pygame.font.SysFont("Times New Roman", 15)
font3 = pygame.font.SysFont("Arial", 15)

TOP = 0
BOOTTOM = HEIGHT
outline = 0
BLACK     = (  0,  0,  0)                       
RED       = (255,  0,  0)                     
GREEN     = (  0,255,  0)                     
BLUE      = (  0,  0,255)                     
ORANGE    = (255,127,  0)               
CYAN      = (  0,183,235)                   
MAGENTA   = (255,  0,255)                   
YELLOW    = (255,255,  0)
WHITE     = (255,255,255) 

# functions
def redrawGameWindow():
    if startmenu == True:
        drawStartMenu()
    if playerscore == 1:    
        drawLevelOne()
    if playerscore == 2:
        drawLevelTwo()
    if playerscore == 3:
        drawLevelThree()
    if endmenu == True:
        drawEndMenu()
    pygame.display.update()

def drawStartMenu():
    gameWindow.blit(background, (0, 0))
    gameWindow.blit(logo, (logoX, logoY))
    startprompt = font.render("PRESS SPACE TO START", 2, WHITE)
    controls = font2.render("USE THE ARROW KEYS TO MOVE", 2, WHITE)
    replay = font2.render("PRESS R TO REPLAY THE COOL ANIMATION", 2, WHITE)
    gameWindow.blit(startprompt, (startpromptX, startpromptY))
    gameWindow.blit(controls, (controlsX, controlsY))
    gameWindow.blit(replay, (replayX, replayY))

def drawLevelOne():
    gameWindow.blit(background, (0, 0))
    seconds = (pygame.time.get_ticks() - start_ticks)/1000
    time = font3.render("TIME: " + str(seconds), 2, WHITE)
    gameWindow.blit(time, (440, 5))
    livesleft = font3.render("LIVES LEFT: " + str(lives), 2, WHITE)
    gameWindow.blit(livesleft, (280, 5))
    pygame.draw.rect(gameWindow, RED, (0, 500, 100, 100), outline)
    gameWindow.blit(portal, (75, 70))
    gameWindow.blit(portal, (75, 135))
    gameWindow.blit(portal, (110, 550))
    gameWindow.blit(portal, (185, 550))
    gameWindow.blit(portal, (30, 535))
    gameWindow.blit(portal, (135, 340))
    gameWindow.blit(portal, (620, 10))
    gameWindow.blit(portal, (685, 10))
    gameWindow.blit(portal, (685, 420))
    gameWindow.blit(portal, (625, 420))
    gameWindow.blit(portal, (625, 530))
    gameWindow.blit(portal, (685, 490))
    gameWindow.blit(endportal, (755, 545))
    gameWindow.blit(gokuPic[gokuPicNum], (gokuX, gokuY))
    gameWindow.blit(hlaser, (laserX[0] + laserS[0], 250))
    gameWindow.blit(hlaser, (laserX[1] + laserS[1], 350))
    gameWindow.blit(hlaser, (laserX[2] + laserS[2], 275))
    gameWindow.blit(hlaser, (laserX[3] + laserS[3], 225))
    gameWindow.blit(hlaser, (laserX[4] + laserS[4], 175))
    gameWindow.blit(hlaser, (laserX[5] + laserS[5], 125))
    gameWindow.blit(hlaser, (laserX[6] + laserS[6], 175))
    gameWindow.blit(hlaser, (laserX[7] + laserS[7], 275))
    gameWindow.blit(vlaser, (370, laserY[0] + laserSy[0]))
    gameWindow.blit(vlaser, (520, laserY[1] + laserSy[1]))
    gameWindow.blit(vlaser, (370, laserY[2] + laserSy[2]))
    gameWindow.blit(vlaser, (520, laserY[3] + laserSy[3]))
    gameWindow.blit(startlevel1, (level1X, level1Y))
    pygame.draw.rect(gameWindow, WHITE, (120, 0, 10, 390), outline)
    pygame.draw.rect(gameWindow, WHITE, (0, 120, 130, 10), outline)
    pygame.draw.rect(gameWindow, WHITE, (680, 470, 130, 10), outline)
    pygame.draw.rect(gameWindow, WHITE, (670, 0, 10, 600), outline)
    pygame.draw.rect(gameWindow, WHITE, (120, 390, 560, 10), outline)
    pygame.draw.rect(gameWindow, WHITE, (230, 400, 10, 210), outline)
    pygame.draw.rect(gameWindow, WHITE, (0, 500, 100, 10), outline)
    pygame.draw.rect(gameWindow, WHITE, (90, 500, 10, 100), outline)
    pygame.draw.rect(gameWindow, WHITE, (360, 500, 320, 10), outline)

def drawLevelTwo():
    gameWindow.blit(background, (0, 0))
    seconds = (pygame.time.get_ticks() - start_ticks)/1000
    time = font3.render("TIME: " + str(seconds), 2, WHITE)
    gameWindow.blit(time, (440, 5))
    livesleft = font3.render("LIVES LEFT: " + str(lives), 2, WHITE)
    gameWindow.blit(livesleft, (280, 5))
    gameWindow.blit(portal, (75, 70))
    gameWindow.blit(portal, (75, 135))
    gameWindow.blit(portal, (5, 555))
    gameWindow.blit(portal, (135, 555))
    gameWindow.blit(portal, (625, 490))
    gameWindow.blit(portal, (625, 420))
    gameWindow.blit(portal, (135, 135))
    gameWindow.blit(portal, (135, 70))
    gameWindow.blit(portal, (625, 5))
    gameWindow.blit(portal, (685, 5))
    gameWindow.blit(portal, (685, 420))
    gameWindow.blit(portal, (685, 555))
    gameWindow.blit(endportal, (755, 485))
    gameWindow.blit(gokuPic[gokuPicNum], (gokuX, gokuY))
    gameWindow.blit(hlaser, (laserX2[0] + laserS2[0], 220))
    gameWindow.blit(hlaser, (laserX2[1] + laserS2[1], 350))
    gameWindow.blit(hlaser, (laserX2[2] + laserS2[2], 480))
    gameWindow.blit(hlaser, (laserX2[3] + laserS2[3], 110))
    gameWindow.blit(hlaser, (laserX2[4] + laserS2[4], 240))
    gameWindow.blit(hlaser, (laserX2[5] + laserS2[5], 370))
    gameWindow.blit(vlaser, (270, laserY2[0] + laserSy2[0]))
    gameWindow.blit(vlaser, (390, laserY2[1] + laserSy2[1]))
    gameWindow.blit(vlaser, (510, laserY2[2] + laserSy2[2]))
    gameWindow.blit(vlaser, (270, laserY2[3] + laserSy2[3]))
    gameWindow.blit(vlaser, (390, laserY2[4] + laserSy2[4]))
    gameWindow.blit(vlaser, (510, laserY2[5] + laserSy2[5]))
    gameWindow.blit(vlaser, (270, laserY2[6] + laserSy2[6]))                 
    gameWindow.blit(vlaser, (390, laserY2[7] + laserSy2[7]))
    gameWindow.blit(vlaser, (510, laserY2[8] + laserSy2[8]))
    gameWindow.blit(vlaser, (270, laserY2[9] + laserSy2[9]))            
    gameWindow.blit(vlaser, (390, laserY2[10] + laserSy2[10]))
    gameWindow.blit(vlaser, (510, laserY2[11] + laserSy2[11]))
    gameWindow.blit(vlaser, (270, laserY2[12] + laserSy2[12]))            
    gameWindow.blit(vlaser, (390, laserY2[13] + laserSy2[13]))
    gameWindow.blit(vlaser, (510, laserY2[14] + laserSy2[14]))
    gameWindow.blit(startlevel2, (level1X, level2Y))
    pygame.draw.rect(gameWindow, WHITE, (120, 0, 10, 600), outline)
    pygame.draw.rect(gameWindow, WHITE, (0, 120, 680, 10), outline)
    pygame.draw.rect(gameWindow, WHITE, (120, 470, 800, 10), outline)
    pygame.draw.rect(gameWindow, WHITE, (670, 0, 10, 600), outline)
    pygame.draw.rect(gameWindow, WHITE, (120, 240, 420, 10), outline)
    pygame.draw.rect(gameWindow, WHITE, (250, 360, 420, 10), outline)

def drawLevelThree():
    gameWindow.blit(background, (0, 0))
    seconds = (pygame.time.get_ticks() - start_ticks)/1000
    time = font3.render("TIME: " + str(seconds), 2, WHITE)
    gameWindow.blit(time, (660, 25))
    livesleft = font3.render("LIVES LEFT: " + str(lives), 2, WHITE)
    gameWindow.blit(livesleft, (660, 5))
    gameWindow.blit(portal, (75, 70))
    gameWindow.blit(portal, (5, 135))
    gameWindow.blit(portal, (75, 555))
    gameWindow.blit(portal, (135, 555))
    gameWindow.blit(portal, (205, 5))
    gameWindow.blit(portal, (265, 5))
    gameWindow.blit(portal, (335, 555))
    gameWindow.blit(portal, (395, 555))
    gameWindow.blit(portal, (465, 5))
    gameWindow.blit(portal, (525, 5))
    gameWindow.blit(portal, (596, 555))
    gameWindow.blit(portal, (655, 555))
    gameWindow.blit(endportal, (755, 5))
    gameWindow.blit(gokuPic[gokuPicNum], (gokuX, gokuY))
    gameWindow.blit(hlaser, (laserX3[0] + laserS3[0], 220))
    gameWindow.blit(hlaser, (laserX3[1] + laserS3[1], 350))
    gameWindow.blit(hlaser, (laserX3[2] + laserS3[2], 480))
    gameWindow.blit(hlaser, (laserX3[3] + laserS3[3], 220))
    gameWindow.blit(hlaser, (laserX3[4] + laserS3[4], 350))
    gameWindow.blit(hlaser, (laserX3[5] + laserS3[5], 480))
    gameWindow.blit(hlaser, (laserX3[6] + laserS3[6], 90))
    gameWindow.blit(hlaser, (laserX3[7] + laserS3[7], 220))
    gameWindow.blit(hlaser, (laserX3[8] + laserS3[8], 350))
    gameWindow.blit(hlaser, (laserX3[9] + laserS3[9], 480))
    gameWindow.blit(hlaser, (laserX3[10] + laserS3[10], 90))
    gameWindow.blit(hlaser, (laserX3[11] + laserS3[11], 220))
    gameWindow.blit(hlaser, (laserX3[12] + laserS3[12], 350))
    gameWindow.blit(hlaser, (laserX3[13] + laserS3[13], 480))
    gameWindow.blit(hlaser, (laserX3[14] + laserS3[14], 90))
    gameWindow.blit(hlaser, (laserX3[15] + laserS3[15], 220))
    gameWindow.blit(hlaser, (laserX3[16] + laserS3[16], 350))
    gameWindow.blit(hlaser, (laserX3[17] + laserS3[17], 480))
    gameWindow.blit(hlaser, (laserX3[18] + laserS3[18], 90))
    gameWindow.blit(hlaser, (laserX3[19] + laserS3[19], 90))
    gameWindow.blit(hlaser, (laserX3[20] + laserS3[20], 510))
    gameWindow.blit(hlaser, (laserX3[21] + laserS3[21], 350))
    gameWindow.blit(hlaser, (laserX3[22] + laserS3[22], 420))
    gameWindow.blit(hlaser, (laserX3[23] + laserS3[23], 180))
    gameWindow.blit(hlaser, (laserX3[24] + laserS3[24], 250))
    gameWindow.blit(startlevel3, (level1X, level3Y))
    pygame.draw.rect(gameWindow, WHITE, (120, 0, 10, 600), outline)
    pygame.draw.rect(gameWindow, WHITE, (0, 120, 130, 10), outline)
    pygame.draw.rect(gameWindow, WHITE, (250, 0, 10, 600), outline)
    pygame.draw.rect(gameWindow, WHITE, (380, 0, 10, 600), outline)
    pygame.draw.rect(gameWindow, WHITE, (510, 0, 10, 600), outline)
    pygame.draw.rect(gameWindow, WHITE, (640, 0, 10, 600), outline)
    pygame.draw.rect(gameWindow, WHITE, (650, 120, 100, 10), outline)
    pygame.draw.rect(gameWindow, WHITE, (700, 295, 50, 10), outline)
    pygame.draw.rect(gameWindow, WHITE, (700, 470, 130, 10), outline)
    
def drawEndMenu():
    gameWindow.blit(background, (0, 0))
    endprogram = font.render("PRESS ESCAPE TO END THE PROGRAM", 2, WHITE)
    if playerlose == True:
        gameWindow.blit(gameover, (gameoverX, gameoverY))
        gameWindow.blit(endprogram, (175, 350))
    if playerwin == True:
        gameWindow.blit(youwin, (youwinX, youwinY))
        finalscore = font.render("YOUR FINAL TIME: " + str(finalseconds), 2, WHITE)
        gameWindow.blit(finalscore, (270, 350))
        gameWindow.blit(endprogram, (175, 400))

# time
#start_ticks = pygame.time.get_ticks()

# music
music = path.dirname(path.realpath(__file__)) + '\music\music.mp3'
pygame.mixer.music.load(music)
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)

# sound effects
ps = path.dirname(path.realpath(__file__)) + '\music\portalsound.wav'
ls = path.dirname(path.realpath(__file__)) + '\music\lasersound.wav'
portalSound = pygame.mixer.Sound(ps)
laserSound = pygame.mixer.Sound(ls)

temp = path.dirname(path.realpath(__file__)) + '\images\logo.png'
logo = pygame.image.load(temp)
raw_string = r"\images\background.gif"
temp = path.dirname(path.realpath(__file__)) + raw_string
background = pygame.image.load(temp)
temp = path.dirname(path.realpath(__file__)) + '\images\level1.png'
startlevel1 = pygame.image.load(temp)
temp = path.dirname(path.realpath(__file__)) + '\images\level2.png'
startlevel2 = pygame.image.load(temp)
temp = path.dirname(path.realpath(__file__)) + '\images\level3.png'
startlevel3 = pygame.image.load(temp)
temp = path.dirname(path.realpath(__file__)) + '\images\gameover.png'
gameover = pygame.image.load(temp)
temp = path.dirname(path.realpath(__file__)) + '\images\youwin.png'
youwin = pygame.image.load(temp)
temp = path.dirname(path.realpath(__file__)) + '\images\horizontallaser.png'
hlaser = pygame.image.load(temp)
raw_string = r"\images\verticallaser.png"
temp = path.dirname(path.realpath(__file__)) + raw_string
vlaser = pygame.image.load(temp)
temp = path.dirname(path.realpath(__file__)) + '\images\goku0.png'
goku = pygame.image.load(temp)
temp = path.dirname(path.realpath(__file__)) + '\images\portal.png'
portal = pygame.image.load(temp)
temp = path.dirname(path.realpath(__file__)) + '\images\endportal.png'
endportal = pygame.image.load(temp)
gokuH = 37
gokuW = 27
gokuX = 0
gokuY = 0
gokuVx = 0
gokuVy = 0
gokuPicnum = 0
gokuDir = "right"
gokuPic = [0]*8
for i in range(8):
    temp = path.dirname(path.realpath(__file__)) + '\images\goku' + str(i) + '.png'
    gokuPic[i] = pygame.image.load(temp)
RUN_SPEED = 4

nextLeftPic  = [4, 4, 5, 5, 6, 6, 7, 7]
nextRightPic = [0, 0, 1, 1, 2, 2, 3, 3]
clock = pygame.time.Clock()
FPS = 30

# assign variables
endmenu = False
playerwin = False
playerlose = False
startmenu = True
logoX = 212
logoY = -200
startpromptX = -492
startpromptY = 359
controlsX = 1510
controlsY = 402
replayX = 250
replayY = 2000
gameoverX = 100
gameoverY = -200
youwinX = 100
youwinY = -200
level1X = 110
level1Y = -200
level2Y = -200
level3Y = -200
playerscore = 0
lives = 5

# lasers for level 1
laserS = [4]*8
laserX = [0, 60, 130, 350, 180, 325, 680, 750]
laserY = [430, 460, 520, 550]
laserSy = [1.5]*4

# lasers for level 2
laserS2 = [4]*6
laserX2 = [0, 40, 80, 680, 710, 750]
laserY2 = [0, 30, 60, 130, 160, 190, 260, 290, 320, 390, 420, 430, 510, 540, 560]
laserSy2 = [4]*15

# lasers for level 3
laserS3 = [6]*25
laserX3 = [0, 40, 80, 130, 160, 190, 175, 260, 290, 320, 300, 390, 420, 450, 430, 520, 550, 580, 565, 695, 725, 680, 710, 680, 710]

#collision
gokutopRect = goku.get_rect()
gokuleftRect = goku.get_rect()
gokurightRect = goku.get_rect()
gokubottomRect = goku.get_rect()

# main program
inPlay = True
while inPlay:
    redrawGameWindow()
    clock.tick(FPS)

    startmenu = True

    # text images that come down when a condition is met
    if logoY != 120:
        logoY = logoY + 20
    else:
        logoY = 120
    if startpromptX != 268:
        startpromptX = startpromptX + 20
    else:
        startpromptX = 268
    if controlsX != 290:
        controlsX = controlsX - 20
    else:
        controlsX = 290
    if replayY != 440:
        replayY = replayY - 20
    else:
        replayY = 440
    if endmenu == True:
        if playerlose == True:
            if gameoverY != 180:
                gameoverY = gameoverY + 20
            else:
                gameoverY = 180
        if playerwin == True:
            if youwinY != 180:
                youwinY = youwinY + 20
            else:
                youwinY = 180
    if playerscore == 1:
        if level1Y != 600:
            level1Y = level1Y + 20
        else:
            level1Y = 600
    if playerscore == 2:
        if level2Y != 600:
            level2Y = level2Y + 20
        else:
            level2Y = 600
    if playerscore == 3:
        if level3Y != 600:
            level3Y = level3Y + 20
        else:
            level3Y = 600

    pygame.event.clear()
    keys = pygame.key.get_pressed()
    if playerscore != 1:
        if keys[pygame.K_SPACE]:
            gokuX, gokuY = 0, 0
            playerscore = 1
            startmenu = False
            start_ticks = pygame.time.get_ticks()
    if keys[pygame.K_ESCAPE]:
        inPlay = False
    if keys[pygame.K_r]:
        logoY = -200
        startpromptX = -492
        controlsX = 1510
        replayY = 2000

    # set direction and select picture depending on the arrow keys
    if keys[pygame.K_LEFT]:
        gokuVx = -RUN_SPEED
        gokuDir = "left"
    elif keys[pygame.K_RIGHT]:
        gokuVx = RUN_SPEED
        gokuDir = "right"
    else:                               # if neither left nor right arrow is pressed
        gokuVx = 0                     # goku is in standing still position
        if gokuDir == "left":          # when standing,
            gokuPicNum = 4             # the animation view is either 1 or 5,
        elif gokuDir == "right":       # depending on the direction in which
            gokuPicNum = 0             # goku is facing
            
    if keys[pygame.K_UP]:
        gokuVy = -RUN_SPEED
        if gokuDir == "left":          
            gokuDir = "left"             
        elif gokuDir == "right":       
            gokuDir = "right"
    elif keys[pygame.K_DOWN]:
        gokuVy = RUN_SPEED
        if gokuDir == "left":          
            gokuDir = "left"   
        elif gokuDir == "right":       
            gokuDir = "right"
    else:                             
        gokuVy = 0                 
        if gokuDir == "left":          
            gokuPicNum = 4           
        elif gokuDir == "right":     
            gokuPicNum = 0

# move goku in horizontal direction
    gokuX = gokuX + gokuVx
# move goku in vertical direction
    gokuY = gokuY + gokuVy

# detect goku collision with borders
    if gokuX <= 0:
        gokuX = 0
    if gokuX >= 773:
        gokuX = 773
    if gokuY <= 0:
        gokuY = 0
    if gokuY >= 563:
        gokuY = 563

    gokutopRect = pygame.Rect(gokuX + 1, gokuY, gokuW - 2, gokuH - 36)
    gokuleftRect = pygame.Rect(gokuX, gokuY + 1, gokuW - 26, gokuH - 2)
    gokurightRect = pygame.Rect(gokuX + 26, gokuY + 1, gokuW - 26, gokuH - 2)
    gokubottomRect = pygame.Rect(gokuX + 1, gokuY + 36, gokuW - 2, gokuH - 36)

    if playerscore == 1:

    # level 1 collision with rectangles
        lvl1r0 = pygame.Rect(120, 0, 10, 390)
        lvl1r1 = pygame.Rect(0, 120, 120, 10)
        lvl1r2 = pygame.Rect(680, 470, 130, 10)
        lvl1r3 = pygame.Rect(670, 0, 10, 600)
        lvl1r4 = pygame.Rect(130, 390, 540, 10)
        lvl1r5 = pygame.Rect(230, 390, 10, 210)
        lvl1r6 = pygame.Rect(0, 500, 90, 10)
        lvl1r7 = pygame.Rect(90, 510, 10, 100)
        lvl1r8 = pygame.Rect(360, 500, 320, 10)
        
        lvl1rlist = [lvl1r0, lvl1r1, lvl1r2, lvl1r3, lvl1r4, lvl1r5, lvl1r6, lvl1r7, lvl1r8]

        restart = pygame.Rect(30, 535, 40, 50)

        if gokutopRect.colliderect(restart) or gokuleftRect.colliderect(restart) or gokurightRect.colliderect(restart) or gokubottomRect.colliderect(restart):
            gokuX = 0
            gokuY = 0
            lives = lives - 1

        # detecting collision with sides of goku rectangle
        for i in range(len(lvl1rlist)):
            if gokutopRect.colliderect(lvl1rlist[i]):
                gokuY = gokuY + 4
            if gokuleftRect.colliderect(lvl1rlist[i]):
                gokuX = gokuX + 4
            if gokurightRect.colliderect(lvl1rlist[i]):
                gokuX = gokuX - 4
            if gokubottomRect.colliderect(lvl1rlist[i]):
                gokuY = gokuY - 4

        # level 1 collision with portals
        lvl1p0 = pygame.Rect(105, 90, 3, 20)
        lvl1p1 = pygame.Rect(110, 590, 35, 3)
        lvl1p2 = pygame.Rect(190, 590, 30, 3)
        lvl1p3 = pygame.Rect(630, 15, 30, 3)
        lvl1p4 = pygame.Rect(685, 455, 30, 3)
        lvl1p5 = pygame.Rect(655, 530, 3, 40)
        lvl1p6 = pygame.Rect(760, 585, 30, 3)

        # teleportation between portals
        if gokurightRect.colliderect(lvl1p0) or gokubottomRect.colliderect(lvl1p0):
            gokuX = 75
            gokuY = 135
            portalSound.play()
        if gokurightRect.colliderect(lvl1p1) or gokubottomRect.colliderect(lvl1p1) or gokuleftRect.colliderect(lvl1p1):
            gokuX = 135
            gokuY = 340
            portalSound.play()
        if gokurightRect.colliderect(lvl1p2) or gokubottomRect.colliderect(lvl1p2):
            gokuX = 30
            gokuY = 535
            portalSound.play()
        if gokurightRect.colliderect(lvl1p3) or gokutopRect.colliderect(lvl1p3):
            gokuX = 685
            gokuY = 10
            portalSound.play()
        if gokuleftRect.colliderect(lvl1p4) or gokubottomRect.colliderect(lvl1p4):
            gokuX = 625
            gokuY = 420
            portalSound.play()
        if gokurightRect.colliderect(lvl1p5):
            gokuX = 685
            gokuY = 490
            portalSound.play()
        if gokuleftRect.colliderect(lvl1p6) or gokubottomRect.colliderect(lvl1p6):
            gokuX = 0
            gokuY = 0
            portalSound.play()
            playerscore = 2

        # level 1 lasers
        for i in range(len(laserX)):
            laserX[i] = laserX[i] + laserS[i]
        for i in range(len(laserY)):
            laserY[i] = laserY[i] + laserSy[i]
        
        lvl1l0 = pygame.Rect(laserX[0] + laserS[0], 250, 40, 8)
        lvl1l1 = pygame.Rect(laserX[1] + laserS[1], 350, 40, 8)
        lvl1l2 = pygame.Rect(laserX[2] + laserS[2], 275, 40, 8)
        lvl1l3 = pygame.Rect(laserX[3] + laserS[3], 225, 40, 8)
        lvl1l4 = pygame.Rect(laserX[4] + laserS[4], 175, 40, 8)
        lvl1l5 = pygame.Rect(laserX[5] + laserS[5], 125, 40, 8)
        lvl1l6 = pygame.Rect(laserX[6] + laserS[6], 175, 40, 8)
        lvl1l7 = pygame.Rect(laserX[7] + laserS[7], 275, 40, 8)
        lvl1l8 = pygame.Rect(370, laserY[0] + laserSy[0], 8, 40)
        lvl1l9 = pygame.Rect(520, laserY[1] + laserSy[1], 8, 40)
        lvl1l10 = pygame.Rect(370, laserY[2] + laserSy[2], 8, 40)
        lvl1l11 = pygame.Rect(520, laserY[3] + laserSy[3], 8, 40)

        lvl1llist = [lvl1l0, lvl1l1, lvl1l2, lvl1l3, lvl1l4, lvl1l5, lvl1l6, lvl1l7, lvl1l8, lvl1l9, lvl1l10, lvl1l11]

        for i in range(9):
            if lvl1l0.colliderect(lvl1rlist[i]) or laserX[0] <= 0:
                laserS[0] = -laserS[0]
            if lvl1l1.colliderect(lvl1rlist[i]) or laserX[1] <= 0:
                laserS[1] = -laserS[1]
            if lvl1l2.colliderect(lvl1rlist[i]):
                laserS[2] = -laserS[2]
            if lvl1l3.colliderect(lvl1rlist[i]):
                laserS[3] = -laserS[3]
            if lvl1l4.colliderect(lvl1rlist[i]):
                laserS[4] = -laserS[4]
            if lvl1l5.colliderect(lvl1rlist[i]):
                laserS[5] = -laserS[5]
            if lvl1l6.colliderect(lvl1rlist[i]) or laserX[6] + 40 >= 800:
                laserS[6] = -laserS[6] 
            if lvl1l7.colliderect(lvl1rlist[i]) or laserX[7] + 40 >= 800:
                laserS[7] = -laserS[7]
            if lvl1l8.colliderect(lvl1rlist[i]):
                laserSy[0] = -laserSy[0]
            if lvl1l9.colliderect(lvl1rlist[i]):
                laserSy[1] = -laserSy[1]
            if lvl1l10.colliderect(lvl1rlist[i]) or laserY[2] + 40 >= 600:
                laserSy[2] = -laserSy[2]
            if lvl1l11.colliderect(lvl1rlist[i]) or laserY[3] + 40 >= 600:
                laserSy[3] = -laserSy[3]

        # goku collision with lasers
        for i in range(len(lvl1llist)):
            if gokutopRect.colliderect(lvl1llist[i]) or gokuleftRect.colliderect(lvl1llist[i]) or gokurightRect.colliderect(lvl1llist[i]) or gokubottomRect.colliderect(lvl1llist[i]):
                gokuX = 0
                gokuY = 0
                laserSound.play()
                lives = lives - 1
                

    if playerscore == 2:
        # level 2 collision with rectangles
        lvl2r0 = pygame.Rect(120, 0, 10, 600)
        lvl2r1 = pygame.Rect(0, 120, 680, 10)
        lvl2r2 = pygame.Rect(120, 470, 800, 10)
        lvl2r3 = pygame.Rect(670, 0, 10, 600)
        lvl2r4 = pygame.Rect(120, 240, 420, 10)
        lvl2r5 = pygame.Rect(250, 360, 430, 10)
        lvl2leftwall = pygame.Rect(-3, 0, 3, 600)
        lvl2rightwall = pygame.Rect(800, 0, 3, 600)
        lvl2topwall = pygame.Rect(0, -3, 800, 3)
        lvl2bottomwall = pygame.Rect(0, 600, 600, 3)

        lvl2rlist = [lvl2r0, lvl2r1, lvl2r2, lvl2r3, lvl2r4, lvl2r5, lvl2leftwall, lvl2rightwall, lvl2topwall, lvl2bottomwall]

        for i in range(len(lvl2rlist)):
            if gokutopRect.colliderect(lvl2rlist[i]):
                gokuY = gokuY + 4
            if gokuleftRect.colliderect(lvl2rlist[i]):
                gokuX = gokuX + 4
            if gokurightRect.colliderect(lvl2rlist[i]):
                gokuX = gokuX - 4
            if gokubottomRect.colliderect(lvl2rlist[i]):
                gokuY = gokuY - 4

        # level 2 collision with portals
        lvl2p0 = pygame.Rect(105, 90, 3, 20)
        lvl2p1 = pygame.Rect(0, 592, 30, 3)
        lvl2p2 = pygame.Rect(635, 495, 30, 3)
        lvl2p3 = pygame.Rect(135, 140, 30, 3)
        lvl2p4 = pygame.Rect(630, 10, 30, 3)
        lvl2p5 = pygame.Rect(690, 455, 30, 3)
        lvl2p6 = pygame.Rect(765, 495, 30, 3)

        # teleportation between portals
        if gokurightRect.colliderect(lvl2p0) or gokubottomRect.colliderect(lvl2p0):
            gokuX = 75
            gokuY = 135
            portalSound.play()
        if gokuleftRect.colliderect(lvl2p1) or gokubottomRect.colliderect(lvl2p1):
            gokuX = 130
            gokuY = 550
            portalSound.play()
        if gokurightRect.colliderect(lvl2p2) or gokutopRect.colliderect(lvl2p2):
            gokuX = 625
            gokuY = 420
            portalSound.play()
        if gokuleftRect.colliderect(lvl2p3) or gokutopRect.colliderect(lvl2p3):
            gokuX = 135
            gokuY = 70
            portalSound.play()
        if gokuleftRect.colliderect(lvl2p4) or gokutopRect.colliderect(lvl2p4):
            gokuX = 685
            gokuY = 5
            portalSound.play()
        if gokuleftRect.colliderect(lvl2p5) or gokubottomRect.colliderect(lvl2p5):
            gokuX = 685
            gokuY = 555
            portalSound.play()
        if gokurightRect.colliderect(lvl2p6) or gokubottomRect.colliderect(lvl2p6):
            gokuX = 0
            gokuY = 0
            portalSound.play()
            playerscore = 3

        # level 2 collision with lasers
        for i in range(len(laserX2)):
            laserX2[i] = laserX2[i] + laserS2[i]
        for i in range(len(laserY2)):
            laserY2[i] = laserY2[i] + laserSy2[i]
        
        lvl2l0 = pygame.Rect(laserX2[0] + laserS2[0], 220, 40, 8)                         
        lvl2l1 = pygame.Rect(laserX2[1] + laserS2[1], 350, 40, 8)
        lvl2l2 = pygame.Rect(laserX2[2] + laserS2[2], 480, 40, 8)
        lvl2l3 = pygame.Rect(laserX2[3] + laserS2[3], 110, 40, 8)
        lvl2l4 = pygame.Rect(laserX2[4] + laserS2[4], 240, 40, 8)
        lvl2l5 = pygame.Rect(laserX2[5] + laserS2[5], 370, 40, 8)
        lvl2l6 = pygame.Rect(270, laserY2[0] + laserSy2[0], 8, 40)
        lvl2l7 = pygame.Rect(390, laserY2[1] + laserSy2[1], 8, 40)
        lvl2l8 = pygame.Rect(510, laserY2[2] + laserSy2[2], 8, 40)
        lvl2l9 = pygame.Rect(270, laserY2[3] + laserSy2[3], 8, 40)
        lvl2l10 = pygame.Rect(390, laserY2[4] + laserSy2[4], 8, 40)
        lvl2l11 = pygame.Rect(510, laserY2[5] + laserSy2[5], 8, 40)
        lvl2l12 = pygame.Rect(270, laserY2[6] + laserSy2[6], 8, 40)
        lvl2l13 = pygame.Rect(390, laserY2[7] + laserSy2[7], 8, 40)
        lvl2l14 = pygame.Rect(510, laserY2[8] + laserSy2[8], 8, 40)
        lvl2l15 = pygame.Rect(270, laserY2[9] + laserSy2[9], 8, 40)
        lvl2l16 = pygame.Rect(390, laserY2[10] + laserSy2[10], 8, 40)
        lvl2l17 = pygame.Rect(510, laserY2[11] + laserSy2[11], 8, 40)
        lvl2l18 = pygame.Rect(270, laserY2[12] + laserSy2[12], 8, 40)
        lvl2l19 = pygame.Rect(390, laserY2[13] + laserSy2[13], 8, 40)
        lvl2l20 = pygame.Rect(510, laserY2[14] + laserSy2[14], 8, 40)

        lvl2llist = [lvl2l0, lvl2l1, lvl2l2, lvl2l3, lvl2l4, lvl2l5, lvl2l6, lvl2l7, lvl2l8, lvl2l9, lvl2l10, lvl2l11, lvl2l12, lvl2l13, lvl2l14, lvl2l15, lvl2l16, lvl2l17, lvl2l18, lvl2l19, lvl2l10]

        for i in range(len(lvl2rlist)):
            if lvl2l0.colliderect(lvl2rlist[i]):
                laserS2[0] = -laserS2[0]
            if lvl2l1.colliderect(lvl2rlist[i]):
                laserS2[1] = -laserS2[1]
            if lvl2l2.colliderect(lvl2rlist[i]):
                laserS2[2] = -laserS2[2]
            if lvl2l3.colliderect(lvl2rlist[i]):
                laserS2[3] = -laserS2[3]
            if lvl2l4.colliderect(lvl2rlist[i]):
                laserS2[4] = -laserS2[4]
            if lvl2l5.colliderect(lvl2rlist[i]):
                laserS2[5] = -laserS2[5]
            if lvl2l6.colliderect(lvl2rlist[i]):
                laserSy2[0] = -laserSy2[0]
            if lvl2l7.colliderect(lvl2rlist[i]):
                laserSy2[1] = -laserSy2[1]
            if lvl2l8.colliderect(lvl2rlist[i]):
                laserSy2[2] = -laserSy2[2]
            if lvl2l9.colliderect(lvl2rlist[i]):
                laserSy2[3] = -laserSy2[3]
            if lvl2l10.colliderect(lvl2rlist[i]):
                laserSy2[4] = -laserSy2[4]
            if lvl2l11.colliderect(lvl2rlist[i]):
                laserSy2[5] = -laserSy2[5]
            if lvl2l12.colliderect(lvl2rlist[i]):
                laserSy2[6] = -laserSy2[6]
            if lvl2l13.colliderect(lvl2rlist[i]):
                laserSy2[7] = -laserSy2[7]
            if lvl2l14.colliderect(lvl2rlist[i]):
                laserSy2[8] = -laserSy2[8]
            if lvl2l15.colliderect(lvl2rlist[i]):
                laserSy2[9] = -laserSy2[9]
            if lvl2l16.colliderect(lvl2rlist[i]):
                laserSy2[10] = -laserSy2[10]
            if lvl2l17.colliderect(lvl2rlist[i]):
                laserSy2[11] = -laserSy2[11]
            if lvl2l18.colliderect(lvl2rlist[i]):
                laserSy2[12] = -laserSy2[12]
            if lvl2l19.colliderect(lvl2rlist[i]):
                laserSy2[13] = -laserSy2[13]
            if lvl2l20.colliderect(lvl2rlist[i]):
                laserSy2[14] = -laserSy2[14]

        # goku collision with lasers
        for i in range(len(lvl2llist)):
            if gokutopRect.colliderect(lvl2llist[i]) or gokuleftRect.colliderect(lvl2llist[i]) or gokurightRect.colliderect(lvl2llist[i]) or gokubottomRect.colliderect(lvl2llist[i]):
                gokuX = 0
                gokuY = 0
                laserSound.play()
                lives = lives - 1

    if playerscore == 3:
        # level 3 collision with rectangles 
        lvl3r0 = pygame.Rect(120, 0, 10, 600)
        lvl3r1 = pygame.Rect(0, 120, 130, 10)
        lvl3r2 = pygame.Rect(250, 0, 10, 600)
        lvl3r3 = pygame.Rect(380, 0, 10, 600)
        lvl3r4 = pygame.Rect(510, 0, 10, 600)
        lvl3r5 = pygame.Rect(640, 0, 10, 600)
        lvl3r6 = pygame.Rect(650, 120, 100, 10)
        lvl3r7 = pygame.Rect(700, 295, 50, 10)
        lvl3r8 = pygame.Rect(700, 470, 130, 10)
        lvl3leftwall = pygame.Rect(-3, 0, 3, 600)
        lvl3rightwall = pygame.Rect(800, 0, 3, 800)

        lvl3rlist = [lvl3r0, lvl3r1, lvl3r2, lvl3r3, lvl3r4, lvl3r5, lvl3r6, lvl3r7, lvl3r8, lvl3leftwall, lvl3rightwall]

        for i in range(len(lvl3rlist)):
            if gokutopRect.colliderect(lvl3rlist[i]):
                gokuY = gokuY + 4
            if gokuleftRect.colliderect(lvl3rlist[i]):
                gokuX = gokuX + 4
            if gokurightRect.colliderect(lvl3rlist[i]):
                gokuX = gokuX - 4
            if gokubottomRect.colliderect(lvl3rlist[i]):
                gokuY = gokuY - 4

        # level 3 collision with portals
        lvl3p0 = pygame.Rect(105, 90, 3, 20)
        lvl3p1 = pygame.Rect(85, 590, 30, 3)
        lvl3p2 = pygame.Rect(215, 10, 30, 3)
        lvl3p3 = pygame.Rect(340, 590, 30, 3)
        lvl3p4 = pygame.Rect(470, 10, 30, 3)
        lvl3p5 = pygame.Rect(601, 590, 30, 3)
        lvl3p6 = pygame.Rect(765, 15, 30, 3)

        # teleportation between portals
        if gokurightRect.colliderect(lvl3p0) or gokubottomRect.colliderect(lvl3p0):
            gokuX = 0
            gokuY = 135
            portalSound.play()
        if gokurightRect.colliderect(lvl3p1) or gokubottomRect.colliderect(lvl3p1):
            gokuX = 135
            gokuY = 555
            portalSound.play()
        if gokurightRect.colliderect(lvl3p2) or gokutopRect.colliderect(lvl3p2):
            gokuX = 265
            gokuY = 5
            portalSound.play()
        if gokurightRect.colliderect(lvl3p3) or gokubottomRect.colliderect(lvl3p3):
            gokuX = 395
            gokuY = 555
            portalSound.play()
        if gokurightRect.colliderect(lvl3p4) or gokutopRect.colliderect(lvl3p4):
            gokuX = 525
            gokuY = 5
            portalSound.play()
        if gokurightRect.colliderect(lvl3p5) or gokubottomRect.colliderect(lvl3p5):
            gokuX = 655
            gokuY = 555
            portalSound.play()
        if gokurightRect.colliderect(lvl3p6) or gokutopRect.colliderect(lvl3p6):
            playerscore = 4
            portalSound.play()
            finalseconds = pygame.time.get_ticks()/1000
            endmenu = True
            playerwin = True

        # level 3 collision with lasers
        for i in range(len(laserX3)):
            laserX3[i] = laserX3[i] + laserS3[i]
        
        lvl3l0 = pygame.Rect(laserX3[0] + laserS3[0], 220, 40, 8)                         
        lvl3l1 = pygame.Rect(laserX3[1] + laserS3[1], 350, 40, 8)
        lvl3l2 = pygame.Rect(laserX3[2] + laserS3[2], 480, 40, 8)
        lvl3l3 = pygame.Rect(laserX3[3] + laserS3[3], 220, 40, 8)                         
        lvl3l4 = pygame.Rect(laserX3[4] + laserS3[4], 350, 40, 8)
        lvl3l5 = pygame.Rect(laserX3[5] + laserS3[5], 480, 40, 8)
        lvl3l6 = pygame.Rect(laserX3[6] + laserS3[6], 90, 40, 8)
        lvl3l7 = pygame.Rect(laserX3[7] + laserS3[7], 220, 40, 8)                         
        lvl3l8 = pygame.Rect(laserX3[8] + laserS3[8], 350, 40, 8)
        lvl3l9 = pygame.Rect(laserX3[9] + laserS3[9], 480, 40, 8)
        lvl3l10 = pygame.Rect(laserX3[10] + laserS3[10], 90, 40, 8)
        lvl3l11 = pygame.Rect(laserX3[11] + laserS3[11], 220, 40, 8)                         
        lvl3l12 = pygame.Rect(laserX3[12] + laserS3[12], 350, 40, 8)
        lvl3l13 = pygame.Rect(laserX3[13] + laserS3[13], 480, 40, 8)
        lvl3l14 = pygame.Rect(laserX3[14] + laserS3[14], 90, 40, 8)
        lvl3l15 = pygame.Rect(laserX3[15] + laserS3[15], 220, 40, 8)                         
        lvl3l16 = pygame.Rect(laserX3[16] + laserS3[16], 350, 40, 8)
        lvl3l17 = pygame.Rect(laserX3[17] + laserS3[17], 480, 40, 8)
        lvl3l18 = pygame.Rect(laserX3[18] + laserS3[18], 90, 40, 8)
        lvl3l19 = pygame.Rect(laserX3[19] + laserS3[19], 90, 40, 8)
        lvl3l20 = pygame.Rect(laserX3[20] + laserS3[20], 510, 40, 8)
        lvl3l21 = pygame.Rect(laserX3[21] + laserS3[21], 350, 40, 8)
        lvl3l22 = pygame.Rect(laserX3[22] + laserS3[22], 420, 40, 8)
        lvl3l23 = pygame.Rect(laserX3[23] + laserS3[23], 180, 40, 8)
        lvl3l24 = pygame.Rect(laserX3[24] + laserS3[24], 250, 40, 8)

        lvl3llist = [lvl3l0, lvl3l1, lvl3l2, lvl3l3, lvl3l4, lvl3l5, lvl3l6, lvl3l7, lvl3l8, lvl3l9, lvl3l10, lvl3l11, lvl3l12, lvl3l13, lvl3l14, lvl3l15, lvl3l16, lvl3l17, lvl3l18, lvl3l19, lvl3l20, lvl3l21, lvl3l22, lvl3l23, lvl3l24]

        for i in range(len(lvl3rlist)):
            if lvl3l0.colliderect(lvl3rlist[i]):
                laserS3[0] = -laserS3[0]
            if lvl3l1.colliderect(lvl3rlist[i]):
                laserS3[1] = -laserS3[1]
            if lvl3l2.colliderect(lvl3rlist[i]):
                laserS3[2] = -laserS3[2]
            if lvl3l3.colliderect(lvl3rlist[i]):
                laserS3[3] = -laserS3[3]
            if lvl3l4.colliderect(lvl3rlist[i]):
                laserS3[4] = -laserS3[4]
            if lvl3l5.colliderect(lvl3rlist[i]):
                laserS3[5] = -laserS3[5]
            if lvl3l6.colliderect(lvl3rlist[i]):
                laserS3[6] = -laserS3[6]
            if lvl3l7.colliderect(lvl3rlist[i]):
                laserS3[7] = -laserS3[7]
            if lvl3l8.colliderect(lvl3rlist[i]):
                laserS3[8] = -laserS3[8]
            if lvl3l9.colliderect(lvl3rlist[i]):
                laserS3[9] = -laserS3[9]
            if lvl3l10.colliderect(lvl3rlist[i]):
                laserS3[10] = -laserS3[10]
            if lvl3l11.colliderect(lvl3rlist[i]):
                laserS3[11] = -laserS3[11]
            if lvl3l12.colliderect(lvl3rlist[i]):
                laserS3[12] = -laserS3[12]
            if lvl3l13.colliderect(lvl3rlist[i]):
                laserS3[13] = -laserS3[13]
            if lvl3l14.colliderect(lvl3rlist[i]):
                laserS3[14] = -laserS3[14]
            if lvl3l15.colliderect(lvl3rlist[i]):
                laserS3[15] = -laserS3[15]
            if lvl3l16.colliderect(lvl3rlist[i]):
                laserS3[16] = -laserS3[16]
            if lvl3l17.colliderect(lvl3rlist[i]):
                laserS3[17] = -laserS3[17]
            if lvl3l18.colliderect(lvl3rlist[i]):
                laserS3[18] = -laserS3[18]
            if lvl3l19.colliderect(lvl3rlist[i]):
                laserS3[19] = -laserS3[19]
            if lvl3l20.colliderect(lvl3rlist[i]):
                laserS3[20] = -laserS3[20]
            if lvl3l21.colliderect(lvl3rlist[i]):
                laserS3[21] = -laserS3[21]
            if lvl3l22.colliderect(lvl3rlist[i]):
                laserS3[22] = -laserS3[22]
            if lvl3l23.colliderect(lvl3rlist[i]):
                laserS3[23] = -laserS3[23]
            if lvl3l24.colliderect(lvl3rlist[i]):
                laserS3[24] = -laserS3[24]

        # goku collision with lasers
        for i in range(len(lvl3llist)):
            if gokutopRect.colliderect(lvl3llist[i]) or gokuleftRect.colliderect(lvl3llist[i]) or gokurightRect.colliderect(lvl3llist[i]) or gokubottomRect.colliderect(lvl3llist[i]):
                gokuX = 0
                gokuY = 0
                laserSound.play()
                lives = lives - 1

    # game over
    if lives == 0:
        endmenu = True
        playerlose = True
        plaerscore = 0
            
pygame.quit()
    
