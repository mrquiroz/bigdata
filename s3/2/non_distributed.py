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
done