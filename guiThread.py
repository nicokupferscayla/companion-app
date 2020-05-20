#!/usr/bin/env python3
import threading
import sys
sys.path.append('.')
import tkinter as tk


class GuiThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        root = tk.Tk()
        canvas1 = tk.Canvas(root, width=300, height=300)
        label1 = tk.Label(root, text='Scayla Inline Edit', fg='#004e70', font=('helvetica', 25, 'bold'))
        canvas1.create_window(150, 100, window=label1)
        canvas1.pack()
        root.mainloop()
