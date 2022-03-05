#!/usr/bin/python3
import sys
sys.path.append('../..')
import unittest
from ...models.base_model import BaseModel



class TestBaseModel(unittest.TestCase):

    def test_id(self):
        self.m1 = BaseModel()
        self.m2 = BaseModel()
        self.assertNotEqual(self.m1.id, self.m2.id)

    def test_update(self):
        self.m1 = BaseModel()
        update = self.m1.updated_at
        self.m1.save()
        self.assertNotEqual(self.m1.updated_at, update)

    def test_to_from_json(self):
        self.m1 = BaseModel()
        self.m1_json = self.m1.to_dict()
        self.m2 = BaseModel(**self.m1_json)
        self.m2_json = self.m2.to_dict()
        self.assertEqual(self.m1_json, self.m2_json)

if __name__ == '__main__':
    unittest.main()
