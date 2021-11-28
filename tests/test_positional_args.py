import os
import subprocess
import tempfile
import unittest

PYTHON3 = "python3"
RENAMER = "main.py"


def get_command():
    return [PYTHON3, RENAMER]


class TestPositionalArgs(unittest.TestCase):

    def test_no_args(self):
        process = subprocess.run(get_command())
        self.assertEqual(process.returncode, 1)

    def test_file(self):
        prefix = os.path.basename(__file__)
        with tempfile.NamedTemporaryFile(prefix=prefix, delete=False) as tf:
            self.assertEqual(os.path.exists(tf.name), True)
            out = subprocess.Popen([PYTHON3, RENAMER, tf.name],
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
            out = out.communicate()
            renamed_file_path = out[0].rstrip().decode()
            os.remove(renamed_file_path)
