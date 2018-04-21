#!/usr/bin/env python3
#coding: utf-8

class alerm_window():
    def __init__(self):
        with open('alerm\\list', 'r') as f:
            r = f.read()
        ra = r.split()
        rb = list()
        for a in range(0, len(ra)):
            if len(ra[a]) == 0:
                del ra[a]
        self.tk = Toplevel()
        self.tk.title('Set Alerm')
        self.lbl = list()
        for b in  range(0, len(rb)):
            self.lbl.append(Label(self.tk, text=('Alerm ' + str(b) + ' : ' + '')))
            self.lbl[b].pack()
        self.tk.update()
