# hearts flower pattern

import turtle 

# turtle.speed(15780)
turtle.bgcolor('black')
turtle.pensize(5)

def func():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

def heart(c1,c2):
    turtle.color(c1,c2)
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(111.65)
    func()
    turtle.left(120)
    func()
    turtle.forward(111.65)
    turtle.end_fill()
    turtle.hideturtle()
    
# for i in range(5):
#     heart('#14786'+str(i),"#96582"+str(i))    
heart('pink','red')
heart('yellow','cyan')
heart('red','pink')
heart('cyan','yellow')
heart('pink','red')
heart('pink','red')
heart('yellow','cyan')
heart('red','pink')
heart('cyan','yellow')
heart('pink','red')
    
turtle.done()
