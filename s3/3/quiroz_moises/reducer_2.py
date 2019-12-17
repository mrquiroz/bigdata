#!/usr/bin/python3.6
import sys

feed_output = sys.stdin

previos_countes = None

total_count = 0
puntaje = 0

for line_o in feed_output:
    usr,relevance = line_o.split('\t')
    if usr != previos_countes:
        if previos_countes is not None:
            print(previos_countes,'\t',str(puntaje/total_count))
        previos_countes = usr
        total_count = 0
        puntaje = 0
    total_count += 1
    puntaje += float(relevance)
print(previos_countes+'\t'+str(puntaje/total_count))