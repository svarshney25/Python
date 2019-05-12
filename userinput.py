import turtle, time
t = turtle.Pen()
t.speed(10)
# Ask the user for the number of circles in their rosette, default to 20
number_of_circles = int (turtle.numinput("Number of circles", "How many circles do you want in your rosette?", 20))

for x in range(number_of_circles):
    t.circle(100)
    t.right(360/number_of_circles)

time.sleep(5)
