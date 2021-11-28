import os
import unittest
from utils.parse_file import parse_file


class TestParseFile(unittest.TestCase):

    def test_return_tuple(self):
        resp = parse_file("")
        self.assertEqual(len(resp), 3)

    def test_name(self):
        resp = parse_file("name.py")
        self.assertEqual(resp[0], os.getcwd())
        self.assertEqual(resp[1], "name")
        self.assertEqual(resp[2], ".py")
