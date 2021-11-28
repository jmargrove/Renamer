import unittest
from utils.get_file_extension import get_file_extension

file_extension_passes = {
    "py": {"python.py", "test.py", "no-file.py", "camelCase.py"},
    "ts": {"constants.ts", "formatter.ts"},
    "jsx": {"Component.jsx", "FunctionalComponent.jsx"},
    "docx": {"word.docx"},
    "pdf": {"vector-file.pdf"},
    "png": {"image.png"},
    "jpg": {"image.jpg"},
    "jpeg": {"image of cats.jpeg"},
}


class TestGetFileExtension(unittest.TestCase):

    def test_file_extension_passes(self):
        for [key, setName] in file_extension_passes.items():
            for name in setName:
                extension = get_file_extension(name)
                self.assertEqual(extension, key)

    def test_file_extension_fails(self):
        self.assertRaises(NameError, get_file_extension, "python.py$")

    def test_dir_prefix(self):
        extension = get_file_extension('directory/test.py')
        self.assertEqual(extension, 'py')

    def test_dir_prefix_dot_slash(self):
        extension = get_file_extension("./directory/test.py")
        self.assertEqual(extension, 'py')

    def test_dir_with_kebabcase(self):
        extension = get_file_extension('./directory/test-test.tsx')
        self.assertEqual(extension, 'tsx')

    def test_nested_dir(self):
        extension = get_file_extension('./dir/dir/directory/test-test.tsx')
        self.assertEqual(extension, 'tsx')

    def test_dir_with_numbers(self):
        extension = get_file_extension('./directory-88/test-test.tsx')
        self.assertEqual(extension, 'tsx')

    def test_file_name_with_numbers(self):
        extension = get_file_extension('./directory-88/test-test-88.tsx')
        self.assertEqual(extension, 'tsx')
