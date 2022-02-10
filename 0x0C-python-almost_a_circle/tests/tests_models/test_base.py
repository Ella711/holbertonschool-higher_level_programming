import inspect
import unittest
import json
import pep8
import os
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

    def test_methods_documentation(self):
        """ Test if all Base methods are documented
            """
        methods = inspect.getmembers(Base)
        for method in methods:
            self.assertTrue(inspect.getdoc(method))

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
        r = Rectangle(15, 7, 6, 5, 30)
        r_dict = r.to_dictionary()
        json_str = Base.to_json_string([r_dict])

        self.assertIsInstance(json_str, str)
        dict_r = json.loads(json_str)
        self.assertEqual(dict_r, [r_dict])

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
        dict_list = [
            {'id': 10, 'size': 15, 'x': 1, 'y': 2},
            {'id': 7, 'size': 14, 'x': 2, 'y': 1, }
        ]
        json_str = Base.to_json_string(dict_list)
        json_dict_list = Base.from_json_string(json_str)

        self.assertIsInstance(json_dict_list, list)
        self.assertIsInstance(json_dict_list[0], dict)
        self.assertIsInstance(json_dict_list[1], dict)

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

    def test_from_json_string_wrong_type(self):
        """ Test passing wrong data type to from_json_string method """
        with self.assertRaises(TypeError):
            json_dict_list = Base.from_json_string(["r1", "r2"])

    def test_create(self):
        """Test setting attributes from a dictionary to another instance"""
        r = Rectangle(3, 5, 1, 2, 99)
        rdic = r.to_dictionary()
        r2 = Rectangle.create(**rdic)
        self.assertEqual(str(r), '[Rectangle] (99) 1/2 - 3/5')
        self.assertEqual(str(r2), '[Rectangle] (99) 1/2 - 3/5')
        self.assertIsNot(r, r2)

    def test_create_without_dict(self):
        """ Test create method by not passing a dict"""
        r1 = Rectangle(9, 10)
        with self.assertRaises(TypeError):
            r2 = Rectangle.create(**r1)

    def test_create_more_arguments(self):
        """ Test create method by passing more arguments than expected"""
        r1 = Rectangle(10, 15)
        r2 = Rectangle(20, 25)
        r1_dict = r1.to_dictionary()
        r2_dict = r2.to_dictionary()
        with self.assertRaises(TypeError):
            r = Rectangle.create(**r1_dict, **r2_dict)

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

    def test_save_to_file_more_arguments(self):
        """ Test save_to_file method with more arguments """
        r = Rectangle(4, 5)

        with self.assertRaises(TypeError):
            r.save_to_file([r], [])

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
