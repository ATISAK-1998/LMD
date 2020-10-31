from tltk import nlp
import tltk
import codecs
import csv


def NLExpreesionToLMD(remain_phrase):
    import copy

    จาน = ['x', 'x', 'p', 'q', 'n']
    ถาด = ['x', 'x', 'p', 'q', 'n']
    มีด = ['x', 'x', 'p', 'q', 'n']
    สุนัข = ['x', 'x', 'p', 'q', 'n']
    ยาย = ['x', 'x', 'p', 'q', 'n']
    กา = ['x', 'x', 'p', 'q', 'n']
    ตู้ = ['x', 'x', 'p', 'q', 'n']
    แจกัน = ['x', 'x', 'p', 'q', 'n']
    แก้วน้ำ = ['x', 'x', 'p', 'q', 'n']
    แว่นตา = ['x', 'x', 'p', 'q', 'n']
    แหวน = ['x', 'x', 'p', 'q', 'n']
    ลูกโป่ง = ['x', 'x', 'p', 'q', 'n']
    ดินสอ = ['x', 'x', 'p', 'q', 'n']
    รองเท้า = ['x', 'x', 'p', 'q', 'n']
    ดอกไม้ = ['x', 'x', 'p', 'q', 'n']
    สมุด = ['x', 'x', 'p', 'q', 'n']
    ช้อน = ['x', 'x', 'p', 'q', 'n']
    ส้อม = ['x', 'x', 'p', 'q', 'n']
    นาฬิกา = ['x', 'x', 'p', 'q', 'n']
    หนังสือ = ['x', 'x', 'p', 'q', 'n']
    ปืน = ['x', 'x', 'p', 'q', 'n']
    ขวด = ['x', 'x', 'p', 'q', 'n']
    ตะหลิว = ['x', 'x', 'p', 'q', 'n']
    กระทะ = ['x', 'x', 'p', 'q', 'n']
    เข็ม = ['x', 'x', 'p', 'q', 'n']
    หวี = ['x', 'x', 'p', 'q', 'n']
    ตู้เย็น = ['x', 'x', 'p', 'q', 'n']
    เข็มขัด = ['x', 'x', 'p', 'q', 'n']
    ชาม = ['x', 'x', 'p', 'q', 'n']
    พัดลม = ['x', 'x', 'p', 'q', 'n']
    ลูกบอล = ['x', 'x', 'p', 'q', 'n']
    เตารีด = ['x', 'x', 'p', 'q', 'n']
    ไม้กวาด = ['x', 'x', 'p', 'q', 'n']
    วิทยุ = ['x', 'x', 'p', 'q', 'n']
    กล่อง = ['x', 'x', 'p', 'q', 'n']
    โต๊ะ = ['x', 'x', 'p', 'q', 'n']
    ส้อม = ['x', 'x', 'p', 'q', 'n']
    โรงเรียน = ['x', 'x', 'p', 'q', 'n']
    ยางลบ = ['x', 'x', 'p', 'q', 'n']
    พ่อ = ['x', 'x', 'p', 'q', 'n']
    แม่ = ['x', 'x', 'p', 'q', 'n']
    เรา = ['x', 'x', 'p', 'q', 'pn']
    ฉัน = ['x', 'x', 'p', 'q', 'pn']
    เธอ = ['x', 'x', 'p', 'q', 'pn']
    ไป = ['x', 'x', 'p', 'q', 'v']
    ทำ = ['x', 'x', 'p', 'q', 'v']
    หยิบ = ['x', 'x', 'p', 'q', 'v']
    วาง = ['x', 'x', 'p', 'q', 'v']
    อยู่ = ['x', 'x', 'p', 'q', 'adv']
    มา = ['x', 'x', 'p', 'q', 'v']
    กลิ้ง = ['x', 'x', 'p', 'q', 'v']
    จับ = ['x', 'x', 'p', 'q', 'v']
    ที่ = ['x', 'x', 'p', 'q', 'pp']
    ใน = ['x', 'x', 'p', 'q', 'pp']
    บน = ['x', 'x', 'p', 'q', 'pp']
    ใต้ = ['x', 'x', 'p', 'q', 'pp']


    All_cab = ['จาน', 'ถาด', 'มีด', 'สุนัข', 'ยาย', 'กา', 'ตู้', 'แจกัน', 'แก้วน้ำ', 'แว่นตา', 'แหวน', 'ลูกโป่ง','ดินสอ',
               'รองเท้า', 'ดอกไม้', 'สมุด', 'ช้อน', 'นาฬิกา', 'หนังสือ', 'ปืน', 'ขวด', 'ตะหลิว', 'กระทะ', 'เข้ม', 'หวี',
               'มีด', 'ตู้เย็น', 'เข็มขัด', 'ชาม', 'พัดลม', 'ลูกบอล', 'เตารีด', 'ไม้กวาด', 'วิทยุ', 'กล่อง', 'โต๊ะ','ส้อม',
               'ยางลบ', 'เรา', 'ฉัน', 'เธอ', 'พ่อ', 'แม่', 'ไป', 'ทำ', 'หยิบ', 'วาง', 'อยู่', 'มา', 'กลิ้ง', 'จับ', 'ที่',
               'ใน', 'บน', 'ใต้', 'โรงเรียน', 'ตลาด']



    temp = []; temp1 = []; temp2 = []
    for w in remain_phrase:
        for ww in w:
            if len(ww) == 1:
                for www in ww:
                    if not www[-1].isdigit():
                        i = remain_phrase.index(w)
                        if i not in temp:
                            temp.append(i)
                        for x in All_cab:
                            if www == x[0][:-1]:
                                temp.append(x)
                        temp1.append(temp)
                        temp = []
                    else:
                        i = remain_phrase.index(w)
                        if i not in temp:
                            temp.append(i)
                        for x in All_cab:
                            if www[:-1] == x[0][:-1]:
                                temp.append(x)
                        temp1.append(temp)
                        temp = []
            else:
                for www in ww:
                    if not www[-1].isdigit():
                        i = remain_phrase.index(w)
                        if i not in temp:
                            temp.append(i)
                        for x in All_cab:
                            if www == x[0][:-1]:
                                temp.append(x)
                        else:
                            i = remain_phrase.index(w)
                            if i not in temp:
                                temp.append(i)
                            for x in All_cab:
                                if www[:-1] == x[0][:-1]:
                                    temp.append(x)
                temp1.append(temp)
                temp = []
        temp2.append(temp1)
        temp1 = []
    #print(temp2)
    #===== End of changing NL expression to be logical term =====

        #===== Start to make the difference, in case of there are morn than 1 input sentence =====
    temp = []; temp1 = []
    for w in  temp2:
        i = temp2.index(w)
        for new_ww in w:
            #print(len(ww),ww)
            ww = copy.deepcopy(new_ww)          #.deepcopy is used to copy every objext in the variable.
            if (len(ww) == 2) and (ww[0] == i):
                if len(ww[1][2]) == 1:
                    if len(ww[1][2][0]) == 7:
                        ww[1][2][0].insert(7,i)
                    else:
                        if ww[1][2][0][7] != i:
                            ww[1][2][0].pop(7)
                            ww[1][2][0].insert(7,i)
                    #print(ww)
                    temp.append(ww)

                else:
                    for x in ww[1][2]:
                        if len(x) == 7:
                            x.insert(7,1)
                        else:
                            if x[7] != i:
                                x.pop(7)
                                x.insert(7,i)
                    #print(ww)
                    temp.append(ww)
            elif (len(ww) > 2) and (ww[0] == i):
                j = 1
                while j <= len(ww)-1:
                    for y in ww[j][2]:
                        if len(y) == 7:
                            y.insert(7,i)
                        else:
                            if y[7] != i:
                                y.pop(7)
                                y.insert(7,i)
                    j+=1
                #print(ww)
                temp.append(ww)
            temp1.append(temp)
            temp = []
        #print("\n===== After combination =====")
        #print(temp1)
        #===== End of making the difference =====

        for w in temp1:
            for ww in w:
                #print(ww)
                ww.pop(0)
        #print("\n===== After combination =====")
        #print("\n%s"%temp1)

        return temp1
        # ===== Finish to change natural expression to be logical terms =====
