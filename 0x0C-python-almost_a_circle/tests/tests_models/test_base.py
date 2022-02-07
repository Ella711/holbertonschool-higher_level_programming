import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_id(self):
        self.assertTrue(Base(1), self.id == 1)
        self.assertTrue(Base(), self.id == 1)
        self.assertTrue(Base(), self.id == 2)
        self.assertTrue(Base(12), self.id == 12)
        self.assertTrue(Base(0), self.id == 0)
        self.assertTrue(Base(-20), self.id == -20)

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


if __name__ == "__main__":
    unittest.main()
