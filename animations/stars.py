import turtle, random

t = turtle.Pen()
t.speed(8)

turtle.bgcolor("black")
t.pencolor("gold")  # setting color
limit = 400
ylimit = 330
count = random.choice(range(1, 50))
for n in range(count):
    t.penup()
    t.setpos(0, 0)
    location = (random.choice(range(-limit, limit)), random.choice(range(-ylimit, ylimit)))
    t.setpos(location)
    t.pendown()
    t.width(random.choice(range(3, 6)))

    t.setheading(144/4)
    size = random.choice(range(2, 9))
    for x in range(5):
        t.forward(size*20)  # moving forward
        t.left(144)  # moving left

turtle.done()
