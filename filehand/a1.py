import turtle  

def circle(t):
    t.pensize(20)
    t.setposition(0,-280)
    t.pendown()
    t.begin_fill()
    t.color("yellow")
    t.pencolor("blue")
    t.circle(300)
    t.end_fill()
    t.penup()

def circle2(t):
    t.pensize(2)
    t.setposition(0,-230)
    t.pendown()
    t.begin_fill()
    t.color("red")
    t.circle(250)
    t.end_fill()
    t.penup()

def draw_s(t):
    t.setposition(-100,290)  
    t.pendown()
    t.begin_fill()
    t.color("red")
    t.pensize(10)
    t.pencolor("white")
    t.forward(340)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.backward(250)
    t.right(90)
    t.forward(200)
    t.left(90)
    t.forward(250)
    t.right(90)
    t.forward(250)
    t.left(90)
    t.backward(290)
    t.penup()
    t.setposition(-100,290)
    t.pendown()
    t.right(90)
    t.forward(290)
    t.left(90)
    t.forward(240)
    t.left(90)
    t.backward(170)
    t.right(90)
    t.backward(260)
    t.left(50)
    t.backward(80)
    t.right(40) 
    t.forward(120)
    t.end_fill()
    t.penup()




    
    

    


    
    



    

if __name__=='__main__':
    win=turtle.Screen()
    win.bgcolor("black")

    avengers=turtle.Turtle()
    avengers.speed(10)
    avengers.pensize(10)
    avengers.penup()
    
    circle(avengers)
    circle2(avengers)
    draw_s(avengers)
    avengers.penup()

    avengers.setposition(300,300)
    avengers.pencolor("red")

    avengers.write("code by SARUGESH") 
    avengers.hideturtle()
turtle.done()    
    
    