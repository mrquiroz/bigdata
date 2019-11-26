import re, sys

feed_document = sys.stdin

for line in feed_document:
    line = re.sub(r'^\W+|\W+$','',line)
    words = re.split(r'\W+',line)

    for word in words:
        print(word.lower() + '\t' + '1') 