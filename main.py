import lib
from vpython import rate

# definisco costanti di dimensionamento
wallThickness=int(input('Walls\' thickness? '))
print('Box dimensions.')
roomWidth=int(input('Width: '))
roomDepth=int(input('Depth: '))
roomHeight=int(input('Height: '))

# Creo una sequenza contenitore delle palline:
balls=[]

# Creo una matrice contenitore dei delta:
deltas=[]

lib.create_box(wallThickness, roomWidth, roomDepth, roomHeight)

numBalls=int(input('How many balls?'))

for x in range(numBalls):
    balls.append(lib.createBall(roomWidth, roomDepth, roomHeight))
    deltas.append(lib.randomDelta())

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
