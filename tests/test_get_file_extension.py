import unittest
from utils.parse_file import parse_file

file_out_passes = {
    ".py": {"python.py", "test.py", "no-file.py", "camelCase.py"},
    ".ts": {"constants.ts", "formatter.ts"},
    ".jsx": {"Component.jsx", "FunctionalComponent.jsx"},
    ".docx": {"word.docx"},
    ".pdf": {"vector-file.pdf"},
    ".png": {"image.png"},
    ".jpg": {"image.jpg"},
    ".jpeg": {"image of cats.jpeg"},
}


class TestGetFileExtension(unittest.TestCase):

    def test_file_out_passes(self):
        for [key, setName] in file_out_passes.items():
            for name in setName:
                out = parse_file(name)
                self.assertEqual(out[2], key)

    def test_dir_prefix(self):
        out = parse_file('directory/test.py')
        self.assertEqual(out[2], '.py')

    def test_dir_prefix_dot_slash(self):
        out = parse_file("./directory/test.py")
        self.assertEqual(out[2], '.py')

    def test_dir_with_kebabcase(self):
        out = parse_file('./directory/test-test.tsx')
        self.assertEqual(out[2], '.tsx')

    def test_nested_dir(self):
        out = parse_file('./dir/dir/directory/test-test.tsx')
        self.assertEqual(out[2], '.tsx')

    def test_dir_with_numbers(self):
        out = parse_file('./directory-88/test-test.tsx')
        self.assertEqual(out[2], '.tsx')

    def test_file_name_with_numbers(self):
        out = parse_file('./directory-88/test-test-88.tsx')
        self.assertEqual(out[2], '.tsx')

    def test_double_dot_path(self):
        out = parse_file('../../directory-88/test-test-88.tsx')
        self.assertEqual(out[2], '.tsx')
