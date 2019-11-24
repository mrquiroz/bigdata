import re, sys

word_count = {}

feed_document = sys.stdin

for line in feed_document:
    line = re.sub(r'\W+|-\W+$','',line)
    words = re.split(r'\W+',line)

    for word in words:
        word = word.lower()
        word_count[word] = word_count.get(word,0) +1

    print(word_count)

print(word_count)