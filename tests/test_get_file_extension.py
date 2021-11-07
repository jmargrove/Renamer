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
        print("testing test file")
        self.assertRaises(NameError, get_file_extension, "python.py$")
