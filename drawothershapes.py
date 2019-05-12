# 2.2 turtle circle 
import time
import turtle

t = turtle.Pen()


t.fillcolor("aqua")
# begin to fill
# circle number 1
t.begin_fill()
t.circle(100)
t.right(90)
t.end_fill()
# circle number 2 
t.fillcolor("hotpink")
t.begin_fill()
t.circle(100)
t.right(90)
t.end_fill()
# circle number 3 
t.fillcolor("royalblue")
t.begin_fill()
t.circle(100)
t.right(90)
t.end_fill()
# circle number 4 
t.fillcolor("mediumspringgreen")
t.begin_fill()
t.circle(100)
t.right(90)
# end to fill color
t.end_fill()

# waiting 5 seconds and quit 
time.sleep(10)
