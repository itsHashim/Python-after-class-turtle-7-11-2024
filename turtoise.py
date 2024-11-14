import turtle


screen = turtle.Screen()
screen.bgcolor("white")


pen = turtle.Turtle()


def draw_triangle():
    pen.penup()
    pen.goto(-200, 100)  
    pen.pendown()
    pen.color("blue")
    for _ in range(3):
        pen.forward(100)  
        pen.left(120)      


def draw_rectangle():
    pen.penup()
    pen.goto(0, 100)  
    pen.pendown()
    pen.color("green")
    for _ in range(2):
        pen.forward(150)  
        pen.right(90)
        pen.forward(80)   
        pen.right(90)


def draw_hexagon():
    pen.penup()
    pen.goto(200, 100)   
    pen.pendown()
    pen.color("red")
    for _ in range(6):
        pen.forward(70)   
        pen.left(60)      


def draw_shapes():
    draw_triangle()
    draw_rectangle()
    draw_hexagon()


draw_shapes()
turtle.done()



