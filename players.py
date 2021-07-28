# pygame import
import pygame
pygame.init()
screen = pygame.display.set_mode((1400,900))

# Players of 44 * 44 size

# Blue players
BlueP1 = pygame.image.load('img/B.png')
BlueP2 = pygame.image.load('img/B.png')
BlueP3 = pygame.image.load('img/B.png')
BlueP4 = pygame.image.load('img/B.png')

def playerB1(x,y):
    screen.blit(BlueP1,(x,y))
def playerB2(x,y):
    screen.blit(BlueP2,(x,y))
def playerB3(x,y):
    screen.blit(BlueP3,(x,y))
def playerB4(x,y):
    screen.blit(BlueP4,(x,y))

# Red players
RedP1= pygame.image.load('img/R.png')
RedP2= pygame.image.load('img/R.png')
RedP3= pygame.image.load('img/R.png')
RedP4= pygame.image.load('img/R.png')

def playerR1(x,y):
    screen.blit(RedP1,(x,y))
def playerR2(x,y):
    screen.blit(RedP2,(x,y))
def playerR3(x,y):
    screen.blit(RedP3,(x,y))
def playerR4(x,y):
    screen.blit(RedP4,(x,y))

# Green players
GreenP1 =pygame.image.load('img/G.png')
GreenP2 =pygame.image.load('img/G.png')
GreenP3 =pygame.image.load('img/G.png')
GreenP4 =pygame.image.load('img/G.png')

def playerG1(x,y):
    screen.blit(GreenP1,(x,y))
def playerG2(x,y):
    screen.blit(GreenP2,(x,y))
def playerG3(x,y):
    screen.blit(GreenP3,(x,y))
def playerG4(x,y):
    screen.blit(GreenP4,(x,y))

# Yellow players
YellowP1 = pygame.image.load('img/Y.png')
YellowP2 = pygame.image.load('img/Y.png')
YellowP3 = pygame.image.load('img/Y.png')
YellowP4 = pygame.image.load('img/Y.png')

def playerY1(x,y):
    screen.blit(YellowP1,(x,y))
def playerY2(x,y):
    screen.blit(YellowP2,(x,y))
def playerY3(x,y):
    screen.blit(YellowP3,(x,y))
def playerY4(x,y):
    screen.blit(YellowP4,(x,y))
