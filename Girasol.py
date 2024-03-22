import math
import turtle

turtle.bgcolor("black")
turtle.shape("turtle")
turtle.speed(0)

# Dibujar la flor
turtle.fillcolor("brown")
turtle.begin_fill()
phi = 137.508 * (math.pi / 180.0)
for i in range(160 + 40):
    r = 4 * math.sqrt(i)
    theta = i * phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(i * 137.508)
    turtle.pendown()
    turtle.end_fill()
    if i < 160:
        turtle.stamp()
    else:
        turtle.fillcolor("yellow")
        turtle.begin_fill()
        turtle.right(20)
        turtle.forward(70)
        turtle.left(40)
        turtle.forward(70)
        turtle.left(140)
        turtle.forward(70)
        turtle.left(40)
        turtle.forward(70)
        turtle.end_fill()

# Agregar el tallo
turtle.penup()
turtle.goto(-12, -155)  # Posición inicial del tallo
turtle.pendown()
turtle.color("green")
turtle.pensize(15)
turtle.setheading(270)  # Orientar hacia abajo
turtle.forward(150)  # Longitud del tallo

# Agregar el título
turtle.penup()
turtle.goto(0, 250)  # Ajusta la posición donde se mostrará el texto
turtle.pendown()
turtle.color("red")
turtle.write("Te quiero <3", align="center", font=("Arial", 28, "normal"))

turtle.hideturtle()
turtle.done()























