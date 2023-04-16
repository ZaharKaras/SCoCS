import re
from collections import Counter

def count_sentences(text):
    return len(re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\"?\s', text))

def count_nondeclarative_sentences(text):
    return len(re.findall(r'[?!][^.?!]*', text))

def avg_sentence_length(text):
    sentences = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\"?\s', text)
    words_count = sum(len(s.split()) for s in sentences)
    return words_count / len(sentences)

def avg_word_length(text):
    words = re.findall('[a-zA-Z0-9]+', text)
    word_lengths = [len(w) for w in words]
    return sum(word_lengths) / len(words)

def top_k_ngrams(text, k=10, n=4):
    text = text.lower()
    text = re.sub('[^a-zA-Z0-9 ]+', '', text)
    words = text.split()
    n_grams = [' '.join(words[i:i+n]) for i in range(len(words)-n+1)]
    sorted_n_gram_counts = Counter(n_grams).most_common(k)
    return sorted_n_gram_counts
