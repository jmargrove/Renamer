from typing import Iterable
from utils.words import words

import unittest


class TestWords(unittest.TestCase):

    def test_single_word(self):
        res = words("Word")
        self.assertEqual(len(res), 1)

    def test_is_same_single_word(self):
        res = words("Word")
        self.assertEqual(res[0], "Word")

    def test_two_words(self):
        res = words("Word word")
        self.assertEqual(len(res), 2)

    def test_is_same_words(self):
        res = words("Word word")
        self.assertEqual(res[0], "Word")
        self.assertEqual(res[1], "word")

    def test_is_iterable(self):
        res = words("Word word word")
        self.assertIsInstance(res, Iterable)

    def test_does_contain_punctuation(self):
        res = words("Word!")
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0], "Word")
