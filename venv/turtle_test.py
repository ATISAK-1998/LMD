from turtle import *
import turtle
import os
img = [['โรงเรียน',r"D:\Python for Project\GIF\โรงเรียน1.gif"],['สมุด',r"D:\Python for Project\GIF\สมุด.gif"]]
สมุด = r"D:\Python for Project\GIF\สมุด.gif"
sent_6 = [['ฉัน', 'สมุด', 'ตู้', 'ฉัน', 'a']] #
win = turtle.Screen()
win.setup(800,600)
t1 = turtle.Turtle()
t2 = turtle.Turtle()

จาน = r"D:\Python for Project\GIF\จาน.gif"
มีด = r"D:\Python for Project\GIF\มีด.gif"
ยาย = r"D:\Python for Project\GIF\ยาย.gif"
ตู้ = r"D:\Python for Project\GIF\ตู้.gif"
แจกัน = r"D:\Python for Project\GIF\แจกัน.gif"
แก้วน้ำ = r"D:\Python for Project\GIF\แก้วน้ำ.gif"
แว่นตา = r"D:\Python for Project\GIF\แว่นตา.gif"
แหวน = r"D:\Python for Project\GIF\แหวน.gif"
ลูกโป่ง = r"D:\Python for Project\GIF\ลูกโป่ง.gif"
ดินสอ = r"D:\Python for Project\GIF\ดินสอ.gif"
รองเท้า = r"D:\Python for Project\GIF\รองเท้า.gif"
ดอกไม้ = r"D:\Python for Project\GIF\ดอกไม้.gif"
ช้อน = r"D:\Python for Project\GIF\ช้อน.gif"
นาฬิกา = r"D:\Python for Project\GIF\นาฬิกา.gif"
หนังสือ = r"D:\Python for Project\GIF\หนังสือ.gif"
ปืน = r"D:\Python for Project\GIF\ปืน.gif"
ขวด = r"D:\Python for Project\GIF\ขวด.gif"
ตะหลิว = r"D:\Python for Project\GIF\ตะหลิว.gif"
กระทะ = r"D:\Python for Project\GIF\กระทะ.gif"
เข็ม = r"D:\Python for Project\GIF\เข็ม.gif"
หวี = r"D:\Python for Project\GIF\หวี.gif"
ตู้เย็น = r"D:\Python for Project\GIF\ตู้เย็น.gif"
เข็มขัด = r"D:\Python for Project\GIF\เข็มขัด.gif"
สมุด = r"D:\Python for Project\GIF\สมุด1.gif"
พัดลม = r"D:\Python for Project\GIF\พัดลม.gif"
ลูกบอล = r"D:\Python for Project\GIF\ลูกบอล.gif"
เตารีด = r"D:\Python for Project\GIF\เตารีด.gif"
ไม้กวาด = r"D:\Python for Project\GIF\ไม้กวาด.gif"
วิทยุ = r"D:\Python for Project\GIF\วิทยุ.gif"
กล่อง = r"D:\Python for Project\GIF\กล่อง.gif"
โต๊ะ = r"D:\Python for Project\GIF\โต๊ะ1.gif"
ส้อม = r"D:\Python for Project\GIF\ส้อม.gif"
โรงเรียน1 = r"D:\Python for Project\GIF\โรงเรียน1.gif"
ยางลบ = r"D:\Python for Project\GIF\ยางลบ.gif"
สีแดง = r"D:\Python for Project\GIF\สีแดง.gif"
สีเหลือง = r"D:\Python for Project\GIF\สีเหลือง.gif"
ฉัน = r"D:\Python for Project\GIF\ฉัน.gif"
ฉัน_3 = r"D:\Python for Project\GIF\ฉัน3.gif"
เธอ = r"D:\Python for Project\GIF\เธอ.gif"

if sent_6[0] == img[0][0]:
    t1.goto(-0,-0)
    win.addshape(img[0][1])
    t1.shape(img[0][1])
    if sent_6[1] == img[1][0]:
        t2.goto(-100, -100)
        win.addshape(img[1][1])
        t2.shape(img[1][1])


# Shuting the window down :
turtle.mainloop()
#
# screen = turtle.Screen()
# screen.setup(800, 650)
#
#
# i = r'E:\โครงงานจบ\GIF\ฉัน.gif'
# school=r'E:\โครงงานจบ\GIF\โรงเรียน.gif'
#
#
# if temp2[0] == ['ฉัน', 'ฉัน', 'p', 'โรงเรียน', 'a']:
#     if temp2[0][0] == 'ฉัน':
#         t2 = turtle.Turtle()
#         t2.color('White')
#         t2.backward(300)
#         t2.left(90)
#         t2.color('darkgray')
#         t2.backward(100)
#         screen.addshape(i)
#         t2.shape("D:\Python for Project\GIF\ฉัน.gif")
#     if temp2[0][3] == 'โรงเรียน':
#         t1 = turtle.Turtle()
#         t1.color('White')
#         t1.goto(100,60)
#         screen.addshape("D:\Python for Project\GIF\โรงเรียน.gif")
#         t1.shape("D:\Python for Project\GIF\โรงเรียน.gif")
# if temp2 ==[['จาน', 'จาน', 'โต๊ะ', 'โต๊ะ', 'a'], ['SAND'], ['บน', 'บน', 'โต๊ะ', 'จาน', 'v']]:
#     if temp2[2][2] == 'โต๊ะ':
#         t2 = turtle.Turtle()
#         t2.color('White')
#         t2.sety(-98)
#         screen.addshape("E:\โครงงานจบ\GIF\โต๊ะ1.gif")
#         t2.shape("E:\โครงงานจบ\GIF\โต๊ะ1.gif")
#     if temp2[1] == ['SAND']:
#         if temp2[2][0] == 'บน':
#             t1 = turtle.Turtle()
#             t1.color('White')
#             t1.sety(50)
#             if temp2[0][0] == 'จาน':
#                 screen.addshape("E:\โครงงานจบ\GIF\จาน3.gif")
#                 t1.shape("E:\โครงงานจบ\GIF\จาน3.gif")
# if temp2 == [['ลูกบอล', 'ลูกบอล', 'กล่อง', 'กล่อง', 'a'], ['SAND'], ['ใน', 'ใน', 'กล่อง', 'ลูกบอล', 'v']]:
#     if temp2[0][0] == 'ลูกบอล':
#         t2 = turtle.Turtle()
#         t2.penup()
#         screen.addshape("E:\โครงงานจบ\GIF\ลูกบอล.gif")
#         t2.shape("E:\โครงงานจบ\GIF\ลูกบอล.gif")
#         t2.sety(50)
#     if temp2[1] == ['SAND']:
#         if temp2[2][0] == 'ใน':
#             t1 = turtle.Turtle()
#             if temp2[2][2] == 'กล่อง':
#                 screen.addshape("E:\โครงงานจบ\GIF\กล่อง1.gif")
#                 t1.shape("E:\โครงงานจบ\GIF\กล่อง1.gif")
#
# turtle.mainloop()
#