#it's my first line 
import turtle, time 
t = turtle.Pen()

for x in range (1,100):
    #draw line 100  
    t.forward(100+x)
    t.left(90)
    t.forward(100+x)
    t.left(90)
    t.forward(100+x)
    t.left(90)
    t.forward(100+x)

time.sleep(10)


