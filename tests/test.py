import unittest
from friendlier_json import Reader, Object


class TestModul(unittest.TestCase):
    def testSelect(self):
        reader = Reader()
        reader.file = 'test.json'
        self.assertEqual(reader.select(name='Maik')[0], {"name": "Maik", "age": 15})

    def testInsert(self):
        reader = Reader()
        reader.file = 'test.json'
        obj = Object(name='Try', age=2300)
        self.assertEqual(reader.insert(obj), True)


if __name__ == '__main__':
    unittest.main()
