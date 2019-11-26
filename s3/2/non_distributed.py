#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re, sys

word_count_dict = {}

feed_document = sys.stdin


for line_in_document in feed_document:
    line_in_document = re.sub(r'^\W+|\W+$', '', line_in_document)
    words_in_line = re.split(r'\W+', line_in_document)

    for word in words_in_line:
        word = word.lower()
        word_count_dict[word] = word_count_dict.get(word, 0) + 1

    print(word_count_dict)



i=7
while [ $i -le 9 ]
do
cat clarissa_$i.txt | python3 non_distributed.py > word_count_clarissa_$i.txt
((i++))

cat survey_data.txt | python mapper_4_1.py | sort -k1,1 | python reducer_4_1.py > out_reducer_4_1.txt

done

aws s3 cp s3://mrquiroz/richardson_clarissa/clarissa_1.txt - | cat | python mapper.py | sort -k1,1 | python reducer.py > out_reducer.txt

i=1
while [ $i -le 3 ]
do
aws s3 cp s3://mrquiroz/richardson_clarissa/clarissa_$i.txt - | cat | python mapper.py | sort -k1,1 | python reducer.py > out_reducer_$i.txt
aws s3 cp out_reducer_$i.txt s3://mrquiroz/richardson_clarissa/
tail out_reducer_$i.txt
rm -rf out_reducer_$i.txt
((i++))
done


i=1
while [ $i -le 9 ]
do
aws s3 cp s3://mrquiroz/richardson_clarissa/clarissa_$i.txt - | cat | python3 maprimitivo.py  > name_count_clarissa_$i.txt
aws s3 cp name_count_clarissa_$i.txt s3://mrquiroz/richardson_clarissa_namecount/
tail name_count_clarissa_$i.txt
rm -rf name_count_clarissa_$i.txt
((i++))
done

