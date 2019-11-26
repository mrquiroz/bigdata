import re, sys

feed_document = sys.stdin

for line in feed_document:
    line = re.sub(r'^\W+|\W+$','',line)
    words = re.split(r'\W+',line)
    cod = words[-1]

    for word in words[:-1]:
        print(cod + '\t' +word.lower())