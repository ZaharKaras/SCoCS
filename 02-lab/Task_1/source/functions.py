import re

def count_sentences(text):
    return(re.split('[.?!]+', text))

def count_nondeclarative_sentences(text):
    return len(re.findall(r'[?!][^.?!]*', text))


