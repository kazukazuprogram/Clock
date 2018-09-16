#!/usr/bin/env python3
#coding: utf-8

#Clock 0.0.0
#Copyright 2017 Cabbage All Rights Reserved.
#python C:\Users\owner\code\Clock\clock.pyw

from tkinter import *
import time, sys, os, alerm.alerm #, lang.ImportList , lang.ja_JP, lang.en_US
from json import loads
from configparser import ConfigParser
from glob import glob
from os.path import dirname, splitext
#sys.setrecursionlimit(10000)

#Source Code Pro Medium : 450, 60/225,30
#7barSPBd               : 360, 80/180,50
#FuxedSys               : 320, 70/160, 35
#メニューバーで+20

#OSの種類によって文字コードを変える
if os.name == 'nt':
    enc = 'utf-8'
else:
    enc = 'cp932'

def read_language(fp, enc):
    global lang
    with open(fp, encoding=enc) as f:
        r = f.read()
    return loads(r)

def start_timer():
    global timer_time
    with open('timer/timer') as f:
        r = f.read()
    rz = ra.split('\n')
    ra = list()
    for x in range(len(rz)):
        if rz[x] == "":    break
        else:
            ra = r.split(' ')
            rba = ra[0].split('/')
            rbb = ra[1].split(':')
            rb = rba + rbb

def readargs():
    global textcolor
    global backgroundcolor
    global netcheck
    arg = sys.argv
    textcolor = 'black'
    if '-c' in arg:
        textcolor = arg[(arg.index('-c') + 1)]
    backgroundcolor = 'white'
    if '-b' in arg:
        backgroundcolor = arg[(arg.index('-b') + 1)]
    netcheck = False
    if '--fullscreen' in arg:
        tk.attributes('-fullscreen', True)

def sk(i):
    sa = str(i)
    if len(sa) == 1:
        sa = '0' + sa
    return sa

def fpma(fontname_a):
    if fontname_a == 'Source Code Pro Medium':
        ft = [225, 40]
    elif fontname_a =='7barSPBd':
        ft = [180, 50]
    elif fontname_a == 'FuxedSys':
        ft = [160, 35]
    return ft

def fpm():
    nx = fpma(fontname_mae)[0]
    ny = fpma(fontname_mae)[1]
    mx = fpma(fontname.get())[0]
    my = fpma(fontname.get())[1]
    if fontname.get() == '7barSPBd':
        ca.configure(width=mx * 2, height=my * 2 - 20)
    else:
        ca.configure(width=mx * 2, height=my * 2)
    ca.move(id, (mx - nx), (my - ny))
    tk.update()

def chfont():
    global fontname_mae
    print('Change font : ' + fontname_mae + ' >> ' + fontname.get())
    fpm()
    ca.itemconfig(id, font=(fontname.get(), textsize))
    fontname_mae = fontname.get()

def ChangeTopmostStatus():
    global TopmostStatusVariable
    if TopmostStatusVariable.get() == 1:
        tk.attributes('-topmost', True)
    else:
        tk.attributes('-topmost', False)

def restart():
    exit_program()
    main()

saveconf_ForMenu = lambda :saveconf('clock.conf', ['font', 'AlwaysOnTop'], [fontname.get(), str(TopmostStatusVariable.get())])

def ChangeLanguage():
    cm()

def cm():
    global tk
    global lang
    lang = read_language('lang/'+LANGNAME.get()+'.js', enc=enc)
    menubar = Menu(tk)
    FileMenu = Menu(menubar, tearoff=0)
    ViewMenu = Menu(menubar, tearoff=0)
    LangMenu = Menu(ViewMenu, tearoff=0)
    ToolMenu = Menu(menubar, tearoff=0)
    fontmenu = Menu(ToolMenu, tearoff=0)
    FontChangeMenu = Menu(fontmenu, tearoff=0)
    ChangeLangMenu = Menu(ToolMenu, tearoff=0)
    HelpMenu = Menu(menubar, tearoff=0)
    FileMenu.add_command(label=lang["Save Configuration"], command=saveconf_ForMenu)
    FileMenu.add_separator()
    FileMenu.add_command(label=lang["Restart"], command=restart)
    FileMenu.add_command(label=lang["Exit"], command=exit_program)
    menubar.add_cascade(label=lang["File"], menu=FileMenu) # focusについて調べる
    ViewMenu.add_checkbutton(label=lang["Always on top"], variable=TopmostStatusVariable, command=ChangeTopmostStatus)
    ViewMenu.add_cascade(label=lang["Language"], menu=LangMenu)
    for x in glob("./lang/*"):
        val = x[len(dirname(x))+1:len(x)-len(splitext(x))-1]
        LangMenu.add_radiobutton(label=val, variable=LANGNAME, value=val, command=ChangeLanguage)
    del val
    menubar.add_cascade(label=lang["View"], menu=ViewMenu)
    FontChangeMenu.add_radiobutton(label='Source Code Pro Medium', variable=fontname, value='Source Code Pro Medium', command=chfont)
    FontChangeMenu.add_radiobutton(label='7barSPBd', variable=fontname, value='7barSPBd', command=chfont)
    FontChangeMenu.add_radiobutton(label='FuxedSys', variable=fontname, value='FuxedSys', command=chfont)
    menubar.add_cascade(label=lang["Tool"], menu=ToolMenu)
    ToolMenu.add_cascade(label=lang["Font"], menu=fontmenu)
    fontmenu.add_cascade(label=lang["Change..."], menu=FontChangeMenu)
    HelpMenu.add_command(label=lang["About"], command=show_version, under=0)
    menubar.add_cascade(label=lang["Help"], menu=HelpMenu)
    tk.config(menu=menubar)

def exit_program():
    global tf
    tf = True
    tk.destroy()
    saveconf_ForMenu()

def getconf(path):
    cfp = ConfigParser()
    cfp.read(path)
    font = cfp['core']['Font']
    aot = cfp['core']['AlwaysOnTop']
    return font, aot, cfp['core']['Language']

def saveconf(path, name, value):
    cfp = ConfigParser()
    cfp.read(path)
    for x in range(len(name)):
        cfp['core'][name[x]] = value[x]
    with open(path, 'w') as fp:
        cfp.write(fp)

#About
def show_version():
    vtk = Toplevel()
    vtk.title('About')
    vca = Canvas(vtk, width=300, height=230, bg='white')
    vca.pack()
    i = PhotoImage(file='icon\\cabbage.png')
    vid = [vca.create_image(150, 80, image=i, anchor=NW),
    vca.create_text(150, 170, text='Cabbage Clock', font=('Helvetica', 30)),
    vca.create_text(150, 215, text=ver)]
    vtk.attributes('-topmost', True)
    vtk.resizable(0, 0) # 画面サイズ変更を禁止
    # raise
    vtk.update()

def start():
    global tk
    global ca
    global id
    global textcolor
    global backgroundcolor
    global printdebug
    global textsize
    global netcheck
    global fontname
    global fs
    global tf
    global fontname_mae
    global ver
    global TopmostStatusVariable
    global LANGNAME
    with open('help\\ver') as fv:
        ver = fv.read()
    with open('help\\en') as fen:
        help = fen.read()
    with open('help\\jp', 'br') as fjp:
        jhelpa = fjp.read()
        jhelp = jhelpa.decode('utf-8')
    print(ver)
    if '-h' in sys.argv or '--help' in sys.argv:
        print(help)
        exit()
    elif '-H' in sys.argv or '--japanese-help' in sys.argv:
        print(jhelp)
        exit()
    if '-v' in sys.argv:
        exit()
    readargs()
    # input('stringvar_m')
    gc = getconf('clock.conf')
    fontname_k = gc[0]
    aot = gc[1]
    #=============================================================================================
    #Start GUI
    tk = Tk()
    tk.title('Clock')
    ca = Canvas(tk, width=(fpma(fontname_k)[0] * 2), height=((fpma(fontname_k)[1] * 2) + 20), bg=backgroundcolor)
    ca.pack()
    tk.update()
    tk.resizable(0, 0) # 画面サイズ変更を禁止
    tk.iconbitmap(tk, 'icon\\cabbage.ico')
    tk.attributes('-topmost', True)    #最前面に表示
    # Fin Start GUI
    fontname = StringVar()
    fontname.set(fontname_k)
    TopmostStatusVariable = IntVar()
    TopmostStatusVariable.set(int(aot))
    ChangeTopmostStatus()
    tk.protocol("WM_DELETE_WINDOW", exit_program) # ウインドウを閉じたときにエラーになるのを回避
    LANGNAME = StringVar()
    LANGNAME.set(gc[2])
    #=============================================================================================
    fontname_mae = fontname.get()
    if '-f' in sys.argv:
        fontname.set(sys.argv[sys.argv.index('-f') + 1])
    textsize = 70
    if '-s' in sys.argv:
        textsize = int(sys.argv[sys.argv.index('-s') + 1])
    #del_id = [ca.create_rectangle(0, 0, 500, 500, fill=backgroundcolor)]
    id = ca.create_text(fpma(fontname.get())[0], fpma(fontname.get())[1], text='', fill=textcolor, font=(fontname.get(), textsize))
    fs = False
    cm()
    #時間調整
    s = time.localtime().tm_sec
    while True:
        if s != time.localtime().tm_sec:
            break
            del s
    tf = False
    ca.bind_all('<KeyPress-F11>', ev)
    ca.bind_all('<Escape>', ev)

def rv():
    global id
    t = time.localtime()
    tt = sk(str(t.tm_hour)) + ':' + sk(str(t.tm_min)) + ':' + sk(str(t.tm_sec))
    try:
        ca.itemconfig(id, text=tt)
    except:
        global tf
        exit_program

def ev(event):
    global fs
    if fs:
        #フルスクリーンをオフにする
        tk.attributes('-fullscreen', False)
        fs = False
    else:
        if event.keysym == 'F11':
            #フルスクリーンをオンにする
            tk.attributes('-fullscreen', True)
            fs = True

def main():
    start()
    #a = alerm_window()
    while True:
        rv()
        try:
            tk.update()
        except:
            exit_program()
        time.sleep(0.2)
        if tf:
            break

if __name__ != '__main__':
    print('This is run by ' + __name__)

main()
