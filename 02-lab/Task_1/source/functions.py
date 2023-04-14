import re

def count_sentences(text):
    return(re.split('[.?!]+', text))

def count_nondeclarative_sentences(text):
    return len(re.findall(r'[?!][^.?!]*', text))

def avg_sentence_length(text):
    sentences = re.split('[.?!]+', text)
    words_count = sum(len(s.split()) for s in sentences)
    return words_count / len(sentences)
