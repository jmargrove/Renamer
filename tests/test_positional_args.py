from subprocess import run
import unittest

PYTHON3 = "python3"
RENAMER = "main.py"


def get_command():
    return [PYTHON3, RENAMER]


class TestPositionalArgs(unittest.TestCase):

    def test_no_args(self):
        process = run(get_command())
        self.assertEqual(process.returncode, 1)
