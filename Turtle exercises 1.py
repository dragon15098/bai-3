from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for i in range (3,7):
    color(colors[i-2])
    for j in range (i):    
        forward(100)
        left(360/i)
