import turtle
import tkinter as tk
from turtle import RawTurtle, TurtleScreen, ScrolledCanvas

class App_gui:
    def __init__(self,master):
        self.master = master
        self.Cavas = tk.Canvas(master)
        self.Cavas.config(width=800, height=600)
        self.Cavas.pack(side=tk.RIGHT)
        self.screen = turtle.TurtleScreen(self.Cavas)
        self.screen.bgcolor("cyan")

    def lmd_image(temp2):

        temp2.img = [['จาน', r"D:\Python for Project\GIF\จาน.gif"], ['มีด', r"D:\Python for Project\GIF\มีด.gif"],
               ['ตู้', r"D:\Python for Project\GIF\ตู้.gif"], ['แจกัน', r"D:\Python for Project\GIF\แจกัน.gif"],
               ['แก้วน้ำ', r"D:\Python for Project\GIF\แก้วน้ำ.gif"], ['แว่นตา', r"D:\Python for Project\GIF\แว่นตา.gif"],
               ['แหวน', r"D:\Python for Project\GIF\แหวน.gif"], ['ลูกโป่ง', r"D:\Python for Project\GIF\ลูกโป่ง.gif"],
               ['ดินสอ', r"D:\Python for Project\GIF\ดินสอ.gif"], ['รองเท้า', r"D:\Python for Project\GIF\รองเท้า.gif"],
               ['ดอกไม้', r"D:\Python for Project\GIF\ดอกไม้.gif"], ['ช้อน', r"D:\Python for Project\GIF\ช้อน.gif"],
               ['นาฬิกา', r"D:\Python for Project\GIF\นาฬิกา.gif"], ['หนังสือ', r"D:\Python for Project\GIF\หนังสือ.gif"],
               ['ปืน', r"D:\Python for Project\GIF\ปืน.gif"], ['ขวด', r"D:\Python for Project\GIF\ขวด.gif"],
               ['ตะหลิว', r"D:\Python for Project\GIF\ตะหลิว.gif"], ['กระทะ', r"D:\Python for Project\GIF\กระทะ.gif"],
               ['หวี', r"D:\Python for Project\GIF\หวี.gif"], ['ตู้เย็น', r"D:\Python for Project\GIF\ตู้เย็น.gif"],
               ['เข็มขัด', r"D:\Python for Project\GIF\เข็มขัด.gif"], ['สมุด', r"D:\Python for Project\GIF\สมุด.gif"],
               ['พัดลม', r"D:\Python for Project\GIF\พัดลม.gif"],  ['ลูกบอล', r"D:\Python for Project\GIF\ลูกบอล.gif"],
               ['เตารีด', r"D:\Python for Project\GIF\เตารีด.gif"], ['ไม้กวาด', r"D:\Python for Project\GIF\ไม้กวาด.gif"],
               ['วิทยุ', r"D:\Python for Project\GIF\วิทยุ.gif"], ['กล่อง', r"D:\Python for Project\GIF\กล่อง.gif"],
               ['โต๊ะ', r"D:\Python for Project\GIF\โต๊ะ.gif"], ['โรงเรียน', r"D:\Python for Project\GIF\โรงเรียน.gif"],
               ['ปากกา', r"D:\Python for Project\GIF\ปากกา.gif"], ['ฉัน', r"D:\Python for Project\GIF\ฉัน3.gif"]]

        screen = turtle.Screen()
        screen.setup(800, 600)
        t1 = turtle.Turtle()
        t2 = turtle.Turtle()
        t3 = turtle.Turtle()
        t1.color("white")
        t2.color("white")
        t3.color("white")
        t1.penup()
        t2.penup()
        t3.penup()

        lmd_img = temp2
        print("ประโยคเพื่อการอธิบายจินตภาพ : ",lmd_img)

        for c in range(len(lmd_img)):
            count_c = c
            for cc in range(len(lmd_img[0])):
                # print(img[cc])
                for p in range(len(img[0:50])):  # นับที่อยู่ของภาพ
                    # print(p)
                    if count_c == 0:
                        if lmd_img[0][cc] == lmd_img[0][1]:
                            if lmd_img[0][0] == img[p][0]:
                                t1.goto(-150, 0)
                                screen.addshape(img[p][1])
                                t1.shape(img[p][1])
                            elif (lmd_img[0][2] != lmd_img[0][3]) and lmd_img[0][2] == 'p': #ไปที่ใด
                                if lmd_img[0][3] == img[p][0]:
                                    t2.goto(200, 100)
                                    screen.addshape(img[p][1])
                                    t2.shape(img[p][1])
                        elif (lmd_img[0][cc] != lmd_img[0][1]) and (lmd_img[0][0] != lmd_img[0][1]): # หยิบ จับ ถือ
                            if lmd_img[0][1] == img[p][0]:
                                t2.goto(30, 80)
                                screen.addshape(img[p][1])
                                t2.shape(img[p][1])
                            elif lmd_img[0][2] != lmd_img[0][3]: #ถือที่ตำแหน่งใด
                                if lmd_img[0][2] == img[p][0]:
                                    t3.goto(100, -20)
                                    screen.addshape(img[p][1])
                                    t3.shape(img[p][1])
                        elif (lmd_img[0][cc] == lmd_img[0][3]) and (lmd_img[0][2] == lmd_img[0][3]):
                            if lmd_img[0][3] == img[p][0]:
                                t2.goto(30, 90)
                                screen.addshape(img[p][1])
                                t2.shape(img[p][1])
                    elif count_c == 2:
                        if (lmd_img[2][0] == 'บน') or (lmd_img[2][0] == 'ที่'):
                            if lmd_img[0][cc] == lmd_img[0][1]:
                                if lmd_img[0][0] == img[p][0]:
                                    t2.goto(20,30)
                                    screen.addshape(img[p][1])
                                    t2.shape(img[p][1])
                            elif lmd_img[0][cc] == lmd_img[0][3]:
                                if lmd_img[0][2] == img[p][0]:
                                    t1.goto(0, 0)
                                    screen.addshape(img[p][1])
                                    t1.shape(img[p][1])
                        elif lmd_img[2][0] == 'ใน':
                            if lmd_img[0][cc] == lmd_img[0][1]:
                                if lmd_img[0][0] == img[p][0]:
                                    t2.goto(0, 0)
                                    screen.addshape(img[p][1])
                                    t2.shape(img[p][1])
                            elif lmd_img[0][cc] == lmd_img[0][3]:
                                if lmd_img[0][2] == img[p][0]:
                                    t1.goto(0, 0)
                                    screen.addshape(img[p][1])
                                    t1.shape(img[p][1])
                        elif lmd_img[2][0] == 'ใต้':
                            if lmd_img[0][cc] == lmd_img[0][1]:
                                if lmd_img[0][0] == img[p][0]:
                                    t2.goto(0, -80)
                                    screen.addshape(img[p][1])
                                    t2.shape(img[p][1])
                            elif lmd_img[0][cc] == lmd_img[0][3]:
                                if lmd_img[0][2] == img[p][0]:
                                    t1.goto(0, 0)
                                    screen.addshape(img[p][1])
                                    t1.shape(img[p][1])
        turtle.mainloop()
if __name__ == '__main__':
    root = tk.Tk()
    app = App_gui(root)
    root.mainloop()


# def lmd_image(temp2):
#
#     img = [['จาน', r"D:\Python for Project\GIF\จาน.gif"], ['มีด', r"D:\Python for Project\GIF\มีด.gif"],
#            ['ตู้', r"D:\Python for Project\GIF\ตู้.gif"], ['แจกัน', r"D:\Python for Project\GIF\แจกัน.gif"],
#            ['แก้วน้ำ', r"D:\Python for Project\GIF\แก้วน้ำ.gif"], ['แว่นตา', r"D:\Python for Project\GIF\แว่นตา.gif"],
#            ['แหวน', r"D:\Python for Project\GIF\แหวน.gif"], ['ลูกโป่ง', r"D:\Python for Project\GIF\ลูกโป่ง.gif"],
#            ['ดินสอ', r"D:\Python for Project\GIF\ดินสอ.gif"], ['รองเท้า', r"D:\Python for Project\GIF\รองเท้า.gif"],
#            ['ดอกไม้', r"D:\Python for Project\GIF\ดอกไม้.gif"], ['ช้อน', r"D:\Python for Project\GIF\ช้อน.gif"],
#            ['นาฬิกา', r"D:\Python for Project\GIF\นาฬิกา.gif"], ['หนังสือ', r"D:\Python for Project\GIF\หนังสือ.gif"],
#            ['ปืน', r"D:\Python for Project\GIF\ปืน.gif"], ['ขวด', r"D:\Python for Project\GIF\ขวด.gif"],
#            ['ตะหลิว', r"D:\Python for Project\GIF\ตะหลิว.gif"], ['กระทะ', r"D:\Python for Project\GIF\กระทะ.gif"],
#            ['หวี', r"D:\Python for Project\GIF\หวี.gif"], ['ตู้เย็น', r"D:\Python for Project\GIF\ตู้เย็น.gif"],
#            ['เข็มขัด', r"D:\Python for Project\GIF\เข็มขัด.gif"], ['สมุด', r"D:\Python for Project\GIF\สมุด.gif"],
#            ['พัดลม', r"D:\Python for Project\GIF\พัดลม.gif"],  ['ลูกบอล', r"D:\Python for Project\GIF\ลูกบอล.gif"],
#            ['เตารีด', r"D:\Python for Project\GIF\เตารีด.gif"], ['ไม้กวาด', r"D:\Python for Project\GIF\ไม้กวาด.gif"],
#            ['วิทยุ', r"D:\Python for Project\GIF\วิทยุ.gif"], ['กล่อง', r"D:\Python for Project\GIF\กล่อง.gif"],
#            ['โต๊ะ', r"D:\Python for Project\GIF\โต๊ะ.gif"], ['โรงเรียน', r"D:\Python for Project\GIF\โรงเรียน.gif"],
#            ['ปากกา', r"D:\Python for Project\GIF\ปากกา.gif"], ['ฉัน', r"D:\Python for Project\GIF\ฉัน3.gif"]]
#
#     screen = turtle.Screen()
#     screen.setup(800, 600)
#     t1 = turtle.Turtle()
#     t2 = turtle.Turtle()
#     t3 = turtle.Turtle()
#     t1.color("white")
#     t2.color("white")
#     t3.color("white")
#     t1.penup()
#     t2.penup()
#     t3.penup()
#
#     lmd_img = temp2
#     print("ประโยคเพื่อการอธิบายจินตภาพ : ",lmd_img)
#
#     for c in range(len(lmd_img)):
#         count_c = c
#         for cc in range(len(lmd_img[0])):
#             # print(img[cc])
#             for p in range(len(img[0:50])):  # นับที่อยู่ของภาพ
#                 # print(p)
#                 if count_c == 0:
#                     if lmd_img[0][cc] == lmd_img[0][1]:
#                         if lmd_img[0][0] == img[p][0]:
#                             t1.goto(-150, 0)
#                             screen.addshape(img[p][1])
#                             t1.shape(img[p][1])
#                         elif (lmd_img[0][2] != lmd_img[0][3]) and lmd_img[0][2] == 'p': #ไปที่ใด
#                             if lmd_img[0][3] == img[p][0]:
#                                 t2.goto(200, 100)
#                                 screen.addshape(img[p][1])
#                                 t2.shape(img[p][1])
#                     elif (lmd_img[0][cc] != lmd_img[0][1]) and (lmd_img[0][0] != lmd_img[0][1]): # หยิบ จับ ถือ
#                         if lmd_img[0][1] == img[p][0]:
#                             t2.goto(30, 80)
#                             screen.addshape(img[p][1])
#                             t2.shape(img[p][1])
#                         elif lmd_img[0][2] != lmd_img[0][3]: #ถือที่ตำแหน่งใด
#                             if lmd_img[0][2] == img[p][0]:
#                                 t3.goto(100, -20)
#                                 screen.addshape(img[p][1])
#                                 t3.shape(img[p][1])
#                     elif (lmd_img[0][cc] == lmd_img[0][3]) and (lmd_img[0][2] == lmd_img[0][3]):
#                         if lmd_img[0][3] == img[p][0]:
#                             t2.goto(30, 90)
#                             screen.addshape(img[p][1])
#                             t2.shape(img[p][1])
#                 elif count_c == 2:
#                     if (lmd_img[2][0] == 'บน') or (lmd_img[2][0] == 'ที่'):
#                         if lmd_img[0][cc] == lmd_img[0][1]:
#                             if lmd_img[0][0] == img[p][0]:
#                                 t2.goto(20,30)
#                                 screen.addshape(img[p][1])
#                                 t2.shape(img[p][1])
#                         elif lmd_img[0][cc] == lmd_img[0][3]:
#                             if lmd_img[0][2] == img[p][0]:
#                                 t1.goto(0, 0)
#                                 screen.addshape(img[p][1])
#                                 t1.shape(img[p][1])
#                     elif lmd_img[2][0] == 'ใน':
#                         if lmd_img[0][cc] == lmd_img[0][1]:
#                             if lmd_img[0][0] == img[p][0]:
#                                 t2.goto(0, 0)
#                                 screen.addshape(img[p][1])
#                                 t2.shape(img[p][1])
#                         elif lmd_img[0][cc] == lmd_img[0][3]:
#                             if lmd_img[0][2] == img[p][0]:
#                                 t1.goto(0, 0)
#                                 screen.addshape(img[p][1])
#                                 t1.shape(img[p][1])
#                     elif lmd_img[2][0] == 'ใต้':
#                         if lmd_img[0][cc] == lmd_img[0][1]:
#                             if lmd_img[0][0] == img[p][0]:
#                                 t2.goto(0, -80)
#                                 screen.addshape(img[p][1])
#                                 t2.shape(img[p][1])
#                         elif lmd_img[0][cc] == lmd_img[0][3]:
#                             if lmd_img[0][2] == img[p][0]:
#                                 t1.goto(0, 0)
#                                 screen.addshape(img[p][1])
#                                 t1.shape(img[p][1])
#     turtle.mainloop()
