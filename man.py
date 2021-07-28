import pygame
import random
import datetime

from cordinates import *
from players import *
from playervariable import *
from movement_mechanics import *
from home_circuit_movement import *


#initializing pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((1400,900))

#Title and logo
pygame.display.set_caption("Ludo Legends")
icn=pygame.image.load('img/icon.png')
pygame.display.set_icon(icn)

# Background image load
background = pygame.image.load('img/bck2.png')


# Dice sprite
sprite=list()
i=1
while i!=31:
    nam='Dice_sprite/'+str(i)+'.png'
    name='jobhi'+str(i)
    name = pygame.image.load(nam)
    sprite.append(name)
    i+=1

def doco(j):
    screen.blit(sprite[j],(1100,700))

def Blue_turn(mposx,mposy,bx,by,bp,fla,flag,cflag,T,dflag):
    #print(datetime.datetime.now(),bx,by)

    if ( ( (mposx >= bx) and (mposx <= (bx+44)) ) and ( (mposy >= by) and (mposy <= (by+44)) ) ) or (fla==1):

        if [bx,by] in bh:
            if dflag == 6:
                bx,by=mc[1]
                cflag=1

        elif [int(bx),int(by)] in bhc:
            fla=1
            bx,by,bp,flag,T,fla=move_bhc(bx,by,bp,flag,T,fla)
            if dflag == 6:
                cflag=1

        else:
            fla=1
            bx,by,bp,flag,T,fla=bmove(bx,by,bp,flag,T,fla)
            if dflag == 6:
                cflag=1
    #print(datetime.datetime.now(),bx,by)
    return mposx,mposy,bx,by,bp,fla,flag,cflag,T

def red_turn(mposx,mposy,rx,ry,rp,fla,flag,cflag,T,dflag):
    #print(datetime.datetime.now(),bx,by)

    if ( ( (mposx >= rx) and (mposx <= (rx+44)) ) and ( (mposy >= ry) and (mposy <= (ry+44)) ) ) or (fla==1):

        print("yaa",[int(rx),int(ry)],rhc)
        if [rx,ry] in rh:
            if dflag == 6:
                rx,ry=mc[14]
                cflag=1

        elif [int(rx),int(ry)] in rhc:
            fla=1
            rx,ry,rp,flag,T,fla=move_rhc(rx,ry,rp,flag,T,fla)
            if dflag == 6:
                cflag=1

        else:
            fla=1
            rx,ry,rp,flag,T,fla=rmove(rx,ry,rp,flag,T,fla)
            if dflag == 6:
                cflag=1



    #print(datetime.datetime.now(),bx,by)
    return mposx,mposy,rx,ry,rp,fla,flag,cflag,T


# Game variables
fla=0
flag=0
dflag=0
cflag=1
i=1
mposx=0
mposy=0
j=0 # managing dice slowness
blist=[ [bp1x,bp1y,bp1,fla_b1] , [bp2x,bp2y,bp2,fla_b2] , [bp3x,bp3y,bp3,fla_b3] , [bp4x,bp4y,bp4,fla_b4] ]
rlist=[ [rp1x,rp1y,rp1,fla_r1] , [rp2x,rp2y,rp2,fla_r2] , [rp3x,rp3y,rp3,fla_r3] , [rp4x,rp4y,rp4,fla_r4] ]


#Game loop
window = True
while window:
    #RGB - Red , Green , Blue
    screen.fill((12,40,60))

    #Background update
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window=False
        # code for detecting mouseclick on ghoti
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if event.button == 1:
                mposx,mposy=pos
                if ( (mposx >= 1100) and (mposx <= (1100+130)) ) and ( (mposy >= 700) and (mposy <= (700+130)) ):
                    if dflag == 0:
                        dflag=(random.randint(1,6))
                        T=dflag
                    else:
                        dflag=0
                else:
                    flag=1


    # Dice and ghoti cordination
    if flag==1 and dflag==0:
        flag=0


    if dflag != 0:

        screen.blit(sprite[23+dflag],(1100,700))

        # code for making the ghoti move to next block
        if flag == 1:

            if cflag == 1:

                #print(blist,type(blist))
                for ito in blist:
                    #print(1,type(ito))
                    mposx,mposy,ito[0],ito[1],ito[2],ito[3],flag,cflag,T=Blue_turn(mposx,mposy,ito[0],ito[1],ito[2],ito[3],flag,cflag,T,dflag)

                fdd=1
                for ito in blist:
                    fs='bp'+str(fdd)+'x'
                    exec("%s = %d" % (fs,ito[0]))
                    fs='bp'+str(fdd)+'y'
                    exec("%s = %d" % (fs,ito[1]))
                    fs='bp'+str(fdd)
                    exec("%s = %d" % (fs,ito[2]))
                    fs='bp'+str(fdd)
                    exec("%s = %d" % (fs,ito[3]))
                    fdd+=1

                for ito in rlist:
                    mposx,mposy,ito[0],ito[1],ito[2],ito[3],flag,cflag,T=red_turn(mposx,mposy,ito[0],ito[1],ito[2],ito[3],flag,cflag,T,dflag)

                fdd=1
                for ito in rlist:
                    fs='rp'+str(fdd)+'x'
                    exec("%s = %d" % (fs,ito[0]))
                    fs='rp'+str(fdd)+'y'
                    exec("%s = %d" % (fs,ito[1]))
                    fs='rp'+str(fdd)
                    exec("%s = %d" % (fs,ito[2]))
                    fs='rp'+str(fdd)
                    exec("%s = %d" % (fs,ito[3]))
                    fdd+=1

    if dflag == 0:
        doco((int)(j))
        j+=0.2
        if (int)(j)==24:
            j=0


    # Updating all 16 players position

    playerB1(bp1x,bp1y)
    playerB2(bp2x,bp2y)
    playerB3(bp3x,bp3y)
    playerB4(bp4x,bp4y)

    playerR1(rp1x,rp1y)
    playerR2(rp2x,rp2y)
    playerR3(rp3x,rp3y)
    playerR4(rp4x,rp4y)

    playerG1(gp1x,gp1y)
    playerG2(gp2x,gp2y)
    playerG3(gp3x,gp3y)
    playerG4(gp4x,gp4y)

    playerY1(yp1x,yp1y)
    playerY2(yp2x,yp2y)
    playerY3(yp3x,yp3y)
    playerY4(yp4x,yp4y)

    pygame.display.update()
