from __future__ import  unicode_literals
import codecs
import os



output_file = codecs.open("analogy.csv" , "w+", encoding="utf-8")
output_file.write(u'\uFEFF')
output_file.write('CATEGORY,WORD1,WORD2,WORD3,TARGET')
output_file.write('\n')




data_category_files = []
for file in os.listdir():
    if file.endswith(".txt"):
        data_category_files.append(file)

for file in data_category_files:
    rows = []
    outs =[]
    categoty = file.replace('.txt', '')
    file = open(file , encoding="utf8")
    sents = file.readlines()
    for sent in sents:
        sent = sent.replace("\n","")
        sent = sent.replace('﻿', "")
        row = sent.split("\t")
        rows.append(row)
    for row1 in rows:
        for row2 in rows:
            if row1 != row2:
                outs.append(categoty+','+row1[0]+','+row1[1]+','+row2[0]+','+row2[1])


    for out in outs:
        output_file.write(out)
        output_file.write("\n")
