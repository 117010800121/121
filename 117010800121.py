import turtle

turtle.bgcolor("red")
turtle.fillcolor("yellow")
turtle.color('yellow')
turtle.speed(10)

turtle.begin_fill()
turtle.up()
turtle.goto(-300,170) 
turtle.down()
for i in range (5):    
    turtle.forward(150)
    turtle.right(144)
turtle.end_fill()

turtle.begin_fill()
turtle.up()
turtle.goto(-80,250)
turtle.setheading(305)
turtle.down()
for i in range (5):    
    turtle.forward(50)
    turtle.left(144)

turtle.end_fill()


turtle.begin_fill()
turtle.up()
turtle.goto(-40,150)
turtle.setheading(30)
turtle.down()
for i in range (5):  
    turtle.forward(50)
    turtle.right(144)

turtle.end_fill()

turtle.begin_fill()
turtle.up()
turtle.goto(-35,80)
turtle.setheading(5)
turtle.down()
for i in range (5):   
    turtle.forward(50)
    turtle.right(144)

turtle.end_fill()

turtle.begin_fill()
turtle.up()
turtle.goto(-80,20)
turtle.setheading(300)
turtle.down()
for i in range (5):  
    turtle.forward(50)
    turtle.left(144)

turtle.end_fill()
