from pygame import *
init()
screen=display.set_mode((800, 600))

enemyBullet1=image.load("images/Bullets/enemyBullet1.png").convert()
enemyBullet2=transform.scale(image.load("images/Bullets/enemyBullet2.png").convert(),(20,20))
enemyBullet3=image.load('images/Bullets/enemyBullet3.png').convert()
enemyBullet4=image.load('images/Bullets/enemyBullet4.png').convert()
enemyBullet5=image.load('images/Bullets/enemyBullet5.png').convert()
enemyBullet6=transform.scale(image.load('images/Bullets/enemyBullet6.png').convert(),(15,15))
enemyBullet7=image.load('images/Bullets/enemyBullet7.png')

splitBullets=[transform.scale(image.load("images/Bullets/splitBullet.png"),(13*x,13*x)) for x in range(1,9)]
for i in range(len(splitBullets)):
    splitBullets[i].set_colorkey((255,255,255))

enemyBullet2.set_colorkey((0,0,0))
enemyBullet3.set_colorkey((0,0,0))
enemyBullet4.set_colorkey((0,0,0))
enemyBullet5.set_colorkey((0,0,0))
enemyBullet6.set_colorkey((0,0,0))
enemyBullet7.set_colorkey((enemyBullet7.get_at((0,0))))

bossBullet1=image.load('images/Bullets/bossBullet1.png').convert()
bossBullet2=image.load('images/Bullets/bossBullet2.png').convert()
bossBullet3=image.load('images/Bullets/bossBullet3.png').convert()
bossBullet1.set_colorkey((0,0,0))
bossBullet2.set_colorkey((0,0,0))
bossBullet3.set_colorkey((0,0,0))

enemyProbeFrames=[]
for i in range(8):
    enemyProbeFrames.append(image.load('images/Enemies/enemyProbe'+str(i)+'.png').convert())
    enemyProbeFrames[i].set_colorkey((0,0,0))

bossProbeFrames=[]
for i in range(8):
    bossProbeFrames.append(image.load('images/Enemies/probeBoss'+str(i)+'.png').convert())
    bossProbeFrames[i].set_colorkey((0,0,0))

alienFrames=[]
for i in range(16):
    alienFrames.append(image.load("images/Enemies/alien/alien"+str(i)+".png").convert())
    alienFrames[i].set_colorkey((0,0,0))
    alienFrames[i]=transform.scale(alienFrames[i],(80,60))

enemyCarrierFrames=[]
for i in range(4):
    enemyCarrierFrames.append(image.load('images/Enemies/alienCarrier'+str(i)+'.png').convert())
    enemyCarrierFrames[i].set_colorkey((255,255,255))
    enemyCarrierFrames[i]=transform.scale(enemyCarrierFrames[i],(138,60))

bossCarrierFrames=[]
for i in range(4):
    bossCarrierFrames.append(image.load('images/Enemies/alienCarrier'+str(i)+'.png').convert())
    bossCarrierFrames[i].set_colorkey((255,255,255))
    bossCarrierFrames[i]=transform.scale(bossCarrierFrames[i],(268,117))

enemyLeaderFrames=[]
for i in range(3):
    enemyLeaderFrames.append(image.load('images/Enemies/alienLeader'+str(i)+'.png').convert())
    enemyLeaderFrames[i].set_colorkey((255,255,255))
    enemyLeaderFrames[i]=transform.scale(enemyLeaderFrames[i],(111,80))
    
    

bossLeaderFrames=[]
for i in range(3):
    bossLeaderFrames.append(image.load('images/Enemies/alienLeader'+str(i)+'.png').convert())
    bossLeaderFrames[i].set_colorkey((255,255,255))

alienGodFrames=[]
for i in range(4):
    alienGodFrames.append(image.load('images/Enemies/alienGod'+str(i)+'.png').convert())   
    alienGodFrames[i].set_colorkey((alienGodFrames[i].get_at((0,0))))
    
spinBoss=[image.load('images/Enemies/spinBoss.png')]
miniSpin=[transform.scale(spinBoss[0],(256,256))]




#[x,y,current attack delay,total attack delay,hp,spawnTime,[attack code,args],[movement code,args],spawned bool,[img],[attackImg],[scoreNum,spawnRange,lifeNum,bombNum]]

    
level1Enemies=[

[20,300,20,100,50,5,'[2,1,2,0]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[20,280,20,100,50,5.5,'[2,1,2,0]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[20,320,20,100,50,5.5,'[2,1,2,0]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[20,260,20,100,50,6,'[2,1,2,0]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[20,340,20,100,50,6,'[2,1,2,0]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],

[600,300,20,100,50,12,'[2,1,2,0]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[600,280,20,100,50,12.5,'[2,1,2,0]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[600,320,20,100,50,12.5,'[2,1,2,0]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[600,260,20,100,50,13,'[2,1,2,0]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[600,340,20,100,50,13,'[2,1,2,0]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],

[310,200,20,80,100,22,'[1,20,3,0,0]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[5,20,0,0]],
[250,200,20,60,40,22,'[2,3,2,10]',[3,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[370,200,20,60,40,22,'[2,3,2,10]',[3,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],

[20,260,20,60,50,35,'[2,1,2,30]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[5,20,0,0]],
[20,300,20,60,50,35,'[2,1,2,30]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[5,20,0,0]],
[20,220,20,60,50,35,'[2,1,2,30]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[5,20,0,0]],
[600,240,20,60,50,35,'[2,1,2,30]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[5,20,0,0]],
[600,280,20,60,50,35,'[2,1,2,30]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[5,20,0,0]],
[600,200,20,60,50,35,'[2,1,2,30]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[5,20,0,0]],

[210,15,20,70,40,45,'[2,1,2,0]',[2,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[420,15,20,70,40,46,'[2,1,2,0]',[2,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[230,15,20,70,40,47,'[2,1,2,0]',[2,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[400,15,20,70,40,48,'[2,1,2,0]',[2,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[250,15,20,70,40,49,'[2,2,2,10]',[2,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[380,15,20,70,40,50,'[2,2,2,10]',[2,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[270,15,20,70,40,51,'[2,2,2,10]',[2,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[360,15,20,70,40,52,'[2,2,2,10]',[2,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],

[290,15,20,60,40,53,'[2,1,2,10]',[2,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[340,15,20,60,40,54,'[2,2,2,10]',[2,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[10,60,20,60,40,55,'[2,1,2,10]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[600,80,20,60,40,56,'[2,2,2,10]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[330,15,20,60,40,57,'[2,1,2,10]',[2,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[300,15,20,60,40,58,'[2,2,2,10]',[2,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[10,80,20,60,40,59,'[2,1,2,10]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[600,100,20,60,40,60,'[2,2,2,10]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],

[310,200,20,60,250,65,'[1,20,3,20,0]',[0],0,[enemyProbeFrames,0],enemyBullet2,[6,20,1,1]],

[290,15,20,65,40,70,'[2,1,2,15]',[2,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[340,15,20,65,40,71,'[2,2,2,15]',[2,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[10,60,20,65,40,72,'[2,1,2,15]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[600,80,20,65,40,73,'[2,2,2,15]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[330,15,20,65,40,74,'[2,1,2,15]',[2,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[300,15,20,65,40,75,'[2,2,2,15]',[2,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[10,80,20,65,40,76,'[2,1,2,15]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[600,100,20,65,40,77,'[2,2,2,15]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],

[210,250,20,80,150,82,'[1,15,4,0,10]',[0],0,[enemyProbeFrames,0],enemyBullet2,[5,20,0,0]],
[420,250,60,80,150,82,'[1,15,4,0,10]',[0],0,[enemyProbeFrames,0],enemyBullet2,[5,20,0,0]],

[20,260,20,65,60,90,'[2,1,2,30]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[5,20,0,0]],
[20,300,20,65,60,92,'[2,1,2,30]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[20,220,20,65,60,94,'[2,1,2,30]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[5,20,0,0]],
[600,240,20,65,60,91,'[2,1,2,30]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[600,280,20,65,60,93,'[2,1,2,30]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[5,20,0,0]],
[600,200,20,65,60,95,'[2,1,2,30]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],

[290,15,20,80,40,100,'[2,2,2,15]',[2,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[340,15,20,80,40,101,'[2,2,2,15]',[2,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[10,60,20,80,40,102,'[2,2,2,15]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[600,80,20,80,40,103,'[2,2,2,15]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[330,15,20,80,40,104,'[2,2,2,15]',[2,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[300,15,20,80,40,105,'[2,3,2,15]',[2,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[10,80,20,40,80,106,'[2,3,2,15]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[600,100,20,80,40,107,'[2,3,2,15]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],

[210,250,20,80,150,114,'[1,15,4,0,10]',[0],0,[enemyProbeFrames,0],enemyBullet2,[5,20,1,0]],
[420,250,60,80,150,114,'[1,15,4,0,10]',[0],0,[enemyProbeFrames,0],enemyBullet2,[5,20,0,1]],
[10,80,20,65,40,114,'[2,5,2,15]',[3,3],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[600,100,20,65,40,114,'[2,5,2,15]',[3,3],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],

[20,260,20,60,50,122,'[2,1,2,30]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[5,20,0,0]],
[20,300,20,60,50,122,'[2,1,2,30]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[5,20,0,0]],
[20,220,20,60,50,122,'[2,1,2,30]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[5,20,0,0]],
[600,240,20,60,50,122,'[2,1,2,30]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[5,20,0,0]],
[600,280,20,60,50,122,'[2,1,2,30]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[5,20,0,0]],
[600,200,20,60,50,122,'[2,1,2,30]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[5,20,0,0]],

[290,15,20,65,40,127,'[2,2,2,15]',[2,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[340,15,20,65,40,128,'[2,2,2,15]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[10,60,20,65,40,129,'[2,2,2,15]',[3,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[500,80,20,65,40,130,'[2,2,2,15]',[2,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[330,15,20,65,40,131,'[2,2,2,15]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[300,15,20,65,40,132,'[2,2,2,15]',[3,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[10,80,20,40,65,133,'[2,2,2,15]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[500,100,20,65,40,134,'[2,2,2,15]',[2,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],

[210,250,20,80,150,139,'[2,5,2,90]',[0],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[420,250,60,80,150,139,'[2,5,2,90]',[0],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],
[10,80,20,40,65,141,'[2,1,2,15]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[5,20,0,0]],
[600,100,20,65,40,141,'[2,1,2,15]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[5,20,0,0]],
[10,80,20,40,65,143,'[2,1,2,15]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[5,20,0,0]],
[600,100,20,65,40,143,'[2,1,2,15]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet1,[5,20,0,0]],

[0,15,10,65,20,148,'[1,4,4,0,10]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[5,20,0,0]],
[600,15,10,65,20,150,'[1,4,4,0,10]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[5,20,0,0]],
[0,15,10,65,20,152,'[1,4,4,0,10]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[5,20,0,0]],
[600,15,10,65,20,154,'[1,4,4,0,10]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[5,20,0,0]],
[0,15,10,65,20,156,'[1,4,4,0,10]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[5,20,0,0]],
[600,15,10,65,20,158,'[1,4,4,0,10]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[5,20,0,0]],
[0,15,10,65,20,160,'[1,4,4,0,10]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[5,20,0,0]],
[600,15,10,65,20,162,'[1,4,4,0,10]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[5,20,0,0]],
[0,15,10,65,20,164,'[1,4,4,0,10]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[5,20,0,0]],
[600,15,10,65,20,166,'[1,4,4,0,10]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[5,20,0,0]],

[210,250,20,80,150,170,'[1,15,4,0,10]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[5,20,1,0]],
[420,250,60,80,150,170,'[1,15,4,0,10]',[1,2,-1],0,[enemyProbeFrames,0],enemyBullet2,[5,20,0,1]],

[315,255,20,60,1000,180, #180
  'choice([[1,50,3,0,5,50],[3,30,10,0,10,5,[1,25],80,False],[2,15,3,40,60],[2,30,randint(-4,4),80,40],[3,20,12,0,15,2,[10,37],50,True],[7,300,5,[20,300,20,100,50,totalTime,"[2,1,2,0]",[3,3],0,[enemyProbeFrames,0],enemyBullet1,[2,20,0,0]],100]])',
  [3,0.1],0,[bossProbeFrames,0],enemyBullet2,[100,75,1,1],'boss'],

         ]

level2Enemies=[

    [0,150,20,80,160,5,'[2,1,2,5]',[1,2,1],0,[alienFrames,0],enemyBullet3,[6,20,0,0]],
    [600,130,20,80,160,6,'[2,1,2,5]',[1,2,1],0,[alienFrames,0],enemyBullet3,[6,20,0,0]],
    [0,110,20,80,160,7,'[2,1,2,5]',[1,2,1],0,[alienFrames,0],enemyBullet3,[6,20,0,0]],
    [600,90,20,80,160,8,'[2,1,2,5]',[1,2,1],0,[alienFrames,0],enemyBullet3,[6,20,0,0]],
    [0,70,20,80,160,9,'[2,1,2,5]',[1,2,1],0,[alienFrames,0],enemyBullet3,[6,20,0,0]],
    [600,50,20,80,160,10,'[2,1,2,5]',[1,2,1],0,[alienFrames,0],enemyBullet3,[6,20,0,0]],

    [310,40,20,60,200,18,'[2,3,2,5]',[3,1.5],0,[alienFrames,0],enemyBullet1,[6,20,0,0]],
    [420,90,50,60,200,18,'[2,3,2,5]',[3,1.5],0,[alienFrames,0],enemyBullet1,[6,20,0,0]],

    [20,100,20,80,160,25,'[2,2,2,5]',[1,2,1],0,[alienFrames,0],enemyBullet3,[6,20,0,0]],
    [20,110,20,80,160,26,'[2,1,1,5]',[1,1.5,1],0,[enemyProbeFrames,0],enemyBullet2,[6,20,0,0]],
    [20,120,20,80,160,27,'[2,2,2,5]',[1,2,1],0,[alienFrames,0],enemyBullet3,[6,20,0,0]],
    [20,130,20,80,160,28,'[2,2,2,5]',[1,2,1],0,[alienFrames,0],enemyBullet3,[6,20,0,0]],
    [20,140,20,80,160,29,'[2,1,1,5]',[1,1.5,1],0,[enemyProbeFrames,0],enemyBullet2,[6,20,0,0]],
    [20,150,20,80,160,30,'[2,2,2,5]',[1,2,1],0,[alienFrames,0],enemyBullet3,[6,20,0,0]],
    [20,160,20,80,160,31,'[2,2,2,5]',[1,2,1],0,[alienFrames,0],enemyBullet3,[6,20,0,0]],
    [20,170,20,80,160,32,'[2,1,1,5]',[1,1.5,1],0,[enemyProbeFrames,0],enemyBullet2,[6,20,0,0]],

    [315,200,50,60,250,45,'[3,25,10,0,15,3,[17,157],None,False]',[3,0.5],0,[enemyProbeFrames,0],enemyBullet3,[7,20,1,0]],
    [310,20,20,60,150,48,'[2,3,2,50]',[3,1],0,[alienFrames,0],enemyBullet1,[6,20,0,0]],
    [420,50,50,60,150,48,'[2,3,2,50]',[3,1],0,[alienFrames,0],enemyBullet1,[6,20,0,0]],
    
    [280,40,1,60,20,52,'[2,5,2,100]',[1,1,-1],0,[enemyProbeFrames,0],enemyBullet1,[6,20,0,0]],
    [450,90,1,60,20,55,'[2,5,2,100]',[1,1,1],0,[enemyProbeFrames,0],enemyBullet1,[6,20,0,0]],
    [250,60,1,60,20,58,'[2,5,2,100]',[1,1,-1],0,[enemyProbeFrames,0],enemyBullet1,[6,20,0,0]],
    [430,110,1,60,20,61,'[2,5,2,100]',[1,1,1],0,[enemyProbeFrames,0],enemyBullet1,[6,20,0,0]],
    [230,80,1,60,20,64,'[2,5,2,100]',[1,1,-1],0,[enemyProbeFrames,0],enemyBullet1,[6,20,0,0]],
    [400,130,1,60,20,67,'[2,5,2,100]',[1,1,1],0,[enemyProbeFrames,0],enemyBullet1,[6,20,0,0]],
    [200,100,1,60,20,70,'[2,5,2,100]',[1,1,-1],0,[enemyProbeFrames,0],enemyBullet1,[6,20,0,0]],
    [370,150,1,40,250,73,'[2,40,2,180]',[1,1,1],0,[enemyProbeFrames,0],enemyBullet3,[8,20,1,1]],

    [200,20,20,60,150,86,'[2,3,1,50]',[2,2,1],0,[alienFrames,0],enemyBullet3,[6,20,0,0]],
    [400,20,50,60,150,86,'[2,3,1,50]',[2,2,1],0,[alienFrames,0],enemyBullet3,[6,20,0,0]],
    [230,20,20,65,150,89,'[2,3,1.5,50]',[2,2,1],0,[alienFrames,0],enemyBullet3,[6,20,0,0]],
    [370,20,50,65,150,89,'[2,3,1.5,50]',[2,2,1],0,[alienFrames,0],enemyBullet3,[6,20,0,0]],
    [260,20,20,70,150,92,'[2,3,2,50]',[2,2,1],0,[alienFrames,0],enemyBullet3,[6,20,0,0]],
    [340,20,50,70,150,92,'[2,3,2,50]',[2,2,1],0,[alienFrames,0],enemyBullet3,[6,20,0,0]],

    [260,20,20,100,300,101,'[2,3,3,10]',[2,2,1],0,[alienFrames,0],enemyBullet1,[6,20,0,0]],
    [260,0,50,60,30,102,'[2,5,2,180]',[2,2,1],0,[enemyProbeFrames,0],enemyBullet3,[6,20,0,0]],
    [435,20,20,100,300,105,'[2,3,3,10]',[2,2,1],0,[alienFrames,0],enemyBullet1,[6,20,0,0]],
    [435,0,50,60,30,106,'[2,5,2,180]',[2,2,1],0,[enemyProbeFrames,0],enemyBullet3,[6,20,0,0]],
    [300,20,20,100,300,109,'[2,3,3,10]',[2,2,1],0,[alienFrames,0],enemyBullet1,[6,20,0,0]],
    [300,0,50,60,30,110,'[2,5,2,180]',[2,2,1],0,[enemyProbeFrames,0],enemyBullet3,[6,20,0,0]],
    [375,20,20,100,300,113,'[2,3,3,10]',[2,2,1],0,[alienFrames,0],enemyBullet1,[6,20,0,0]],
    [375,0,50,60,30,114,'[2,5,2,180]',[2,2,1],0,[enemyProbeFrames,0],enemyBullet3,[6,20,0,0]],

    [600,100,20,80,160,121,'[2,2,2,5]',[1,2,1],0,[alienFrames,0],enemyBullet3,[6,20,0,0]],
    [600,110,20,80,160,122,'[2,1,1,5]',[1,1.5,1],0,[enemyProbeFrames,0],enemyBullet2,[6,20,0,0]],
    [600,120,20,80,160,123,'[2,2,2,5]',[1,2,1],0,[alienFrames,0],enemyBullet3,[6,20,0,0]],
    [600,130,20,80,160,124,'[2,2,2,5]',[1,2,1],0,[alienFrames,0],enemyBullet3,[6,20,0,0]],
    [600,140,20,80,160,125,'[2,1,1,5]',[1,1.5,1],0,[enemyProbeFrames,0],enemyBullet2,[6,20,0,0]],
    [600,150,20,80,160,126,'[2,2,2,5]',[1,2,1],0,[alienFrames,0],enemyBullet3,[6,20,0,0]],
    [600,160,20,80,160,127,'[2,2,2,5]',[1,2,1],0,[alienFrames,0],enemyBullet3,[6,20,0,0]],
    [600,170,20,80,160,128,'[2,1,1,5]',[1,1.5,1],0,[enemyProbeFrames,0],enemyBullet2,[6,20,0,0]],

    [210,200,20,80,250,145,'[1,40,2,0,17]',[1,2,1],0,[alienFrames,0],enemyBullet2,[7,20,1,0]],
    [420,200,60,80,250,145,'[1,40,2,0,17]',[1,2,1],0,[alienFrames,0],enemyBullet2,[7,20,0,1]],
    [20,160,20,80,160,150,'[2,3,2,5]',[3,0.5],0,[alienFrames,0],enemyBullet3,[6,20,0,0]],
    [600,160,20,80,160,150,'[2,3,2,5]',[3,0.5],0,[alienFrames,0],enemyBullet3,[6,20,0,0]],
    [20,160,20,80,160,150,'[2,3,2,5]',[3,0.5],0,[alienFrames,0],enemyBullet3,[6,20,0,0]],
    [600,160,20,80,160,150,'[2,3,2,5]',[3,0.5],0,[alienFrames,0],enemyBullet3,[6,20,0,0]],

    [20,260,20,60,150,162,'[2,3,2,10]',[1,2,1],0,[alienFrames,0],enemyBullet3,[5,20,0,0]],
    [20,300,20,60,150,164,'[2,3,2,10]',[1,2,1],0,[alienFrames,0],enemyBullet3,[5,20,0,0]],
    [20,220,20,60,150,166,'[2,3,2,10]',[1,2,1],0,[alienFrames,0],enemyBullet3,[5,20,0,0]],
    [600,240,20,60,150,163,'[2,3,2,10]',[1,2,1],0,[alienFrames,0],enemyBullet3,[5,20,0,0]],
    [600,280,20,60,150,165,'[2,3,2,10]',[1,2,1],0,[alienFrames,0],enemyBullet3,[5,20,0,0]],
    [600,200,20,60,150,167,'[2,3,2,10]',[1,2,1],0,[alienFrames,0],enemyBullet3,[5,20,0,0]],

    [200,20,20,60,150,176,'[2,3,1,50]',[2,2,1],0,[alienFrames,0],enemyBullet3,[6,20,0,0]],
    [400,20,50,60,150,176,'[2,3,1,50]',[2,2,1],0,[alienFrames,0],enemyBullet3,[6,20,0,0]],
    [230,20,20,65,150,178,'[2,3,1.5,50]',[2,2,1],0,[alienFrames,0],enemyBullet3,[6,20,0,0]],
    [370,20,50,65,150,178,'[2,3,1.5,50]',[2,2,1],0,[alienFrames,0],enemyBullet3,[6,20,0,0]],
    [260,20,20,70,150,180,'[2,3,2,50]',[2,2,1],0,[alienFrames,0],enemyBullet3,[6,20,0,0]],
    [340,20,50,70,150,180,'[2,3,2,50]',[2,2,1],0,[alienFrames,0],enemyBullet3,[6,20,0,0]],

    [20,100,1,40,300,188,'[2,40,3,150]',[1,1,1],0,[enemyCarrierFrames,0],enemyBullet4,[8,20,1,0]],
    [600,200,21,40,300,188,'[2,40,3,150]',[1,1,1],0,[enemyCarrierFrames,0],enemyBullet4,[8,20,0,1]],

    [315,100,20,60,3000,200, #200
      'choice([[4,3,20,30,-30,8,80],[2,50,2.5,90,50],[3,45,10,0,25,3,[17,60],70,True],[2,15,3,25,40],[3,50,25,0,15,4,[37,34],50,False],[7,300,4,[20,300,20,100,80,totalTime,"[2,3,2,10]",[3,1],0,[enemyProbeFrames,0],enemyBullet3,[2,20,0,0]],100]])',
      [3,0.1],0,[bossCarrierFrames,0],bossBullet1,[150,100,1,1],'boss'],


    ]

level3Enemies=[
    [20,200,20,60,100,5,'[1,25,2,0,17]',[1,2,1],0,[alienFrames,0],enemyBullet3,[10,20,0,0]],
    [580,200,60,60,100,5,'[1,25,2,0,17]',[1,2,1],0,[alienFrames,0],enemyBullet3,[10,20,0,0]],

    [20,200,20,60,150,12,'[2,3,2,10]',[1,2,1],0,[alienFrames,0],enemyBullet2,[8,20,0,0]],
    [600,200,20,60,150,12,'[2,3,2,10]',[1,2,1],0,[alienFrames,0],enemyBullet2,[8,20,0,0]],
    [20,200,20,60,150,15,'[2,3,2,10]',[1,2,1],0,[alienFrames,0],enemyBullet2,[8,20,0,0]],
    [600,200,20,60,150,15,'[2,3,2,10]',[1,2,1],0,[alienFrames,0],enemyBullet2,[8,20,0,0]],
    [20,200,20,60,150,18,'[2,3,2,10]',[1,2,1],0,[alienFrames,0],enemyBullet2,[8,20,0,0]],
    [600,200,20,60,150,18,'[2,3,2,10]',[1,2,1],0,[alienFrames,0],enemyBullet2,[8,20,0,0]],
    [20,200,20,60,150,21,'[2,3,2,10]',[1,2,1],0,[alienFrames,0],enemyBullet2,[8,20,0,0]],
    [600,200,20,60,150,21,'[2,3,2,10]',[1,2,1],0,[alienFrames,0],enemyBullet2,[8,20,0,0]],

    [20,100,20,70,200,30,'[2,20,3,30]',[1,1,1],0,[enemyCarrierFrames,0],enemyBullet4,[10,20,0,0]],
    [600,200,55,70,200,30,'[2,20,3,30]',[1,1,1],0,[enemyCarrierFrames,0],enemyBullet4,[10,20,0,0]],

    [20,200,30,1000,50,42,'[7,200,4,[20,300,20,100,80,totalTime,"[1,10,2,0,13]",[1,1,-1],0,[alienFrames,0],enemyBullet3,[2,20,0,0]]]',[1,1,1],0,[enemyCarrierFrames,0],enemyBullet4,[5,20,0,0]],
    [600,200,30,1000,50,47,'[7,200,4,[20,300,20,100,80,totalTime,"[1,10,2,0,13]",[1,1,1],0,[alienFrames,0],enemyBullet3,[2,20,0,0]]]',[1,1,1],0,[enemyCarrierFrames,0],enemyBullet4,[5,20,0,0]],
    [20,200,30,1000,50,52,'[7,200,4,[20,300,20,100,80,totalTime,"[1,10,2,0,13]",[1,1,-1],0,[alienFrames,0],enemyBullet3,[2,20,0,0]]]',[1,1,1],0,[enemyCarrierFrames,0],enemyBullet4,[5,20,0,0]],
    [600,200,30,1000,50,57,'[7,200,4,[20,300,20,100,80,totalTime,"[1,10,2,0,13]",[1,1,1],0,[alienFrames,0],enemyBullet3,[2,20,0,0]]]',[1,1,1],0,[enemyCarrierFrames,0],enemyBullet4,[5,20,0,0]],

    [315,50,20,35,500,66,'[2,75,3,180]',[3,0.4],0,[bossProbeFrames,0],enemyBullet5,[25,40,1,1]],

    [600,140,20,55,150,74,'[2,4,2,10]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[8,20,0,0]],
    [600,150,20,55,150,75,'[2,4,2,10]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[8,20,0,0]],
    [600,160,20,55,150,76,'[2,4,2,10]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[8,20,0,0]],
    [600,130,55,65,250,75.5,'[1,20,3,0,37]',[1,2,1],0,[enemyCarrierFrames,0],enemyBullet4,[10,20,0,0]],

    [20,210,20,55,150,85,'[2,4,2,10]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[8,20,0,0]],
    [20,200,20,55,150,86,'[2,4,2,10]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[8,20,0,0]],
    [20,190,20,55,150,87,'[2,4,2,10]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[8,20,0,0]],
    [20,230,55,65,250,86.5,'[1,20,3,0,37]',[1,2,1],0,[enemyCarrierFrames,0],enemyBullet4,[15,20,0,0]],

    [600,140,20,55,150,96,'[2,4,2,10]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[8,20,0,0]],
    [600,130,20,55,150,97,'[2,4,2,10]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[8,20,0,0]],
    [600,120,20,55,150,98,'[2,4,2,10]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[8,20,0,0]],
    [600,110,55,65,250,97.5,'[1,20,3,0,37]',[1,2,1],0,[enemyCarrierFrames,0],enemyBullet4,[20,20,1,0]],

    [20,160,20,55,150,107,'[2,4,2,10]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[8,20,0,0]],
    [20,150,20,55,150,108,'[2,4,2,10]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[8,20,0,0]],
    [20,170,20,55,150,109,'[2,4,2,10]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[8,20,1,0]],
    [20,160,55,65,250,108.5,'[1,20,3,0,37]',[1,2,1],0,[enemyCarrierFrames,0],enemyBullet4,[25,20,0,1]],

    [315,200,30,300,250,117,'[7,400,4,[20,300,20,100,80,totalTime,"[1,5,2,0,13]",[1,2,1],0,[alienFrames,0],enemyBullet3,[2,20,0,0]]]',[1,1,1],0,[enemyCarrierFrames,0],enemyBullet4,[30,50,1,2]],

    [260,20,20,100,300,122,'[2,3,3,10]',[2,2,1],0,[alienFrames,0],enemyBullet3,[8,20,0,0]],
    [260,0,50,60,30,124,'[2,5,3,130]',[2,2,1],0,[enemyProbeFrames,0],enemyBullet2,[8,20,0,0]],
    [435,20,20,100,300,126,'[2,3,3,10]',[2,2,1],0,[alienFrames,0],enemyBullet3,[8,20,0,0]],
    [435,0,50,60,30,128,'[2,5,3,130]',[2,2,1],0,[enemyProbeFrames,0],enemyBullet2,[8,20,0,0]],
    [300,20,20,100,300,130,'[2,3,3,10]',[2,2,1],0,[alienFrames,0],enemyBullet3,[8,20,0,0]],
    [300,0,50,60,30,132,'[2,5,3,130]',[2,2,1],0,[enemyProbeFrames,0],enemyBullet2,[8,20,0,0]],
    [375,20,20,100,300,134,'[2,3,3,10]',[2,2,1],0,[alienFrames,0],enemyBullet3,[8,20,0,0]],
    [375,0,50,60,30,136,'[2,5,3,130]',[2,2,1],0,[enemyProbeFrames,0],enemyBullet2,[8,20,0,0]],

    [20,100,20,80,130,142,'[2,3,2,5]',[1,2,1],0,[alienFrames,0],enemyBullet3,[8,20,0,0]],
    [20,110,20,80,130,143,'[2,2,3,5]',[1,1.5,1],0,[enemyProbeFrames,0],enemyBullet2,[8,20,0,0]],
    [20,120,20,80,130,144,'[2,3,3,5]',[1,2,1],0,[alienFrames,0],enemyBullet3,[8,20,0,0]],
    [20,130,20,80,130,145,'[2,3,2,5]',[1,2,1],0,[alienFrames,0],enemyBullet3,[8,20,0,0]],
    [315,60,20,65,250,145.5,'[2,40,3,150]',[0],0,[enemyCarrierFrames,0],enemyBullet4,[15,20,0,0]],
    [20,140,20,80,130,146,'[2,2,3,5]',[1,1.5,1],0,[enemyProbeFrames,0],enemyBullet2,[8,20,0,0]],
    [20,150,20,80,130,147,'[2,3,2,5]',[1,2,1],0,[alienFrames,0],enemyBullet3,[8,20,0,0]],
    [20,160,20,80,130,148,'[2,3,3,5]',[1,2,1],0,[alienFrames,0],enemyBullet3,[8,20,0,0]],
    [20,170,20,80,130,149,'[2,2,2,5]',[1,1.5,1],0,[enemyProbeFrames,0],enemyBullet2,[8,20,0,0]],

    [315,250,20,100,1000,160,'[5,13,2,0,13,150]',[0],0,[bossProbeFrames,0],enemyBullet5,[25,50,1,1]],

    [600,140,20,55,150,174,'[2,4,3,10]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[8,20,0,0]],
    [600,150,20,55,150,175,'[2,4,3,10]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[8,20,0,0]],
    [600,160,20,55,150,176,'[2,4,3,10]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[8,20,0,0]],
    [600,130,55,65,250,175.5,'[1,20,4,0,37]',[1,2,1],0,[enemyCarrierFrames,0],enemyBullet4,[15,20,1,1]],

    [20,140,20,55,150,177,'[2,4,3,10]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[8,20,0,0]],
    [20,150,20,55,150,178,'[2,4,3,10]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[8,20,0,0]],
    [20,160,20,55,150,179,'[2,4,3,10]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[8,20,0,0]],
    [20,130,55,65,250,178.5,'[1,20,4,0,37]',[1,2,1],0,[enemyCarrierFrames,0],enemyBullet4,[15,20,1,1]],

    [315,250,55,150,65,195,'[1,20,4,0,37]',[0],0,[enemyCarrierFrames,0],enemyBullet4,[15,20,1,1]],
    
    [315,250,20,60,2700,198, #198
      'choice([[1,60,4,0,45,60],[2,75,2,180,80],[6,10,2,0,10,1,[17,60],10,200,100,True],[3,30,15,0,15,4,[17,13],60,True],[7,400,6,[20,300,20,100,2,totalTime,"[2,7,1,25]",[1,2,1],0,[alienFrames,0],enemyBullet6,[2,20,0,0]],240]])',
      [0],0,[spinBoss,0],bossBullet3,[250,100,2,2],'boss'],
    

    ]

level4Enemies=[

    [20,200,30,300,180,5,'[7,400,4,[20,300,20,60,40,totalTime,"[1,20,4,0,13]",[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[2,20,0,0]]]',[1,1,1],0,[enemyCarrierFrames,0],enemyBullet4,[30,50,0,0]],
    [600,150,30,300,180,14,'[7,400,4,[20,300,20,60,40,totalTime,"[1,20,4,0,13]",[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[2,20,0,0]]]',[1,1,1],0,[enemyCarrierFrames,0],enemyBullet4,[30,50,0,0]],
    [20,250,30,300,180,23,'[7,400,4,[20,300,20,60,40,totalTime,"[1,20,4,0,13]",[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[2,20,0,0]]]',[1,1,1],0,[enemyCarrierFrames,0],enemyBullet4,[30,50,0,0]],
    [600,100,30,300,180,34,'[7,400,4,[20,300,20,60,40,totalTime,"[1,20,4,0,13]",[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[2,20,0,0]]]',[1,1,1],0,[enemyCarrierFrames,0],enemyBullet4,[30,50,0,0]],

    [190,160,20,55,150,48,'[2,10,3,10]',[0],0,[enemyProbeFrames,0],bossBullet3,[8,20,0,0]],
    [240,170,20,55,150,48,'[2,10,3,10]',[0],0,[enemyProbeFrames,0],bossBullet3,[8,20,0,0]],
    [440,160,20,55,150,48,'[2,10,3,10]',[0],0,[enemyProbeFrames,0],bossBullet3,[8,20,0,0]],
    [390,170,20,55,150,48,'[2,10,3,10]',[0],0,[enemyProbeFrames,0],bossBullet3,[8,20,0,0]],
    [305,15,20,70,130,50,'[2,15,3,50]',[2,1,1],0,[alienFrames,0],enemyBullet3,[8,20,1,1]],

    [20,260,20,60,100,62,'[1,11,3,0,13]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet3,[9,20,0,0]],
    [20,300,20,60,100,64,'[1,11,3,0,13]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet3,[9,20,0,0]],
    [20,220,20,60,100,66,'[1,11,3,0,13]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet3,[9,20,0,0]],
    [600,240,20,60,100,63,'[1,11,3,0,13]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet3,[9,20,0,0]],
    [600,280,20,60,100,65,'[1,11,3,0,13]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet3,[9,20,0,0]],
    [600,200,20,60,100,67,'[1,11,3,0,13]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet3,[9,20,0,0]],
    [305,15,20,70,450,73,'[4,2,20,60,-60,8]',[2,0.1,1],0,[alienFrames,0],enemyBullet3,[8,20,0,1]],

    [315,250,20,60,550,83,'[5,17,2,0,13,150]',[0],0,[bossProbeFrames,0],enemyBullet5,[25,50,1,1]], 

    [20,200,30,500,250,92,'[7,300,4,[20,300,20,100,180,totalTime,"[1,15,2.5,0,13]",[1,1,-1],0,[alienFrames,0],enemyBullet3,[5,20,0,0]]]',[1,1,1],0,[enemyCarrierFrames,0],enemyBullet4,[9,20,0,0]],
    [600,200,30,500,250,98,'[7,300,4,[20,300,20,100,180,totalTime,"[1,15,2.5,0,13]",[1,1,1],0,[alienFrames,0],enemyBullet3,[5,20,0,0]]]',[1,1,1],0,[enemyCarrierFrames,0],enemyBullet4,[9,20,0,0]],
    [20,200,30,500,250,104,'[7,300,4,[20,300,20,100,180,totalTime,"[1,15,2.5,0,13]",[1,1,-1],0,[alienFrames,0],enemyBullet3,[5,20,0,0]]]',[1,1,1],0,[enemyCarrierFrames,0],enemyBullet4,[9,20,0,0]],
    [600,200,30,500,250,110,'[7,300,4,[20,300,20,100,180,totalTime,"[1,15,2.5,0,13]",[1,1,1],0,[alienFrames,0],enemyBullet3,[5,20,0,0]]]',[1,1,1],0,[enemyCarrierFrames,0],enemyBullet4,[9,20,0,0]],
    
    [315,250,20,60,800,122,'[6,8,10,0,25,2,[17,60],15,100,None,True]',[0],0,[miniSpin,0],enemyBullet2,[25,10,1,1]],
    
    [20,200,30,300,80,135,'[7,400,4,[20,300,20,240,40,totalTime,"[5,13,2,0,13,150]",[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[2,20,0,0]]]',[1,1,1],0,[enemyCarrierFrames,0],enemyBullet4,[30,50,0,0]],
    [20,200,30,300,80,143,'[7,400,4,[20,300,20,240,40,totalTime,"[5,13,2,0,13,150]",[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[2,20,0,0]]]',[1,1,1],0,[enemyCarrierFrames,0],enemyBullet4,[30,50,0,0]],
    [20,200,30,300,80,151,'[7,400,4,[20,300,20,240,40,totalTime,"[5,13,2,0,13,150]",[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[2,20,0,0]]]',[1,1,1],0,[enemyCarrierFrames,0],enemyBullet4,[30,50,0,0]],
    [20,200,30,300,80,159,'[7,400,4,[20,300,20,240,40,totalTime,"[5,13,2,0,13,150]",[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[2,20,0,0]]]',[1,1,1],0,[enemyCarrierFrames,0],enemyBullet4,[30,50,0,0]],

    [315,100,20,20,500,165,'[3,30,45,0,13,4,[0,10],None]',[0],0,[enemyProbeFrames,0],enemyBullet2,[50,20,2,2]], 

    [210,100,20,45,200,175,'[1,40,4,0,27]',[0],0,[enemyLeaderFrames,0],enemyBullet7,[20,20,0,0]],
    [420,100,42,45,200,175,'[1,40,4,0,27]',[0],0,[enemyLeaderFrames,0],enemyBullet7,[20,20,0,0]],

    [600,200,30,300,80,186,'[7,400,4,[20,300,20,240,40,totalTime,"[5,13,2,0,13,150]",[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[2,20,0,0]]]',[1,1,1],0,[enemyCarrierFrames,0],enemyBullet4,[30,50,0,0]],
    [600,200,30,300,80,194,'[7,400,4,[20,300,20,240,40,totalTime,"[5,13,2,0,13,150]",[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[2,20,0,0]]]',[1,1,1],0,[enemyCarrierFrames,0],enemyBullet4,[30,50,0,0]],
    [600,200,30,300,80,202,'[7,400,4,[20,300,20,240,40,totalTime,"[5,13,2,0,13,150]",[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[2,20,0,0]]]',[1,1,1],0,[enemyCarrierFrames,0],enemyBullet4,[30,50,0,0]],
    [600,200,30,300,80,210,'[7,400,4,[20,300,20,240,40,totalTime,"[5,13,2,0,13,150]",[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[2,20,0,0]]]',[1,1,1],0,[enemyCarrierFrames,0],enemyBullet4,[30,50,0,0]],

    [210,100,20,45,500,220,'[2,20,3,30]',[3,1],0,[enemyLeaderFrames,0],enemyBullet7,[20,20,2,0]],
    [420,100,42,45,500,220,'[2,20,3,30]',[3,1],0,[enemyLeaderFrames,0],enemyBullet7,[20,20,0,2]],

    [315,250,20,60,5000,230, #230
      'choice([[2,20,4,25,60],[2,100,1.5,180,60],[1,25,2,0,10,40],[5,8,5,0,13,150,80],[4,2,20,30,-30,8,60],[7,400,6,[20,300,20,100,2,totalTime,"[2,10,3,50]",[1,2,1],0,[enemyProbeFrames,0],enemyBullet6,[2,20,0,0]],100]])',
      [0],0,[bossLeaderFrames,0],enemyBullet7,[250,100,2,2],'boss'],
   ]

level5Enemies=[

    [20,300,20,60,150,5,'[2,15,4,0]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet3,[9,20,0,0]],
    [20,280,20,60,150,5.5,'[2,5,4,0]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet3,[9,20,0,0]],
    [20,320,20,60,150,5.5,'[2,5,4,0]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet3,[9,20,0,0]],
    [20,260,20,60,150,6,'[2,5,4,0]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet3,[9,20,0,0]],
    [20,340,20,60,150,6,'[2,5,4,0]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet3,[9,20,0,0]],

    [600,300,20,60,150,13,'[2,5,4,0]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet3,[9,20,0,0]],
    [600,280,20,60,150,13.5,'[2,5,4,0]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet3,[9,20,0,0]],
    [600,320,20,60,150,13.5,'[2,5,4,0]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet3,[9,20,0,0]],
    [600,260,20,60,150,14,'[2,5,4,0]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet3,[9,20,0,0]],
    [600,340,20,60,150,14,'[2,5,4,0]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet3,[9,20,0,0]],

    [310,200,20,100,250,24,'[5,13,3,0,13,100]',[1,2,1],0,[enemyProbeFrames,0],bossBullet2,[12,20,0,0]],
    [250,200,20,60,80,24,'[2,5,4,10]',[3,1],0,[enemyProbeFrames,0],enemyBullet3,[9,20,0,0]],
    [370,200,20,60,80,24,'[2,5,4,10]',[3,1],0,[enemyProbeFrames,0],enemyBullet3,[9,20,0,0]],

    [20,260,20,60,100,35,'[2,5,4,30]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[10,20,0,0]],
    [20,300,40,60,100,36,'[1,8,2,0,10]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[10,20,0,0]],
    [20,220,20,60,100,37,'[2,5,4,30]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[10,20,0,0]],
    [600,240,60,60,100,38,'[1,8,2,0,10]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[10,20,0,0]],
    [600,280,20,60,100,39,'[2,5,4,30]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[10,20,0,0]],
    [600,200,80,60,100,40,'[1,8,2,0,10]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[10,20,0,0]],

    [20,100,20,70,160,50,'[2,5,4,5]',[1,2,1],0,[alienFrames,0],enemyBullet3,[10,20,0,0]],
    [20,110,30,70,160,51,'[2,4,3,5]',[1,1.5,1],0,[enemyProbeFrames,0],enemyBullet2,[10,20,0,0]],
    [20,120,40,70,160,52,'[2,5,4,5]',[1,2,1],0,[alienFrames,0],enemyBullet3,[10,20,0,0]],
    [20,130,50,70,160,53,'[2,5,4,5]',[1,2,1],0,[alienFrames,0],enemyBullet3,[10,20,0,0]],
    [20,140,60,70,160,54,'[2,4,3,5]',[1,1.5,1],0,[enemyProbeFrames,0],enemyBullet2,[10,20,0,0]],
    [20,150,70,70,160,55,'[2,5,4,5]',[1,2,1],0,[alienFrames,0],enemyBullet3,[10,20,0,0]],
    [20,160,10,70,160,56,'[2,5,4,5]',[1,2,1],0,[alienFrames,0],enemyBullet3,[10,20,0,0]],
    [20,170,20,70,160,57,'[2,4,3,5]',[1,1.5,1],0,[enemyProbeFrames,0],enemyBullet2,[10,20,0,0]],

    [210,200,20,80,250,70,'[1,40,4,0,17]',[1,2,1],0,[alienFrames,0],enemyBullet2,[17,20,1,0]],
    [420,200,60,80,250,70,'[1,40,4,0,17]',[1,2,1],0,[alienFrames,0],enemyBullet2,[17,20,0,1]],
    [20,160,20,80,130,70,'[2,5,3,3]',[3,0.3],0,[alienFrames,0],enemyBullet3,[10,20,0,0]],
    [600,160,20,80,130,70,'[2,5,3,3]',[3,0.3],0,[alienFrames,0],enemyBullet3,[10,20,0,0]],
    [20,160,20,80,130,70,'[2,5,3,3]',[3,0.3],0,[alienFrames,0],enemyBullet3,[10,20,0,0]],
    [600,160,20,80,130,70,'[2,5,3,3]',[3,0.3],0,[alienFrames,0],enemyBullet3,[10,20,0,0]],

    [20,210,20,55,150,87,'[2,6,2,5]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[8,20,0,0]],
    [20,200,20,55,150,88,'[2,6,2,5]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[8,20,0,0]],
    [20,190,20,55,150,89,'[2,6,2,5]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[8,20,0,0]],
    [20,230,55,65,250,88.5,'[1,30,3.5,0,37]',[1,2,1],0,[enemyCarrierFrames,0],enemyBullet4,[20,20,0,0]],

    [600,140,20,55,150,98,'[2,6,2,5]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[8,20,0,0]],
    [600,130,20,55,150,99,'[2,6,2,5]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[8,20,0,0]],
    [600,120,20,55,150,100,'[2,6,2,5]',[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[8,20,0,0]],
    [600,110,55,65,250,99.5,'[1,30,3.5,0,37]',[1,2,1],0,[enemyCarrierFrames,0],enemyBullet4,[20,20,0,0]],

    [20,200,30,1000,100,110,'[7,300,8,[20,300,20,80,180,totalTime,"[1,10,2,0,13]",[1,1,-1],0,[alienFrames,0],enemyBullet3,[2,20,0,0]]]',[1,1,1],0,[enemyCarrierFrames,0],enemyBullet4,[15,20,0,0]],
    [600,200,30,1000,100,116,'[7,300,8,[20,300,20,80,180,totalTime,"[1,10,2,0,13]",[1,1,1],0,[alienFrames,0],enemyBullet3,[2,20,0,0]]]',[1,1,1],0,[enemyCarrierFrames,0],enemyBullet4,[15,20,0,0]],
    [20,200,30,1000,150,123,'[7,300,12,[20,300,20,60,180,totalTime,"[1,10,2,0,13]",[1,1,-1],0,[alienFrames,0],enemyBullet3,[2,20,0,0]]]',[1,1,1],0,[enemyCarrierFrames,0],enemyBullet4,[15,20,1,1]],
    [600,200,30,1000,150,130,'[7,300,12,[20,300,20,60,180,totalTime,"[1,10,2,0,13]",[1,1,1],0,[alienFrames,0],enemyBullet3,[2,20,0,0]]]',[1,1,1],0,[enemyCarrierFrames,0],enemyBullet4,[15,20,1,1]],

    [315,250,20,80,1000,140,'[5,11,2,0,13,150]',[0],0,[bossProbeFrames,0],enemyBullet7,[25,50,1,1]],

    [210,100,20,55,500,150,'[2,12,3,40]',[3,1],0,[enemyLeaderFrames,0],enemyBullet7,[20,20,0,0]],
    [420,100,42,55,500,150,'[2,12,3,40]',[3,1],0,[enemyLeaderFrames,0],enemyBullet7,[20,20,0,0]],
    [315,250,20,60,800,156,'[6,8,10,0,25,2,[17,60],15,100,None,True]',[0],0,[miniSpin,0],enemyBullet2,[25,10,1,1]],

    [600,200,30,300,80,166,'[7,400,6,[20,300,20,240,40,totalTime,"[5,13,2,0,13,150]",[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[2,20,0,0]]]',[1,1,1],0,[enemyCarrierFrames,0],enemyBullet4,[30,50,0,0]],
    [20,200,30,300,80,174,'[7,400,6,[20,300,20,240,40,totalTime,"[5,13,2,0,13,150]",[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[2,20,0,0]]]',[1,1,1],0,[enemyCarrierFrames,0],enemyBullet4,[30,50,0,0]],
    [600,200,30,300,80,182,'[7,400,6,[20,300,20,240,40,totalTime,"[5,13,2,0,13,150]",[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[2,20,0,0]]]',[1,1,1],0,[enemyCarrierFrames,0],enemyBullet4,[30,50,0,0]],
    [20,200,30,300,80,190,'[7,400,6,[20,300,20,240,40,totalTime,"[5,13,2,0,13,150]",[1,2,1],0,[enemyProbeFrames,0],enemyBullet2,[2,20,0,0]]]',[1,1,1],0,[enemyCarrierFrames,0],enemyBullet4,[30,50,0,0]],

    
    [210,100,20,20,700,200,'[3,20,10,0,4,4,[0,1],None,True]',[0],0,[bossProbeFrames,0],enemyBullet2,[50,20,1,1]],
    [420,100,60,20,700,200,'[3,20,10,0,4,4,[0,1],None,True]',[0],0,[bossProbeFrames,0],enemyBullet2,[50,20,1,1]],

    [315,100,20,20,1000,215,'[3,15,500,0,4,4,[0,1],None,True]',[0],0,[bossProbeFrames,0],bossBullet2,[50,20,3,3]],


    [315,250,20,60,10000,225, 
      'choice([[6,9,25,0,25,2,[17,60],15,100,100,False],[3,15,200,0,8,2.5,[0,1],60,True],[3,25,200,0,5,5,[0,1],60,True],[6,11,15,0,25,3,[11,37],15,50,120,False],[2,100,5,180,60],[4,2,20,37,-53,8,60],[1,45,4,0,10,40],[5,16,5,0,13,150,80],[4,2,20,19,-29,8,60],[7,400,6,[20,300,20,80,100,totalTime,"[2,10,3,50]",[1,3,1],0,[enemyLeaderFrames,0],enemyBullet6,[2,20,0,0]],100]])',
      [0],0,[alienGodFrames,0],enemyBullet6,[750,300,5,5],'boss'],
    


    


    ]
quit()
