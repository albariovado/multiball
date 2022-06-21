import vpython as vpy
from time import *
from random import randrange

# Funzione che crea palline in posizioni e di colori casuali
def createBall(roomWidth, roomDepth, roomHeight):
    radius=randrange(1,50,1)/10
    xInBox=int(roomWidth/2-radius)
    yInBox=int(roomHeight/2-radius)
    zInBox=int(roomDepth/2-radius)
    xPos=randrange(-xInBox,xInBox)
    yPos=randrange(-yInBox,yInBox)
    zPos=randrange(-zInBox,zInBox)
    redColor=randrange(0,100,1)/100
    greenColor=randrange(0,100,1)/100
    blueColor=randrange(0,100,1)/100

    return vpy.sphere(pos=vpy.vector(xPos,yPos,zPos),color=vpy.vector(redColor,greenColor,blueColor),radius=radius)

def randomDelta():
    deltaX=randrange(0,10,1)/10
    deltaY=randrange(0,10,1)/10
    deltaZ=randrange(0,10,1)/10
    seq=[deltaX,deltaY,deltaZ]

    return seq

def create_box():
    yCeiling=(roomHeight/2+wallThickness/2)
    yFloor=-(roomHeight/2+wallThickness/2)
    xSizeCeiling=roomWidth+2*wallThickness
    zSizeCeiling=roomDepth+wallThickness
    xSizeFloor=xSizeCeiling
    zSizeFloor=zSizeCeiling
    xWall=roomWidth/2+wallThickness/2
    zWall=-(wallThickness/2+roomDepth/2)
    xSizeWall=roomWidth+wallThickness*2
    ySizeWall=roomHeight+wallThickness*2
    zSizeWall=roomDepth+wallThickness

    floor=vpy.box(pos=vpy.vector(0,yFloor,0),color=color.white,size=vpy.vector(xSizeFloor,wallThickness,zSizeFloor),opacity=0.2)
    ceiling=vpy.box(pos=vpy.vector(0,yCeiling,0),color=color.white,size=vpy.vector(xSizeCeiling,wallThickness,zSizeCeiling),opacity=0.2)
    rightWall=vpy.box(pos=vpy.vector(xWall,0,0),color=color.white,size=vpy.vector(wallThickness,ySizeWall,zSizeWall),opacity=0.2)
    leftWall=vpy.box(pos=vpy.vector(-xWall,0,0),color=color.white,size=vpy.vector(wallThickness,ySizeWall,zSizeWall),opacity=0.2)
    backWall=vpy.box(pos=vpy.vector(0,0,zWall),color=color.white,size=vpy.vector(xSizeWall,ySizeWall,wallThickness),opacity=0.2)
    frontWall=vpy.box(pos=vpy.vector(0,0,-zWall),color=color.white,size=vpy.vector(xSizeWall,ySizeWall,wallThickness),opacity=0.2)