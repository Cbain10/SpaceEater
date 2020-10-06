import turtle,random

t = turtle.Turtle()
t.up()
screen = turtle.Screen()
screen.tracer(0)
score = 0
lives = 3
level = 1

scoreKeeper = turtle.Turtle()
scoreKeeper.up()
scoreKeeper.goto(-200,220)
scoreKeeper.ht()

liveKeeper = turtle.Turtle()
liveKeeper.up()
liveKeeper.goto(-200,210)
liveKeeper.ht()

box = turtle.Turtle()
box.speed(0)
box.up()
box.goto(-200,200)
box.down()
for i in range(4):
  box.forward(400)
  box.right(90)
box.ht()
screen.update()

balls = []
for i in range(3):
  ball = turtle.Turtle()
  ball.speed(0)
  ball.up()
  ball.goto(random.randint(-190,190), random.randint(-190,190))
  ball.shape("circle")
  ball.right(random.randint(0,360))
  ball.color("red")
  balls.append(ball)
screen.update

def changeLevel():
  screen.bgcolor("blue")
  scoreKeeper.color("white")
  liveKeeper.color("white")
  t.color("white")
  box.color("white")
  for i in range(4):
    box.forward(400)
    box.right(90)
  for i in range(5):
    ball2 = turtle.Turtle()
    ball2.speed(0)
    ball2.up()
    ball2.goto(random.randint(-190,190), random.randint(-190,190))
    ball2.shape("circle")
    ball2.right(random.randint(0,360))
    ball2.color("red")
    balls.append(ball2)

def changeBallColor():
  for ball in balls:
    ball.color("yellow")

def gameOver():
  t.goto(-30,0)
  t.write("GAME OVER!")
  t.ht()

def turnLeft():
  t.left(15)
def turnRight():
  t.right(15)

screen.onkey(turnLeft, "left")
screen.onkey(turnRight, "right")
screen.listen()

while True:
  if level == 1:
    t.forward(2)
  elif level == 2:
    t.forward(5)
  for ball in balls:
    ball.forward(3)
    if ball.xcor() > 200 or ball.xcor() < -200 or ball.ycor() > 200 or ball.ycor() < -200:
      ball.right(180)
    if abs(ball.xcor() - t.xcor()) < 10 and abs(ball.ycor() - t.ycor()) < 10:
      ball.goto(random.randint(-190,190), random.randint(-190,190))
      score += 1
    else: 
      scoreKeeper.clear()
      scoreKeeper.write("Score: " + str(score))
    
  if t.xcor() > 200 or t.xcor() < -200 or t.ycor() > 200 or t.ycor() < -200:
    t.right(180)
    lives -= 1
  else:
    liveKeeper.clear()
    liveKeeper.write("Health: " + str(lives))
  screen.update()

  if score == 5:
    level +=1
    changeLevel()
    changeBallColor()
    score +=1
  #has an end to the game, can be beaten or lost
  if lives == 0:
    gameOver()
    lives = -1
  screen.update()  