from turtle import *

setup(width = 1.0, height=1.0)
goto(-150,40)
bgcolor("black")
tracer(5)
hideturtle()

def star(size):
    if size<=7:
        return
    else:
        for i in range(5):
            fd(size)
            star(size/2)
            rt(144)

speed(0)

colors = ["#DD4124", "#6B5B95", "#88B04B", "#F7CAC9", "#009B77", "#D65076","#45B8AC","black"]
switch = True

for i,col in enumerate(colors):

	if i >=6:
		switch = False
		begin_fill()
		color(col)
		star(235)
		end_fill()
		width(2)
	elif i>1 and i<3 or i>4 and i<6:
		color(col)
		star(235)		
	elif switch:
	    color(col)
	    star(235)
	    clear()

done()
