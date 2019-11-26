import sys

feed_map = sys.stdin

previos_countes = None
total_word = 0
valor_word = 0

for line in feed_map:
    word, ocurrence = line.split('\t')

    if word != previos_countes:
        if previos_countes is not None:
            prom = valor_word/total_word
            print(previos_countes + '\t' + str(prom))
        previos_countes = word
        total_word = 0
        valor_word = 0
    valor_word += float(ocurrence)
    total_word += 50

print(previos_countes + '\t' + str(prom))