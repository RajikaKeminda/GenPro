import os
import unittest

class TestReadFile(unittest.TestCase):
    def test_read(self):
        with open(os.path.join(os.path.dirname(__file__), "sample.py"), "r") as file:
            code = file.read()
            code = code.replace("Hello !", "Hello world")
            print(code)

        with open(os.path.join(os.path.dirname(__file__), "sample.py"), "w") as file:
            file.write(code)