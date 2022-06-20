from vpython import *
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

    return sphere(pos=vector(xPos,yPos,zPos),color=vector(redColor,greenColor,blueColor),radius=radius)

def randomDelta():
    deltaX=randrange(0,10,1)/10
    deltaY=randrange(0,10,1)/10
    deltaZ=randrange(0,10,1)/10
    seq=[deltaX,deltaY,deltaZ]
    return seq

# definisco costanti di dimensionamento
wallThickness=int(input('Quanto sono spessi i muri? '))
print('Inserisci le dimensioni della scatola.')
roomWidth=int(input('Larghezza: '))
roomDepth=int(input('Profondità: '))
roomHeight=int(input('Altezza: '))

# calcolo tutti i valori basandomi sulle costanti scelte
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

# Creo una sequenza contenitore delle palline:
balls=[]

# Creo una matrice contenitore dei delta:
deltas=[]

floor=box(pos=vector(0,yFloor,0),color=color.white,size=vector(xSizeFloor,wallThickness,zSizeFloor),opacity=0.2)
ceiling=box(pos=vector(0,yCeiling,0),color=color.white,size=vector(xSizeCeiling,wallThickness,zSizeCeiling),opacity=0.2)
rightWall=box(pos=vector(xWall,0,0),color=color.white,size=vector(wallThickness,ySizeWall,zSizeWall),opacity=0.2)
leftWall=box(pos=vector(-xWall,0,0),color=color.white,size=vector(wallThickness,ySizeWall,zSizeWall),opacity=0.2)
backWall=box(pos=vector(0,0,zWall),color=color.white,size=vector(xSizeWall,ySizeWall,wallThickness),opacity=0.2)
frontWall=box(pos=vector(0,0,-zWall),color=color.white,size=vector(xSizeWall,ySizeWall,wallThickness),opacity=0.2)

numBalls=int(input('Quante palle vuoi creare?'))

for x in range(numBalls):
    balls.append(createBall(roomWidth, roomDepth, roomHeight))
    deltas.append(randomDelta())

while True:
    rate(120)

    for x in range(numBalls):
        balls[x].pos.x+=deltas[x][0]
        if balls[x].pos.x>=(roomWidth/2-balls[x].radius) or balls[x].pos.x<=-(roomWidth/2-balls[x].radius):
            deltas[x][0]*=-1
        balls[x].pos.y+=deltas[x][1]
        if balls[x].pos.y>=(roomHeight/2-balls[x].radius) or balls[x].pos.y<=-(roomHeight/2-balls[x].radius):
            deltas[x][1]*=-1
        balls[x].pos.z+=deltas[x][2]
        if balls[x].pos.z>=(roomDepth/2-balls[x].radius) or balls[x].pos.z<=-(roomDepth/2-balls[x].radius):
            deltas[x][2]*=-1

    pass
