from tltk import nlp
import tltk
import codecs
import csv
# import APP

จาน = ['x', 'x', 'p', 'q', 'n']
มีด = ['x', 'x', 'p', 'q', 'n']
ยาย = ['x', 'x', 'p', 'q', 'n']
ตู้ = ['x', 'x', 'p', 'q', 'n']
แจกัน = ['x', 'x', 'p', 'q', 'n']
แก้วน้ำ = ['x', 'x', 'p', 'q', 'n']
แว่นตา = ['x', 'x', 'p', 'q', 'n']
แหวน = ['x', 'x', 'p', 'q', 'n']
ลูกโป่ง = ['x', 'x', 'p', 'q', 'n']
ดินสอ = ['x', 'x', 'p', 'q', 'n']
รองเท้า = ['x', 'x', 'p', 'q', 'n']
ดอกไม้ = ['x', 'x', 'p', 'q', 'n']
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
สมุด = ['x', 'x', 'p', 'q', 'n']
พัดลม = ['x', 'x', 'p', 'q', 'n']
ลูกบอล = ['x', 'x', 'p', 'q', 'n']
เตารีด = ['x', 'x', 'p', 'q', 'n']
ไม้กวาด = ['x', 'x', 'p', 'q', 'n']
วิทยุ = ['x', 'x', 'p', 'q', 'n']
กล่อง = ['x', 'x', 'p', 'q', 'n']
โต๊ะ = ['x', 'x', 'p', 'q', 'n']
ส้อม = ['x', 'x', 'p', 'q', 'n']
โรงเรียน = ['x', 'x', 'p', 'q', 'n']
ปากกา = ['x', 'x', 'p', 'q', 'n']
สีแดง = ['x', 'x', 'p', 'q', 'n']
สีเหลือง = ['x', 'x', 'p', 'q', 'n']
เรา = ['x', 'x', 'p', 'q', 'pn']
ฉัน = ['x', 'x', 'p', 'q', 'pn']
เธอ = ['x', 'x', 'p', 'q', 'pn']
ไป = ['x', 'x', 'p', 'q', 'v']
ถือ = ['x', 'y', 'z', 'x', 'v']
วาง = ['x', 'y', 'x', 'x', 'v']
อยู่ = ['x', 'y', 'x', 'x', 'adv']
มา = ['x', 'x', 'q', 'p', 'v']
จับ = ['x', 'y', 'z', 'x', 'v']
หยิบ = ['x', 'y', 'z', 'x', 'v']
ที่ = ['x', 'x', 'y', 'x', 'pp']
ใน = ['x', 'x', 'y', 'x', 'pp']
บน = ['x', 'x', 'y', 'x', 'pp']
ใต้ = ['x', 'x', 'x', 'y', 'pp']
สีเขียว = ['x', 'x', 'p', 'q', 'n']
สีชมพู = ['x', 'x', 'p', 'q', 'n']
สีฟ้า = ['x', 'x', 'p', 'q', 'n']

All_cab = ['จาน', 'มีด', 'ยาย', 'ตู้', 'แจกัน', 'แก้วน้ำ', 'แว่นตา', 'แหวน', 'ลูกโป่ง', 'ดินสอ', 'รองเท้า', 'ดอกไม้',
           'ช้อน', 'นาฬิกา', 'หนังสือ', 'ปืน', 'ขวด', 'ตะหลิว', 'กระทะ', 'เข็ม', 'หวี', 'ตู้เย็น', 'เข็มขัด', 'สมุด',
           'พัดลม', 'ลูกบอล', 'เตารีด', 'ไม้กวาด', 'วิทยุ', 'กล่อง', 'โต๊ะ', 'ส้อม', 'ปากกา', 'เรา', 'ฉัน', 'เธอ',
           'ไป', 'วาง', 'อยู่', 'มา', 'จับ', 'ถือ', 'ที่', 'ใน', 'บน', 'ใต้', 'โรงเรียน', 'สีแดง', 'สีเหลือง',
           'สีเขียว', 'สีชมพู', 'สีฟ้า', 'หยิบ']


def run(sen):
    test = sen  # ประโยคที่ใช้ทดสอบ
    test = tltk.nlp.word_segment(test)  # ตัดคำ
    test = test.replace("<s/>", "")  # เอา</s>ออกจากประโยค
    print("แบ่งประโยค : ", test)
    return sentolist(test)


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
    for count in range(len(result)):
        c = count
        if c < 2:
            if result[1] == 'ที่อยู่':
                del result[1]
            elif result[1] == 'ใต้โต๊ะ':
                result.pop()
                result.append('ใต้')
                result.append('โต๊ะ')
        elif c < 3:
            if result[2] == 'ที่อยู่':
                del result[2]
            elif result[2] == 'ใต้โต๊ะ':
                result.pop()
                result.append('ใต้')
                result.append('โต๊ะ')
                # print(result)
        elif c < 4:
            if result[3] == 'ที่อยู่':
                del result[3]
            elif result[3] == 'ใต้โต๊ะ':
                result.pop()
                result.append('ใต้')
                result.append('โต๊ะ')
                # print(result)
    print(type(result))
    print("แบ่งคำลงใน List : ", result)
    return check_Vocab(result)


def check_Vocab(result):
    word = []
    sentence = []
    for i in range(len(result)):
        for ii in range(len(All_cab)):
            if result[i] == All_cab[ii]:
                word.append(All_cab[ii])
    for c in range(len(result)):
        count_c = c
    for cc in range(len(word)):
        count_cc = cc
    if c == cc:
        print("คำที่มีในระบบ : ", word)
        sentence.append(word)
        return To_Lmd_Expression(sentence)
    elif c != cc:
        print("บางคำไม่ได้อยู่ในระบบ")
        return start()

    return None


def To_Lmd_Expression(sentence):
    temp = [];
    temp1 = [];
    temp2 = []
    # print(sentence)
    #### ตัดคำที่ไม่จำเป็นออกจากประโยค ####
    for q in range(len(sentence[0])):
        count_q = q
        # print(count_q)
    if count_q == 4:
        if sentence[0][1] == 'วาง' and sentence[0][2] == 'อยู่':
            del sentence[0][1:3]
            print("ตัดคำ : ", sentence)
    elif count_q == 3:
        # if (sentence[0][1] == 'หยิบ' or 'จับ' or 'ถือ') and (sentence[0][2] == 'ใน' or 'ที่' or 'บน' or 'ใต้'):
        #         print("ตัดคำ : ", sentence)
        if (sentence[0][1] == 'วาง' or 'อยู่') and (sentence[0][2] == 'ใน' or 'ที่' or 'บน' or 'ใต้'):
            del sentence[0][1]
            print("ตัดคำ : ", sentence)
    print("ตัดคำ : ", sentence)

    ########## เข้ารูปภาษาเพื่อการอธิบายจินตภาพ #############
    for l in range(len(sentence)):
        temp = sentence[l]
        for w in range(len(temp)):
            if temp[w] == 'ฉัน':
                for ww in range(len(ฉัน)):
                    # print(w)
                    if ww <= 1:
                        ฉัน.pop(ww)
                        ฉัน.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(ฉัน)
            elif temp[w] == 'ไป':
                for ww in range(len(ไป)):
                    if ww <= 1:
                        ไป.pop(ww)
                        ไป.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(ไป)
            elif temp[w] == 'โรงเรียน':
                for ww in range(len(โรงเรียน)):
                    if ww <= 1:
                        โรงเรียน.pop(ww)
                        โรงเรียน.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(โรงเรียน)
            elif temp[w] == 'จาน':
                for ww in range(len(จาน)):
                    if ww <= 1:
                        จาน.pop(ww)
                        จาน.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(จาน)
            elif temp[w] == 'มีด':
                for ww in range(len(มีด)):
                    if ww <= 1:
                        มีด.pop(ww)
                        มีด.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(มีด)
            elif temp[w] == 'ยาย':
                for ww in range(len(ยาย)):
                    if ww <= 1:
                        ยาย.pop(ww)
                        ยาย.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(ยาย)
            elif temp[w] == 'ตู้':
                for ww in range(len(ตู้)):
                    if ww <= 1:
                        ตู้.pop(ww)
                        ตู้.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(ตู้)
            elif temp[w] == 'แจกัน':
                for ww in range(len(แจกัน)):
                    if ww <= 1:
                        แจกัน.pop(ww)
                        แจกัน.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(แจกัน)
            elif temp[w] == 'แก้วน้ำ':
                for ww in range(len(แก้วน้ำ)):
                    if ww <= 1:
                        แก้วน้ำ.pop(ww)
                        แก้วน้ำ.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(แก้วน้ำ)
            elif temp[w] == 'แว่นตา':
                for ww in range(len(แว่นตา)):
                    if ww <= 1:
                        แว่นตา.pop(ww)
                        แว่นตา.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(แว่นตา)
            elif temp[w] == 'แหวน':
                for ww in range(len(แหวน)):
                    if ww <= 1:
                        แหวน.pop(ww)
                        แหวน.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(แหวน)
            elif temp[w] == 'ลูกโป่ง':
                for ww in range(len(ลูกโป่ง)):
                    if ww <= 1:
                        ลูกโป่ง.pop(ww)
                        ลูกโป่ง.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(ลูกโป่ง)
            elif temp[w] == 'ดินสอ':
                for ww in range(len(ดินสอ)):
                    if ww <= 1:
                        ดินสอ.pop(ww)
                        ดินสอ.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(ดินสอ)
            elif temp[w] == 'รองเท้า':
                for ww in range(len(รองเท้า)):
                    if ww <= 1:
                        รองเท้า.pop(ww)
                        รองเท้า.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(รองเท้า)
            elif temp[w] == 'ดอกไม้':
                for ww in range(len(ดอกไม้)):
                    if ww <= 1:
                        ดอกไม้.pop(ww)
                        ดอกไม้.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(ดอกไม้)
            elif temp[w] == 'ช้อน':
                for ww in range(len(ช้อน)):
                    if ww <= 1:
                        ช้อน.pop(ww)
                        ช้อน.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(ช้อน)
            elif temp[w] == 'ส้อม':
                for ww in range(len(ส้อม)):
                    if ww <= 1:
                        ส้อม.pop(ww)
                        ส้อม.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(ส้อม)
            elif temp[w] == 'นาฬิกา':
                for ww in range(len(นาฬิกา)):
                    if ww <= 1:
                        นาฬิกา.pop(ww)
                        นาฬิกา.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(นาฬิกา)
            elif temp[w] == 'หนังสือ':
                for ww in range(len(หนังสือ)):
                    if ww <= 1:
                        หนังสือ.pop(ww)
                        หนังสือ.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(หนังสือ)
            elif temp[w] == 'ปืน':
                for ww in range(len(ปืน)):
                    if ww <= 1:
                        ปืน.pop(ww)
                        ปืน.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(ปืน)
            elif temp[w] == 'ขวด':
                for ww in range(len(ขวด)):
                    if ww <= 1:
                        ขวด.pop(ww)
                        ขวด.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(ขวด)
            elif temp[w] == 'ตะหลิว':
                for ww in range(len(ตะหลิว)):
                    if ww <= 1:
                        ตะหลิว.pop(ww)
                        ตะหลิว.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(ตะหลิว)
            elif temp[w] == 'กระทะ':
                for ww in range(len(กระทะ)):
                    if ww <= 1:
                        กระทะ.pop(ww)
                        กระทะ.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(กระทะ)
            elif temp[w] == 'เข็ม':
                for ww in range(len(เข็ม)):
                    if ww <= 1:
                        เข็ม.pop(ww)
                        เข็ม.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(เข็ม)
            elif temp[w] == 'หวี':
                for ww in range(len(หวี)):
                    if ww <= 1:
                        หวี.pop(ww)
                        หวี.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(หวี)
            elif temp[w] == 'ตู้เย็น':
                for ww in range(len(ตู้เย็น)):
                    if ww <= 1:
                        ตู้เย็น.pop(ww)
                        ตู้เย็น.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(ตู้เย็น)
            elif temp[w] == 'เข็มขัด':
                for ww in range(len(เข็มขัด)):
                    if ww <= 1:
                        เข็มขัด.pop(ww)
                        เข็มขัด.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(เข็มขัด)
            elif temp[w] == 'สมุด':
                for ww in range(len(สมุด)):
                    if ww <= 1:
                        สมุด.pop(ww)
                        สมุด.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(สมุด)
            elif temp[w] == 'พัดลม':
                for ww in range(len(พัดลม)):
                    if ww <= 1:
                        พัดลม.pop(ww)
                        พัดลม.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(พัดลม)
            elif temp[w] == 'ลูกบอล':
                for ww in range(len(ลูกบอล)):
                    if ww <= 1:
                        ลูกบอล.pop(ww)
                        ลูกบอล.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(ลูกบอล)
            elif temp[w] == 'เตารีด':
                for ww in range(len(เตารีด)):
                    if ww <= 1:
                        เตารีด.pop(ww)
                        เตารีด.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(เตารีด)
            elif temp[w] == 'ไม้กวาด':
                for ww in range(len(ไม้กวาด)):
                    if ww <= 1:
                        ไม้กวาด.pop(ww)
                        ไม้กวาด.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(ไม้กวาด)
            elif temp[w] == 'วิทยุ':
                for ww in range(len(วิทยุ)):
                    if ww <= 1:
                        วิทยุ.pop(ww)
                        วิทยุ.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(วิทยุ)
            elif temp[w] == 'กล่อง':
                for ww in range(len(กล่อง)):
                    if ww <= 1:
                        กล่อง.pop(ww)
                        กล่อง.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(กล่อง)
            elif temp[w] == 'โต๊ะ':
                for ww in range(len(โต๊ะ)):
                    if ww <= 1:
                        โต๊ะ.pop(ww)
                        โต๊ะ.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(โต๊ะ)
            elif temp[w] == 'ปากกา':
                for ww in range(len(ปากกา)):
                    if ww <= 1:
                        ปากกา.pop(ww)
                        ปากกา.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(ปากกา)
            elif temp[w] == 'เรา':
                for ww in range(len(เรา)):
                    if ww <= 1:
                        เรา.pop(ww)
                        เรา.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(เรา)
            elif temp[w] == 'เธอ':
                for ww in range(len(เธอ)):
                    if ww <= 1:
                        เธอ.pop(ww)
                        เธอ.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(เธอ)
            elif temp[w] == 'ถือ':
                for ww in range(len(ถือ)):
                    if ww <= 1:
                        ถือ.pop(ww)
                        ถือ.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(ถือ)
            elif temp[w] == 'วาง':
                for ww in range(len(วาง)):
                    if ww <= 1:
                        วาง.pop(ww)
                        วาง.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(วาง)
            elif temp[w] == 'อยู่':
                for ww in range(len(อยู่)):
                    if ww <= 1:
                        อยู่.pop(ww)
                        อยู่.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(อยู่)
            elif temp[w] == 'มา':
                for ww in range(len(มา)):
                    if ww <= 1:
                        มา.pop(ww)
                        มา.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(มา)
            elif temp[w] == 'จับ':
                for ww in range(len(จับ)):
                    if ww <= 1:
                        จับ.pop(ww)
                        จับ.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(จับ)
            elif temp[w] == 'ที่':
                for ww in range(len(ที่)):
                    if ww <= 1:
                        ที่.pop(ww)
                        ที่.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(ที่)
            elif temp[w] == 'ใน':
                for ww in range(len(ใน)):
                    if ww <= 1:
                        ใน.pop(ww)
                        ใน.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(ใน)
            elif temp[w] == 'บน':
                for ww in range(len(บน)):
                    if ww <= 1:
                        บน.pop(ww)
                        บน.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(บน)
            elif temp[w] == 'ใต้':
                for ww in range(len(ใต้)):
                    if ww <= 1:
                        ใต้.pop(ww)
                        ใต้.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(ใต้)
            elif temp[w] == 'หยิบ':
                for ww in range(len(หยิบ)):
                    if ww <= 1:
                        หยิบ.pop(ww)
                        หยิบ.insert(ww, temp[w])
                        # print(ฉัน)
                        # temp1.append(ฉัน)
                        # print('====================')
                temp1.append(หยิบ)

    print("LMD  : ", temp1)
    j = 0;
    temp3 = []

    ######## ลดรูปภาษาเพื่อการอธิบายจินตภาพ ##########
    for j in range(len(temp1)):
        # temp2.append(temp1[j])
        count_j = j
        # print(j)
    if count_j == 2:
        if temp1[1][4] == 'v' and temp1[2][4] == 'n':  # VERB(กริยา) + NOUN(นาม)
            if temp1[1][4] == 'v' and temp1[1][0] == 'ไป':
                temp2 = [['x', 'x', 'p', temp1[2][0], 'v']]
                temp3.append(temp1[0])
                temp3 += temp2
                temp2.clear()
                if temp3[0][4] == 'pn' and temp3[1][4] == 'v':
                    print("LMD : ", temp3)
                    temp2 = [[temp3[0][1], temp3[0][1], 'p', temp1[2][0], 'a']]
            elif temp1[1][4] == 'v' and temp1[1][0] == 'มา':
                temp2 = [['x', 'x', temp1[2][0], 'q', 'v']]
                temp3.append(temp1[0])
                temp3 += temp2
                temp2.clear()
                if temp3[0][4] == 'pn' and temp3[1][4] == 'v':
                    print("LMD : ", temp3)
                    temp2 = [[temp3[0][1], temp3[0][1], temp1[2][0], 'q', 'a']]
            elif temp1[1][4] == 'v' and (temp1[1][0] == 'ถือ' or 'หยิบ' or 'จับ'):
                temp2 = [['x', temp1[2][0], 'y', 'x', 'v']]
                temp3.append(temp1[0])
                temp3 += temp2
                temp2.clear()
                if temp3[0][4] == 'pn' and temp3[1][4] == 'v':
                    print("LMD : ", temp3)
                    temp2 = [[temp3[0][0], temp3[1][1], temp1[0][0], temp1[0][0], 'a']]
        elif temp1[1][4] == 'pp' and temp1[2][4] == 'n':
            if temp1[1][4] == 'pp' and ((temp1[1][0] == 'ใน' or 'ที่' or 'บน') and temp1[1][0] != 'ใต้'):
                temp2 = [[temp1[1][0], temp1[1][0], temp1[2][0], temp1[0][0], 'v']]
                temp3 = [temp1[0]] + temp2
                temp2.clear()
                print('temp3 :', temp3)
                if temp3[0][4] == 'n' and temp3[1][4] == 'v':
                    temp2 = [[temp3[0][0], temp3[0][0], temp3[1][2], temp3[1][2], 'a'], ['SAND'], temp3[1]]
                elif temp3[0][4] == 'pn' and temp3[1][4] == 'v':
                    temp2 = [[temp3[0][0], temp3[0][0], temp3[1][2], temp3[1][2], 'a'], ['SAND'], temp3[1]]
            elif temp1[1][4] == 'pp' and temp1[1][0] == 'ใต้':
                temp2 = [[temp1[1][0], temp1[1][0], temp1[0][0], temp1[2][0], 'v']]
                temp3 = [temp1[0]] + temp2
                temp2.clear()
                print('temp3 :', temp3)
                if temp3[0][4] == 'n' and temp3[1][4] == 'v':
                    temp2 = [[temp3[0][0], temp3[0][0], temp3[1][3], temp3[1][3], 'a'], ['SAND'], temp3[1]]
                elif temp3[0][4] == 'pn' and temp3[1][4] == 'v':
                    temp2 = [[temp3[0][0], temp3[0][0], temp3[1][2], temp3[1][2], 'a'], ['SAND'], temp3[1]]
    elif count_j == 4:
        if temp1[3][4] == 'pp' and temp1[4][4] == 'n':
            if temp1[3][4] == 'pp' and (temp1[3][0] == 'ใน' or 'ที่' or 'บน'):
                temp2 = [[temp1[3][0], temp1[3][0], temp1[4][0], 'x', 'v']]
                del temp1[3:5]
                temp1.append(temp2[0])
                temp2.clear()
                print("LMD : ", temp1)
                if temp1[2][4] == 'n' and (temp1[3][4] == 'v' and (temp1[3][0] == 'ใน' or 'ที่' or 'บน' or 'ใต้')):
                    temp2 = [[temp1[3][0], temp1[3][0], temp1[3][2], temp1[2][0], 'v']]
                    del temp1[2:5]
                    temp1.append(temp2[0])
                    temp2.clear()
                    # print(temp1)
                    if (temp1[1][4] == 'v' and (temp1[1][0] == 'หยิบ' or 'จับ')) and (
                            temp1[2][4] == 'v' and (temp1[2][0] == 'ใน' or 'ที่' or 'บน' or 'ใต้')):
                        temp2 = [['x', temp1[2][3], temp1[2][2], 'x', 'v']]
                        if temp1[0][4] == 'pn' and (temp1[1][4] == 'v' and (temp1[1][0] == 'หยิบ' or 'จับ')):
                            temp2 = [[temp1[0][0], temp1[2][3], temp1[2][2], temp1[0][0], 'a']]
                        print("TEMP1 : ", temp1)
                        print("TEMP2 : ", temp2)

    print('LMD temp2 : ', temp2)
    return temp2
    # App.lmd_img(temp2)
    # call_back_input(temp2)


def start(messegesinput):
    # sen = input("text: ")
    sen = messegesinput
    run(sen)


# start()


