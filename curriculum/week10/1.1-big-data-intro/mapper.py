
# mapper.py
import sys
import re
import string

# get text from standard input
for line in sys.stdin:
    line = line.strip()
    remove = string.punctuation
    remove = remove.replace("-", "") # don't remove hyphens
    pattern = r"[{}]".format(remove) # create the pattern
    re.sub(pattern, "", line)
    words = line.split()
    for word in words:
        word = word.lower()
        word = word.replace('.', '')
        word = word.replace('\'s', '')
        word = word.replace(',', '')
        word = word.replace('\"', '')
        word = word.replace(';', '')
        word = word.replace('_', '')
        print '%s\t%s' % (word, 1)
