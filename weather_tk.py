#! /usr/bin/env python3
#-*- coding:utf-8 -*-
#__author__ == nobu
#__date__ == 2018/10/16
#__version__ == 1.0.0

# import
import tkinter as tk



# class
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")


root = tk.Tk()

def main():

    app = Application(master=root)
    app.mainloop()
    return 0


if __name__ == '__main__':
    main()