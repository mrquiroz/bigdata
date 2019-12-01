#!/usr/bin/python3.6

import re,sys

feed_document = sys.stdin

for line_in in feed_document:
    generos = line_in.replace('\n','').split('|')
    temp = generos.pop(0)
    temp = temp.replace('\n','').split(',')
    movie_id = temp.pop(0)
    temp_genero = temp.pop(-1)
    generos.append(temp_genero)
    movie = ''.join(temp)
    for i in generos:
        print(movie+'\t'+i)
    