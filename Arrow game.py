import turtle
import math
import random


score = 0
wn = turtle.Screen()
wn.bgcolor("black")
wn.tracer(1)
#border
bp=turtle.Turtle()
bp.color("white")
bp.penup()
bp.setposition(-300,-300)
bp.pendown()
bp.pensize(3)
for side in range (4):
	bp.forward(600)
	bp.left(90)
bp.hideturtle()
bp.penup()
bp.setposition(-290,310)
scorestring="Score: %s" %score
bp.write(scorestring, False, align="left", font=("Arial",14,"normal"))

player=turtle.Turtle()
player.color("red")#spalva
player.shape("triangle")#forma
player.penup()#pašalina uodega
player.speed(0)
#zgoal

maxGoals=3

goals = []
for count in range(maxGoals):
	goals.append(turtle.Turtle())
	goals[count].color("blue")#spalva
	goals[count].shape("circle")#forma
	goals[count].penup()
	goals[count].speed(0)
	goals[count].setposition(random.randint(-250,250),random.randint(-250,250))
	#goals[count].right(random.randint(0,360))
# variables
speed=1

#functions
def turnleft():
	player.left(30)
def turnright():
	player.right(30)
def morespeed():
	global speed
	speed +=1
def lessspeed():
	global speed
	speed -=1
def isColision(t1,t2):
	d=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
	if d < 20:
		return True
	else: return False
#bindings
turtle.listen()
turtle.onkey(turnleft,"a")
turtle.onkey(turnright,"d")
turtle.onkey(morespeed,"w")
turtle.onkey(lessspeed,"s")
while True:
	player.forward(speed)
	#check
	if player.xcor() > 290 or player.xcor() < -290:
		player.right(180)
	if player.ycor() > 290 or player.ycor() < -290:
		player.right(180)
	#Moving goal
	for count in range(maxGoals):
		goals[count].forward(random.randint(3,5))
		#check
		if goals[count].xcor() > 290 or goals[count].xcor() < -290:
			goals[count].right(180)
		if goals[count].ycor() > 290 or goals[count].ycor() < -290:
			goals[count].right(180)
		#Colision?

		if isColision(player, goals[count]):
			goals[count].setposition(random.randint(-250,250),random.randint(-250,250)) 
			goals[count].right(random.randint(0,360))
			score +=1
			bp.undo()
			bp.penup()
			bp.hideturtle()
			bp.setposition(-290,310)
			scorestring="Score: %s" %score

			bp.write(scorestring, False, align="left", font=("Arial",14,"normal"))

delay = raw_input("Press enter to finish.")