import unittest

from utils.kebab_case import kebab_case


class TestKebabCase(unittest.TestCase):

    def test_uppercase(self):
        res = kebab_case("Test-UpperCase")
        self.assertEqual(res, 'test-uppercase')

    def test_add_dash(self):
        res = kebab_case("no dash at all")
        self.assertEqual(res, 'no-dash-at-all')

    def test_single_quote_replace(self):
        res = kebab_case("what's-with's-single's-quote's")
        self.assertEqual(res, "whats-withs-singles-quotes")

    def test_double_space(self):
        res = kebab_case("double  space")
        self.assertEqual(res, "double-space")

    def test_tripple_space(self):
        res = kebab_case("tripple   space")
        self.assertEqual(res, "tripple-space")

    def test_trim_start(self):
        res = kebab_case(" start-space")
        self.assertEqual(res, "start-space")

    def test_trim_end(self):
        res = kebab_case("end-space ")
        self.assertEqual(res, "end-space")

    def test_trim(self):
        res = kebab_case(" start-space-end ")
        self.assertEqual(res, "start-space-end")

    def test_questionmark(self):
        res = kebab_case("question-mark?")
        self.assertEqual(res, "question-mark")

    def test_bash(self):
        res = kebab_case("bash!")
        self.assertEqual(res, "bash")

    def test_stop(self):
        res = kebab_case("bash.")
        self.assertEqual(res, "bash")