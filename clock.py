from tkinter import *
import time, sys

tk = Tk()
tk.title('Clock')
ca = Canvas(tk, width=200, height=50)
ca.pack()
tk.update()

print(sys.argv)

def start():
    global del_id
    global id
    del_id = [ca.create_rectangle(0, 0, 500, 500, fill='white')]
    id = ca.create_text(100, 30, text='', font=('Source Code Pro Medium', 30))

def sk(i):
    sa = str(i)
    if len(sa) == 1:
        sa = '0' + sa
    return sa

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
