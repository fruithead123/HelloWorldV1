#Hello World
#Developed by Gary Sun and Kevin Yuan for their FSE
#This game was inspired by Touhou and the bullet hell genre
#Good luck and have fun in the world's easiest bullet hell!

#P.S. DOnt forget to install fonts inside the fonts folder
#Also, to see all the levels, go into the levelsCompleted.txt and change all values to 1

from pygame import *
from math import *
from random import *
from os.path import *
from fileinput import *
from enemyLists import *

mixer.pre_init(44100, -16, 4, 1024) #Allows sounds to buffer faster
init()
mixer.init()
mixer.set_num_channels(45)

#Defining colors for text and boxes/buttons
BORDERCOL=(120,120,120)
BORDERINCOL=(180,180,180)
HOVERCOL=(166, 124, 234) #For hovering over buttons
WHITE=(255,255,255)
BLACK=(0,0,0)
GREEN=(0,255,0)


borderRect=Rect(20,10,610,700)

size=(960,720)
screen=display.set_mode(size)
bg=Surface((600,690)) #Surface for background scroll
fps=time.Clock()

#For starfield parallax in menu screens
originX=screen.get_width()/2
originY=screen.get_height()/2

#Creates a score file if none exists with all scores of 0
if exists("scores.txt")==False:
    scoreFile=open("scores.txt","w")
    scoreFile.write("1. 0\n")
    scoreFile.write("2. 0\n")
    scoreFile.write("3. 0\n")
    scoreFile.write("4. 0\n")
    scoreFile.write("5. 0\n")
    scoreFile.close()

#Creates a trp[hy file if none exists with no trophy icon
if exists("trophies.txt")==False:
    trophiesFile=open("trophies.txt","w")
    trophiesFile.write("0\n"*4)
    trophiesFile.write("0")
    trophiesFile.close()

#CReates a level complete file if none exists with all levels incomplete
if exists("levelsCompleted.txt")==False:
    lvlFile=open("levelsCompleted.txt","w")
    lvlFile.write("0\n"*4)
    lvlFile.write("0")
    lvlFile.close()

### Setting up Fonts ###
display.set_caption("Hello, world! FPS:0")
labelFont=font.SysFont("JoystixMonospace-Regular",20)
scoreFont=font.SysFont("JoystixMonospace-Regular",30)
titleFont=font.SysFont("Earth Orbiter",30)
selectFont=font.SysFont("GiantRobotArmy Medium", 65)
menuFont=font.SysFont("GiantRobotArmy Medium", 35)
smallMenuFont=font.SysFont("GiantRobotArmy Medium", 26)
mediumMenuFont=font.SysFont("GiantRobotArmy Medium", 85)
largeMenuFont=font.SysFont("GiantRobotArmy Medium", 150)
leaderFont=font.SysFont("JoystixMonospace-Regular", 65)
captionFont=font.SysFont("JoystixMonospace-Regular",45)
subCaptionFont=font.SysFont("QaskinBlack_PersonalUse", 30)
scoreBonusFont=font.SysFont("JoystixMonospace-Regular", 33)

titleCaption=titleFont.render("Gary & Kevin's",1,(WHITE))
selectCaption=selectFont.render("Choose Your Ship",1,(WHITE))
beginCaption=menuFont.render("START GAME",1,(WHITE))
deathCaption=selectFont.render("YOU DIED!",1,(WHITE))
practiceDoneCaption=selectFont.render("Practice Complete",1,(WHITE))
menuCaption=menuFont.render("MENU",1,(WHITE))
againCaption=menuFont.render("PLAY AGAIN",1,(WHITE))
practiceModeCaption=menuFont.render("PRACTICE MODE",1,(WHITE))
backPracticeCaption=mediumMenuFont.render("PRACTICE SELECTION",1,(WHITE))
practiceButtonCaption=smallMenuFont.render("PRACTICE SELECTION",1,(WHITE))
leaderCaption=leaderFont.render("LEADERBOARD",1,(WHITE))
nextLevelCaption=menuFont.render("NEXT LEVEL",1,(WHITE))
scoreCaption=labelFont.render("SCORE",1,(WHITE))
lifeCaption=labelFont.render("HEALTH",1,(WHITE))
grazeCaption=labelFont.render("GRAZE",1,(WHITE))
bombCaption=labelFont.render("BOMB",1,(WHITE))
pauseCaption=selectFont.render("PAUSED",1,(WHITE))
resumeCaption=menuFont.render("RESUME",1,(WHITE))
restartCaption=menuFont.render("RESTART",1,(WHITE))
beatTheGameCaption=mediumMenuFont.render("YOU BEAT THE GAME!",1,(WHITE))

scoreBonusCaption=scoreBonusFont.render('LEVEL COMPLETE BONUS',1,(WHITE))
scoreAmounts=[scoreBonusFont.render('+'+str((x+1)*100000),1,(WHITE)) for x in range(5)]

scoreSet=scoreFont.render(8*'0',1,WHITE)
grazeSet=scoreFont.render(8*'0',1,WHITE)

noAccessCaption=leaderFont.render('???',1,(WHITE))
largeQuestionMark=largeMenuFont.render('???',1,(WHITE))
practiceCaption1=leaderFont.render('LEVEL 1',1,(WHITE))
practiceCaption2=leaderFont.render('LEVEL 2',1,(WHITE))
practiceCaption3=leaderFont.render('LEVEL 3',1,(WHITE))
practiceCaption4=leaderFont.render('LEVEL 4',1,(WHITE))
practiceCaption5=leaderFont.render('LEVEL 5',1,(WHITE))
practiceCaptions=[eval('practiceCaption'+str((x+1))) for x in range(5)]
practiceInfoTxt=labelFont.render('Reach this level in',1,(WHITE))
practiceInfoTxt2=labelFont.render('normal mode',1,(WHITE))
practiceInfoTxt3=labelFont.render('to practice it',1,(WHITE))



practicePrevs=[transform.scale(image.load('images/PracticePreview/level'+str(x+1)+'Prev.png'),(385,446)) for x in range(5)]

levelCaptions=[captionFont.render('STAGE '+str(x+1),1,(WHITE)) for x in range(5)]
subCaptions=[subCaptionFont.render('Adrift in Darkness',1,(WHITE)),subCaptionFont.render('The Approaching Fleet',1,(WHITE)),subCaptionFont.render('Imminent Attack',1,(WHITE)),
             subCaptionFont.render('Total Eclipse',1,(WHITE)),subCaptionFont.render('Mutually Assured Destruction',1,(WHITE))]
txtAlpha=0 #Used for level headings


### Loading Images ###
titlepic=image.load("images/title.jpg").convert()
instructions=transform.scale(image.load("images/instructions.png"),(960,720))
selectback=image.load("images/Backgrounds/selectbackground.png")
background=image.load("images/Backgrounds/background.png").convert()
level1BG=image.load("images/Backgrounds/scrollingBackground1.png").convert()
leaderBackground=transform.scale(image.load("images/Backgrounds/leaderBackground.png"),(960,720)).convert()
practiceCompleteBG=image.load('images/Backgrounds/practiceCompletebg.png').convert()
gameCompletePic=image.load('images/Backgrounds/gameComplete.png').convert()
logo=image.load("images/logo.png")
leaderboardIcon=image.load("images/leaderboardIcon.png")
playPic=transform.scale(image.load('images/howToPlay.png'),(50,50))
playerBullet=transform.scale(image.load("images/Bullets/beam.png").convert(),(18,40))
nextLevelPic=image.load("images/nextLevelPic.png")
scorePic1=image.load('images/scorePic1.png').convert()
scorePic2=image.load('images/scorePic2.png').convert()
dropLife=transform.scale(image.load('images/dropLife.png'),(30,30))
dropBomb=transform.scale(image.load('images/dropBomb.png'),(30,30))
    
playerBullet.set_colorkey((0,0,0))
enemyBullet1.set_colorkey((0,0,0))
scorePic1.set_colorkey((0,0,0))
scorePic2.set_colorkey((0,0,0))

trophyPics=[]
for i in range(5):
    trophyPics.append(image.load("images/trophies/trophy"+str(i)+".png"))


### Creating Animation Lists

healthList=[]
for i in range(5):
    healthList.append(image.load("images/Health/health"+str(i)+".png"))
healthList[4]=transform.scale(healthList[4],(272,48))

#Ingame ship animations
ship1=[]
ship2=[]
ship3=[]
ship4=[]
practiceShip=[]
for i in range(4):
    ship1.append(image.load("images/Ships/Ingame/newShip"+str(4+i)+".png"))
    ship2.append(image.load("images/Ships/Ingame/newShip"+str(i)+".png"))
    ship3.append(image.load("images/Ships/Ingame/newShip"+str(8+i)+".png"))
    ship4.append(image.load("images/Ships/Ingame/newShip"+str(12+i)+".png"))
    practiceShip.append(image.load("images/Ships/Ingame/newShip"+str(16+i)+".png"))



#Level completion ship animations
ship1Next=[]
ship2Next=[]
ship3Next=[]
ship4Next=[]

for i in range(4):
    ship1Next.append(image.load("images/Ships/Selection/newShip"+str(i)+".png"))
    ship2Next.append(image.load("images/Ships/Selection/newShip"+str(4+i)+".png"))
    ship3Next.append(image.load("images/Ships/Selection/newShip"+str(8+i)+".png"))
    ship4Next.append(image.load("images/Ships/Selection/newShip"+str(12+i)+".png"))

#Selection screen ship animations
selectionShips=[]
for i in range(16):
    selectionShips.append(image.load("images/Ships/Selection/newShip"+str(i)+".png"))

#Selection screen probe animations
selectionProbes=[]
for i in range(32):
    selectionProbes.append(image.load("images/Probes/BigProbe/probe%02d.png"%(i)))

#Ingame probe animations                                   
probe1=[]
probe2=[]
probe3=[]
probe4=[]
practiceProbe=[]
for i in range(8):
    probe1.append(image.load("images/Probes/probe0"+str(i)+".png").convert())
    probe2.append(image.load("images/Probes/probe2"+str(i)+".png").convert())
    probe3.append(image.load("images/Probes/probe3"+str(i)+".png").convert())
    probe4.append(image.load("images/Probes/probe4"+str(i)+".png").convert())
    practiceProbe.append(transform.scale(image.load("images/Probes/probe5"+str(i)+".png").convert(),(24,24))) 
    
#Explosion animation
explosions=[]
for i in range(14):
    explosions.append(image.load("images/explosion/Explosion%03d"%(i+1)+".png"))

#Bomb animations on the side of the screen during gameplay
bombList=[]
for i in range(10):
    bombList.append(image.load("images/bombs/bomb"+str(i)+".png"))




### For Character Selection ###
#Determines which ship is selected by the player
shipRect=Rect(150,325,160,145)
ship1Rect=Rect(320,325,160,145)
ship2Rect=Rect(490,325,160,145)
ship3Rect=Rect(660,325,160,145)

###Load Sounds###
doGrazeFX=mixer.Sound('Sounds/doGraze.wav')
getBombFX=mixer.Sound('Sounds/getBomb.wav')
getLifeFX=mixer.Sound('Sounds/getLife.wav')
getProbeFX=mixer.Sound('Sounds/getProbe.wav')
getScoreFX=mixer.Sound('Sounds/getScore.wav')
hitEnemyFX=mixer.Sound('Sounds/hitEnemy.wav')
pauseFX=mixer.Sound('Sounds/pause.wav')
plDeadFX=mixer.Sound('Sounds/plDead.wav')
plShotFX=mixer.Sound('Sounds/plShot.wav')
shootFX=mixer.Sound('Sounds/shoot.wav')
enemyShootFX=mixer.Sound('Sounds/enemyShoot.wav')
useBombFX=mixer.Sound('Sounds/useBomb.wav')

shootFX.set_volume(0.05)
doGrazeFX.set_volume(0.01)
hitEnemyFX.set_volume(0.01)
enemyShootFX.set_volume(0.02)
plShotFX.set_volume(0.3)



#Creating variabes for games
ship=[275,600,6,6,6,0]  #[x,y,currentShootDelay,totalShootDelay,playerSpeed,frame]
playerBullets=[] #[x,y]  
playerLevel=0    #Determines the number of probes the player has
playerProbes=[[ship[0]-24,ship[1]+50,0,0,49,0],
              [ship[0]+62,ship[1]+50,0,0,49,0],
              [ship[0]-24,ship[1]+26,0,0,49,0],
              [ship[0]+62,ship[1]+26,0,0,49,0],
              [ship[0]-24,ship[1]+2,0,0,49,0],
              [ship[0]+62,ship[1]+2,0,0,49,0]]  #[x,y,active Bool,shootDelay,totalShootDelay,frame]

probeBullets=[] #[x,y,angle,targetData]

enemies=[] #Stores a list of all enemies in the level
activeEnemies=[] #Stores all enemies on the screen
enemyBullets=[]  #Stores all enemy bullet data
scoreList=[]     #Stores all dropped score, health and bombs
totalTime=0      #Total time in seconds since the beginnin of the level
score=0          #Player score
graze=0          #Total graze
bomb=5           #Number of bombs
bombRadius=0     #How far the bomb has expanded
health=3         #How much health the player has
IFrames=80       #Number of frames where the player is invincible
probeFocus=False #Indicated which attack pattern probes will shoot at
activeBomb=[False,0,0,0,700,False] #[activeBool, x,y, delay, maxRadius, lethal Bool]
gameOver=False #Indicates whether the player is still alive
gameLevel=1    #Indicates which level the player is playing
bombFrame=0    #Current bomb frame for bombs on side of the game screen

damageTaken=1  #Indicates how much damage the player takes per hit
practiceMode=False #Indicates whether the player is in practice mode or mormal mode

scrOpacity=0   #How transparent the screen is. Used in fade out effects
explosionAnis=[] #[x,y,frame]
scrollOffset=0 #How far the scrolling background has scrolled

bossAttack=None #Stores a boss attack for burst type attacks
bossSprites=[[bossProbeFrames,0],[bossCarrierFrames,0],[miniSpin,0],[bossLeaderFrames,0],[alienGodFrames,0]]

period=0 #USed for periodic burst waves (See createEnemyBullets)
incdec=1

deadSoundPlayed=False
scoreGiven=False


def restartGame(level=1):
    'Reset game variables to start over'
    global ship, playerBullets,playerLevel,probeBullets,enemies,activeEnemies,enemyBullets,scoreList,totalTime,score,scoreSet,grazeSet,health,graze,bomb,gameOver,gameLevel, playerProbes
    ship=[275,600,6,6,6,0]
    playerBullets=[]
    playerLevel=0
    probeBullets=[]
    activeEnemies=[]    #Clears the game screen
    enemyBullets=[]
    scoreList=[]
    totalTime=0
    score=0
    scoreSet=scoreFont.render(8*'0',1,WHITE) #Changes score and graze to 0
    grazeSet=scoreFont.render(8*'0',1,WHITE)
    health=3
    graze=0
    bomb=5
    gameOver=False
    gameLevel=level  #The game always starts at level 1 except during practice mode
    playerProbes=[[ship[0]-24,ship[1]+50,0,0,49,0], #Sets all probe values to 0 since the player hasn't unlocked them
              [ship[0]+62,ship[1]+50,0,0,49,0],
              [ship[0]-24,ship[1]+26,0,0,49,0],
              [ship[0]+62,ship[1]+26,0,0,49,0],
              [ship[0]-24,ship[1]+2,0,0,49,0],
              [ship[0]+62,ship[1]+2,0,0,49,0]]
    
def nextLevel():
    'Sets up the game for the next level'
    global gameLevel, enemies, totalTime, scrOpacity, enemyBullets, playerBullets, level1Enemies,level2Enemies, level3Enemies, level4Enemies, level5Enemies
    totalTime=0
    scrOpacity=0
    enemyBullets=[]
    playerBullets=[]
    if gameLevel==1:
        enemies=[x[:] for x in level1Enemies]   #Determines which list to use for enemies
    elif gameLevel==2:
        enemies=[x[:] for x in level2Enemies]
    elif gameLevel==3:
        enemies=[x[:] for x in level3Enemies]
    elif gameLevel==4:
        enemies=[x[:] for x in level4Enemies]
    elif gameLevel==5:
        enemies=[x[:] for x in level5Enemies]


def fadeToBlack(opacity):
    'Screen turns black for transition'
    fade=Surface((960,720),SRCALPHA) #Screen becomes less transparent every frame
    if opacity<255:
        draw.rect(fade,(0,0,0,opacity),[0,0,960,720])
        screen.blit(fade,(0,0))
        opacity+=1
    return opacity
    
def movePlayer():
    'Detects user input to move the ship'
    keys=key.get_pressed()
    if keys[K_LEFT] and ship[0]>0:
        ship[0]-=ship[4]              #ship x value is decreased by ship speed
        for probe in playerProbes:
            probe[0]-=ship[4]         #Probe position moves by the same amount to follow the player
    if keys[K_RIGHT] and ship[0]<535:
        ship[0]+=ship[4]             #ship x value is increased by ship speed
        for probe in playerProbes:
            probe[0]+=ship[4]
    if keys[K_UP] and ship[1]>5:
        ship[1]-=ship[4]              #Ship y value is decreases by ship speed
        for probe in playerProbes:
            probe[1]-=ship[4]
    if keys[K_DOWN] and ship[1]<632:
        ship[1]+=ship[4]             #Ship y value is increased by ship speed
        for probe in playerProbes:
            probe[1]+=ship[4]
            
  
def checkPlayerLevel():
    'Determines number of upgrade probes based on score'
    keys=key.get_pressed()
    if practiceMode:
        playerLevel=3 #The player starts with 3 probes in practice mode
    else:
        if 90000>score>280000:
            playerLevel=1            #Player level is determined by score
        elif 280000>score>400000:
            playerLevel=2
        elif score>400000:
            playerLevel=3
        else:
            playerLevel=0
    return playerLevel

def drawPlayer(surface):
    'Draws the player on screen'
    if not gameOver:
        surface.blit(player[int(ship[5])],(ship[0],ship[1]))  #(ship[0],ship[1]) --> [x,y]
        ship[5]+=0.05                                         #ship[5] --> frame number
        if ship[5]>=4:
            ship[5]=0

def createPlayerBullets():
    'Detects when the player shoots'
    keys=key.get_pressed()
    ship[2]-=1 #Ship[2] --> delay ; ship can only shoot when delay is 0
    if ship[2]==0:
        ship[2]=ship[3]  #ship[3] --> totalShootDelay ; Ship's shooting delay is set to total delay to reset the shooting delay
        if keys[K_z]:    #If the z key is pressed, shoot
            playerBullets.append([ship[0]+1,ship[1]]) #Each bullets represented by [x,y]
            playerBullets.append([ship[0]+44,ship[1]])  #Bulelts are added right in front of the ship's cannon in the sprite
            shootFX.play(0,100)
            
def updatePlayerBullets():
    'Updates player bullets to go upwards'
    if not gameOver:
        for bullet in playerBullets:
            if bullet[1]>10:          #Player bullets only shoot by and their y value is decreased by 15 every frame
                bullet[1]-=15

def drawPlayerBullets(surface):
    if not gameOver:
        for bullet in playerBullets:
            surface.blit(playerBullet,(bullet[0],bullet[1]))  #Draw the player bulelts on screen at their positions

    
def drawPlayerProbes(surface):
    'Draws any upgrade probes beside the ship'
    if not gameOver:
        for i in range(playerLevel*2): #Each level, the player gets 2 probes, one on each side
            surface.blit(playerProbe[int(playerProbes[i][5])],(playerProbes[i][0],playerProbes[i][1])) #Blit probes in sets of 2 based on their predetermined offsets to the ship (Defined at beginning of program)
            playerProbes[i][5]+=0.2 #Probe frame number gradually increased
            if playerProbes[i][5]>=8:
                playerProbes[i][5]=0

def shootProbes(probeFocus):
    'Detects when upgrade probes can shoot'
    if not gameOver:
        for i in range(playerLevel*2):     
            playerProbes[i][3]+=1 
            if playerProbes[i][3]>=playerProbes[i][4]: #When the probe delay reaches the total delay, it is reset and the probe can shoot
                playerProbes[i][3]=0    
                if probeFocus: #If the probes are in focus mode, they shoot upwards at a random angle offset
                    probeBullets.append([playerProbes[i][0],playerProbes[i][1],radians(90+randint(-15,15)),0])          
                else:
                    if len(activeEnemies)>0: #If they're not focussed, they choose a target and shoot at them
                        target=choice(activeEnemies)
                        probeBullets.append([playerProbes[i][0],playerProbes[i][1],atan2(-(target[1]+target[9][0][0].get_height()//2)+playerProbes[i][1],target[0]+target[9][0][0].get_width()//2-playerProbes[i][0]),target]) #[x,y,ang,target]
            playerProbes[i][4]=49 #Probe delay is reset after every shot  #Check if you need this
        #probeFocus=False
    
                
def updateProbeBullets():
    'Update probe bullets every frame'
    for bullet in probeBullets:
        if bullet[3] in activeEnemies and playerLevel==3: #At level 3, probe bulelts change their angle every frame to lock onto their target
            bullet[2]=atan2(-(bullet[3][1]+bullet[3][9][0][0].get_height()//2)+bullet[1],bullet[3][0]+bullet[3][9][0][0].get_width()//2-bullet[0])
        bullet[0]+=15*cos(bullet[2])  #Update based on their angle
        bullet[1]-=15*sin(bullet[2])

def drawProbeBullets(surface):
    'Draw probe bullets on a surface'
    if not gameOver:
        for bullet in probeBullets: #Rotate bulelt according to angle and blit in on screen
            rotatedBullet=transform.rotate(playerBullet,degrees(bullet[2])-90)
            surface.blit(rotatedBullet,(bullet[0],bullet[1]))
        

        
def checkFocus(surface):
    'Determine whether or not the user is focussed'
    keys=key.get_pressed()
    if keys[K_LSHIFT] and not gameOver: #Holdong shift caused focus mode
        if practiceMode:
            draw.circle(surface,((255,0,0)),[ship[0]+31,ship[1]+29],7)
        else:
            draw.circle(surface,((255,255,255)),[ship[0]+31,ship[1]+29],7)
            
        ship[3]=3 #Changes shooting delay to 2
        ship[4]=3 #Changes speed to half
        probeFocus=True #Probes change their attack pattern when focussed
        for i in playerProbes:
            i[4]=45-6*gameLevel #Probe delay is shortened for every gameLevel, ie they shoot faster later in the game
    else:
        ship[3]=6
        ship[4]=6 #Reset values when not focussed
        probeFocus=False
    return probeFocus

def initBomb(activeBomb,bomb):
    'Detects whether or not a bomb can be used and initiates a bomb if the user pressed z'
    keys=key.get_pressed()

    if activeBomb[3]>0: #Subtracts from the delay of the bomb --> The bomb cn only be used every 2 seconds and only when the player isn't invincible
        activeBomb[3]-=1
        
    if keys[K_x] and bomb>0 and activeBomb[3]==0: #Pressing x initiates a bomb if there is one in stock
        bomb-=1
        activeBomb=[True,ship[0],ship[1],160,700,True] #[bomb is active, starts at ship position, delay of 160 ticks, maxRadius of 700, can kill enemies]
        useBombFX.play()
    return activeBomb,bomb

def checkBomb(activeBomb,bombRadius):
    'Update bomb radius and inflicts damage to enemies and remove enemy bullets'
    if activeBomb[0] and not gameOver:  
        bombRadius+=10 #Increase bomb radius every frame
        if bombRadius<activeBomb[4]: #If the bomb hasn't reached its max size
            if activeBomb[5]: #Damege enemies if they are within range and the bomb is lethal
                for i in activeEnemies:
                    if hypot(i[0]-ship[0],i[1]-ship[1])<bombRadius: #Enemies closer to the bomb will take more damage
                        i[4]-=(2+int(gameLevel*0.8))
            for i in enemyBullets: #Clears the screen of all bullets
                if hypot(i[0]-ship[0],i[1]-ship[1])<bombRadius:
                    enemyBullets.remove(i)
        elif bombRadius>activeBomb[4]:
            activeBomb=[False,0,0,activeBomb[3],700,False] #Resets bomb state when bomb has reached max radius
            
            bombRadius=0
    return activeBomb,bombRadius

def drawBomb(x,y,frame,bomblist):
    'Draws the bomb sprites in game'
    if int(frame)!=4 and int(frame)!=5 and int(frame)!=6: #These frames are inherently different sizes so they must be blitted higher to compensate
        screen.blit(bombList[int(frame)],(x,y))
    else:
        screen.blit(bombList[int(frame)],(x,y-4))
    frame+=0.05
    if frame>=10:
        frame=0

    return frame

def createEnemies():
    'Transfers enemies from enemies to activeEnemies to be shown on screen'
    for enemy in enemies:
        if enemy[5]<totalTime and enemy[8]==0: #copies an enemy from the enemies list to active enemies when its spawn time, enemy[5], is reached
            enemy[8]=1
            activeEnemies.append(enemy)

def updateEnemies():
    'Updates enemy position based on their movement code'
    for i in activeEnemies:       
        if i[7][0]==0: #No movement
            pass
        elif i[7][0]==1: #Horizontal movement
            i[0],i[7][2]=enemyMovement1(i[0],i[7][1],i[7][2])
        elif i[7][0]==2: #Vertical movement
            i[1],i[7][2]=enemyMovement1(i[1],i[7][1],i[7][2])
        elif i[7][0]==3: #Homes towards the player
            i[0],i[1]=enemyMovement2(i[0],i[1],i[7][1])
    
def createEnemyBullets(bossAttack):
    'Detects whether or not an enemy can attack and excecutes its attack based on its attack code'
    for enemy in activeEnemies:
        enemy[2]-=1 #Subtract from delay and enemies attack when delay is 0
        if enemy[2]==0:
            if enemy[-1]!='boss': #If enemy is not the boss, get its attack and excecute it
                attack=eval(enemy[6])
                #These attacks are excecuted more than once to give a burst effect
                
                if attack[0]==3: #Burst around a circle,
                    if attack[7]!=None:
                        attack=attack[7]
                    attack[3],enemy[2],attack[6][0]=enemyAttack3(enemy[0],enemy[1],attack[1],attack[2],attack[3],attack[4],enemy[2],attack[5],attack[6][0],attack[6][1],enemy[10])
                        #(x,y,numPerCircle,burstNum,currentBurstNum,BurstDelay,delay,speed,angleShift,img)
                    
                    if attack[8]:
                        attack[6][1]=period #If the attacks is periodic, set value equal to the period, which is always occilating
                        
                    enemy[6]=str(attack) #Set a stored attack
                    if attack[3]==0:
                        attack[7]=None   #Reset stored attack when complete

                        
                elif attack[0]==6: #Burst in a circle
                    if attack[9]!=None:
                        attack=attack[9]
                        
                    for i in range(attack[7]): #Number of circles
                        ang=i*360/attack[7]
                        
                        attack[3],enemy[2],attack[6][0]=enemyAttack3(enemy[0]+attack[8]*cos(radians(ang)),enemy[1]-attack[8]*sin(radians(ang)),
                                                          attack[1],attack[2],attack[3],attack[4],enemy[2],attack[5],attack[6][0],attack[6][1],enemy[10])

                        if attack[10]:
                            attack[6][1]=period
                        
                        enemy[6]=str(attack)
                        if attack[3]==0:
                            attack[9]=None
                            
                    
                else:   
                    enemy[2]=enemy[3] #Reset delay
                    if attack[0]==1: #Shoot around a circle
                        attack[3]=enemyAttack1(enemy[0],enemy[1],attack[1],enemy[10],attack[2],attack[3],attack[4]) #x,y,num,img,speed,angOff,angOffInc
                    elif attack[0]==2: #Shoot a wave at the player
                        enemyAttack2(enemy[0],enemy[1],attack[1],enemy[10],attack[2],attack[3]) #x,y,num,img,angDispalce
                    elif attack[0]==4: #Create a bullet that splits at different angles
                        enemyAttack4(enemy[0],enemy[1],attack[1],attack[2],attack[3],attack[4],attack[5])
                    elif attack[0]==5: #shoot in a circle
                        for i in range(attack[1]):
                            ang=i*360/attack[1]
                            enemyAttack1(enemy[0]+attack[5]*cos(radians(ang)),enemy[1]-attack[5]*sin(radians(ang)),attack[1],enemy[10],attack[2],attack[3],attack[4])
                    elif attack[0]==7: #Creates new enemies
                        enemyAttack5(enemy[0],enemy[1],attack[1],attack[2],attack[3])

            #Same as code above but stores attack to bossAttack (For bursts) to prevent from choosing an attack (Since bosses use choice() to choose attacks after every delay      
            elif enemy[-1]=='boss': #If the enemy is the boss
                if bossAttack!=None: #Use the current boss attack if there is one
                    attack=bossAttack
                else:
                    attack=eval(enemy[6]) #choose an attack if the boss has no current attack
                    
                if attack[0]==3: #Special attack
                    attack[3],enemy[2],attack[6][0]=enemyAttack3(enemy[0],enemy[1],attack[1],attack[2],attack[3],attack[4],enemy[2],attack[5],attack[6][0],attack[6][1],enemy[10])
                            #(x,y,numPerCircle,burstNum,currentBurstNum,BurstDelay,delay,speed,angleShift,img)
                    
                    if attack[8]:
                        attack[6][1]=period
                    bossAttack=attack
                    if attack[3]==0:
                        bossAttack=None
                        
                elif attack[0]==6:
                    for i in range(attack[7]): #Number of circles
                        ang=i*360/attack[7]
                        attack[3],enemy[2],attack[6][0]=enemyAttack3(enemy[0]+attack[8]*cos(radians(ang)),enemy[1]-attack[8]*sin(radians(ang)),
                                                          attack[1],attack[2],attack[3],attack[4],enemy[2],attack[5],attack[6][0],attack[6][1],enemy[10])
                    if attack[10]:
                        attack[6][1]=period
                    bossAttack=attack
                    if attack[3]==0:
                        bossAttack=None
                        
                
                else:   

                    if attack[0]==1:
                        attack[3],enemy[2]=enemyAttack1(enemy[0],enemy[1],attack[1],enemy[10],attack[2],attack[3],attack[4],attack[5]) #x,y,num,img,speed,angOff,angOffInc
                    elif attack[0]==2:
                        enemy[2]=enemyAttack2(enemy[0],enemy[1],attack[1],enemy[10],attack[2],attack[3],attack[4]) #x,y,num,img,angDispalce
                    elif attack[0]==4:
                        enemy[2]=enemyAttack4(enemy[0],enemy[1],attack[1],attack[2],attack[3],attack[4],attack[5],attack[6]) #[x,y,speed,splitDelay,ang1,ang2,size,delay]
                    elif attack[0]==5:
                        for i in range(attack[2]):
                            ang=i*360/attack[2]
                            attack[3],enemy[2]=enemyAttack1(enemy[0]+attack[5]*cos(radians(ang)),enemy[1]-attack[5]*sin(radians(ang)),attack[1],enemy[10],attack[2],attack[3],attack[4],attack[6])
                    elif attack[0]==7:
                        enemy[2]=enemyAttack5(enemy[0],enemy[1],attack[1],attack[2],attack[3],attack[4])
                        
                    bossAttack=None #These attacks dont require multiple frames
            enemyShootFX.play()
    return bossAttack
                
            
            
def updateEnemyBullets():
    'Update bullet positions based on their angle'
    for i in enemyBullets:
        i[0]+=cos(radians(i[2]))*i[4] #x coords += cos(angle)*speed
        i[1]-=sin(radians(i[2]))*i[4] #Y coords -= sin(angle)*speed (Since y axis is inverted in pygame)
        
def drawEnemyBullets(surface):
    'Draws enemy bullets on a surface'
    for i in enemyBullets:
        if i[3] in splitBullets:                 #Split bullets must be drawn upwards to prevent wierd textures
            surface.blit(i[3],(i[0],i[1]))
        else:
            rotatedBullet=transform.rotate(i[3],i[2]-90) #Rotate bulelt based on their angle and draw it
            surface.blit(rotatedBullet,(i[0],i[1])) 
        #draw.rect(screen,GREEN,[i[0],i[1],enemyBullet1.get_width(),enemyBullet1.get_height()],1)
        
def drawEnemies(surface):
    'Draws all active enemies on a surface with their picture and frame'
    for i in activeEnemies:
        if i[9][0]==spinBoss or i[9][0]==miniSpin:    #These enemies dont have anmation frames and are shown based on their ritation value
            rotPic=transform.rotate(i[9][0][0],i[9][1])
            surface.blit(rotPic,(i[0]-rotPic.get_width()//2,i[1]-rotPic.get_height()//2))
            i[9][1]+=1
            if i[9][1]>=360:           #Add a degree of rotation each frame and blit it
                i[9][1]=0
        else:          
            surface.blit(i[9][0][int(i[9][1])],(i[0]-i[9][0][0].get_width()//2,i[1]-i[9][0][0].get_height()//2))
            i[9][1]+=0.1
            if i[9][1]>=len(i[9][0]):       #Blit the enemy picture (i[9]) and add 1 to its animation frame number
                i[9][1]=0
        
        
def killBullets():
    'Remove bullets when offscreen to prevent using extra memory'
    for i in playerBullets:
        if i[1]<15:       #Player bullets only travel upwards
            playerBullets.remove(i)
    for i in enemyBullets:
        if i[0]<15 or i[0]>600 or i[1]<10 or i[1]>660:  #Remove when off screen
            enemyBullets.remove(i)
    for i in probeBullets:
        if i[0]<15 or i[0]>600 or i[1]<10 or i[1]>650:
            probeBullets.remove(i)

def checkPlayerBulletCollisions():
    'Check if a player bulelt hits an enemy and inflicts damage'
    for i in playerBullets:
        for j in activeEnemies: #Cycle through each enemy and bullet and detremine if their rectangles collide
            draw.rect(screen,(0,255,0),[j[0],j[1],j[9][0][0].get_width(),j[9][0][0].get_height()],1)
            if Rect(i[0],i[1],playerBullet.get_width(),playerBullet.get_height()).colliderect(Rect(j[0]-j[9][0][0].get_width()//2,j[1]-j[9][0][0].get_height()//2,j[9][0][0].get_width(),j[9][0][0].get_height())):
                j[4]-=3                          #If so, remove the bullet to prevent penetration and deal damege to the enemy
                hitEnemyFX.play()
                if i in playerBullets:
                    playerBullets.remove(i)
    for i in probeBullets:
        for j in activeEnemies:         #Cycle through all bulelts and enemies etc.
            if Rect(i[0],i[1],playerBullet.get_width(),playerBullet.get_height()).colliderect(Rect(j[0],j[1],j[9][0][0].get_width(),j[9][0][0].get_height())):
                j[4]-=5
                if i in probeBullets:
                    probeBullets.remove(i)


def checkEnemyPlayerCollisions():
    'Detects whether or not the player got shot by an enemy'
    global health,IFrames,explosions,activeBomb, gameOver
    if IFrames>0:
        IFrames-=1  #Subtract from the Invinsible frames
    if IFrames==0:
        for i in enemyBullets: #If IFrames==0, ie the player is not invincible, check if the bullet is in the player hitbox
            bulletCenter=[i[0]+i[3].get_width()//2,i[1]+i[3].get_height()//2]  #EAch bullet hitbox is the point at the center of its sprite
            if hypot(bulletCenter[0]-(ship[0]+31),bulletCenter[1]-(ship[1]+29))<7 and IFrames==0:
                health-=damageTaken  #Subtract 1 from health, 0 in practice mode
                IFrames=160 #Reset IFrames
                enemyBullets.remove(i) #Remove the bullet
                activeBomb=[True,ship[0],ship[1],160,700,False] #Activate a bomb to clear the screen to prevent from getting hit consecuvely
                plShotFX.play()
            health=max(health,-1) #Going below -1 will cause the full health img to be shown
            if health==-1 and gameOver==False:
                explosionAnis.append([ship[0],ship[1],0]) #Play explosion animation at ship position is the player has lost all their lives
                gameOver=True
            

def checkGraze():
    'Check if the player grazed bullets and adds it to the graze counter'
    global score,graze
    for bullet in enemyBullets:        
        if 7<hypot(ship[0]+31-bullet[0],ship[1]+29-bullet[1])<25: #If the bullet is close to the ship but not in the hitbox, add graze
            graze+=1
            score+=10 #Grazing a bullet gives 10 score
            doGrazeFX.play()

    
            
def killDeadEnemies():
    'Remove enemies if they have less than 1 health to indicate iot has died'
    for enemy in activeEnemies:
        if enemy[4]<1:
            explosionAnis.append([enemy[0],enemy[1],0]) #[x,y,frame] Add an explosion animation when an enemy dies
            #Spawn dropped items based on their data; enemy[11] --> [dropped score, drop radius, dropped life, dropped bombs]
            for i in range(enemy[11][0]): #Add score
                scoreList.append([enemy[0]+randint(-enemy[11][1],enemy[11][1]),enemy[1]+randint(-enemy[11][1],enemy[11][1]),
                                  90,1,choice([scorePic1,scorePic2])]) #[x,y,ang,speed,img]

            for i in range(enemy[11][2]): #Add life
                scoreList.append([enemy[0]+randint(-enemy[11][1],enemy[11][1]),enemy[1]+randint(-enemy[11][1],enemy[11][1]),
                                  90,1,dropLife]) #[x,y,ang,speed,img]

            for i in range(enemy[11][3]): #Add bomb
                scoreList.append([enemy[0]+randint(-enemy[11][1],enemy[11][1]),enemy[1]+randint(-enemy[11][1],enemy[11][1]),
                                  90,1,dropBomb]) #[x,y,ang,speed,img]
            

            activeEnemies.remove(enemy) #Remove the enemy to stop drawing it
            

def killLingeringEnemies():  
    'Kills enemies that have been active too long to allow the game to be possible if you cant kill the enemies fast enough'
    for i in activeEnemies:
        if i[5]+15+(5-gameLevel)*2<totalTime and i[-1]!='boss': #The higher level, the faster enemies will despawn
            activeEnemies.remove(i)

def updateScoreList():
    'Caused dropped score to fall downwards and fly towards the player if they are high enough'
    for i in scoreList:
        if ship[1]<125: #Score will mvoe towards the ship when above 125 (Critical line)
            i[3]=20
            i[2]=degrees(atan2(-(i[1]-ship[1]),i[0]-ship[0]))
            
        i[0]-=i[3]*cos(radians(i[2]))  #Update score based on its angle
        i[1]+=i[3]*sin(radians(i[2]))
        
        if i[0]>630 or i[0]<20 or i[1]<10 or i[1]>730:
            scoreList.remove(i) #Remove score when offscreen

def drawScoreList(surface):
    'Draw dropped score on a surface'
    for i in scoreList: #Draw all elements in the score list based on their picture 
        if i[4]==dropLife: #i[4] is the picture, i[0],i[1] --> x,y
            surface.blit(dropLife,(i[0],i[1]))
        elif i[4]==dropBomb:
            surface.blit(dropBomb,(i[0],i[1]))
        else:
            surface.blit(i[4],(i[0],i[1]))

def giveScore():
    'Detects if a player has collected dropped score and updates their score, health or graze'
    global score, graze, health, bomb
    for i in scoreList: #Check if the score collides with the player sprite and add based on the type
        if Rect(ship[0],ship[1],player[0].get_width(),player[0].get_height()).colliderect(Rect(i[0],i[1],i[4].get_width(),i[4].get_height())):
            if i[4]==dropLife:
                if not practiceMode: #Dont add life in practice mode to keep golden health bar
                    health=min(health+1,3) #Add a life with a max of 3
                getLifeFX.play()
            elif i[4]==dropBomb: 
                bomb=min(bomb+1,5) #Add bomb with a max of 5
                getBombFX.play()
            else:
                score+=int(50+0.05*graze) #Add score (Graze acts as a multiplier to score)
                getScoreFX.play()
            scoreList.remove(i) #Remove collected score to stop drawing it
            

def enemyMovement1(axis,speed,direction): 
    'Allows an enemy to move left and right or up and down'
    #1 represents a positive movement (either right or down), -1 represents a negative movement(left or up)
    #An enemy's x cood will cause it to move horizontally whereas its y coord will cause it to move vertically
    if axis>550 and direction==1: #Switch directions when passed a certain threshold and the ship is going the other direction
        direction=-1
    elif axis<30 and direction==-1:
        direction=1
    axis+=direction*speed #Update the its position
    return [axis,direction]


def enemyMovement2(x,y,speed):
    'Allows an enemy to lock on to the player'
    if hypot(ship[0]-x,ship[1]-y)>5: #If the enemy is more than 5 units away
        ang=atan2(-(ship[1]-y),ship[0]-x) #Find the angle between the enemy and the ship
        x+=cos(ang)*speed  #Update its position based on the angle to get enemy to home onto the player
        y-=sin(ang)*speed
    return [x,y]

def enemyAttack1(x,y,num,img,speed,ang,angOff,delay=None): #Shoot in a circle
    'Allows enemies to shoot in a number of directions around a circle'
    for i in range(num): #append bullets on points equally spaced around the circumference of a circle
        enemyBullets.append([x,y,i*360/num+ang,img,speed]) #[x,y,ang,img,speed]
        ang+=angOff #Offset the angle each attack so the player cant just stay in one spot
    if delay!=None: #Non-boss enemies wont supply a delay value. If a delay value is supplied, the function will return it as well
        return ang,delay
    return ang
        
def enemyAttack2(x,y,num,img,speed,angDisplacement,delay=None): #Shoot at player
    'Allows enemies to shoot a wave of bulelts at the player'
    for i in range(num):
        ang=degrees(atan2(-ship[1]+y,ship[0]-x))+randint(-angDisplacement,angDisplacement) 
        enemyBullets.append([x,y,ang,img,speed]) #Find the angle between the shot and the player and create a bullet travelling in that direction
    if delay!=None:
        return delay

def enemyAttack3(x,y,numPerCircle,burstNum,currentBurstCount,burstDelay,delay,speed,angleShift,angInc,img):
    'Allows an enemy to burst in a circle'
    #NumPerCircle --> cuts up the circle into that many sections
    #BurstNum, CurrentBurstCount --> how many times to burst, how manytimes it has bursted
    #BurstDelay, delay --> Delay after bursts (During the attack), delay ater attack is finished
    #speed --> speed of bullet
    #angleShift, angInc --> original offset of shot, angle increase fer shot
    if currentBurstCount<burstNum:
        for i in range(numPerCircle): 
            enemyBullets.append([x,y,i*360/numPerCircle+angleShift,img,speed])
        currentBurstCount+=1
        delay=burstDelay
        angleShift+=angInc
    else:
        currentBurstCount=0
        delay=100

    return currentBurstCount,delay, angleShift

def enemyAttack4(x,y,speed,splitDelay,ang1,ang2,size,delay=None):
    'Allows an emeny to fire a bullet that splits over time'
    img=splitBullets[size-1] #Creates a bullet of max size
    enemyBullets.append([x,y,-90,img,speed,splitDelay,ang1,ang2,size])
    if delay!=None:
        return delay

def checkForSplit():
    'Splits bullets from the previous attack type and updates their angle'
    for i in enemyBullets:
        if i[3] in splitBullets:
            i[5]-=1 #Decreases delay by 1
            if i[5]==0: 
                i[8]-=1 #Decreased size by 1
                if i[8]>1:
                    enemyBullets.remove(i) #Remove the old bullet and create 2 smaller ones with angle based on given params
                    enemyBullets.append([i[0],i[1],i[2]+i[6],splitBullets[i[8]-1],i[4],20,i[6],i[7],i[8]])
                    enemyBullets.append([i[0],i[1],i[2]+i[7],splitBullets[i[8]-1],i[4],20,i[6],i[7],i[8]])

def enemyAttack5(x,y,dist,num,spawn,delay=None):
    'Allows enemies to spawn other enemies on screen'
    global activeEnemies
    a=[] #Stores a list of new enemies
    for i in range(num):
        current=spawn[::] #Copy the enemy template given
        current[0]=x+dist*cos(i*360)/num #Place them a given distance away equidistant around a circle
        current[1]=y-dist*sin(i*360)/num
        a.append(current) 
    activeEnemies=a+activeEnemies #Add enemies to the beginning of the enemy list to prevent the game from ending when the last enemy is killed
    if delay!=None:
        return delay
    
        
def doExplosions(surface):
    'Processes explosion animations in a list'
    for i in explosionAnis:
        surface.blit(explosions[int(i[2])],(i[0],i[1])) #Blit explosion at position and with the current frame
        i[2]+=0.5 #Increase frame every frame
        if i[2]==14: #Remove the animation when it has finished all 14 frames
            explosionAnis.remove(i)

def showLevelIntro(surface,captions,subCaptions,totalTime,txtAlpha,gameLevel):
    if 0<totalTime<=3:
        txtAlpha+=(127/80) #Alpha must go from 0-->254 in 3 seconds
    elif 3<totalTime<=6:
        txtAlpha-=(127/80) #Alpha must go from 254-->0 in 3 seconds
    else:
        txtAlpha=0 #transparent text if after 6 seconds
        
    currentCaption=captions[gameLevel-1]  #Gets the caption and subcaption that belongs to the current stage
    currentSubCaption=subCaptions[gameLevel-1]

    txtSurface=Surface((280,100)) #Surface to blit text
    if currentSubCaption.get_width()-currentCaption.get_width()>0: #If the caption is smaller than the subCaption
        txtSurface.blit(currentCaption,((currentSubCaption.get_width()-currentCaption.get_width())//2,0)) #Center the caption with the subcaption
        txtSurface.blit(currentSubCaption,(0,50)) 
    elif currentSubCaption.get_width()-currentCaption.get_width()<0: #If the caption is larger than the subcaption
        txtSurface.blit(currentCaption,(0,0))
        txtSurface.blit(currentSubCaption,(-(currentSubCaption.get_width()-currentCaption.get_width())//2,50)) #Center the subcaption with the caption
    
    txtSurface.set_alpha(int(txtAlpha)) #Set transparency based on previously capculated value
    txtSurface.set_colorkey((0,0,0)) #Make black transparent
    
    surface.blit(txtSurface,(170,150)) #Show text near top, centered on the game screen
    return txtAlpha
    

def createScrollStars(maxStars,surface):
    'Creates the initial starfield in levels (2D)'
    stars=[]
    for i in range(maxStars):
        star=[randint(0,surface.get_width()-1),randint(0,surface.get_height()-1),randint(1,100)] #[x,y,speed]
        if star[2]<60: #60% chance to move 1 unit per frame
            star[2]=1
        elif star[2]<95: #35% chance to move 1.5 units per frame
            star[2]=1.5
        else:           #5% chance to move 2 units per frame
            star[2]=2
        stars.append(star)
    return stars

def moveDrawStars(stars,surface):
    'Updates the starfield in levels'
    for star in stars:
        star[1]+=star[2] #Add star speed to y coord (Only move downwards)

        #Reset stars if offscreen
        if star[1]>=surface.get_height(): #If the star goes offscreen, generate another one
            star[1]=0
            star[0]=randint(0,surface.get_width()-1)
            star[2]=choice([1,1.5,2])

        #Set color depending on speed
        if star[2]==1:
          color=(100,100,100) #Stars moving slower are less visible
        elif star[2]==1.5:
          color=(150,150,150)
        elif star[2]==2:
          color=(200,200,200)

        draw.circle(surface,color,[int(star[0]),int(star[1])],int(star[2]))
        
def drawLayout(score,graze,health,bombFrame):
    'Draw the game layout'
    
    screen.blit(background,(0,0))
    draw.rect(screen,BORDERCOL,borderRect,2)   #Background pic and game border 
    scrollBG(level1BG,bg) #Function to draw the game screen
    screen.blit(scoreCaption,(750,10)) #Life and score meters
    screen.blit(lifeCaption,(750,110))
    if health>=0:
        screen.blit(healthList[health],(650,140)) #Health bar
    screen.blit(grazeCaption,(750,210))
    screen.blit(bombCaption,(760,310)) #Score and graze counters
    for i in range(bomb):
        bombFrame=drawBomb(640+60*i,350,bombFrame,bombList) #Bombs on the size

    scoreSet=scoreFont.render('0'*(8-int(len(str(score))))+str(score),1,WHITE)      #Update score and graze when nessecary
    screen.blit(scoreSet,(700,30))
    
    grazeSet=scoreFont.render('0'*(8-int(len(str(graze))))+str(graze),1,WHITE) #Value with enough leading zeros for 8 spaces
    screen.blit(grazeSet,(700,230))
    return bombFrame
    
scrollStarList=createScrollStars(250,bg) #Create the initial 2d starfield

def scrollBG(img,surface):
    'Updates the scrolling background and draws all elements onto the background'
    global scrollOffset, bombRadius, activeBomb, scrollStarList, txtAlpha, probeFocus
    
    imgH=img.get_height() #The height of the scroling background
    surface.blit(img,(0,0+scrollOffset)) #Blit the background with the offset and one right above it to give a continuous feel
    surface.blit(img,(0,-imgH+scrollOffset))
    moveDrawStars(scrollStarList,surface) #Update the 2d starfield
    
    if player==ship1: #Draw the bomb based on the same color as the ship
        draw.circle(surface,(255,0,0),[ship[0]+31,ship[1]+29],min(bombRadius,activeBomb[4]),min(bombRadius,5)) #The bomb can only be as large as the bomb radius and must have a positive width
    elif player==ship2:
        draw.circle(surface,(0,0,255),[ship[0]+31,ship[1]+29],min(bombRadius,activeBomb[4]),min(bombRadius,5))
    elif player==ship3:
        draw.circle(surface,(255,255,0),[ship[0]+31,ship[1]+29],min(bombRadius,activeBomb[4]),min(bombRadius,5))
    elif player==ship4:
        draw.circle(surface,(0,255,0),[ship[0]+31,ship[1]+29],min(bombRadius,activeBomb[4]),min(bombRadius,5))
    elif player==practiceShip:
        draw.circle(surface,(255,255,255),[ship[0]+31,ship[1]+29],min(bombRadius,activeBomb[4]),min(bombRadius,5))

    drawPlayer(surface) 
    drawProbeBullets(surface)
    drawPlayerProbes(surface)       
    drawPlayerBullets(surface)    #Draw all game features on the surface so it can smoothly exit the screen versus clipping the background
    drawScoreList(surface)   
    drawEnemyBullets(surface)
    drawEnemies(surface)
    doExplosions(surface)
    probeFocus=checkFocus(surface)
    txtAlpha=showLevelIntro(surface,levelCaptions,subCaptions,totalTime,txtAlpha,gameLevel)

    #REMOVE BEFORE SUBMIT
    #drawEnemyHitbox(surface)    
    #draw.rect(surface,(0,255,0),[ship[0],ship[1],player[0].get_width(),player[0].get_height()],1)
    #draw.circle(surface,(0,255,0),[ship[0]+31,ship[1]+29],25,1)
    
    screen.blit(surface,(25,15))   
    scrollOffset+=0.5
    if scrollOffset==imgH: #If the background has scrolled all the way past the screen, it can be reset so no more than 2 backgrounds are ever present
        scrollOffset=0

def createStars(numStars,maxDepth):
    'Creates the initial 3D starfield in the menus'
    stars=[]
    for i in range(numStars):
        star=[randint(-25,25), randint(-25,25), randint(1,maxDepth)] #[x,y,z]
        stars.append(star)
    return stars

def updateDrawStars(stars,maxDepth,oX,oY):
    'Updates 3D starfield and projects them with perspective projection'
    for star in stars:
        star[2]-=0.19 #Decrease depth

        #IF the star passes the screen, create a new star at the back
        if star[2]<=0:
            star[0]=randint(-25,25)
            star[1]=randint(-25,25)
            star[2]=maxDepth

        #Convert 3d coords into 2d via perspectivce projection (I searched the internet on how to do this)
        k=128/star[2]
        x=int(star[0]*k+originX)
        y=int(star[1]*k+originY)

        if 0<=x<originX*2 and 0<=y<originY*2: #If the star is on the screen
            size=(1-star[2]/maxDepth)*5
            shade=(1-star[2]/maxDepth)*255 #The star is darker the 'further' away it is
            draw.rect(screen,(shade,shade,shade),[x,y,size,size])

def drawBossSprites(bossSprites):
    'Draw the boss sprites on screen when the player beats the game'
    for i in bossSprites:
        if i[0]==miniSpin:
            i[1]+=1
            rotPic=transform.rotate(miniSpin[0],i[1])
            screen.blit(rotPic,(480-rotPic.get_width()//2,290-rotPic.get_height()//2))
        else:
            if bossSprites.index(i)==0: #Each index represents a different boss
                screen.blit(i[0][int(i[1])],(50,560))
            if bossSprites.index(i)==1:
                screen.blit(i[0][int(i[1])],(60,320))
            if bossSprites.index(i)==3:
                screen.blit(i[0][int(i[1])],(635,300))
            if bossSprites.index(i)==4:
                screen.blit(i[0][int(i[1])],(780,500))
            i[1]+=0.1
            if i[1]>=len(i[0]):
                i[1]=0
    return bossSprites

def checkHighScore():
    global score, gameLevel
    scoreFile=open("scores.txt","r")
    scoreLines=scoreFile.readlines()
    for i in range(5):
        scoreLines[i]=scoreLines[i].strip("\n") #get a list of all saved scores

    trophiesFile=open("trophies.txt","r")
    trophiesLines=trophiesFile.readlines()
    for i in range(5):
        trophiesLines[i]=trophiesLines[i].strip("\n") #get a list of trophy "ranks", tied to scores


    scoreList=[]
    score1=scoreLines[0].split(". ")
    score2=scoreLines[1].split(". ")
    score3=scoreLines[2].split(". ")
    score4=scoreLines[3].split(". ")
    score5=scoreLines[4].split(". ")
    scoreList.append(int(score1[1]))
    scoreList.append(int(score2[1]))
    scoreList.append(int(score3[1]))
    scoreList.append(int(score4[1]))
    scoreList.append(int(score5[1]))
    
    #scoreList is now full of all scores, from biggest to smallest

    if gameLevel==6: #so the trophies don't bug out if you beat the game (game level is 6)
        gameLevel=5
        
    if score>int(scoreList[0]): #new highest score
        scoreFile=open("scores.txt","w")
        scoreFile.write("1. %i\n" %(score))
        scoreFile.write("2. %i\n" %(int(score1[1])))
        scoreFile.write("3. %i\n" %(int(score2[1])))
        scoreFile.write("4. %i\n" %(int(score3[1])))
        scoreFile.write("5. %i" %(int(score4[1])))
        scoreFile.close()
        
        trophiesFile=open("trophies.txt","w") #corresponding trophy (what level they recieved that score on)
        trophiesFile.write(str(gameLevel)+"\n")
        trophiesFile.write(trophiesLines[0]+"\n")
        trophiesFile.write(trophiesLines[1]+"\n")
        trophiesFile.write(trophiesLines[2]+"\n")
        trophiesFile.write(trophiesLines[3])
        trophiesFile.close()

    if score==int(scoreList[0]) or score>int(scoreList[1]) and score<int(scoreList[0]): #second place
        scoreFile=open("scores.txt","w")
        scoreFile.write("1. %i\n" %(int(score1[1])))
        scoreFile.write("2. %i\n" %(score))
        scoreFile.write("3. %i\n" %(int(score2[1])))
        scoreFile.write("4. %i\n" %(int(score3[1])))
        scoreFile.write("5. %i" %(int(score4[1])))
        scoreFile.close()

        trophiesFile=open("trophies.txt","w") #corresponding trophy (what level they recieved that score on)
        trophiesFile.write(trophiesLines[0]+"\n")
        trophiesFile.write(str(gameLevel)+"\n")
        trophiesFile.write(trophiesLines[1]+"\n")
        trophiesFile.write(trophiesLines[2]+"\n")
        trophiesFile.write(trophiesLines[3])
        trophiesFile.close()

    if score==int(scoreList[1]) or score>int(scoreList[2]) and score<int(scoreList[1]): #third place
        scoreFile=open("scores.txt","w")
        scoreFile.write("1. %i\n" %(int(score1[1])))
        scoreFile.write("2. %i\n" %(int(score2[1])))
        scoreFile.write("3. %i\n" %(score))
        scoreFile.write("4. %i\n" %(int(score3[1])))
        scoreFile.write("5. %i" %(int(score4[1])))
        scoreFile.close()

        trophiesFile=open("trophies.txt","w")#corresponding trophy (what level they recieved that score on)
        trophiesFile.write(trophiesLines[0]+"\n")
        trophiesFile.write(trophiesLines[1]+"\n")
        trophiesFile.write(str(gameLevel)+"\n")
        trophiesFile.write(trophiesLines[2]+"\n")
        trophiesFile.write(trophiesLines[3])
        trophiesFile.close()

    if score==int(scoreList[2]) or score>int(scoreList[3]) and score<int(scoreList[2]): #fourth place
        scoreFile=open("scores.txt","w")
        scoreFile.write("1. %i\n" %(int(score1[1])))
        scoreFile.write("2. %i\n" %(int(score2[1])))
        scoreFile.write("3. %i\n" %(int(score3[1])))
        scoreFile.write("4. %i\n" %(score))
        scoreFile.write("5. %i" %(int(score4[1])))
        scoreFile.close()

        trophiesFile=open("trophies.txt","w")#corresponding trophy (what level they recieved that score on)
        trophiesFile.write(trophiesLines[0]+"\n")
        trophiesFile.write(trophiesLines[1]+"\n")
        trophiesFile.write(trophiesLines[2]+"\n")
        trophiesFile.write(str(gameLevel)+"\n")
        trophiesFile.write(trophiesLines[3])
        trophiesFile.close()

    if score==int(scoreList[3]) or score>int(scoreList[4]) and score<int(scoreList[3]) or score==int(scoreList[0]) and score==int(scoreList[1]) and score==int(scoreList[2]) and score==int(scoreList[3]) and score==int(scoreList[4]):
        #fifth place
        scoreFile=open("scores.txt","w")
        scoreFile.write("1. %i\n" %(int(score1[1])))
        scoreFile.write("2. %i\n" %(int(score2[1])))
        scoreFile.write("3. %i\n" %(int(score3[1])))
        scoreFile.write("4. %i\n" %(int(score4[1])))
        scoreFile.write("5. %i" %(int(score)))
        scoreFile.close()

        trophiesFile=open("trophies.txt","w")#corresponding trophy (what level they recieved that score on)
        trophiesFile.write(trophiesLines[0]+"\n")
        trophiesFile.write(trophiesLines[1]+"\n")
        trophiesFile.write(trophiesLines[2]+"\n")
        trophiesFile.write(trophiesLines[3]+"\n")
        trophiesFile.write(str(gameLevel))
        trophiesFile.close()


def reWriteLevels():
    'Determine which levels have been beaten'
    global gameLevel
    currentLevels=[1 for x in range(gameLevel)]+[0 for x in range(5-gameLevel)] #1 to represent the level has been beaten
    prevFile=open('LevelsCompleted.txt','r')
    prevLevels=prevFile.readlines()
    prevLevels=[int(x) for x in prevLevels] #Previous state of levels
    prevFile.close()

    newFile=open('LevelsCompleted.txt','w')
    for i in range(5):
        if prevLevels[i]==0 and currentLevels[i]==0: #Create a new file with the new levels (The outcome will only be a 0 if the player hasnt beat the level previously and hasnt beat it now)
            newFile.write('0\n')
        else:
            newFile.write('1\n')
    newFile.close()
            
def drawTrophies():
    'Draw trophies on leaderboard screen'
    trophiesFile=open("trophies.txt","r")
    trophiesLines=trophiesFile.readlines()
    for i in range(5):
        trophiesLines[i]=trophiesLines[i].strip("\n")
    x,y=200,100
    for i in range(5):
        if trophiesLines[i]=="0": #if booted up a fresh game, no trophy (equivalent to level 1)
            screen.blit(trophyPics[0],(x,y))
        else:
            screen.blit(trophyPics[int(trophiesLines[i])-1],(x,y)) #trophies correspond to level reached when obtaining high score - organized from least prestigious to most
                                                                    
        y+=125     

def stopMusic():
    'Stops the current music to allow for a smooth transition to the next screen'
    mixer.music.fadeout(750) #fade music
    mixer.music.stop() #stop music
        
        
def menu():
    'Logic for program menu'
    running=True
    fps=time.Clock()
    buttons=[Rect(330,y*80+400,300,60) for y in range(2)]
    vals=["practice","selection"] #Where the buttons will lead
    mixer.music.load("music/title.mp3") #Play title song
    mixer.music.play(-1)
    starList=createStars(512,32) #Create the initial 3d starfield
    while running:
        for evnt in event.get():          
            if evnt.type==QUIT:
                return "quit"
                
        mpos=mouse.get_pos()
        mb=mouse.get_pressed()
        
        screen.blit(titlepic,(0,-10)) 
        updateDrawStars(starList,32,originX,originY) #Update starfield
        #Draw all pictures and texts
        screen.blit(titleCaption,(260,120))
        screen.blit(logo,(320,180))        
        leaderRect=Rect(860,650,80,47)
        instructionRect=Rect(875,570,50,50)        
        screen.blit(leaderboardIcon,(860,650))
        screen.blit(playPic,(875,570))
        
        if leaderRect.collidepoint(mpos) and mb[0]==1:
            return "leaderboard"
        if instructionRect.collidepoint(mpos) and mb[0]==1:
            return 'instruction'
        
        for r,v in zip(buttons,vals):
            draw.rect(screen,BORDERINCOL,r)
            screen.blit(practiceModeCaption,(340,416))
            screen.blit(beginCaption,(370,495))
            if r.collidepoint(mpos):
                draw.rect(screen,HOVERCOL,r,2)
                if mb[0]==1:
                    time.wait(200) #Prevents the user from automatically clicking a ship when in selection mode
                    return v
            else:
                draw.rect(screen,(BORDERCOL),r,2)

        display.flip()
        fps.tick(80)
        display.set_caption("Hello, world! FPS:%i"%fps.get_fps())

def practice():
    global player, playerProbe, practiceMode, damageTaken, health
    running=True
    fps=time.Clock()
    buttons=[Rect(50,y*110+150,450,90) for y in range(5)]
    vals=[1,2,3,4,5]

    lvlFile=open('levelsCompleted.txt','r') #Determine which levels the player has reached
    lvlBeat=lvlFile.readlines()
    lvlBeat=[int(x) for x in lvlBeat]
    while running:
        for evnt in event.get():          
            if evnt.type==QUIT:
                return "menu"
            if evnt.type==KEYDOWN:
                if evnt.key==K_ESCAPE:
                    return 'menu'
        mpos=mouse.get_pos()
        mb=mouse.get_pressed()
        screen.blit(selectback,(0,0))
        screen.blit(backPracticeCaption,(25,40))
        for box,pLevel in zip(buttons,vals):
            draw.rect(screen,BORDERINCOL,box)
            draw.rect(screen,BORDERCOL,box,3)
            if lvlBeat[pLevel-1]==1:
                screen.blit(practiceCaptions[pLevel-1],(90,pLevel*110+42))
            else:
                screen.blit(noAccessCaption,(180,pLevel*108+50))
                
                
            if box.collidepoint(mpos):
                draw.rect(screen,HOVERCOL,box,3)
                if lvlBeat[pLevel-1]==1:
                    screen.blit(practicePrevs[pLevel-1],(545,185)) #BLit a picture of the level's boss
                    draw.rect(screen,BORDERCOL,[545,185,385,446],2)
                else:
                    draw.rect(screen,BORDERINCOL,[545,185,385,446])
                    draw.rect(screen,BORDERCOL,[545,185,385,446],2)
                    screen.blit(largeQuestionMark,(590,325)) #If the player hasnt reached the level, blit a question mark and text saying you must reach the level to preactice it
                    screen.blit(practiceInfoTxt,(585,500))
                    screen.blit(practiceInfoTxt2,(650,525))
                    screen.blit(practiceInfoTxt3,(615,550))
                
                if mb[0]==1 and lvlBeat[pLevel-1]==1:
                    practiceMode=True
                    damageTaken=0
                    player=practiceShip  #Set values for the game to make it practice mode, ie no damage, white ship etc
                    playerProbe=practiceProbe
                    restartGame(pLevel)
                    nextLevel()
                    health=4
                    return 'game'


        display.flip()
        fps.tick(80)
        display.set_caption("Hello, world! FPS:%i"%fps.get_fps())
        
    lvlFile.close()
    return 'menu'

def practiceCompleteScr():
    'Screen shown when the player completes practice'    
    running = True
    fps=time.Clock()
    buttons=[Rect(330,y*80+400,300,60) for y in range(2)]
    vals=['practice','menu']
    mixer.music.load("music/bad.mp3")
    mixer.music.play(-1)
    screen.blit(leaderCaption,(320,200))
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
            if evnt.type==KEYDOWN:
                if evnt.key==K_ESCAPE:
                    return 'menu'
        mpos=mouse.get_pos()
        mb=mouse.get_pressed()
        screen.fill((255,128,200))
        screen.blit(practiceCompleteBG,(0,-20))
        screen.blit(practiceDoneCaption,(210,70))
        
        for r,v in zip(buttons,vals):
            draw.rect(screen,BORDERINCOL,r)
            screen.blit(menuCaption,(425,494))
            screen.blit(practiceButtonCaption,(340,419))
            if r.collidepoint(mpos):
                draw.rect(screen,HOVERCOL,r,2)
                if mb[0]==1:
                    stopMusic()
                    time.wait(500)
                    return v
            else:
                draw.rect(screen,(BORDERCOL),r,2)
        display.flip()
        fps.tick(80)
        display.set_caption("Hello, world! FPS:%i"%fps.get_fps())

    return "menu"
        
def selection():
    'Screen to allow player to select a ship for playing'
    global player, playerProbe, practiceMode, health
    running=True
    
    x=130
    y=320
    shipFrame=0
    probeFrame=0
    starList=createStars(512,32) #Create initial starfield
    while running:
        for evnt in event.get():
            if evnt.type==QUIT:
                return "menu"
            if evnt.type==KEYDOWN:
                if evnt.key==K_ESCAPE:
                    return "menu"

        mpos=mouse.get_pos()
        mb=mouse.get_pressed()

        
        screen.blit(selectback,(0,0))
        updateDrawStars(starList,32,originX,originY) #Update stars
        screen.blit(selectCaption,(220,150))
        
        for i in range(4):
            screen.blit(selectionShips[int(4*i+shipFrame)],(170*i+x,y))
            screen.blit(selectionProbes[int(8*i+probeFrame)],(170*i+x+40,y+155)) #Blit animatated shiups and probes
        shipFrame+=0.1
        probeFrame+=0.1
        if shipFrame>=4:
            shipFrame=0
        if probeFrame>=8:
            probeFrame=0
            
        if shipRect.collidepoint(mpos) and mb[0]==1:
            pos=0
            player=ship1
            playerProbe=probe1
            time.wait(100)
            running=False

        if ship1Rect.collidepoint(mpos) and mb[0]==1:  #Determine which ship the player selects
            pos=1
            player=ship2
            playerProbe=probe2
            time.wait(100)
            running=False

        if ship2Rect.collidepoint(mpos) and mb[0]==1:
            pos=2
            player=ship3
            playerProbe=probe3
            time.wait(100)
            running=False

        if ship3Rect.collidepoint(mpos) and mb[0]==1:
            pos=3
            player=ship4
            playerProbe=probe4
            time.wait(100)
            running=False


        display.flip()
        fps.tick(80)
        display.set_caption("Hello, world! FPS:%i"%fps.get_fps())
        
    stopMusic() #Stops the music so the level music can play
    practiceMode=False
    health=3
    restartGame()
    nextLevel() #Resets all game variables for a fresh start
    return "game"

def game():
    'Game loop'
    global totalTime,scrOpacity,practiceMode,playerLevel,damageTaken, probeFocus, activeBomb,bomb,bombRadius,bombFrame, bossAttack, period,incdec, deadSoundPlayed,score,scoreGiven
    keys=key.get_pressed()
    running=True
    fps=time.Clock()
    mixer.music.load('music/level'+str(gameLevel)+'.mp3')
    mixer.music.play(-1)
    if not practiceMode:
        damageTaken=1
    scoreGiven=False
    while running:
        for evt in event.get():          
            if evt.type==QUIT:
                running=False
            if evt.type==KEYDOWN:
                if evt.key==K_ESCAPE:
                    pauseFX.play()
                    if practiceMode:
                        return 'practicePause'
                    return 'pause'

                
        totalTime+=0.0125 #Time increased as game progressed to spawn enemies
        
        period+=incdec  #Generates periodic values between 5 and negative 5 for certain burst attacks 
        if period>5:
            incdec=-0.03
        elif period<-5:
            incdec=0.03

        movePlayer()
        createPlayerBullets() #Move player and make it shoot
        updatePlayerBullets()

        activeBomb,bomb=initBomb(activeBomb,bomb)
        activeBomb,bombRadius=checkBomb(activeBomb,bombRadius)  #Bomb logic

        playerLevel=checkPlayerLevel()
        shootProbes(probeFocus) #Probes and focus logic
        updateProbeBullets()

        createEnemies() #Enemy logic
        updateEnemies()
        
        bossAttack=createEnemyBullets(bossAttack)
        checkForSplit()            #Enemy bullet logic
        updateEnemyBullets()

        checkGraze()
        checkPlayerBulletCollisions() #Collison logic
        checkEnemyPlayerCollisions()

        updateScoreList() #Dropped item logic
        giveScore()
        
        killBullets()
        killLingeringEnemies() #Memory saving logic
        killDeadEnemies()

        bombFrame=drawLayout(score,graze,health,bombFrame)
        screen.blit(transform.scale(logo,(275,145)),(660,480))   #Blitting bombs and logo on screen     


        if gameOver and len(explosionAnis)==0: #Screen will fade to black when you're out of lives and your explosion is done animating
            if deadSoundPlayed==0:
                plDeadFX.play()
                deadSoundPlayed=1 #Sound only plays once
            scrOpacity=fadeToBlack(scrOpacity) 
            stopMusic() #Stops music
            if scrOpacity==255:                
                return 'deathScr'
        
        if enemies[-1][5]<totalTime and activeEnemies==[] and len(explosionAnis)==0: #If the totaltime is after the last enemy spawn time and there are no enemies on screen
            screen.blit(scoreBonusCaption,(50,200))
            screen.blit(scoreAmounts[gameLevel-1],(225,275))
            if not scoreGiven:
                score+=(gameLevel*100000)
                scoreGiven=True
            scrOpacity=fadeToBlack(scrOpacity)
            stopMusic()
            if scrOpacity==255:
                if practiceMode:
                    return 'practiceCompleteScr'
                return 'levelCompleteScr'
        
        display.flip()
        fps.tick(80)
        display.set_caption("Hello, world! FPS:%i"%fps.get_fps())

    return "menu"

def deathScr(score):
    'Screen shwn when the player dies'
    running = True
    fps=time.Clock()
    buttons=[Rect(330,y*80+370,300,60) for y in range(2)]
    vals=["selection","menu"]
    screen.fill((255,0,0))
    finalScore=scoreFont.render("Your score was: %s" %(score),1,WHITE)
    screen.blit(finalScore,(480-finalScore.get_width()//2,290))
    mixer.music.load("music/death.mp3")
    mixer.music.play(-1)
    screen.blit(deathCaption,(320,200))
    checkHighScore() #Check highscore to see if you need to be placed on the leaderboards
    reWriteLevels() #Check if you reached a new level
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
            if evnt.type==KEYDOWN:
                if evnt.key==K_ESCAPE:
                    return 'menu'
        mpos=mouse.get_pos()
        mb=mouse.get_pressed()
        for r,v in zip(buttons,vals):
            draw.rect(screen,BORDERINCOL,r)
            screen.blit(againCaption,(380,386))
            screen.blit(menuCaption,(430,465))
            if r.collidepoint(mpos):
                draw.rect(screen,HOVERCOL,r,2)
                if mb[0]==1:
                    stopMusic()
                    time.wait(500)
                    return v
            else:
                draw.rect(screen,(BORDERCOL),r,2)
        display.flip()
        fps.tick(80)
        display.set_caption("Hello, world! FPS:%i"%fps.get_fps())
        
    return "menu"

def levelCompleteScr(score):
    'Screen shown when the player completes a level'
    global gameLevel, player
    running = True
    fps=time.Clock()
    buttons=[Rect(330,y*80+400,300,60) for y in range(1)]
    vals=["game"]
    gameLevel+=1
    if gameLevel==6:
        return 'gameCompleteScr'
    mixer.music.load("music/bad.mp3")
    mixer.music.play(-1)
    starList=createStars(512,32)
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        mpos=mouse.get_pos()
        mb=mouse.get_pressed()
        screen.blit(nextLevelPic,(0,0))
        currentScore=scoreFont.render("Your score is: %s" %(score),1,WHITE)
        screen.blit(currentScore,(480-currentScore.get_width()//2,490))
        updateDrawStars(starList,32,originX,originY)
        #Animate your ship on screen
        if player==ship1:
            screen.blit(ship1Next[int(ship[5])],(400,210))
            ship[5]+=0.1
            if ship[5]>=4:
                ship[5]=0
        if player==ship2:
            screen.blit(ship2Next[int(ship[5])],(400,210))
            ship[5]+=0.1
            if ship[5]>=4:
                ship[5]=0
        if player==ship3:
            screen.blit(ship3Next[int(ship[5])],(400,210))
            ship[5]+=0.1
            if ship[5]>=4:
                ship[5]=0
        if player==ship4:
            screen.blit(ship4Next[int(ship[5])],(400,210))
            ship[5]+=0.1
            if ship[5]>=4:
                ship[5]=0
        for r,v in zip(buttons,vals):
            draw.rect(screen,BORDERINCOL,r)
            screen.blit(nextLevelCaption,(380,414))

            if r.collidepoint(mpos):
                draw.rect(screen,HOVERCOL,r,2)
                if mb[0]==1:
                    stopMusic()
                    nextLevel() #Reset the enemy list so new enemies spawn
                    return v
            else:
                draw.rect(screen,(BORDERCOL),r,2)
        display.flip()
        fps.tick(80)
        display.set_caption("Hello, world! FPS:%i"%fps.get_fps())

    return "quit"



def gameCompleteScr(bossSprites,score): 
    'Screen shown when the player beats the game'

    running = True
    fps=time.Clock()
    buttons=[Rect(330,y*80+450,300,60) for y in range(2)]
    vals=["selection","menu"]
    screen.fill((23,43,123))
    mixer.music.load("music/gameEnd.mp3")
    mixer.music.play(-1)
    checkHighScore() #Check high score for leaderboards
    starList=createStars(512,32)
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
        mpos=mouse.get_pos()
        mb=mouse.get_pressed()
        screen.blit(gameCompletePic,(0,0))
        finalScore=scoreFont.render("Your final score is: %s" %(score),1,WHITE)
        screen.blit(finalScore,(480-finalScore.get_width()//2,660))
        updateDrawStars(starList,32,originX,originY)
        bossSprites=drawBossSprites(bossSprites) #Draw bosses on screen
        screen.blit(beatTheGameCaption,(30,100))
        for r,v in zip(buttons,vals):
            draw.rect(screen,BORDERINCOL,r)
            screen.blit(againCaption,(380,464))
            screen.blit(menuCaption,(430,545))
            if r.collidepoint(mpos):
                draw.rect(screen,HOVERCOL,r,2)
                if mb[0]==1:
                    stopMusic()
                    time.wait(500)
                    return v
            else:
                draw.rect(screen,(BORDERCOL),r,2)
        display.flip()
        fps.tick(80)
        display.set_caption("Hello, world! FPS:%i"%fps.get_fps())
        
    return "menu"

def pause(): 
    running = True
    fps=time.Clock()
    background=Surface((960,720))
    background.set_alpha(0)
    buttons=[Rect(175,y*80+370,300,60) for y in range(3)]
    vals=["game","selection","menu"]
    mixer.music.load("music/pause.mp3")
    mixer.music.play(-1)
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
            if evnt.type==KEYDOWN:
                if evnt.key==K_ESCAPE:
                    return 'game'
        mpos=mouse.get_pos()
        mb=mouse.get_pressed()
        screen.blit(background,(0,0))
        screen.blit(pauseCaption,(195,230))
        for r,v in zip(buttons,vals):
            draw.rect(screen,BORDERINCOL,r)
            screen.blit(resumeCaption,(250,384))
            screen.blit(restartCaption,(245,464))
            screen.blit(menuCaption,(275,544))
            if r.collidepoint(mpos):
                draw.rect(screen,HOVERCOL,r,2)
                if mb[0]==1:
                    stopMusic()
                    if v=="game":
                        mixer.unpause()
                        pauseFX.play()
                    if v=="selection":
                        mixer.music.load("music/title.mp3")
                        mixer.music.play(-1)
                        time.wait(500)
                    return v
            else:
                draw.rect(screen,(BORDERCOL),r,2)
        display.flip()
        fps.tick(80)
        display.set_caption("Hello, world! FPS:%i"%fps.get_fps())
        
    return "menu"

def practicePause():
    running = True
    fps=time.Clock()
    background=Surface((960,720))
    background.set_alpha(0)
    buttons=[Rect(175,y*80+370,300,60) for y in range(3)]
    vals=["game","practice","menu"]
    mixer.music.load("music/pause.mp3")
    mixer.music.play(-1)
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
            if evnt.type==KEYDOWN:
                if evnt.key==K_ESCAPE:
                    return 'game'
        mpos=mouse.get_pos()
        mb=mouse.get_pressed()
        screen.blit(background,(0,0))
        screen.blit(pauseCaption,(195,230))
        for r,v in zip(buttons,vals):
            draw.rect(screen,BORDERINCOL,r)
            screen.blit(resumeCaption,(250,384))
            screen.blit(restartCaption,(245,464))
            screen.blit(menuCaption,(275,544))
            if r.collidepoint(mpos):
                draw.rect(screen,HOVERCOL,r,2)
                if mb[0]==1:
                    stopMusic()
                    if v=="game":
                        mixer.unpause()
                        pauseFX.play()
                    else:
                        time.wait(500)
                    return v
            else:
                draw.rect(screen,(BORDERCOL),r,2)
        display.flip()
        fps.tick(80)
        display.set_caption("Hello, world! FPS:%i"%fps.get_fps())
        
    return "menu"

def instruction():
    'Intruction screen to teach players the basic controls'
    running=True
    while running:
        for evnt in event.get():
            if evnt.type==QUIT:
                running=False
            if evnt.type==KEYDOWN:
                if evnt.key==K_ESCAPE:
                    return 'menu'

        screen.blit(instructions,(0,0))
        display.flip()
        
    return "menu"

def leaderboard():
    'Screen that shows the leaderboard for top scores'
    global leaderFont
    global scoreLines
    scoreFile=open("scores.txt","r")
    scoreLines=scoreFile.readlines()
    for i in range(5):
        scoreLines[i]=scoreLines[i].strip("\n")
    running=True
    score1=leaderFont.render(scoreLines[0],1,WHITE)
    score2=leaderFont.render(scoreLines[1],1,WHITE)
    score3=leaderFont.render(scoreLines[2],1,WHITE) #Render all scores
    score4=leaderFont.render(scoreLines[3],1,WHITE)
    score5=leaderFont.render(scoreLines[4],1,WHITE)
    while running:
        for evnt in event.get():
            if evnt.type==QUIT:
                running=False
            if evnt.type==KEYDOWN:
                if evnt.key==K_ESCAPE:
                    return 'menu'

        screen.blit(leaderBackground,(0,0))
        screen.blit(leaderCaption,(190,0))
        screen.blit(score1,(300,100))
        screen.blit(score2,(300,225)) #Blit scores
        screen.blit(score3,(300,350))
        screen.blit(score4,(300,475))
        screen.blit(score5,(300,600))
        drawTrophies() #Draw corresponding trophy next to the score
        display.flip()

    scoreFile.close()
    return "menu"


###Logic controling which screen to show###   
page="menu"
while page!="quit":
    if page=="menu":
        page=menu()
    if page=="instruction":
        page=instruction()
    if page=='practice':
        page=practice()
    if page=="selection":
        page=selection()
    if page=="leaderboard":
        page=leaderboard()
    if page=="game":
        page=game()
    if page=='deathScr':
        page=deathScr(score)
    if page=='practiceCompleteScr':
        page=practiceCompleteScr()
    if page=='levelCompleteScr':
        page=levelCompleteScr(score)
    if page=='gameCompleteScr':
        page=gameCompleteScr(bossSprites,score)
    if page=='pause':
        page=pause()
    if page=='practicePause':
        page=practicePause()
        
quit()
