import time
import math
from tkinter import *

width,height = 800,800

root = Tk()
root.geometry("800x800")
c = Canvas(root,width=width,height=height,bg="#888888")

root.title("Clock")

#creates a circle with at xy with size and color as args
def oval(x1,y1,size,color):
	o = c.create_oval(x1-size/2,y1-size/2,x1+size/2,y1+size/2,width=0,fill=color)

#creates the pointers
def visualizer(position,lenght,time,color,x1=width/2,y1=height/2,width1=3):
	deg = 360/position
	hyp = lenght
	pointer = []

	sin = math.sin(math.radians(time*deg-90))
	cath = hyp*sin
	aath = math.sqrt(hyp**2-cath**2)

	if time < round(360/deg/2):
		x2,y2 = x1+aath,y1+cath
		l = c.create_line(width/2,height/2,x2,y2,width=width1,fill=color)
	else:
		x2,y2 = x1-aath,y1+cath
		l = c.create_line(width/2,height/2,x2,y2,width=width1,fill=color)

#converts the 24h format to a 12h format so we can easily draw the pointer onto the clock
def twelvehcorrect(hour):
	if hour > 11:
		return hour-12
	else:
		return hour

#im pretty sure this is not needed anymore. will be removed in later version. 
def hcorrect(hour):
	if hour > 60:
		return 0
	else:
		return hour

while True:
	c.delete("all")

	oval(width/2,height/2,410,"#dddddd")
	oval(width/2,height/2,400,"#ffffff")
	for n in range(60):
		visualizer(60,200,n+1,"#000000",width1=1)
	oval(width/2,height/2,350,"#ffffff")
	for n in range(60):
		if (n+1)%5 == 0:
			visualizer(60,200,n+1,"#000000",width1=1)
	oval(width/2,height/2,325,"#ffffff")

	#grabs the local time of the pc and converts them if needed to the right format
	ct = time.localtime()
	ct = [[ct[5]+1,60,170,"#0000ff"],[ct[4],60,150,"#00ff00"],[hcorrect(twelvehcorrect(ct[3])*5),60,100,"#ff0000"]]
	for obj in ct:
		visualizer(obj[1],obj[2],obj[0], obj[3])
	
	c.pack()
	root.update()


"""
																	credits jax0033@protonmail.com
"""