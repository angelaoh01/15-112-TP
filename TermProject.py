#################################################
# TermProject.py
#
# Your name: Gaeun (Angela) Oh
# Your andrew id: gaoh
# Geometry Dash
# TP0 - 4/11
# TP1 - 4/16
#################################################

import cs112_s22_week6_linter
from cmu_112_graphics import *
 
def almostEqual(d1, d2, epsilon=1):
    #https://www.cs.cmu.edu/~112/notes/notes-data-and-operations.html
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

#Background
class Obstacle(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Triangle(Obstacle):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Platform(Obstacle):
    def __init__(self, x, y, a, b):
        self.x = x
        self.y = y
        self.a = a
        self.b = b

class MiniStep(Obstacle):
    def __init__(self, x, y, a = 50):
        self.x = x
        self.y = y
        self.a = a

def appStarted(app):
    app.startGame = False
    app.choice = ""
    app.chooseLevelX = 0
    app.chooseLevelY = 0
    app.levelChoice = ""
    app.chooseModeX = 0
    app.chooseModeY = 0
    app.ground = gameDimensions()[2]
    app.tempGround = app.ground
    app.cellSize = gameDimensions()[3]
    app.kerryX = 150
    app.kerryY = 210
    app.midAir = False
    app.timer = 0
    app.clicks = 0
    app.jumpInt = 0.0001
    app.speed = 2
    app.count = 0
    app.level = 0
    app.gameData = []
    app.levelData = []
    app.timerDelay = 10
    app.gameOver = False
    app.gameOverAlmost = False
    app.notGround = False
    app.hitMax = False
    app.obstacles = []
    app.intro = True
    app.collision = False
    
#Level 1
def createLevel(app):
    if app.levelChoice == "Level 1":
        level1 = []
        t1 = Triangle(400, app.ground)
        level1.append(t1)
        t2 = Triangle(500, app.ground)
        level1.append(t2)
        t3 = Triangle(700, app.ground)
        level1.append(t3)
        m1 = MiniStep(800, app.ground - 40)
        level1.append(m1)
        m2 = MiniStep(880, app.ground - 70)
        level1.append(m2)
        t4 = Triangle(1040, app.ground)
        level1.append(t4)
        t5 = Triangle(1060, app.ground)
        level1.append(t5)
        t6 = Triangle(1200, app.ground)
        level1.append(t6)
        t7 = Triangle(1300, app.ground)
        level1.append(t7)
        t8 = Triangle(1600, app.ground)
        level1.append(t8)
        t9 = Triangle(1700, app.ground)
        level1.append(t9)
        t10 = Triangle(1900, app.ground)
        level1.append(t10)
        t11 = Triangle(1920, app.ground)
        level1.append(t11)
        t15 = MiniStep(2150, app.ground - 40)
        level1.append(t15)
        t16 = MiniStep(2210, app.ground - 70)
        level1.append(t16)
        t13 = Platform(2320, app.ground, 75, 100)
        level1.append(t13)
        t17 = Triangle(2395, app.ground)
        level1.append(t17)
        t18 = Triangle(2500, app.ground)
        level1.append(t18)
        t19 = Triangle(2520, app.ground)
        level1.append(t19)
        t20 = Triangle(2700, app.ground)
        level1.append(t20)
        t21 = Triangle(2720, app.ground)
        level1.append(t21)
        t22 = MiniStep(2800, app.ground - 40)
        level1.append(t22)
        t23 = MiniStep(2870, app.ground - 80)
        level1.append(t23)
        t24 = Platform(2940, app.ground, 400, 70)
        level1.append(t24)
        t25 = Triangle(3000, app.ground - 70)
        level1.append(t25)
        t26 = Triangle(3100, app.ground - 70)
        level1.append(t26)
        app.obstacles.append(level1)

    elif app.levelChoice == "Level 2":
        level2 = []
        t1 = Triangle(400, app.ground)
        level2.append(t1)
        t2 = Triangle(500, app.ground)
        level2.append(t2)
        m1 = MiniStep(620, app.ground - 40)
        level2.append(m1)
        p1 = Platform(690, app.ground, 150, 30)
        level2.append(p1)
        t3 = Triangle(720, app.ground - 30)
        level2.append(t3)
        m2 = MiniStep(740, app.ground - 70)
        level2.append(m2)
        t4 = Triangle(960, app.ground)
        level2.append(t4)
        t5 = Triangle(980, app.ground)
        level2.append(t5)
        m3 = MiniStep(1000, app.ground - 40)
        level2.append(m3)
        m4 = MiniStep(1080, app.ground - 80)
        level2.append(m4)
        t6 = Triangle(1060, app.ground)
        level2.append(t6)
        p2 = Platform(1160, app.ground, 100, 70)
        level2.append(p2)
        p3 = Platform(1300, app.ground, 200, 70)
        level2.append(p3)
        t7 = Triangle(1370, app.ground - 70)
        level2.append(t7)
        t8 = Triangle(1390, app.ground - 70)
        level2.append(t8)
        t9 = Triangle(1700, app.ground)
        level2.append(t9)
        t10 = Triangle(1800, app.ground)
        level2.append(t10)
        t11 = Triangle(1900, app.ground)
        level2.append(t11)
        t12 = Triangle(1920, app.ground)
        level2.append(t12)
        m5 = MiniStep(2010, app.ground - 40)
        level2.append(m5)
        m6 = MiniStep(2090, app.ground - 80)
        level2.append(m6)
        m8 = MiniStep(2170, app.ground - 40)
        level2.append(m8)
        t13 = Triangle(2100, app.ground)
        level2.append(t13)
        t14 = Triangle(2120, app.ground)
        level2.append(t14)
        t15 = Triangle(2200, app.ground)
        level2.append(t15)
        app.obstacles.append(level2)

def createMiniLevels(app, level):
    #Mini Level 1
    if level % 2 == 0:
        miniLevel1 = []
        t1 = Triangle(400, app.ground)
        miniLevel1.append(t1)
        t2 = Triangle(420, app.ground)
        miniLevel1.append(t2)
        t3 = Triangle(600, app.ground)
        miniLevel1.append(t3)
        m1 = MiniStep(800, app.ground - 40)
        miniLevel1.append(m1)
        m2 = MiniStep(880, app.ground - 70)
        miniLevel1.append(m2)
        p1 = Platform(950, app.ground, 170, 40)
        miniLevel1.append(p1)
        p2 = Platform(1200, app.ground, 200, 80)
        miniLevel1.append(p2)
        t4 = Triangle(1020, app.ground - 40)
        miniLevel1.append(t4)
        t6 = Triangle(1270, app.ground - 80)
        miniLevel1.append(t6)
        t7 = Triangle(1410, app.ground)
        miniLevel1.append(t7)
        t8 = Triangle(1430, app.ground)
        miniLevel1.append(t8)
        app.obstacles.append(miniLevel1)

    #Mini Level 2
    if level % 2 == 1:
        miniLevel2 = []
        m1 = MiniStep(400, app.ground - 40)
        miniLevel2.append(m1)
        t0 = Triangle(470, app.ground)
        miniLevel2.append(t0)
        m2 = MiniStep(500, app.ground - 40)
        miniLevel2.append(m2)
        m3 = MiniStep(580, app.ground - 80)
        miniLevel2.append(m3)
        m4 = MiniStep(660, app.ground - 120)
        miniLevel2.append(m4)
        p1 = Platform(690, app.ground, 100, 100)
        miniLevel2.append(p1)
        p2 = Platform (830, app.ground, 100, 60)
        miniLevel2.append(p2)
        t3 = Triangle(1420, app.ground)
        miniLevel2.append(t3)
        t6 = Triangle(1030, app.ground)
        miniLevel2.append(t6)
        m5 = MiniStep(1020, app.ground - 40)
        miniLevel2.append(m5)
        t7 = Triangle(1200, app.ground)
        miniLevel2.append(t7)
        t8 = Triangle(1300, app.ground)
        miniLevel2.append(t8)
        t9 = Triangle(1400, app.ground)
        miniLevel2.append(t9)
        app.obstacles.append(miniLevel2)

def isInBoundary(app, x):
    #Kerry's coordinates
    minX = app.kerryX
    maxX = app.kerryX + 30
    if x <= maxX and x >= minX:
        return True
    return False

def distance(a, kerryX, kerryY, obstacleX, obstacleY):
    b = -1
    c = -2*obstacleX + obstacleY
    return abs(a*kerryX + b*kerryY + c)/(a**2+b**2)**0.5

def isCollision(app, obstacle):
    (kerryMinX, kerryMaxY, kerryMaxX, kerryMinY) = (app.kerryX, app.kerryY - 30, 
                                                    app.kerryX + 30, app.kerryY)
    if type(obstacle) == Triangle:
        if isInBoundary(app, obstacle.x):
            if kerryMinY >= obstacle.y - 25:
                if (distance(2, kerryMaxX, kerryMinY, 
                                        obstacle.x, obstacle.y) <= 0.1
                    or distance(-2, kerryMinX, kerryMinY, obstacle.x+12.5,
                                                    obstacle.y-25 <= 0.1)):
                    app.collision = True
                    return True
            app.collision = False
            return False
    if type(obstacle) == MiniStep:
        if (((app.kerryX > obstacle.x and app.kerryX < obstacle.x+obstacle.a) or 
        (app.kerryX+30 > obstacle.x and app.kerryX+30 < obstacle.x+obstacle.a))
        and (abs((obstacle.y) - kerryMinY) <= 5)):
            app.collision = True
            return True
        elif abs(app.kerryX - (obstacle.x+obstacle.a)) < app.speed:
            app.collision = False
            return False
    if type(obstacle) == Platform:
        if (((app.kerryX > obstacle.x and app.kerryX < obstacle.x+obstacle.a) 
                                        or (app.kerryX+30 >= obstacle.x and 
                                    app.kerryX+30 < obstacle.x+obstacle.a))
            and (((obstacle.y-obstacle.b) - kerryMinY) < 5 and 
                    ((obstacle.y-obstacle.b) - kerryMinY) >= 0)):
            app.collision = True
            return True
        elif abs(app.kerryX - (obstacle.x+obstacle.a)) < app.speed:
            app.collision = False
            return False
        elif (abs((app.kerryX + 30) - obstacle.x) < app.speed 
                and ((app.kerryY-30) >= (obstacle.y - obstacle.b) 
                or (app.kerryY >= (obstacle.y - obstacle.b)))):
            app.levelData.append((app.count))
            gameRestart(app)
        
def checkCollision(app, level):
    for obstacle in level:
        if type(obstacle) == Triangle:
            if isCollision(app, obstacle):
                app.levelData.append((app.count))
                gameRestart(app)
        elif type(obstacle) == MiniStep:
            if isCollision(app, obstacle):
                app.tempGround = obstacle.y
        elif type(obstacle) == Platform:
            if isCollision(app, obstacle):
                app.tempGround = obstacle.y - obstacle.b
            elif app.collision == False:
                app.tempGround = app.ground

def getMostFrequentDeathPoint(app, level):
    data = dict()
    counts = []
    result = []
    for point in level:
        num = 1 + data.get(point, 0)
        data[point] = num
    for key in data:
        counts.append(data[key])
    newCounts = sorted(counts)
    newCounts.reverse()
    for i in range(len(newCounts)):
        for key in data:
            if data[key] == newCounts[i]:
                if key not in result:
                    result.append(key)
    if len(result) >= 3:
        return result[0:3]
    elif len(result) < 3:
        return result

def gameRestart(app):
    app.kerryX = 150
    app.kerryY = 210
    app.midAir = False
    app.timer = 0
    app.count = 0
    app.level = 0
    app.obstacles = []
    app.gameData = []
    app.timerDelay = 10
    app.collision = False
    app.tempGround = app.ground
    app.speed = 2
    app.jumpInt = 0.00001
    if app.choice == "Standard":
        createLevel(app)
    elif app.choice == "Endless":
        createMiniLevels(app, 0)

def timerFired(app):
    if app.startGame == True:
        for i in range(len(app.obstacles)):
            checkCollision(app, app.obstacles[i])
        app.count += 1
        if app.level >= 2:
            points = getMostFrequentDeathPoint(app, 
                                app.gameData[app.level-2])
            if points == []:
                app.speed = 2.45
            else:
                flag = True
                for count in points:
                    #for obstacle in app.obstacles[app.level]:
                    if app.count >= count - 100 and app.count <= count + 100:
                        app.speed = 2
                        flag = False
                if flag:
                    app.speed = 2.45
        for i in range(len(app.obstacles)):
                for obstacle in app.obstacles[i]:
                    obstacle.x -= app.speed
        if app.choice == "Endless":
            if app.kerryX > app.obstacles[len(app.obstacles)-1][-1].x:
                app.gameData.append(app.levelData)
                app.level += 1
                createMiniLevels(app, app.level)
                app.levelData = []
                app.count = 0
        if app.choice == "Standard":
            if app.kerryX > app.obstacles[0][-1].x:
                app.gameOverAlmost = True
            if app.kerryX > app.obstacles[0][-1].x + 300:
                app.gameOver = True
        if app.midAir == True: #going up
            if(app.jumpInt > 0):
                app.jumpInt -= 0.2
            else:
                app.midAir = False
                app.hitMax = True
            moveKerry(app)
        elif app.midAir == False and app.hitMax == True: #falling down
            if app.kerryY >= app.tempGround:
                app.jumpInt = 0.0001
                app.hitMax = False
            else:
                app.jumpInt -= 0.2
                moveKerry(app)
        elif app.midAir == False:
            app.jumpInt -= 0.2
            if app.kerryY >= app.tempGround:
                app.kerryY = app.tempGround 
                app.jumpInt = 0.0001    
            moveKerry(app)
    if app.gameOver == True:
        appStarted(app)
    

def keyPressed(app, event):
    if ((event.key == "Up" or event.key == "Space")
            and (app.midAir == False and app.hitMax == False)):
        moveKerry(app)
        app.jumpInt = 5
        app.midAir = True
        app.intro = False

def mousePressed(app, event):
    app.chooseModeX = event.x
    app.chooseModeY = event.y
    app.clicks += 1
    if (app.chooseModeX >= app.width/2 - 200 
        and app.chooseModeX < app.width/2 - 40) and app.clicks == 1:
        #createLevel(app)
        app.choice = "Standard"
        #app.startGame = True
    elif (app.choice == "Standard" and (app.chooseModeY < app.height/2 - 5
                                    and app.chooseModeY > app.height/2 - 40)
                                    and app.clicks == 2):
        app.levelChoice = "Level 1"
        app.startGame = True
        createLevel(app)
    elif (app.choice == "Standard" and (app.chooseModeY > app.height/2 + 5
                                    and app.chooseModeY < app.height/2 + 40)
                                    and app.clicks == 2):
        app.levelChoice = "Level 2"
        app.startGame = True
        createLevel(app)
    elif (app.chooseModeX >= app.width/2 + 40 
            and app.chooseModeX < app.width/2 + 200
            and app.clicks == 1):
        app.choice = "Endless"
        createMiniLevels(app, app.level)
        app.startGame = True

def moveKerry(app):
    app.kerryY -= app.jumpInt

def addLevel(app):
    createLevel(app, app.level)

def drawIntro(app, canvas):
    canvas.create_text(300, 75, text = "Kerry Dash", fill = "blue", 
                                        font = "Helvetica 36 bold")

def drawChooseLevel(app, canvas):
    canvas.create_rectangle(app.width/6, app.height/6, app.width/6 + 200,
                            app.height/6 + 200, fill = "beige")

def drawGround(app, canvas):
    canvas.create_line(0, app.ground, app.width, app.ground, 
                        fill = "black", width = 2)

def drawKerry(app, canvas):
    x0 = app.kerryX
    y0 = app.kerryY - 30
    x1 = app.kerryX + 30
    y1 = app.kerryY
    #change the dimesensions into something more generic
    canvas.create_rectangle(x0, y0, x1, y1, fill = "mediumslateblue", width = 0)

def drawObstacles(app, canvas):    
    for i in range(len(app.obstacles)):
        for obstacle in app.obstacles[i]:
            if type(obstacle) == Triangle:
                drawTriangles(app, canvas, obstacle.x, obstacle.y)
            if type(obstacle) == Platform:
                drawPlatform(app, canvas, obstacle.x, obstacle.y, 
                                                obstacle.a, obstacle.b)
            if type(obstacle) == MiniStep:
                drawMiniSteps(app, canvas, obstacle.x, obstacle.y)

def drawTriangles(app, canvas, x, y):
    x1 = x + 25
    y1 = y
    x2 = x + 12.5
    y2 = y - 25
    canvas.create_polygon(x, y, x1, y1, x2, y2, fill = "black")

def drawPlatform(app, canvas, x, y, a, b):
    y1 = y - b
    x1 = x + a
    canvas.create_rectangle(x, y1, x1, y, fill = "black")

def drawMiniSteps(app, canvas, x, y):
    x1 = x + 50
    canvas.create_line(x, y, x1, y, fill = "black", width = 2)

def gameDimensions():
    rows = 10
    cols = 20
    cellSize = 30
    ground = rows*cellSize - 3*cellSize
    return (rows, cols, ground, cellSize)

def redrawAll(app, canvas):
    if app.startGame == False and app.intro == True:
        drawIntro(app, canvas)
        canvas.create_text(app.width/2, app.height/2 - 30, text = "Choose Mode",
                            fill = "green", font = "Helvetica 26 bold")
        canvas.create_rectangle(app.width/2 - 40, app.height/3 + 70,
                                app.width/2 - 200, app.height/3 + 160, 
                                fill = "lightblue")
        canvas.create_text(app.width/2-120, app.height/3 + 115, 
                        text = "Standard Mode", fill = "black", 
                        font = "Helvetica 16")
        canvas.create_rectangle(app.width/2 + 40, app.height/3 + 70,
                                app.width/2 + 200, app.height/3 + 160,
                                fill = "lightblue")
        canvas.create_text(app.width/2+120, app.height/3 + 115,
                            text = "Endless Mode", fill = "black",
                            font = "Helvetica 16")
        if app.choice == "Standard":
            canvas.create_rectangle(app.width/2 - 200, app.height/2 - 70,
                                app.width/2 + 200, app.height/2 + 70, 
                                fill = "beige")
            canvas.create_rectangle(app.width/2 - 60, app.height/2 - 40, 
                                app.width/2 + 60, app.height/2 - 5,
                                fill = "pink")
            canvas.create_rectangle(app.width/2 - 60, app.height/2 + 5, 
                                app.width/2 + 60, app.height/2 + 40,
                                fill = "pink")
            canvas.create_text(app.width/2, app.height/2 - 20,
                                text = "Level 1", fill = "black",
                                font = "Helvetica 16") 
            canvas.create_text(app.width/2, app.height/2 + 20,
                                text = "Level 2", fill = "black",
                                font = "Helvetica 16")  

    if app.gameOverAlmost == True:
        canvas.create_text(app.width/2, app.height/3, 
                        text = "Congragulations! You finished!", 
                        fill = "orange",
                        font = "Helvetica 34")
    if app.startGame == True:
        drawGround(app, canvas)
        drawKerry(app, canvas)
        drawObstacles(app, canvas)
    

def playDash():
    (rows, cols) = (gameDimensions()[0], gameDimensions()[1])
    cellSize = gameDimensions()[3]
    gameWidth = (cols*cellSize)
    gameHeight = (rows*cellSize)
    runApp(width = gameWidth, height = gameHeight)

playDash()
