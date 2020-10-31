# import turtle
# import tkinter as tk
#
#
# class App:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("การพัฒนาต้นแบบความเข้าใจภาษาไทยโดยใช้ทฤษฎีการแปลความหมายโดยตรงจากจินตภาพ")
#         self.canvas = tk.Canvas(master)
#         self.canvas.config(width=1360, height=500)
#         self.canvas.pack(side=tk.LEFT)
#         self.screen = turtle.TurtleScreen(self.canvas)
#         self.screen.bgcolor("cyan")
#         self.button = tk.Button(self.master, text="Press me", command=self.press)
#         self.button.pack()
#         self.my_lovely_turtle = turtle.RawTurtle(self.screen, shape="turtle")
#         self.my_lovely_turtle.color("green")
#
#     def do_stuff(self):
#         for color in ["red", "yellow", "green"]:
#             self.my_lovely_turtle.color(color)
#             self.my_lovely_turtle.right(120)
#
#     def press(self):
#         self.do_stuff()
#
#
# if __name__ == '__main__':
#     root = tk.Tk()
#     app = App(root)
#     root.mainloop()


#
# import tkinter as tk
# from turtle import RawTurtle, TurtleScreen, ScrolledCanvas
#
# root = tk.Tk()
# root.geometry("400x200")
# root.title("Getting To Know You")
#
# def draw_circle(): #วาดวงกลมด้วยเต่า
#     turtle.color(color_entry.get()) #เรียกใช้เต่าให้วาดสีจากอินพุท
#     turtle.circle(60)
#
#
# # Favorite Color
#
# tk.Label(root, text="What's your favorite color?").pack() #ชื่อ
#
# color_entry = tk.Entry(root)
# color_entry.pack()
#
# tk.Button(root, text='Draw Circle', command=draw_circle).pack()
#
# canvas = ScrolledCanvas(root)
# canvas.pack(fill=tk.BOTH, expand=tk.YES)
#
# screen = TurtleScreen(canvas)
# turtle = RawTurtle(screen, visible=False)
#
# screen.mainloop()
#
# '''--------------------------------------'''


from tkinter import *
import turtle
import random

def play():
    for mv_a in a:
        mv_a.right(random.randint(0,100))
        mv_a.forward(40)

    scr.ontimer(play, 500)

def create_circle():
    num = int(in_num.get())

    for i in range(num):
        circle = turtle.RawTurtle(drw)
        circle.color("red")
        circle.shape("circle")
        circle.penup()
        circle.goto(x=random.randint(-200, 200), y=random.randint(-200, 200))

        a.append(circle)

# main window
win = Tk()
win.title("Turtle Canvas")

# circle list
a = []

# canvas
drw = Canvas(win, width=500, height=500)
drw.pack()

# label
la_txt = Label(win, text="ใส่ตัวเลขหนาบ่ะ 555  : ")
la_txt.pack(side=LEFT)

# text box
in_num = Entry(win)
in_num.pack(side=LEFT)

# button
btn_ok = Button(win, text="กดเลยบ่ะ", command=create_circle)
btn_ok.pack(side=LEFT)

# turtle
t = turtle.RawTurtle(drw)
t.shape("turtle")
t.color("blue")
t.speed(0)
t.penup()

scr = t.getscreen()
play()

win.mainloop()