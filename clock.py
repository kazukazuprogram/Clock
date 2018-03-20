#coding: utf-8
#Clock 0.0.0
#Copyright 2017 Cabbage All Rights Reserved.
#python C:\Users\owner\code\project01_Clock\clock.py

from tkinter import *
import time, sys

ver = 'Clock 0.0.0\nCopyright 2017 Cabbage All Rights Reserved.'
help = '''<<HELP>>
-c [color]            : Set color of text [color].
-b [color]            : Set color of background [color].
-v                    : Show version and exit.
-f [FONT]             : Set font of text [FONT]
-h or --help          : Show this help and exit.
-H or --japanese-help : Show Japanese help and exit.'''
jhelp = '''<<ヘルプ>>
-c [color]                  : 文字色を[color]にします。
-b [color]                  : 背景色を[color]にします。
-v                          : バージョンを表示し、終了します。
-f [FONT]                   : フォントを[FONT]にします。
-h もしくは --help          : 英語のヘルプを表示し、終了します。
-H もしくは --japanese-help : このヘルプを表示し、終了します。'''
print(ver)
if '-h' in sys.argv or '--help' in sys.argv:
    print(help)
    exit()
elif '-H' in sys.argv or '--japanese-help' in sys.argv:
    print(jhelp)
    exit()

if '-v' in sys.argv:
    exit()

textsize = 50
if '-s' in sys.argv:
    textsize = int(sys.argv[sys.argv.index('-s') + 1])

tk = Tk()
tk.title('Clock')
ca = Canvas(tk, width=450, height=65)
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
    global textsize
    readargs()
    del_id = [ca.create_rectangle(0, 0, 500, 500, fill=backgroundcolor)]
    textsize = 70
    fontname = 'Source Code Pro Medium'
    if '-f' in sys.argv:
        fontname = sys.argv[sys.argv.index('-f') + 1]
    id = ca.create_text(220, 30, text='', fill=textcolor, font=(fontname, textsize))

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
