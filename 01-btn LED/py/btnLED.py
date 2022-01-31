import sys
from tkinter import *
from PIL import Image, ImageTk
import RPi.GPIO as GPIO
import time

ws = Tk()
ledPin = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT)


def change_img(Switch):
    if (Switch == 1):
        img2 = ImageTk.PhotoImage(Image.open("resources/on.png"))
        label.configure(image=img2)
        label.image = img2

    else:
        img2 = ImageTk.PhotoImage(Image.open("resources/off.png"))
        label.configure(image=img2)
        label.image = img2


def switchLED():
    switchResult = 0
    if switchButton.config('text')[-1] == 'APAGAR':
        switchButton.config(text='ENCENDER')
        GPIO.output(ledPin, GPIO.LOW)
        switchResult = 0
    else:
        switchButton.config(text='APAGAR')
        GPIO.output(ledPin, GPIO.HIGH)
        switchResult = 1
    change_img(switchResult)


def Comandos():
    switchLED()
    change_img(switchLED())


def exitAPP():
    GPIO.cleanup()
    sys.exit()


img1 = ImageTk.PhotoImage(Image.open("resources/off.png"))
label = Label(ws, image=img1)
label.pack()

ws.attributes('-fullscreen', True)
switchButton = Button(text="ENCENDER", width=10, command=switchLED)
switchButton.pack(pady=10)
button = Button(ws, text="Change", command=change_img)
ws.bind("<Return>", change_img)
btnExit = Button(ws, text="Salir", command=exitAPP).pack()
ws.mainloop()
