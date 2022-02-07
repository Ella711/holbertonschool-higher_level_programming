import unittest
import json
import pep8
from models import base
from models.base import Base
from models.rectangle import Rectangle
from os.path import exists as file_exists


class TestBase(unittest.TestCase):

    def setUp(self):
        """ Method to prepare each single test """
        Base._Base__nb_objects = 0

    def test_pep8_conformance(self):
        """ Test that we conform to PEP8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_documentation(self):
        """ Test if base module is documented """
        self.assertTrue(base.__doc__)

    def test_class_documentation(self):
        """ Test if Base class is documented """
        self.assertTrue(Base.__doc__)

    def test_id(self):
        """Test ids given"""
        self.assertTrue(Base(1), self.id == 1)
        self.assertTrue(Base(12), self.id == 12)
        self.assertTrue(Base(-20), self.id == -20)

    def test_no_id(self):
        """Test ids match when given"""
        self.assertTrue(Base(), self.id == 1)
        self.assertTrue(Base(), self.id == 2)
        self.assertTrue(Base(), self.id == 3)

    def test_mix_ids(self):
        """" Create multiple Base instance with and without ids"""
        self.assertTrue(Base(), self.id == 1)
        self.assertTrue(Base(5), self.id == 5)
        self.assertTrue(Base(), self.id == 2)

    def test_string_id(self):
        """ Test string id"""
        self.assertTrue(Base("5"), self.id == "5")

    def test_invalid_args(self):
        """Test wrong amount of attributes given"""
        with self.assertRaises(TypeError):
            Base(1, 2, 3, 4, 5, 6, 7)

    def test_private_attr_access(self):
        """Test private attribute accessibility"""
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)
            print(Base.nb_objects)

    def test_class(self):
        """Test class created is indeed Rectangle"""
        self.assertEqual(type(Base(1)), Base)

    def test_to_json_string(self):
        """Test dict given translates into JSON string"""
        testd0 = {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}
        testd1 = {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}
        teststringd01 = Base.to_json_string([testd0, testd1])
        self.assertTrue(type(testd0) == dict)
        self.assertTrue(type(teststringd01) == str)
        self.assertTrue(teststringd01,
                        [{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},
                         {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}])

    def test_none_to_json_string(self):
        """Test no dict given translates into JSON string of empty dict"""
        testd2 = None
        teststringd2 = Base.to_json_string([testd2])
        self.assertTrue(type(teststringd2) == str)
        self.assertTrue(teststringd2, "[]")

    def test_empty_to_json_string(self):
        """Test empty dict given translates into JSON string of empty dict"""
        testd3 = dict()
        teststringd3 = Base.to_json_string([testd3])
        self.assertTrue(len(testd3) == 0)
        self.assertTrue(type(teststringd3) == str)
        self.assertTrue(teststringd3, "[]")

    def test_from_json_string(self):
        """Test JSON string translates into Python dict"""
        s0 = '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},\
               {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}]'
        strs0 = Base.from_json_string(s0)
        self.assertTrue(type(s0) == str)
        self.assertTrue(type(strs0) == list)
        self.assertTrue(type(strs0[0]) == dict)
        self.assertTrue(strs0,
                        [{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},
                         {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}])
        self.assertTrue(strs0[0],
                        {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5})

    def test_from_none_json_string(self):
        """Test no JSON string translates into empty list"""
        s2 = None
        strs2 = Base.from_json_string(s2)
        self.assertTrue(type(strs2) == list)
        self.assertTrue(strs2 == [])

    def test_from_empty_json_string(self):
        """Test no JSON string translates into empty list"""
        s3 = ""
        strs3 = Base.from_json_string(s3)
        self.assertTrue(type(strs3) == list)
        self.assertTrue(strs3 == [])

    def test_create(self):
        """Test setting attributes from a dictionary to another instance"""
        r = Rectangle(3, 5, 1, 2, 99)
        rdic = r.to_dictionary()
        r2 = Rectangle.create(**rdic)
        self.assertEqual(str(r), '[Rectangle] (99) 1/2 - 3/5')
        self.assertEqual(str(r2), '[Rectangle] (99) 1/2 - 3/5')
        self.assertIsNot(r, r2)

    def test_save_to_file(self):
        """Test save to file"""
        r = Rectangle(10, 7, 2, 8, 99)
        r2 = Rectangle(2, 4, 2, 2, 98)
        Rectangle.save_to_file([r, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(
                json.dumps([r.to_dictionary(), r2.to_dictionary()]),
                file.read())

    def test_save_none_to_file(self):
        """Test save None to file"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual('[]', file.read())

    def test_empty_none_to_file(self):
        """Test save empty list to file"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual('[]', file.read())

    def test_load_from_file(self):
        """Test load from file"""
        r = Rectangle(10, 7, 2, 8, 99)
        r2 = Rectangle(2, 4, 2, 2, 98)
        Rectangle.save_to_file([r, r2])
        recs = Rectangle.load_from_file()
        self.assertEqual(len(recs), 2)
        for k, v in enumerate(recs):
            if k == 0:
                self.assertEqual(str(v), '[Rectangle] (99) 2/8 - 10/7')
            if k == 1:
                self.assertEqual(str(v), '[Rectangle] (98) 2/2 - 2/4')

    def test_load_from_none_file(self):
        """Test load from None file"""
        Rectangle.save_to_file(None)
        recs = Rectangle.load_from_file()
        self.assertEqual(type(recs), list)
        self.assertEqual(len(recs), 0)

    def test_load_from_empty_file(self):
        """Test load from empty file"""
        Rectangle.save_to_file([])
        recs = Rectangle.load_from_file()
        self.assertEqual(type(recs), list)
        self.assertEqual(len(recs), 0)


if __name__ == "__main__":
    unittest.main()
