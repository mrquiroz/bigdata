import sys

feed_map = sys.stdin

previos_countes = None
total_word = 0

for line in feed_map:
    word, ocurrence = line.split('\t')

    if word != previos_countes:
        if previos_countes is not None:
            print(str(total_word) + '\t' + previos_countes)
        previos_countes = word
        total_word = 0
    total_word += int(ocurrence)

print(str(total_word) + '\t' + previos_countes)