import unittest
import functions

class TestFunctions(unittest.TestCase):

    def test_count_sentences(self):
        text = "Hello! How are you? I'm doing well."
        self.assertEqual(functions.count_sentences(text), 3)

    def test_count_nondeclarative_sentences(self):
        text = "Hello! How are you? I'm doing well."
        self.assertEqual(functions.count_nondeclarative_sentences(text), 2)

    def test_avg_sentence_length(self):
        text = "Hello! How are you? I'm doing well."
        self.assertAlmostEqual(functions.avg_sentence_length(text), 7/3)

    def test_avg_word_length(self):
        text = "Hello! How are you? I'm doing well."
        self.assertAlmostEqual(functions.avg_word_length(text), 25/8)

    def test_top_k_ngrams(self):
        self.assertEqual(functions.top_k_ngrams('Hello, Maks!'), {'Hell': 1, 'ello': 1, 'llo,': 1, 'lo, ': 1, 'o, M': 1, ', Ma': 1, ' Mak': 1, 'Maks': 1, 'aks!': 1})
        
if __name__ == '__main__':
    unittest.main()