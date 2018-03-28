from tkinter import *

tk = Tk()
c = Canvas(tk, width = 400, height = 300)
c.pack()

d = 150 - 20 # 直径
r = d / 2.0 # 半径
rr = r * r # 半径^2
cx = 20 # 円の左上X
cy = 20 # 円の左上Y
ax = cx + r # X=0の位置
ay = cy + r # Y=0の位置

color = "red"
c.create_oval(20, 20, 150, 150, fill = color)

def on_click(event):
    global color
    x = event.x
    y = event.y

    dx = x - ax # グラフ上の座標X
    dy = y - ay # グラフ上の座標Y

    if dx * dx + dy * dy > rr:
        return
    if color == "red":
        color = "blue"
    elif color == "blue":
        color = "green"
    elif color == "green":
        color = "red"
    c.create_oval(20, 20, 150, 150, fill = color)
c.bind("<Button-1>",on_click)

tk.mainloop()
