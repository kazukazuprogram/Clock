#coding: utf-8
#Clock

from tkinter import *
import time, sys

ver = 'Clock 0.0.0\nCopyright 2017 Cabbage All Rights Reserved.'

print(ver)

if '-v' in sys.argv:
    exit()

tk = Tk()
tk.title('Clock')
ca = Canvas(tk, width=200, height=50)
ca.pack()
tk.update()

def readargs():
    global textcolor
    global backgroundcolor
    arg = sys.argv
    textcolor = 'black'
    if '-c' in arg:
        textcolor = arg[(arg.index('-c') + 1)]
    backgroundcolor = 'white'
    if '-b' in arg:
        backgroundcolor = arg[(arg.index('-b') + 1)]

def sk(i):
    sa = str(i)
    if len(sa) == 1:
        sa = '0' + sa
    return sa

def start():
    global del_id
    global id
    global textcolor
    global backgroundcolor
    global printdebug
    readargs()
    del_id = [ca.create_rectangle(0, 0, 500, 500, fill=backgroundcolor)]
    id = ca.create_text(100, 30, text='', fill=textcolor, font=('Source Code Pro Medium', 30))

def rv():
    global id
    t = time.localtime()
    tt = sk(str(t.tm_hour)) + ':' + sk(str(t.tm_min)) + ':' + sk(str(t.tm_sec))
    ca.itemconfig(id, text=tt)

start()

while True:
    rv()
    tk.update()
    time.sleep(1)
