import turtle, time
t=turtle.Pen()

turtle.bgcolor('black')
colors=['silver', 'dark orchid', 'turquoise', 'deep pink']
for x in range(200):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.left(91)

time.sleep(10)
