#!/usr/bin/python3.6

import re,sys

feed_document = sys.stdin

for line_in in feed_document:
    (movie,tag_id,relevance) = line_in.replace('\n','').split(',')
    print(tag_id+'\t'+relevance)