from turtle import *

forward(15)
speed(0)
color('red', 'yellow')
begin_fill()
counter = 322
lef = 20
rig = 200
forw = -744
while counter:
    counter -= 1
    down()
    forward(forw)
    left(lef)
    forward(forw)
    right(rig)
    forward(forw)
    left(lef)
    forward(forw)
    right(rig)
    forward(forw)
    right(rig)
    forward(forw)
    left(lef)
    lef += 1
    rig += 1
    forw += 9

    if abs(pos()) < 1:
        break
end_fill()
done()