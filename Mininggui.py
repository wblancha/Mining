#!/usr/bin/python
#Mininggui,py

from Tkinter import *
import Mining

def Mine():
	Mining.mine(httpEntry.get(),countedfileentry.get())
	mainwindow.destroy()

	
mainwindow = Tk()

httpLabel = Label(mainwindow, text = "Address to Mine")
httpLabel.pack()

httpEntry = Entry(mainwindow, bd=5)
httpEntry.pack()

countedfilelabel = Label(mainwindow, text = "Name of file")
countedfilelabel.pack()

countedfileentry = Entry(mainwindow, bd=5)
countedfileentry.pack()

httpButton = Button(mainwindow, text = "Mine!", command = Mine)
httpButton.pack()



mainwindow.mainloop()
