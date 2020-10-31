import csv
from progress.bar import IncrementalBar
from tltk import nlp
from  tltk import  corpus
from tltk.nlp import initial, word_segment, syl_segment, word_segment_mm, read_thaidict, reset_thaidict, check_thaidict, spell_candidates
from tltk.corpus import trigram_load, bigram, trigram, unigram, collocates, TNC3g_load


def data_write():
    with open("data_write.csv","w",encoding= 'utf-8', newline="") as f:
        fw = csv.writer(f)
        fw.writerow(['จาน', 'ถาด', 'มีด', 'สุนัข', 'ยาย', 'กา', 'ตู้', 'แจกัน', 'แก้วน้ำ', 'แว่นตา', 'แหวน', 'ลูกโป่ง', 'ดินสอ','รองเท้า'
                     , 'ดอกไม้', 'สมุด', 'ช้อน', 'นาฬิกา', 'หนังสือ', 'ปืน', 'ขวด', 'ตะหลิว', 'กระทะ', 'เข้ม', 'หวี',
                        'มีด', 'ตู้เย็น', 'เข็มขัด', 'ชาม', 'พัดลม', 'ลูกบอล', 'เตารีด', 'ไม้กวาด', 'วิทยุ', 'กล่อง', 'โต๊ะ', 'ส้อม',
                     'โรงเรียน', 'ยางลบ', 'เรา', 'ฉัน', 'เธอ', 'พ่อ', 'แม่', 'ไป', 'ทำ', 'หยิบ', 'วาง', 'อยู่', 'มา', 'กลิ้ง', 'จับ'
                        , 'ที่', 'ใน', 'บน', 'ใต้', 'โรงเรียน', 'ตลาด'])

        print(type(fw))


def read_csv():
    with open(r"C:\Users\A_ATISAK\Desktop\Python for Project\data_write.csv", encoding='utf-8') as A:
        reader = csv.reader(A)
        data = list(reader)
        print(type(data))
        print(data)

read_csv()