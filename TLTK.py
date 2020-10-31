from tltk import nlp
import tltk
import codecs
import csv
def run(sen):
    test = sen  # ประโยคที่ใช้ทดสอบ
    test = tltk.nlp.word_segment(test)  # ตัดคำ
    test = test.replace("<s/>", "")  # เอา</s>ออกจากประโยค
    print("แบ่งประโยค : ", test)
    sen_list = sentolist(test)
    return sen_list
# ทำให้ประโยคจากการตัดคำกลายเป็นlist
def sentolist(test):
    stat = 0
    end = 0
    test_it = []
    for i in range(len(test)):
        if test[i] == "|":
            end = i
            test_it.append(test[stat:end])
            stat = i + 1
    test_it.append(test[stat:len(test)])
    result = test_it
    result.pop()
    print(type(result))
    print("แบ่งคำลงใน List : ", result)
    To_lmd(result)
    return result
def start():
    sen = input("text: ")
    run(sen)

def To_lmd(to_lmd):
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
               'ยางลบ', 'เรา', 'ฉัน', 'เธอ', 'พ่อ', 'แม่', 'ไป', 'ทำ', 'หยิบ', 'วาง', 'อยู่', 'มา', 'กลิ้ง', 'จับ',
               'ที่', 'ใน', 'บน', 'ใต้', 'โรงเรียน', 'ตลาด']
    temp = []; temp1 = []; temp2= []
    for l in range(len(to_lmd)):
        for ll in range(len(All_cab)):
            if to_lmd[l] == All_cab[ll]:
                print("Have : ", All_cab[ll])
                temp.append(All_cab[ll])
                #print(temp)
                for w in range(len(temp)):
                    #print(w)
                    if temp[w] == 'ฉัน':
                        for ww in range(len(ฉัน)):
                            #print(w)
                            if ww <= 1:
                                ฉัน.pop(ww)
                                ฉัน.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(ฉัน)
                    elif temp[w] == 'ไป':
                        for ww in range(len(ไป)):
                            if ww <= 1:
                                ไป.pop(ww)
                                ไป.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(ไป)
                    elif temp[w] == 'โรงเรียน':
                        for ww in range(len(โรงเรียน)):
                            if ww <= 1:
                                โรงเรียน.pop(ww)
                                โรงเรียน.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(โรงเรียน)
                    elif temp[w] == 'จาน':
                        for ww in range(len(จาน)):
                            if ww <= 1:
                                จาน.pop(ww)
                                จาน.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(จาน)
                    elif temp[w] == 'ถาด':
                        for ww in range(len(ถาด)):
                            if ww <= 1:
                                ถาด.pop(ww)
                                ถาด.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(ถาด)
                    elif temp[w] == 'มีด':
                        for ww in range(len(มีด)):
                            if ww <= 1:
                                มีด.pop(ww)
                                มีด.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(มีด)
                    elif temp[w] == 'สุนัข':
                        for ww in range(len(สุนัข)):
                            if ww <= 1:
                                สุนัข.pop(ww)
                                สุนัข.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(สุนัข)
                    elif temp[w] == 'ยาย':
                        for ww in range(len(ยาย)):
                            if ww <= 1:
                                ยาย.pop(ww)
                                ยาย.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(ยาย)
                    elif temp[w] == 'กา':
                        for ww in range(len(กา)):
                            if ww <= 1:
                                กา.pop(ww)
                                กา.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(กา)
                    elif temp[w] == 'ตู้':
                        for ww in range(len(ตู้)):
                            if ww <= 1:
                                ตู้.pop(ww)
                                ตู้.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(ตู้)
                    elif temp[w] == 'แจกัน':
                        for ww in range(len(แจกัน)):
                            if ww <= 1:
                                แจกัน.pop(ww)
                                แจกัน.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(แจกัน)
                    elif temp[w] == 'แก้วน้ำ':
                        for ww in range(len(แก้วน้ำ)):
                            if ww <= 1:
                                แก้วน้ำ.pop(ww)
                                แก้วน้ำ.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(แก้วน้ำ)
                    elif temp[w] == 'แว่นตา':
                        for ww in range(len(แว่นตา)):
                            if ww <= 1:
                                แว่นตา.pop(ww)
                                แว่นตา.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(แว่นตา)
                    elif temp[w] == 'แหวน':
                        for ww in range(len(แหวน)):
                            if ww <= 1:
                                แหวน.pop(ww)
                                แหวน.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(แหวน)
                    elif temp[w] == 'ลูกโป่ง':
                        for ww in range(len(ลูกโป่ง)):
                            if ww <= 1:
                                ลูกโป่ง.pop(ww)
                                ลูกโป่ง.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(ลูกโป่ง)
                    elif temp[w] == 'ดินสอ':
                        for ww in range(len(ดินสอ)):
                            if ww <= 1:
                                ดินสอ.pop(ww)
                                ดินสอ.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(ดินสอ)
                    elif temp[w] == 'รองเท้า':
                        for ww in range(len(รองเท้า)):
                            if ww <= 1:
                                รองเท้า.pop(ww)
                                รองเท้า.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(รองเท้า)
                    elif temp[w] == 'ดอกไม้':
                        for ww in range(len(ดอกไม้)):
                            if ww <= 1:
                                ดอกไม้.pop(ww)
                                ดอกไม้.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(ดอกไม้)
                    elif temp[w] == 'สมุด':
                        for ww in range(len(สมุด)):
                            if ww <= 1:
                                สมุด.pop(ww)
                                สมุด.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(สมุด)
                    elif temp[w] == 'ช้อน':
                        for ww in range(len(ช้อน)):
                            if ww <= 1:
                                ช้อน.pop(ww)
                                ช้อน.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(ช้อน)
                    elif temp[w] == 'ส้อม':
                        for ww in range(len(ส้อม)):
                            if ww <= 1:
                                ส้อม.pop(ww)
                                ส้อม.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(ส้อม)
                    elif temp[w] == 'นาฬิกา':
                        for ww in range(len(นาฬิกา)):
                            if ww <= 1:
                                นาฬิกา.pop(ww)
                                นาฬิกา.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(นาฬิกา)
                    elif temp[w] == 'หนังสือ':
                        for ww in range(len(หนังสือ)):
                            if ww <= 1:
                                หนังสือ.pop(ww)
                                หนังสือ.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(หนังสือ)
                    elif temp[w] == 'ปืน':
                        for ww in range(len(ปืน)):
                            if ww <= 1:
                                ปืน.pop(ww)
                                ปืน.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(ปืน)
                    elif temp[w] == 'ขวด':
                        for ww in range(len(ขวด)):
                            if ww <= 1:
                                ขวด.pop(ww)
                                ขวด.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(ขวด)
                    elif temp[w] == 'ตะหลิว':
                        for ww in range(len(ตะหลิว)):
                            if ww <= 1:
                                ตะหลิว.pop(ww)
                                ตะหลิว.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(ตะหลิว)
                    elif temp[w] == 'กระทะ':
                        for ww in range(len(กระทะ)):
                            if ww <= 1:
                                กระทะ.pop(ww)
                                กระทะ.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(กระทะ)
                    elif temp[w] == 'เข็ม':
                        for ww in range(len(เข็ม)):
                            if ww <= 1:
                                เข็ม.pop(ww)
                                เข็ม.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(เข็ม)
                    elif temp[w] == 'หวี':
                        for ww in range(len(หวี)):
                            if ww <= 1:
                                หวี.pop(ww)
                                หวี.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(หวี)
                    elif temp[w] == 'ตู้เย็น':
                        for ww in range(len(ตู้เย็น)):
                            if ww <= 1:
                                ตู้เย็น.pop(ww)
                                ตู้เย็น.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(ตู้เย็น)
                    elif temp[w] == 'เข็มขัด':
                        for ww in range(len(เข็มขัด)):
                            if ww <= 1:
                                เข็มขัด.pop(ww)
                                เข็มขัด.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(เข็มขัด)
                    elif temp[w] == 'ชาม':
                        for ww in range(len(ชาม)):
                            if ww <= 1:
                                ชาม.pop(ww)
                                ชาม.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(ชาม)
                    elif temp[w] == 'พัดลม':
                        for ww in range(len(พัดลม)):
                            if ww <= 1:
                                พัดลม.pop(ww)
                                พัดลม.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(พัดลม)
                    elif temp[w] == 'ลูกบอล':
                        for ww in range(len(ลูกบอล)):
                            if ww <= 1:
                                ลูกบอล.pop(ww)
                                ลูกบอล.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(ลูกบอล)
                    elif temp[w] == 'เตารีด':
                        for ww in range(len(เตารีด)):
                            if ww <= 1:
                                เตารีด.pop(ww)
                                เตารีด.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(เตารีด)
                    elif temp[w] == 'ไม้กวาด':
                        for ww in range(len(ไม้กวาด)):
                            if ww <= 1:
                                ไม้กวาด.pop(ww)
                                ไม้กวาด.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(ไม้กวาด)
                    elif temp[w] == 'วิทยุ':
                        for ww in range(len(วิทยุ)):
                            if ww <= 1:
                                วิทยุ.pop(ww)
                                วิทยุ.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(วิทยุ)
                    elif temp[w] == 'กล่อง':
                        for ww in range(len(กล่อง)):
                            if ww <= 1:
                                กล่อง.pop(ww)
                                กล่อง.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(กล่อง)
                    elif temp[w] == 'โต๊ะ':
                        for ww in range(len(โต๊ะ)):
                            if ww <= 1:
                                โต๊ะ.pop(ww)
                                โต๊ะ.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(โต๊ะ)
                    elif temp[w] == 'ยางลบ':
                        for ww in range(len(ยางลบ)):
                            if ww <= 1:
                                ยางลบ.pop(ww)
                                ยางลบ.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(ยางลบ)
                    elif temp[w] == 'เรา':
                        for ww in range(len(เรา)):
                            if ww <= 1:
                                เรา.pop(ww)
                                เรา.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(เรา)
                    elif temp[w] == 'เธอ':
                        for ww in range(len(เธอ)):
                            if ww <= 1:
                                เธอ.pop(ww)
                                เธอ.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(เธอ)
                    elif temp[w] == 'พ่อ':
                        for ww in range(len(พ่อ)):
                            if ww <= 1:
                                พ่อ.pop(ww)
                                พ่อ.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(พ่อ)
                    elif temp[w] == 'แม่':
                        for ww in range(len(แม่)):
                            if ww <= 1:
                                แม่.pop(ww)
                                แม่.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(แม่)
                    elif temp[w] == 'ทำ':
                        for ww in range(len(ทำ)):
                            if ww <= 1:
                                ทำ.pop(ww)
                                ทำ.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(ทำ)
                    elif temp[w] == 'หยิบ':
                        for ww in range(len(หยิบ)):
                            if ww <= 1:
                                หยิบ.pop(ww)
                                หยิบ.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(หยิบ)
                    elif temp[w] == 'วาง':
                        for ww in range(len(วาง)):
                            if ww <= 1:
                                วาง.pop(ww)
                                วาง.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(วาง)
                    elif temp[w] == 'อยู่':
                        for ww in range(len(อยู่)):
                            if ww <= 1:
                                อยู่.pop(ww)
                                อยู่.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(อยู่)
                    elif temp[w] == 'มา':
                        for ww in range(len(มา)):
                            if ww <= 1:
                                มา.pop(ww)
                                มา.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(มา)
                    elif temp[w] == 'กลิ้ง':
                        for ww in range(len(กลิ้ง)):
                            if ww <= 1:
                                กลิ้ง.pop(ww)
                                กลิ้ง.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(กลิ้ง)
                    elif temp[w] == 'จับ':
                        for ww in range(len(จับ)):
                            if ww <= 1:
                                จับ.pop(ww)
                                จับ.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(จับ)
                    elif temp[w] == 'ที่':
                        for ww in range(len(ที่)):
                            if ww <= 1:
                                ที่.pop(ww)
                                ที่.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(ที่)
                    elif temp[w] == 'ใน':
                        for ww in range(len(ใน)):
                            if ww <= 1:
                                ใน.pop(ww)
                                ใน.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(ใน)
                    elif temp[w] == 'บน':
                        for ww in range(len(บน)):
                            if ww <= 1:
                                บน.pop(ww)
                                บน.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(บน)
                    elif temp[w] == 'ใต้':
                        for ww in range(len(ใต้)):
                            if ww <= 1:
                                ใต้.pop(ww)
                                ใต้.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(ใต้)



    print(temp1)
    print(temp1[6:10])
                # ===== End of changing NL expression to be logical term =====
start()