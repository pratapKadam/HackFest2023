# random pattern
# everytime corners increase,like star,triangle,rectangle and so on...
from turtle import *
speed(10)
color('yellow')
bgcolor('black')
b=200
while b>0:
    left(b)
    forward(b*2)
    b=b-2
done()   