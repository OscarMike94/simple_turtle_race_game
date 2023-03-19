import turtle
import random

screen = turtle.Screen()
screen.title("Turtle Race")

finish_line = turtle.Turtle()
finish_line.ht()
finish_line.penup()
finish_line.goto(200, 200)
finish_line.pendown()
finish_line.goto(200, -200)

colors = ["red", "blue", "green", "orange", "purple"]
turtles = []
for i in range(5):
    turtles.append(turtle.Turtle(shape="turtle"))
    turtles[i].penup()
    turtles[i].goto(-200, 40*i - 80)
    turtles[i].color(colors[i])
    turtles[i].pendown()
bet = input(f"Enter your bet (color of winning turtle): {colors}")

winner = None
while not winner:
    for t in turtles:
        distance = random.randint(0, 10)
        t.forward(distance)
        if t.xcor() >= 200:
            winner = t.color()[0]
            break

text = turtle.Turtle()
text.penup()
text.ht()
text.goto(-50, 0)
text.write(f"The winner is the {winner} turtle!")
if bet.lower() == winner:
    text.goto(-50, -30)
    text.write("Congratulations, you won your bet!")
else:
    text.goto(-50, -30)
    text.write("Sorry, you lost your bet.")

turtle.done()
