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


'''def check_vocab(result):
    remain_phrase = []
    for j in range(len(result)):
        # print(result[j])
        for i in range(len(all_Vocab)):
            # print(i)
            if result[j] == all_Vocab[i]:
                remain_phrase.append()
    #remain_phrase = To_lmd(remain_phrase)
    print(remain_phrase)
    return remain_phrase'''

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
                    elif temp[w] == 'โต๊ะ':
                        for ww in range(len(โต๊ะ)):
                            if ww <= 1:
                                โต๊ะ.pop(ww)
                                โต๊ะ.insert(ww, temp[w])
                                #print(ฉัน)
                                #temp1.append(ฉัน)
                                #print('====================')
                        temp1.append(โต๊ะ)
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

                # ===== End of changing NL expression to be logical term =====
start()