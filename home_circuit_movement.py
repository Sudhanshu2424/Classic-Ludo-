from cordinates import *

def move_bhc(x,y,z,flag,T,fla):
    try:
        if (int)(x) != bhc[z+1][0] :
            x += ((bhc[z+1][0]-bhc[z][0])/60)
        if (int)(y) != bhc[z+1][1]:
            y += ((bhc[z+1][1]-bhc[z][1])/60)
        if (int)(y) == bhc[z+1][1] and (int)(x) == bhc[z+1][0]:
            T-=1
            if T == 0:
                flag=0
                fla=0
            else :
                flag=1
                fla=1
            z+=1
    except:
            x=450;
            y=450;
            T=0
            if T == 0:
                flag=0
                fla=0
    return x,y,z,flag,T,fla

def move_rhc(x,y,z,flag,T,fla):
    print("gusaa hai",z,rhc[z+1][0],rhc[z+1][1])
    try:
        if (int)(x) != rhc[z+1][0] :
            x += ((rhc[z+1][0]-rhc[z][0])/60)
        if (int)(y) != rhc[z+1][1]:
            y += ((rhc[z+1][1]-rhc[z][1])/60)
        if (int)(y) == rhc[z+1][1] and (int)(x) == rhc[z+1][0]:
            T-=1
            if T == 0:
                flag=0
                fla=0
            else :
                flag=1
                fla=1
            z+=1
    except:
            x=450;
            y=450;
            T=0
            if T == 0:
                flag=0
                fla=0
    return x,y,z,flag,T,fla
