import re, sys

word_count_dict = {}

feed_document = sys.stdin

for line_in_document in feed_document:
    line = re.sub(r'^\W+|\W+$','',line)
    words = re.split(r'\W+',line)
    cod = words[-1]
    print(cod + '\t' + '1')