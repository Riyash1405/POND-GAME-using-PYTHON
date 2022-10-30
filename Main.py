#IU2041230084:-Moksha Kothari
#IU2041230129:-Riyash Patel

import turtle

sc = turtle.Screen()
sc.title("Paddle ball game")
sc.bgcolor("Black")
sc.setup(width=1000, height=600)

left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("yellow")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)

right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("yellow")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)

hit_ball = turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("pink")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5

moksha = 0
riyash = 0
      
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("yellow")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Moksha : 0 Riyash: 0",align="center", font=("Courier", 24, "normal"))

def paddleaup():
  y = left_pad.ycor()
  y += 20
  left_pad.sety(y)

def paddleadown():
   y = left_pad.ycor()
   y -= 20
   left_pad.sety(y)

def paddlebup():
   y = right_pad.ycor()
   y += 20
   right_pad.sety(y)

def paddlebdown():
   y = right_pad.ycor()
   y -= 20
   right_pad.sety(y)
   sc.listen()
   sc.onkeypress(paddleaup, "w")
   sc.onkeypress(paddleadown, "s")
   sc.onkeypress(paddlebup, "Up")
   sc.onkeypress(paddlebdown, "Down")
 
  


sc.update()    
hit_ball.setx(hit_ball.xcor()+hit_ball.dx)
hit_ball.sety(hit_ball.ycor()+hit_ball.dy)
if hit_ball.ycor() > 280:
   hit_ball.sety(280)
   hit_ball.dy *= -1
if hit_ball.ycor() < -280:
   hit_ball.sety(-280)
   hit_ball.dy *= -1

if hit_ball.xcor() > 500:
		hit_ball.goto(0, 0)
		hit_ball.dy *= -1
		moksha += 1
		sketch.clear()
		sketch.write("Moksha : {} Riyash: {}".format(moksha, riyash), align="center",font=("Courier", 24, "normal"))

if hit_ball.xcor() < -500:
		hit_ball.goto(0, 0)
		hit_ball.dy *= -1
		riyash += 1
		sketch.clear()
		sketch.write("Moksha : {} Riyash: {}".format(moksha, riyash), align="center",font=("Courier", 24, "normal"))

if (hit_ball.xcor() > 360 and hit_ball.xcor() < 370) and (hit_ball.ycor() < right_pad.ycor()+40 and hit_ball.ycor() > right_pad.ycor()-40):
		hit_ball.setx(360)
		hit_ball.dx*=-1
		
if (hit_ball.xcor()<-360 and hit_ball.xcor()>-370) and (hit_ball.ycor()<left_pad.ycor()+40 and hit_ball.ycor()>left_pad.ycor()-40):
		hit_ball.setx(-360)
		hit_ball.dx*=-1

        
        
            
 
