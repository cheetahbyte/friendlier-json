import unittest
from unittest import TestCase

from friendlydb import Friendly, JsonObject


class TestModul(TestCase):
    def testInsertBulk1(self):
        db = Friendly(path='test.json')
        objs = [JsonObject(name='test', age=30),
                JsonObject(name='anothertest', age=35)]
        db.insert_bulk(objs)

    def testInsertBulk2(self):
        db = Friendly(path='test.json')
        objs = [{'name': 'test2', 'age': 40}, {'name': 'anothertest2', 'age': 45}]
        db.insert_bulk(objs)


if __name__ == '__main__':
    unittest.main()
