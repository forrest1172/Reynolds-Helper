from cgitb import grey, text
from contextlib import nullcontext
from ctypes import sizeof

from msilib.schema import Font, RadioButton
from multiprocessing import Value
from random import random, randrange
from secrets import choice
import string
from time import sleep
import tkinter as tk
from tkinter import CENTER, E, LEFT, W, font
from turtle import bgcolor, textinput, width
from types import LambdaType
import keyboard
import pyautogui
from setuptools import Command
import time

window = tk.Tk()
window.title("Reynolds Helper")
window.geometry("420x300")
window.configure(bg='blue')




def TakeInput():
    outPutWet = inputWetTech.get()
    outPutDry = inputDryTech.get()
    outPutVin = inputVin.get()
    outPutMiles = inputMiles.get()
    outPutAdv = inputAdv.get()

    if(len(outPutVin) >= 8):
        print("Wet tech-" + outPutWet)
        print("Dry tech(s)-" + outPutDry)
        tagLetter = choice(string.ascii_uppercase)
        tagNumber = choice(string.digits) + choice(string.digits)
        tag = tagLetter + tagNumber
        time.sleep(3)
        MainWrite(outPutVin,outPutAdv,outPutMiles,tag)

    else:
        print("Please enter an 8 digit VIN#")
        return

#Advisor # and label
newlabel = tk.Label(text="Advisor#",width=12)
newlabel.grid(column=0,row=0)
newlabel.configure(bg='yellow')

inputAdv = tk.Entry(window,width=3)
inputAdv.grid(column=0,row=1)


#wet tech vin and label
newlabel = tk.Label(text="Wet Tech#",width=12)
newlabel.grid(column=0,row=2)
newlabel.configure(bg='yellow')

inputWetTech = tk.Entry(window,width=3)
inputWetTech.grid(column=0,row=3)
inputWetTech.insert(0,"PitTroll")


#dry techs vin and label
newlabel = tk.Label(text="Dry Tech(s)#",width=10)
newlabel.grid(column=0,row=4)
newlabel.configure(bg='yellow')

inputDryTech = tk.Entry(window,width=20)
inputDryTech.grid(column=0,row=5)




#vin number input and label
newlabel = tk.Label(text="VIN#")
newlabel.grid(column=0,row=6)
newlabel.configure(bg='yellow')

inputVin = tk.Entry(window,width=17)
inputVin.grid(column=0,row=7)
inputVin.insert(0,"Last 8 of VIN#")

#milage input and label
newlabel = tk.Label(text="Milage")
newlabel.grid(column=0,row=8)
newlabel.configure(bg='yellow')

inputMiles = tk.Entry(window,width=6)
inputMiles.grid(column=0,row=9)


def MainWrite(outputvin,outputadv,outputmiles,tag):
    pyautogui.write("3601")
    pyautogui.keyDown("enter")

    pyautogui.write("2")
    pyautogui.keyDown("enter")

    pyautogui.write(outputvin)
    pyautogui.keyDown("enter")

    pyautogui.write("1")
    pyautogui.keyDown("enter")

    time.sleep(1)
    pyautogui.write(outputadv)
    pyautogui.keyDown("enter")
    pyautogui.keyDown("enter")

    pyautogui.write(outputmiles)
    pyautogui.keyDown("enter")

    pyautogui.write(tag)
    pyautogui.keyDown("enter")
    

def LOF(outputmiles):
    pyautogui.write("1")
    pyautogui.keyDown("enter")

    pyautogui.write("14")
    pyautogui.keyDown("enter")

    pyautogui.write("E")
    pyautogui.keyDown("enter")

    pyautogui.keyDown("enter")
    pyautogui.keyDown("enter")
    pyautogui.keyDown("enter")
    pyautogui.keyDown("enter")

    pyautogui.write("9")
    pyautogui.keyDown("enter")

    pyautogui.write()
    pyautogui.keyDown("enter")

r = tk.StringVar()

#radio buttons
radioBtn = tk.Radiobutton(window,text="LOF",variable=r, value="Lube oil and Filter",border=4,bg="yellow",command=lambda:clicked(r.get()))
radioBtn.place(height=32,width=46,x=150,y=25,anchor=W)


radioBtn1 = tk.Radiobutton(window,text="ROF", variable=r, value="Lube, oil, filter, and a tire rotation",border=4,bg="yellow",command=lambda:clicked(r.get()))
radioBtn1.place(height=32,width=46,x=150,y=65,anchor=W)

radioBtn2 = tk.Radiobutton(window,text="TD",variable=r, value="'Turkey Dinner' ROF, both engine + cabin air filters",border=4,bg="yellow",command=lambda:clicked(r.get()))
radioBtn2.place(height=32,width=100,x=200,y=65,anchor=W)

radioBtn3 = tk.Radiobutton(window,text="ROT",variable=r, value="All four Tire-Rotation",border=4,bg="yellow",command=lambda:clicked(r.get()))
radioBtn3.place(height=32,width=46,x=200,y=25,anchor=W)


def clicked(value):
    infoLabel = tk.Label(window,text=value,bg=("blue"))
    infoLabel.place(height=100,width=300,x=120,y=145,anchor=W)
    infoLabel.configure(font=('Helvetica bold',10))


#submit button
submitBtn= tk.Button(window,text="Submit",height=2,width=8,command = lambda: TakeInput())
submitBtn.grid(column=5,row=25)
submitBtn.configure(bg='yellow')

window.mainloop()
