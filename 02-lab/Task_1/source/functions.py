import re

def count_sentences(text):
    return(re.split('[.?!]+', text))
