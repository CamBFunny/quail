import turtle

colors = ["red", "yellow", "green", "purple", "blue", "orange"]

t = turtle.Pen()
t.speed(10)

# changes the background color
turtle.bgcolor("black")

# make spiral_web
for x in range(1000):
    t.pencolor(colors[x % 6])  # setting color
    t.width(x / 200 + 1)  # setting width
    t.forward(x/2)  # moving forward
    t.left(59)  # moving left

turtle.done()
