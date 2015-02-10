#!/usr/bin/python
#Mininggui,py

from Tkinter import *
import Mining

def Mine():
	Mining.mine(httpEntry.get())

mainwindow = Tk()

httpLabel = Label(mainwindow, text = "Address to Mine")
httpLabel.pack(side =LEFT)

httpEntry = Entry(mainwindow, bd=5)
httpEntry.pack(side =RIGHT	)

httpButton = Button(mainwindow, text = "Mine!", command = Mine)
httpButton.pack()

mainwindow.mainloop()
