import inspect
import os
import unittest
import pep8
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base
from models import rectangle


class TestBase(unittest.TestCase):

    def setUp(self):
        """ Method to prepare each single test """
        Base._Base__nb_objects = 0

    def test_pep8_conformance(self):
        """ Test that we conform to PEP8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_documentation(self):
        """ Test if base module is documented """
        self.assertTrue(rectangle.__doc__)

    def test_class_documentation(self):
        """ Test if Base class is documented """
        self.assertTrue(Rectangle.__doc__)

    def test_methods_documentation(self):
        """ Test if all Rectangle methods are documented
            """
        methods = inspect.getmembers(Rectangle)
        for method in methods:
            self.assertTrue(inspect.getdoc(method))

    def test_id(self):
        """Test ids given"""
        self.assertTrue(Rectangle(10, 2, 5, 4), self.id == 10)
        self.assertTrue(Rectangle(2, 5, 7, 3), self.id == 2)
        self.assertTrue(Rectangle(3, 7, 0, 0, 12), self.id == 3)
        self.assertTrue(Rectangle(3, 4), self.id == 3)

    def test_default_attributes(self):
        """Test attributes given"""
        r4 = Rectangle(3, 4)
        self.assertTrue(r4.id is not None)
        self.assertTrue(r4.width == 3)
        self.assertTrue(r4.height == 4)
        self.assertTrue(r4.x == 0)
        self.assertTrue(r4.y == 0)

    def test_rectangle_full_instance(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertTrue(r.id == 5)
        self.assertTrue(r.width == 1)
        self.assertTrue(r.height == 2)
        self.assertTrue(r.x == 3)
        self.assertTrue(r.y == 4)

    def test_width(self):
        """Test width attribute"""
        r1 = Rectangle(10, 2, 5, 4)
        r2 = Rectangle(2, 5, 7, 3)
        r3 = Rectangle(3, 7, 0, 0, 12)

        self.assertEqual(r1.width, 10)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r3.width, 3)

    def test_widths_valueerror(self):
        """Test width attribute value validations"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-2, 10)
            Rectangle(-2.5, 10)
            Rectangle(0, 10)

    def test_width_typeerror(self):
        """Test width attribute type validations"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(2.5, 10)
            Rectangle("2", 10)
            Rectangle([2], 10)
            Rectangle(["2"], 10)
            Rectangle((2, 3), 10)
            Rectangle({10, }, 1, 1, 1)
            Rectangle({"d": 10}, 1, 1, 1)

    def test_height(self):
        """Test height attribute"""
        r1 = Rectangle(10, 2, 5, 4)
        r2 = Rectangle(2, 5, 7, 3)
        r3 = Rectangle(3, 7, 0, 0, 12)

        self.assertEqual(r1.height, 2)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r3.height, 7)

    def test_height_valueerror(self):
        """Test height attribute value validations"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)
            Rectangle(10, -2.5)
            Rectangle(10, 0)

    def test_height_typeerror(self):
        """Test height attribute type validations"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, 2.5)
            Rectangle(10, "2")
            Rectangle(10, [2])
            Rectangle(10, ["2"])
            Rectangle(10, (2, 3))
            Rectangle(1, {10, }, 1, 1)
            Rectangle(1, {"d": 10}, 1, 1)

    def test_x(self):
        """Test x attribute"""
        r1 = Rectangle(10, 2, 5, 4)
        r2 = Rectangle(2, 5, 7, 3)
        r3 = Rectangle(3, 7, 0, 0, 12)

        self.assertEqual(r1.x, 5)
        self.assertEqual(r2.x, 7)
        self.assertEqual(r3.x, 0)

    def test_x_valueerror(self):
        """Test x attribute value validations"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -5)
            Rectangle(10, -2.5)

    def test_x_typeerror(self):
        """Test x attribute type validations"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, 2.5)
            Rectangle(10, 2, "2")
            Rectangle(10, 2, [2])
            Rectangle(10, 2, ["2"])
            Rectangle(10, 2, (2, 3))
            Rectangle(10, 2, 3, [2])
            Rectangle(1, 1, {10, }, 1, 1)
            Rectangle(1, 1, {"d": 10}, 1, 1)

    def test_y(self):
        """Test y attribute"""
        r1 = Rectangle(10, 2, 5, 4)
        r2 = Rectangle(2, 5, 7, 3)
        r3 = Rectangle(3, 7, 0, 0, 12)

        self.assertEqual(r1.y, 4)
        self.assertEqual(r2.y, 3)
        self.assertEqual(r3.y, 0)

    def test_y_valueerror(self):
        """Test y attribute value validations"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 5, -3)
            Rectangle(10, 2, -5.2)

    def test_y_typeerror(self):
        """Test y attribute type validations"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 2, 5.2)
            Rectangle(10, 2, 3, "2")
            Rectangle(10, 2, 3, [2])
            Rectangle(10, 2, 3, ["2"])
            Rectangle(10, 2, 3, (2, 3))
            Rectangle(10, 2, 3, [2])
            Rectangle(1, 1, 1, {10, }, 1)
            Rectangle(1, 1, 1, {"d": 10}, 1)

    def test_invalid_args_too_many(self):
        """Test wrong amount of attributes given"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6, 7)

    def test_invalid_args_too_few(self):
        """Test wrong amount of attributes given"""
        with self.assertRaises(TypeError):
            Rectangle(1)
            Rectangle()
            Rectangle(None)

    def test_rectangle_instance_update_id(self):
        """ Test updating the value for id """
        r = Rectangle(2, 10)
        r.id = 91
        self.assertEqual(r.id, 91)

    def test_private_attr_access(self):
        """Test private attributes can't be accessed"""
        with self.assertRaises(AttributeError):
            print(Rectangle.__width)
            print(Rectangle.__height)
            print(Rectangle.__x)
            print(Rectangle.__y)

    def test_class(self):
        """Test class created is indeed Rectangle"""
        self.assertEqual(type(Rectangle(1, 2)), Rectangle)

    def test_area(self):
        """Test method: area"""
        r1 = Rectangle(10, 2, 5, 4)
        r2 = Rectangle(2, 5, 7, 3)
        r3 = Rectangle(3, 7, 0, 0, 12)

        self.assertEqual(r1.area(), 20)
        self.assertEqual(r2.area(), 10)
        self.assertEqual(r3.area(), 21)

    def test_rectangle_area_method_update(self):
        """ Test if the area method is updatable """
        r = Rectangle(8, 4)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.area(), 32)

        r.area = 17
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.area, 17)

    def test_display_width_height(self):
        """ Test a Rectangle representation width/height in stdout """
        r = Rectangle(3, 4)
        expected = "###\n###\n###\n###\n"
        with patch('sys.stdout', new=StringIO()) as printed:
            r.display()
            self.assertEqual(printed.getvalue(), expected)

    def test_display_all_attr(self):
        """ Test a Rectangle representation width/height/x/y in stdout """
        r = Rectangle(2, 4, 1, 2)
        expected = "\n\n ##\n ##\n ##\n ##\n"
        with patch('sys.stdout', new=StringIO()) as printed:
            r.display()
            self.assertEqual(printed.getvalue(), expected)

    def test_str(self):
        """Test method: __str__"""
        r3 = Rectangle(3, 7, 0, 0, 12)
        self.assertEqual(str(r3), '[Rectangle] (12) 0/0 - 3/7')

    def test_update(self):
        """Test method: update(*args)"""
        r3 = Rectangle(3, 7, 0, 0, 12)
        self.assertEqual(str(r3), '[Rectangle] (12) 0/0 - 3/7')
        r3.update(1, 2, 3, 4, 5)
        self.assertEqual(str(r3), '[Rectangle] (1) 4/5 - 2/3')
        r3.update()
        self.assertEqual(str(r3), '[Rectangle] (1) 4/5 - 2/3')
        r3.update(7)
        self.assertEqual(str(r3), '[Rectangle] (7) 4/5 - 2/3')
        r3.update(7, 5)
        self.assertEqual(str(r3), '[Rectangle] (7) 4/5 - 5/3')
        r3.update(7, 5, 4)
        self.assertEqual(str(r3), '[Rectangle] (7) 4/5 - 5/4')
        r3.update(7, 5, 4, 3, 2)
        self.assertEqual(str(r3), '[Rectangle] (7) 3/2 - 5/4')

    def test_rectangle_update_empty_arguments(self):
        """ Test method: update without arguments """
        r = Rectangle(9, 6)
        self.assertFalse(r.update())

    def test_update_args_errors(self):
        """Test error *args"""
        r3 = Rectangle(3, 7, 0, 0, 12)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r3.update(7, 1, 2, 3, "string")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r3.update(7, 1, 2, 3, -99)

    def test_update_kwargs(self):
        """Test method: update(**kwargs)"""
        r3 = Rectangle(3, 7, 0, 0, 12)
        r3.update(id=7)
        self.assertEqual(str(r3), '[Rectangle] (7) 0/0 - 3/7')
        r3.update(id=7, x=13, y=17, width=27)
        self.assertEqual(str(r3), '[Rectangle] (7) 13/17 - 27/7')

    def test_update_kwargs_errors(self):
        """Test both valid and invalid *kwargs"""
        r3 = Rectangle(3, 7, 0, 0, 12)
        r3.update(nokey=555, invalid=777, testing=999, id=1111)
        self.assertEqual(str(r3), '[Rectangle] (1111) 0/0 - 3/7')

    def test_to_dictionary(self):
        """Test method: to_dictionary"""
        r3 = Rectangle(3, 7, 0, 0, 12)
        r4 = Rectangle(3, 4)
        r3dic = r3.to_dictionary()
        self.assertEqual(type(r3dic), dict)
        r4.update(**r3dic)
        self.assertEqual(str(r4), '[Rectangle] (12) 0/0 - 3/7')

    def test_save_to_file(self):
        """ Test method: save_to_file """
        r1 = Rectangle(8, 16, 2, 2, 15)
        r2 = Rectangle(7, 16, 3, 3, 15)
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_save_to_file_none(self):
        """ Test method: save_to_file with none argument """
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", 'r', encoding='utf-8') as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty(self):
        """ Test method: save_to_file with empty argument """
        r_list = []
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        Rectangle.save_to_file(r_list)
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", 'r', encoding='utf-8') as f:
            self.assertEqual("[]", f.read())


if __name__ == "__main__":
    unittest.main()
