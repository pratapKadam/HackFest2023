from turtle import *

speed(0)
bgcolor('black')
colors=["red","yellow","cyan"]
for _ in range(3):
    color(colors[_])
    for i in range(500):
        fd(i*2/2+1 + _+1)
        lt(360/2+1.50 +_+1)

done()