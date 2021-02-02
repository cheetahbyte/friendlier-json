from unittest import TestCase
import unittest
from friendlydb import Friendly


class TestModul(TestCase):
    def testSelect(self):
        db = Friendly(path='test.json')
        dct = db.select(age=69)[0]
        self.assertEqual(dct, {
            "first_name": "Derrek",
            "last_name": "Vasiliev",
            "email": "dvasiliev6@rakuten.co.jp",
            "gender": "Genderqueer",
            "age": 69
        })

    def testCachedSelect(self):
        db = Friendly(path='test.json')
        dct = db.select(age=69)[0]
        dct2 = db.select(cache=True)[0]
        self.assertEqual(dct, dct2)


if __name__ == '__main__':
    unittest.main()
