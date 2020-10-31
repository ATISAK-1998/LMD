import tltk
from tltk import nlp
from tltk import corpus
from tltk.nlp import initial, word_segment, syl_segment, word_segment_mm, read_thaidict, reset_thaidict, check_thaidict, spell_candidates
from tltk.corpus import trigram_load, bigram, trigram, unigram, collocates, TNC3g_load
import codecs

def run():
    text = ""
    text = input('ป้อนข้อความ : ')
    text = tltk.nlp.word_segment(text)
    text = text.replace("<s/>", "")
#    result = test_list(text)
    print(text)
#    return result

# ทำให้ประโยคจากการตัดคำกลายเป็นlist
def test_list(text):
    text = ""
    text = input('ป้อนข้อความ : ')
    text = tltk.nlp.word_segment(text)
    text = text.replace("<s/>", "")
    #    result = test_list(text)
    print(text)
    stat = 0
    end = 0
    text_list = []
    for i in  range(len(text())):
        if text[i] == "|":
            end = i
            text.append(text[stat:end])
            stat = i+1
    text.append(text[stat:len(text)])
    print(text)


test_list()