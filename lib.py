import vpython
from random import randrange

def createBall(roomWidth, roomDepth, roomHeight):
    radius=randrange(1,50,1)/10
    xInBox=int(roomWidth/2-radius)
    yInBox=int(roomHeight/2-radius)
    zInBox=int(roomDepth/2-radius)
    xPos=randrange(-xInBox,xInBox)
    yPos=randrange(-yInBox,yInBox)
    zPos=randrange(-zInBox,zInBox)

    return vpython.sphere(pos=vpython.vector(xPos,yPos,zPos),color=randomColor(),radius=radius)

def randomColor():
    redColor=randrange(0,100,1)/100
    greenColor=randrange(0,100,1)/100
    blueColor=randrange(0,100,1)/100
    
    return vpython.vector(redColor, greenColor, blueColor)

def randomDelta():
    deltaX=randrange(0,10,1)/10
    deltaY=randrange(0,10,1)/10
    deltaZ=randrange(0,10,1)/10
    seq=[deltaX,deltaY,deltaZ]

    return seq

def create_box(wallThickness, roomWidth, roomDepth, roomHeight):
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

    vpython.box(pos=vpython.vector(0,yFloor,0),color=vpython.color.white,size=vpython.vector(xSizeFloor,wallThickness,zSizeFloor),opacity=0.2)
    vpython.box(pos=vpython.vector(0,yCeiling,0),color=vpython.color.white,size=vpython.vector(xSizeCeiling,wallThickness,zSizeCeiling),opacity=0.2)
    vpython.box(pos=vpython.vector(xWall,0,0),color=vpython.color.white,size=vpython.vector(wallThickness,ySizeWall,zSizeWall),opacity=0.2)
    vpython.box(pos=vpython.vector(-xWall,0,0),color=vpython.color.white,size=vpython.vector(wallThickness,ySizeWall,zSizeWall),opacity=0.2)
    vpython.box(pos=vpython.vector(0,0,zWall),color=vpython.color.white,size=vpython.vector(xSizeWall,ySizeWall,wallThickness),opacity=0.2)
    vpython.box(pos=vpython.vector(0,0,-zWall),color=vpython.color.white,size=vpython.vector(xSizeWall,ySizeWall,wallThickness),opacity=0.2)
