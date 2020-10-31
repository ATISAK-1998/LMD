from tkinter import *

import Lmd

App = Tk()
App.title('การพัฒนาต้นแบบความเข้าใจภาษาไทยโดยใช้ทฤษฎีการแปลความหมายโดยตรงจากจินตภาพ')
# root.config(bg='#80c1ff')
App.geometry('1360x768+400+50')
App.resizable(True, True)

img = PhotoImage(file='bg2.png')  # นำพื้นหลังเข้ามา
backgrounb = Label(App, image=img)  # กำหนดพื้นหลังให้อยู่ในหน้าต่างโปรแกรม
backgrounb.pack(side=TOP)
All_Vocab = PhotoImage(file='All_Cab_2.png')

def get_sentence(messegesinput):
    # ("This is the entry : ", messegesinput)
    #(messageshow['text']) = (tltk.nlp.word_segment(messegesinput))
    Lmd.start(messegesinput)
    # print(Lmd.To_Lmd_Expression())

def show_lmd():
    pass

# -----------------------------------------# รับประโยคนำเข้า
DataEntryFrame = Frame(App, bg='#99bbff', relief=GROOVE, borderwidth=5)
DataEntryFrame.place(x=10, y=65, width=550, height=700)
frontlabel = Label(DataEntryFrame, text='กรุณากรอกประโยค', width=30, font=('Angsana New', 24, 'italic bold'),
                   bg='#99bbff')
frontlabel.place(x=0, y=10)

Input_Sentence = Entry(DataEntryFrame, font=('Angsana New', 24, 'italic bold'), bg='white')
Input_Sentence.place(x=20, y=80, width=350, height=40)

# --------------------------------------------#button
enterbuttom = Button(DataEntryFrame, text='แปลประโยค', font=('Angsana New', 18, 'italic bold'), command=lambda: get_sentence(Input_Sentence.get()))
enterbuttom.place(x=400, y=80, width=100, height=40)

# ------------------------------------------# แสดงประโยค LMD
frontlabel = Label(DataEntryFrame, text='ประโยค LMD', width=20, font=('Angsana New', 24, 'italic bold'), bg='#99bbff')
frontlabel.place(x=140, y=120)
messageshow = Label(DataEntryFrame, text="", font=('Angsana New', 20, 'italic bold'), bg='white')
messageshow.place(x=10, y=180, width=520, height=100)

# -------------------------------------------# แสดงข้อความในระบบ
frontlabel = Label(DataEntryFrame, text='คำศัพท์ ในระบบ', width=20, font=('Angsana New', 24, 'italic bold'), bg='#99bbff')
frontlabel.place(x=140, y=280)
Label(DataEntryFrame, image=All_Vocab).place(x=10,y=340)

# -------------------------------------------# แสดงรูปภาพ
ShowDataFrame = Frame(App, bg='white', relief=GROOVE, borderwidth=5)
ShowDataFrame.place(x=570, y=65, width=780, height=700)

SS = 'ยินดีต้อนรับสู่ระบบต้นแบบความเข้าใจภาษาไทยโดยใช้ทฤษฎีการแปลความหมายโดยตรงจากจินตภาพ'
SliderLabel = Label(App, text=SS, font=('Angsana New ', 14), relief=RIDGE, borderwidth=4, width=90, bg='cyan')
SliderLabel.place(x=150, y=0)

App.mainloop()

