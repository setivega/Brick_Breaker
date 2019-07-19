ballY = 350
ballX = 500

ySpeed = 10
xSpeed = 10

paddle1 = 400
paddle2 = 400

showBrick1 = True
showBrick2 = True
showBrick3 = True
showBrick4 = True
showBrick5 = True
showBrick6 = True
showBrick7 = True
showBrick8 = True
showBrick9 = True
showBrick10 = True
showBrick11 = True
showBrick12 = True
showBrick13 = True
showBrick14 = True
showBrick15 = True

firstColumn = [showBrick1, showBrick6, showBrick11]
secondColumn = [showBrick2, showBrick7, showBrick12]
thirdColumn = [showBrick3, showBrick8, showBrick13]
fourthColumn = [showBrick4, showBrick9, showBrick14]
fifthColumn = [showBrick5, showBrick10, showBrick15]

firstRow = [showBrick1, showBrick2, showBrick3, showBrick4, showBrick5]
secondRow = [showBrick6, showBrick7, showBrick8, showBrick9, showBrick10]
thirdRow = [showBrick11, showBrick12, showBrick13, showBrick14, showBrick15]

score = 0
lives = 3

# class Brick(object):
#     pass

# class Ball:


# class Game:


# Next steps

# In draw()
# Check if bricks are all gone
# Check bricks for collision
    # class Game:
        # def detect_hit(self, ball, brick):
            # Bouncing off sides and destroying brick
            # if (ballX > brick.left and ballY > brick.top and ballY < brick.bottom) or (ballX < brick.right and ballY > brick.top and ballY < brick.bottom):
                # property of show is false
                #xSpeed = -xSpeed


# Update state

# In setup()
# Create all game objects
# Place ball somewhere


def createGame():
    global score
    global lives
    global showBrick1
    global showBrick2
    global showBrick3
    global showBrick4
    global showBrick5
    global showBrick6
    global showBrick7
    global showBrick8
    global showBrick9
    global showBrick10
    global showBrick11
    global showBrick12
    global showBrick13
    global showBrick14
    global showBrick15

    # Paddle
    rect(mouseX - 75, 700, 150, 20)

    stroke(0, 0, 0)
    strokeWeight(1)

    # Bricks = [showBrick1, showBrick2, showBrick3, showBrick4, showBrick5]

    # x = 0

    # for brick in Bricks:
    #     if brick == True:
    #         fill(200,0,0)
    #         rect(x,0,200,50)
    #         x+=200

    # Check Brick
    if showBrick1 == True:
        fill(200, 0, 0)
        rect(0, 0, 200, 50)

    if showBrick2 == True:
        fill(200, 0, 0)
        rect(200, 0, 200, 50)

    if showBrick3 == True:
        fill(200, 0, 0)
        rect(400, 0, 200, 50)

    if showBrick4 == True:
        fill(200, 0, 0)
        rect(600, 0, 200, 50)

    if showBrick5 == True:
        fill(200, 0, 0)
        rect(800, 0, 200, 50)

    if showBrick6 == True:
        fill(239, 128, 32)
        rect(0, 50, 200, 50)

    if showBrick7 == True:
        fill(239, 128, 32)
        rect(200, 50, 200, 50)

    if showBrick8 == True:
        fill(239, 128, 32)
        rect(400, 50, 200, 50)

    if showBrick9 == True:
        fill(239, 128, 32)
        rect(600, 50, 200, 50)

    if showBrick10 == True:
        fill(239, 128, 32)
        rect(800, 50, 200, 50)

    if showBrick11 == True:
        fill(0, 200, 0)
        rect(0, 100, 200, 50)

    if showBrick12 == True:
        fill(0, 200, 0)
        rect(200, 100, 200, 50)

    if showBrick13 == True:
        fill(0, 200, 0)
        rect(400, 100, 200, 50)

    if showBrick14 == True:
        fill(0, 200, 0)
        rect(600, 100, 200, 50)

    if showBrick15 == True:
        fill(0, 200, 0)
        rect(800, 100, 200, 50)

    # Bottom Level Bricks
    # fill(0,200,0)
    # rect(0,100,200,50)
    # rect(200,100,200,50)
    # rect(400,100,200,50)
    # rect(600,100,200,50)
    # rect(800,100,200,50)

    x = 0
    while x < width - (width / 5):
        textSize(22)
        fill(0, 0, 0)
        text("50", x + 80, 35)
        x += 200

    x = 0
    while x < width:
        textSize(22)
        fill(0, 0, 0)
        text("20", x + 80, 85)
        x += 200

    # x=0
    # while x<width:
    #     textSize(22)
    #     fill(0,0,0)
    #     text("10", x+80, 135)
    #     x += 200

    fill(0, 0, 0)

    fill(255, 255, 255)
    textSize(22)
    text("Score: " + str(score), 10, 790)
    text("Lives: " + str(lives), 910, 790)

    noStroke()
    fill(255, 255, 255)

def gameOver(x):
    background(0, 0, 0)
    textSize(100)
    text("G A M E  O V E R", 100, 200)
    textSize(100)
    text(x, 270, 400)
    textSize(40)
    text("Play Again?", 400, 600)

def setup():

    size(1000, 800)
    background(255, 255, 255)
    createGame()


def draw():
    global ballY
    global ballX
    global ySpeed
    global xSpeed
    global paddle1
    global paddle2
    global score1
    global score2
    global firstColumn
    global secondColumn
    global thirdColumn
    global fourthColumn
    global fifthColumn
    global firstRow
    global secondRow
    global thirdRow
    global showBrick1
    global showBrick2
    global showBrick3
    global showBrick4
    global showBrick5
    global showBrick6
    global showBrick7
    global showBrick8
    global showBrick9
    global showBrick10
    global showBrick11
    global showBrick12
    global showBrick13
    global showBrick14
    global showBrick15
    global lives

    background(0, 0, 0)

    createGame()

    # Bounces off bottom of Brick
    if firstColumn == [True, True, True]:
        if ballY < 165 and ballX > 0 and ballX < 200 and showBrick6 == True:
            showBrick11 = False
            firstColumn = [False, True, True]
            ySpeed = -ySpeed
    elif firstColumn == [False, True, True]:
        if ballY < 115 and ballX > 0 and ballX < 200 and showBrick6 == True:
            showBrick6 = False
            firstColumn = [False, False, True]
            ySpeed = -ySpeed
    else:
        if ballY < 65 and ballX > 0 and ballX < 200 and showBrick1 == True:
            showBrick1 = False
            firstColumn = [False, False, False]
            ySpeed = -ySpeed

    if secondColumn == [True, True, True]:
        if ballY < 165 and ballX > 200 and ballX < 400 and showBrick12 == True:
            showBrick12 = False
            secondColumn = [False, True, True]
            ySpeed = -ySpeed
    elif secondColumn == [False, True, True]:
        if ballY < 115 and ballX > 200 and ballX < 400 and showBrick7 == True:
            showBrick7 = False
            secondColumn = [False, False, True]
            ySpeed = -ySpeed
    else:
        if ballY < 65 and ballX > 200 and ballX < 400 and showBrick2 == True:
            showBrick2 = False
            secondColumn = [False, False, False]
            ySpeed = -ySpeed

    if thirdColumn == [True, True, True]:
        if ballY < 165 and ballX > 400 and ballX < 600 and showBrick13 == True:
            showBrick13 = False
            thirdColumn = [False, True, True]
            ySpeed = -ySpeed
    elif thirdColumn == [False, True, True]:
        if ballY < 115 and ballX > 400 and ballX < 600 and showBrick8 == True:
            showBrick8 = False
            thirdColumn = [False, False, True]
            ySpeed = -ySpeed
    else:
        if ballY < 65 and ballX > 400 and ballX < 600 and showBrick3 == True:
            showBrick3 = False
            thirdColumn = [False, False, False]
            ySpeed = -ySpeed

    if fourthColumn == [True, True, True]:
        if ballY < 165 and ballX > 600 and ballX < 800 and showBrick14 == True:
            showBrick14 = False
            fourthColumn = [False, True, True]
            ySpeed = -ySpeed
    elif fourthColumn == [False, True, True]:
        if ballY < 115 and ballX > 600 and ballX < 800 and showBrick9 == True:
            showBrick9 = False
            fourthColumn = [False, False, True]
            ySpeed = -ySpeed
    else:
        if ballY < 65 and ballX > 600 and ballX < 800 and showBrick4 == True:
            showBrick4 = False
            fourthColumn = [False, False, False]
            ySpeed = -ySpeed

    if fifthColumn == [True, True, True]:
        if ballY < 165 and ballX > 800 and ballX < 1000 and showBrick15 == True:
            showBrick15 = False
            fifthColumn = [False, True, True]
            ySpeed = -ySpeed
    elif fifthColumn == [False, True, True]:
        if ballY < 115 and ballX > 800 and ballX < 1000 and showBrick10 == True:
            showBrick10 = False
            fifthColumn = [False, False, True]
            ySpeed = -ySpeed
    else:
        if ballY < 65 and ballX > 800 and ballX < 1000 and showBrick5 == True:
            showBrick5 = False
            fifthColumn = [False, False, False]
            ySpeed = -ySpeed

    # Bounces off sides of Brick
    # if firstColumn == [True,True,True,True,True]:
    #     if ballY < 150 and ballY > 100 and and ballX < 215 and showBrick1 == True:
    #         showBrick1 = False
    #         firstColumn = [False,True,True,True,True]
    #         ySpeed = -ySpeed
    # elif firstColumn == [False,True,True,True,True]:
    #     if ballY < 150 and ballY > 100 and and ballX < 215 and showBrick1 == True:
    #         showBrick1 = False
    #         firstColumn = [False,False,True,True,True]
    #         ySpeed = -ySpeed

    # Bounce of the Top
    if ballY < 15 and ballX > 0 and ballX < 200:
        ySpeed = -ySpeed
    elif ballY < 15 and ballX > 200 and ballX < 400:
        ySpeed = -ySpeed
    elif ballY < 15 and ballX > 400 and ballX < 600:
        ySpeed = -ySpeed
    elif ballY < 15 and ballX > 600 and ballX < 800:
        ySpeed = -ySpeed
    elif ballY < 15 and ballX > 800 and ballX < 1000:
        ySpeed = -ySpeed

    # elif ballY < 100 and ballX > 0 and ballX < 200:
    #         showBrick6 = False
    #         ySpeed = -ySpeed
    # elif ballY < 100 and ballX > 200 and ballX < 400:
    #         showBrick7 = False
    # elif ballY < 100 and ballX > 400 and ballX < 600:
    #         showBrick8 = False
    #         ySpeed = -ySpeed
    # elif ballY < 100 and ballX > 600 and ballX < 800:
    #         showBrick9 = False
    #         ySpeed = -ySpeed
    # elif ballY < 100 and ballX > 800 and ballX < 1000:
    #         showBrick10 = False
    #         ySpeed = -ySpeed

    ellipse(ballX, ballY, 30, 30)

    # Top and Bottom border
    if ballX > 985:
        xSpeed = -10
    elif ballX < 15:
        xSpeed = 10

    # THIS WHERE THE BALL HITS THE PADDLE
    if ballY > 685 and ballY < 710 and ballX > mouseX - 75 and ballX < mouseX + 75:
        ySpeed = -10
    elif ballY < 15:
        ySpeed = 10

    # Score Counter
    if ballY > 1500:
        if lives > 0:
            lives -= 1
            print(lives)
    #     elif lives == 0:
    #         gameOver("You Lose")
    #         if mousePressed:
    #             if mouseX > 400 and mouseX < 500 and mouseY > 500 and mouseY < 600:
    #                 lives = 3
    #                 score = 0

    # if firstColumn == [False, False] and secondColumn == [False, False] and thirdColumn == [False, False] and fourthColumn == [False, False] and fifthColumn == [False, False]:
    #     gameOver("You Win")
    #     if mousePressed:
    #         if mouseX > 400 and mouseX < 500 and mouseY > 500 and mouseY < 600:
    #             lives = 3
    #             score = 0

        ballY = 350
        ballX = 500
        ellipse(ballX, ballY, 30, 30)

    ballY += ySpeed
    ballX += xSpeed
