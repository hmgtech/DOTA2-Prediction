from tkinter import *
import tkinter as tk

from tkinter import filedialog
from tkinter import messagebox  

import joblib 
import skimage
from skimage.io import imread
from skimage.transform import resize
import numpy as np

from PIL import ImageTk, Image

classifier = joblib.load('dota2.h5') 

global a



def test():
	print("Testing...")
	# Test code will go here....
	a = cluster.get()
	g = gm.get()
	t = gt.get()

	predictions = [[a,	g,	t,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,]]

	

	pos1 = g1.get()
	pos2 = g2.get()
	pos3 = g3.get()
	pos4 = g4.get()
	pos5 = g5.get()
	pos6 = g6.get()
	pos7 = g7.get()
	pos8 = g8.get()
	pos9 = g9.get()
	pos10 = g10.get()

	predictions[0][pos1] = g1h.get()
	predictions[0][pos2] = g2h.get()
	predictions[0][pos3] = g3h.get()
	predictions[0][pos4] = g4h.get()
	predictions[0][pos5] = g5h.get()
	predictions[0][pos6] = g6h.get()
	predictions[0][pos7] = g7h.get()
	predictions[0][pos8] = g8h.get()
	predictions[0][pos9] = g9h.get()
	predictions[0][pos10]= g10h.get()

	print(predictions)

	result = classifier.predict(predictions)

	print(result)

	if a==0 or g==0 or t==0:
		Label(win,text="Please Enter Correct Details!!",fg="blue",bg="yellow",font = ("Calibri 12 bold")).place(x=540,y=580)


	elif result[0] == 1:
	    print("Won")
	    Label(win,text="                                                            ",fg="red",bg="white",font = ("Calibri 12 bold")).place(x=540,y=580)
	    Label(win,text="Team Won!!",fg="blue",bg="yellow",font = ("Calibri 12 bold")).place(x=540,y=580)
	    MsgBox = tk.messagebox.showinfo ('information','Huraay!!, Team Won!! ', icon = 'info')

	    
	else:
	    print("Loss")
	    Label(win,text="                                                              ",fg="red",bg="white",font = ("Calibri 12 bold")).place(x=540,y=580)
	    Label(win,text="Team Lost!!",fg="red",bg="white",font = ("Calibri 12 bold")).place(x=540,y=580)
	    MsgBox = tk.messagebox.showwarning ('warning','Team Lost!!',icon = 'warning')


win =  Tk()

win.geometry("870x650")
# win.geometry("{0}x{1}+0+0".format(500, win.winfo_screenheight()))
win.configure(background="cyan")
win.title("Dota 2 Game Result Prediction By Hitesh")
win.iconbitmap('1.ico')

title = Label(win,text="Dota 2 Game Result Prediction",bg="gray",width="30",height="2",fg="White",font = ("Calibri 20 bold italic underline"))
title.place(x=0,y=0)

my_img = ImageTk.PhotoImage(Image.open("1.jpg"))
my_label = Label(image=my_img)
my_label.place(x=400,y=0)


cluster = IntVar()
gm = IntVar()
gt = IntVar()

g1 = IntVar()
g2 = IntVar()
g3= IntVar()
g4 = IntVar()
g5 = IntVar()
g6 = IntVar()
g7 = IntVar()
g8 = IntVar()
g9 = IntVar()
g10 = IntVar()
g1h = IntVar()
g2h = IntVar()
g3h= IntVar()
g4h = IntVar()
g5h = IntVar()
g6h = IntVar()
g7h = IntVar()
g8h = IntVar()
g9h = IntVar()
g10h = IntVar()




Cluster = Label(win, text="Cluster ID: ",bg="cyan",font = ("Verdana 12")).place(x=12,y=100)
Cluster = Entry(win,textvariable = cluster,width=30)
Cluster.place(x=120,y=100)


Game_mode = Label(win, text="Game Mode: ",bg="cyan",font = ("Verdana 12")).place(x=12,y=140)
Game_mode = Entry(win,textvariable = gm,width=30)
Game_mode.place(x=120,y=140)


Game_type = Label(win, text="Game Type: ",bg="cyan",font = ("Verdana 12")).place(x=12,y=180)
Game_type = Entry(win,textvariable = gt,width=30)
Game_type.place(x=120,y=180)

Label(win, text="At which Game?",bg="cyan",font = ("Verdana 12")).place(x=12,y=220)
Label(win, text="Played as Hero from team side(1) or from Opposite(-1) ?",bg="cyan",font = ("Verdana 12")).place(x=180,y=220)

Game1 = Entry(win,textvariable = g1,width=20).place(x=12,y=260)
Game1h = Entry(win,textvariable = g1h,width=20).place(x=182,y=260)

Game2 = Entry(win,textvariable = g2,width=20).place(x=12,y=300)
Game2h = Entry(win,textvariable = g2h,width=20).place(x=182,y=300)

Game3 = Entry(win,textvariable = g3,width=20).place(x=12,y=340)
Game3h = Entry(win,textvariable = g3h,width=20).place(x=182,y=340)

Game4 = Entry(win,textvariable = g4,width=20).place(x=12,y=380)
Game4h = Entry(win,textvariable = g4h,width=20).place(x=182,y=380)

Game5 = Entry(win,textvariable = g5,width=20).place(x=12,y=420)
Game5h = Entry(win,textvariable = g5h,width=20).place(x=182,y=420)

Game6 = Entry(win,textvariable = g6,width=20).place(x=12,y=460)
Game6h = Entry(win,textvariable = g6h,width=20).place(x=182,y=460)

Game7 = Entry(win,textvariable = g7,width=20).place(x=12,y=500)
Game7h = Entry(win,textvariable = g7h,width=20).place(x=182,y=500)

Game8 = Entry(win,textvariable = g8,width=20).place(x=12,y=540)
Game8h = Entry(win,textvariable = g8h,width=20).place(x=182,y=540)

Game9 = Entry(win,textvariable = g9,width=20).place(x=12,y=580)
Game9h = Entry(win,textvariable = g9h,width=20).place(x=182,y=580)

Game10 = Entry(win,textvariable = g10,width=20).place(x=12,y=620)
Game10h = Entry(win,textvariable = g10h,width=20).place(x=182,y=620)



path = Label(win,bg="cyan",font = ("Verdana 8"))
path.place(x=140,y=600)

submit = Button(win, text="Test", width="12",height="1",activebackground="violet", bg="Pink",command = test,font = ("Calibri 12 ")).place(x=540, y=540)

win.mainloop()


