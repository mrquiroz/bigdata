#!/usr/bin/python3.6

import re,sys

feed_document = sys.stdin

for line_in in feed_document:
    (user_id,movie,rating,timestamp) = line_in.replace('\n','').split(',')
    print(movie+'\t'+rating)