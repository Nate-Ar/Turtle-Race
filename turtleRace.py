import turtle as t
import random
import time
moving = True
# Face Up
t.mode('logo')
# Create Pets
print('Jarry is Green')
print('Benny is Yellow')
print('Frank is Pink')
print('Shrang is Orange')
jarry = t.Turtle()
benny = t.Turtle()
frank = t.Turtle()
shrang = t.Turtle()
line = t.Turtle()
# Define Shape
pets = [jarry, benny, frank, shrang]
colors = ['green', 'yellow', 'pink', 'orange']
num = 150
colCount = 0
# Set Options
for x in pets:
    x.up()
    x.goto(num, -300)
    x.shape('turtle')
    x.down()
    x.fillcolor(colors[colCount])
    colCount = colCount +1
    num = num - 100
# Draw Finish LIine
line.up()
line.goto(-300,380)
line.down()
line.right(90)
line.fd(600)
line.hideturtle()
# Move Characters


while moving:
    if round(jarry.ycor()) >= 380:
        print('Jarry  Won')
        break
    if round(shrang.ycor()) >= 380:
        print('Shrang Won')
        break
    if round(benny.ycor()) >= 380:
        print('Benny Won')
        break
    if round(frank.ycor()) >= 380:
        print('Frank Won')
        break
    jarry.fd(random.randrange(0,10))
    benny.fd(random.randrange(0,10))
    frank.fd(random.randrange(0,10))
    shrang.fd(random.randrange(0,10))


# Give Time to See Who Won
time.sleep(5)
