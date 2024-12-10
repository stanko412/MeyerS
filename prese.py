import turtle


t = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()


screen = turtle.Screen()
screen.setup(1000, 1000)
screen.bgcolor("medium blue")

# Hide the turtles
t.hideturtle()
t2.hideturtle()


t.color("white")
t.penup()
t.goto(0, 75)
t.pendown()
t.write("All About Me", font=("Arial", 65, "bold"), align="center")


t.penup()
t.goto(0, 0)
t.pendown()
t.write("By Meyer Stanko", font=("Arial", 24, "bold"), align="center")


input("Press enter to continue: ")
t.clear()

screen.bgcolor("green")
t.penup()
t.goto(0, 300)
t.pendown()
t.write("My favorite foods are chicken, pasta, and pizza.", font=("Arial", 30, "bold"), align="center")

# Load and display images
turtle.addshape("legs5.gif")
t2.shape("legs5.gif")
t2.goto(0,-100)
a = t2.stamp()

turtle.addshape("pasta.gif")
t2.shape("pasta.gif")
t2.goto(0,-100)
b = t2.stamp()

turtle.addshape("pizza.gif")
t2.shape("pizza.gif")
t2.goto(0,-100)
c = t2.stamp()


input("Press enter to continue: ")
t.clear()


screen.bgcolor("grey")
t.penup()
t.goto(0, 300)
t.pendown()
t.write("My favorite hobbies are: basketball, collecting shoes, music, and video games.", font=("Arial", 15, "bold"), align="center")


turtle.addshape("music.gif")
t2.shape("music.gif")
t2.goto(0,-100)
t2.goto(0,-100)
b= t2.stamp()
turtle.addshape("shoes.gif")
t2.shape("shoes.gif")
t2.goto(0,-100)
b= t2.stamp()
t2.goto(0,-100)
turtle.addshape("ps5.gif")
t2.shape("ps5.gif")
t2.goto(0,-100)
c = t2.stamp()
t2.goto(0,-100)
turtle.addshape("hobbie.gif")
t2.shape("hobbie.gif")
t2.goto(0,-100)
d = t2.stamp()
t2.goto(0,-100)

input("Press enter to continue: ")
t.clear()
screen.bgcolor("blue")
t.penup()
t.goto(0, 300)
t.pendown()
t.write("My favorite movie is whiplash.", font=("Arial", 30, "bold"), align="center")
turtle.addshape("movie.gif")
t2.shape("movie.gif")
t2.goto(0,-100)
a = t2.stamp()


input("Press enter to continue: ")


screen.bgcolor("purple")
t.clear()



turtle.done()