from cordinates import *

def bmove(x,y,z,flag,T,fla):
    try:
        if (int)(x) != mc[z+1][0] :
            x += ((mc[z+1][0]-mc[z][0])/60)
        if (int)(y) != mc[z+1][1]:
            y += ((mc[z+1][1]-mc[z][1])/60)
        if (int)(y) == mc[z+1][1] and (int)(x) == mc[z+1][0]:
            T-=1
            if T == 0:
                flag=0
                fla=0
            else :
                flag=1
                fla=1
            z+=1
    except:
        if (int)(x) != bhc[0][0] :
            x += ((bhc[0][0]-mc[z][0])/60)
        if (int)(y) != bhc[0][1]:
            y += ((bhc[0][1]-mc[z][1])/60)
        if (int)(y) == bhc[0][1] and (int)(x) == bhc[0][0]:
            T-=1
            if T == 0:
                flag=0
                fla=0
            else :
                flag=1
                fla=1
            z=0
    return x,y,z,flag,T,fla


def rmove(x,y,z,flag,T,fla):
    try:
        if (( mc[z][0]== 6) and ( mc[z][1]== 428)):
            if (int)(x) != rhc[0][0] :
                x += ((rhc[0][0]-mc[z][0])/60)
            if (int)(y) != rhc[0][1]:
                y += ((rhc[0][1]-mc[z][1])/60)
            if (int)(y) == rhc[0][1] and (int)(x) == rhc[0][0]:
                T-=1
                if T == 0:
                    flag=0
                    fla=0
                else :
                    flag=1
                    fla=1
                z=0

            return x,y,z,flag,T,fla

        if (int)(x) != mc[z+1][0] :
            x += ((mc[z+1][0]-mc[z][0])/60)
        if (int)(y) != mc[z+1][1]:
            y += ((mc[z+1][1]-mc[z][1])/60)
        if (int)(y) == mc[z+1][1] and (int)(x) == mc[z+1][0]:
            T-=1
            if T == 0:
                flag=0
                fla=0
            else :
                flag=1
                fla=1
            z+=1
    except:
        if (int)(x) != mc[0][0] :
            x += ((mc[0][0]-mc[z][0])/60)
        if (int)(y) != mc[0][1]:
            y += ((mc[0][1]-mc[z][1])/60)
        if (int)(y) == mc[0][1] and (int)(x) == mc[0][0]:
            T-=1
            if T == 0:
                flag=0
                fla=0
            else :
                flag=1
                fla=1
            z=0

    return x,y,z,flag,T,fla
