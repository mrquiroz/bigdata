import re, sys

word_count_dict = {}
word_count_dict['Clarissa']=0
word_count_dict['Arabella']=0
word_count_dict['Robert']=0
word_count_dict['James']=0

feed_document = sys.stdin


for line_in_document in feed_document:
    line_in_document = re.sub(r'^\W+|\W+$', '', line_in_document)
    words_in_line = re.split(r'\W+', line_in_document)

    for word in words_in_line:
        
        if word.lower() == 'clarissa':
            word_count_dict['Clarissa'] = word_count_dict['Clarissa'] +1
        if word.lower() == 'arabella':
            word_count_dict['Arabella'] = word_count_dict['Arabella'] +1
        if word.lower() == 'robert':
            word_count_dict['Robert'] = word_count_dict['Robert'] +1
        if word.lower() == 'james':
            word_count_dict['James'] = word_count_dict['James'] +1

for item,valor in word_count_dict.items():
    print(item +'\t'+str(valor))

