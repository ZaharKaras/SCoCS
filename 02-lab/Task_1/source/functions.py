import re
from collections import Counter

def count_sentences(text):
    return len(re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\"?\s', text))

def count_nondeclarative_sentences(text):
    return len(re.findall(r'([!?]+)', text))

def avg_sentence_length(text):
    new_text = re.sub(r'\d+', '', text)
    sentences = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\"?\s', new_text)
    words_count = sum(len(s.split()) for s in sentences)
    return words_count / len(sentences)

def avg_word_length(text):
    words = re.findall('[a-zA-Z0-9]+', text)
    word_lengths = [len(w) for w in words]
    return sum(word_lengths) / len(words)

def top_k_ngrams(text, k=10, n=4):
    n_grams_dict = {}

    n_grams = [(text[i:i+n]) for i in range(len(text)-n+1)]

    for elem in n_grams:
        n_grams_dict[elem] = n_grams_dict.get(elem, 0) + 1
    
    if not n_grams_dict:
        return {}
    else:
        sorted_dict = dict(sorted(n_grams_dict.items(), key=lambda item: item[1], reverse=True))
        sorted_list = list(sorted_dict)
        k = min(len(sorted_list), k)

        k_repeated = {}
        for i in range(k):
            k_repeated[sorted_list[i]] = sorted_dict[sorted_list[i]]

        return k_repeated

    
