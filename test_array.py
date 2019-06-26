import unittest
from unittest import TestCase
from d_array import DynamicArray


class TestDynamicArray(TestCase):
    def setUp(self):
        self.a = DynamicArray()
        self.a.append("p")
        self.a.append("o")
        self.a.append("f")

    def test_init(self):
        self.assertTrue(type(self.a) == DynamicArray)

    def test_getitem(self):
        self.assertTrue(self.a.__getitem__(0) == "p")
        self.assertTrue(self.a.__getitem__(1) == "o")

    def test_insert(self):
        self.a.insert(1, "g")
        self.assertTrue(self.a[1] == "g")

    def test_len(self):
        self.assertTrue(len(self.a) == 3)

    def test_remove(self):
        self.a.remove("p")
        self.assertTrue(self.a.__getitem__(1) == "f")
        self.assertTrue(len(self.a) == 2)


if __name__ == '__main__':
    unittest.main()
