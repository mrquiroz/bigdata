#!/usr/bin/python3.6
import sys

feed_output = sys.stdin
previos_countes = None
puntaje = 0

for line_o in feed_output:
    mov,nombre = line_o.split('\t')
    if mov != previos_countes:
        if previos_countes is not None:
            if puntaje >=2 and puntaje <=10 :
                print(previos_countes,'\t',str(puntaje))
        previos_countes = mov
        puntaje = 0
    puntaje += 1
print(previos_countes+'\t'+str(puntaje))