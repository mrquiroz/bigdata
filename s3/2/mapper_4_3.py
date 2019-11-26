import re, sys

feed_document = sys.stdin

for line in feed_document:
    line = re.sub(r'^\W+|\W+$','',line)
    words = re.split(r'\W+',line)
    cod = words[-1]

    
    count = sum(list(map(lambda x: int(x),words[:-1])))/len(words[:-1])
    if count >= 0.6:
        print(cod + '\t' + str(sum(list(map(lambda x: int(x),words[:-1])))))