# import os
from subprocess import run
# import tempfile
import unittest

PYTHON3 = "python3"
RENAMER = "main.py"


def get_command():
    return [PYTHON3, RENAMER]


class TestPositionalArgs(unittest.TestCase):

    def test_no_args(self):
        process = run(get_command())
        self.assertEqual(process.returncode, 1)

    # def test_file(self):
    #     prefix = os.path.basename(__file__)
    #     with tempfile.NamedTemporaryFile(prefix) as tf:
    #         process = run([PYTHON3, RENAMER, tf.name])
    #         self.assertEqual(process.returncode, 0)
