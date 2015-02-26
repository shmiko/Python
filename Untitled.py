import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_triangle(some_turtle_2,dist):
    for i in range(1,8):
        some_turtle_2.right(45)
        some_turtle_2.forward(dist)
        some_turtle_2.right(45)
        some_turtle_2.forward(dist)
        

def draw_art():
    window = turtle.Screen()
    window.bgcolor("cyan")

    brad = turtle.Turtle()
    brad.color("red")
    brad.shape("turtle")
    brad.speed(8)

 #   for i in range(1,37):
 #       draw_square(brad)
 #       brad.right(10)

    angie = turtle.Turtle()
    angie.shape("triangle")
    angie.color("black")
    angie.speed(500)
    size = 5
   

    for i in range(1,45):
        draw_triangle(angie,size)
        angie.right(4)
        size = size + 2.5
        
    window.exitonclick()

draw_art()
