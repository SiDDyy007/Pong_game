import turtle
import winsound


win = turtle.Screen()
win.title("Pong Game by Siddhant")
win.bgcolor("black")
win.setup(width=800,height=600)
win.tracer(0)



score_a = 0
score_b = 0


paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.penup()
paddle_a.goto(-350,0)
paddle_a.shapesize(stretch_wid=5,stretch_len=1)


paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.penup()
paddle_b.goto(+350,0)
paddle_b.shapesize(stretch_wid=5,stretch_len=1)

ball = turtle.Turtle()
ball.speed(10)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.3
ball.dy = 0.3

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0,260)
pen.hideturtle()
pen.write("Blue Team:0 Red Team:0",align = "center",font=("Courier",24,"normal"))


def paddle_a_up():
    y = paddle_a.ycor()
    y+= 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y-= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y+= 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y-= 20
    paddle_b.sety(y)


win.listen()
win.onkeypress(paddle_a_up,"w")
win.onkeypress(paddle_a_down,"s")
win.onkeypress(paddle_b_up,"Up")
win.onkeypress(paddle_b_down,"Down")



while True:
    win.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290 :
         ball.sety(290)
         ball.dy *= -1
         winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
         
    if ball.ycor() < -290 :
            ball.sety(-290)
            ball.dy *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
            ball.goto(0,0)
            ball.dx *= -1
            score_a +=1
            pen.clear()
            pen.write("Blue Team:{} Red Team:{}".format(score_a,score_b),align = "center",font=("Courier",24,"normal"))
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:
            ball.goto(0,0)
            ball.dx *= -1
            pen.clear()
            score_b +=1
            pen.write("Blue Team:{} Red Team:{}".format(score_a,score_b),align = "center",font=("Courier",24,"normal"))
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    if (ball.xcor() > 340 and ball.xcor()< 350) and (ball.ycor()<paddle_b.ycor() + 50) and (ball.ycor() > paddle_b.ycor() -50):
        
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor()<paddle_a.ycor() + 50) and (ball.ycor() > paddle_a.ycor() -50):
        
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        

    
    
