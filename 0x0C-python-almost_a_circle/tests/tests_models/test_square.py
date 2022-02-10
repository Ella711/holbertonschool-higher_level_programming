import unittest
import pep8
import inspect
from io import StringIO
from unittest.mock import patch
from models import square
from models.square import Square
from models.base import Base


class TestBase(unittest.TestCase):

    def setUp(self):
        """ Method to prepare each single test """
        Base._Base__nb_objects = 0
        self.s1 = Square(10)
        self.s4 = Square(5, 4)
        self.s2 = Square(2, 5, 7)
        self.s3 = Square(3, 7, 0, 12)

    def test_pep8_conformance(self):
        """ Test that we conform to PEP8 """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_documentation(self):
        """ Test if square module is documented """
        self.assertTrue(square.__doc__)

    def test_class_documentation(self):
        """ Test if Square class is documented """
        self.assertTrue(Square.__doc__)

    def test_methods_documentation(self):
        """ Test if all Square methods are documented """
        methods = inspect.getmembers(Square)
        for method in methods:
            self.assertTrue(inspect.getdoc(method))

    def test_id(self):
        """Test ids given"""
        self.assertTrue(Square(10), self.id == 10)
        self.assertTrue(Square(5, 4), self.id == 2)
        self.assertTrue(Square(2, 5, 7), self.id == 3)
        self.assertTrue(Square(3, 7, 0, 12), self.id == 3)

    def test_default_attributes(self):
        """Test attributes given"""
        s3 = Square(3, 7, 0, 12)
        self.assertTrue(s3.id is not None)
        self.assertTrue(s3.width == 3)
        self.assertTrue(s3.height == 3)
        self.assertTrue(s3.size == 3)
        self.assertTrue(s3.x == 7)
        self.assertTrue(s3.y == 0)

    def test_width(self):
        """Test width attribute"""
        s1 = Square(10)
        s4 = Square(5, 4)
        s2 = Square(2, 5, 7)
        s3 = Square(3, 7, 0, 12)

        self.assertEqual(s1.width, 10)
        self.assertEqual(s2.width, 2)
        self.assertEqual(s3.width, 3)
        self.assertEqual(s4.width, 5)

    def test_widths_valueerror(self):
        """Test width attribute value validations"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-2)
            Square(-2.5)
            Square(0)

    def test_width_typeerror(self):
        """Test width attribute type validations"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(2.5)
            Square("2")
            Square([2])
            Square(["2"])
            Square((2, 3))
            Square({10, })
            Square({"d": 10})

    def test_height(self):
        """Test height attribute"""
        s1 = Square(10)
        s4 = Square(5, 4)
        s2 = Square(2, 5, 7)
        s3 = Square(3, 7, 0, 12)

        self.assertEqual(s1.height, 10)
        self.assertEqual(s2.height, 2)
        self.assertEqual(s3.height, 3)
        self.assertEqual(s4.height, 5)

    def test_size(self):
        """Test height attribute"""
        s4 = Square(5, 4)
        s2 = Square(2, 5, 7)
        s3 = Square(3, 7, 0, 12)

        self.assertEqual(s2.size, 2)
        self.assertEqual(s3.size, 3)
        self.assertEqual(s4.size, 5)

    def test_x(self):
        """Test x attribute"""
        s4 = Square(5, 4)
        s2 = Square(2, 5, 7)
        s3 = Square(3, 7, 0, 12)

        self.assertEqual(s2.x, 5)
        self.assertEqual(s3.x, 7)
        self.assertEqual(s4.x, 4)

    def test_x_valueerror(self):
        """Test x attribute value validations"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(10, -5)
            Square(10, -2.5)

    def test_x_typeerror(self):
        """Test x attribute type validations"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, 2.5)
            Square(10, "2")
            Square(10, [2])
            Square(10, ["2"])
            Square(10, (2, 3))
            Square(10, [2])
            Square(1, {10, })
            Square(1, {"d": 10})

    def test_y(self):
        """Test y attribute"""
        s2 = Square(2, 5, 7)
        s3 = Square(3, 7, 0, 12)

        self.assertEqual(self.s2.y, 7)
        self.assertEqual(self.s3.y, 0)

    def test_y_valueerror(self):
        """Test y attribute value validations"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(10, 2, -3)
            Square(10, 2, -5.2)

    def test_y_typeerror(self):
        """Test y attribute type validations"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 2, 5.2)
            Square(10, 2, "2")
            Square(10, 2, [2])
            Square(10, 2, ["2"])
            Square(10, 2, (2, 3))
            Square(10, 2, [2])
            Square(1, 1, {10, })
            Square(1, 1, {"d": 10})

    def test_invalid_args_too_many(self):
        """Test wrong amount of attributes given"""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5, 6, 7)

    def test_invalid_args_too_few(self):
        """Test wrong amount of attributes given"""
        with self.assertRaises(TypeError):
            Square()
            Square(None)

    def test_private_attr_access(self):
        """Test private attributes can't be accessed"""
        with self.assertRaises(AttributeError):
            print(Square.__width)
            print(Square.__height)
            print(Square.__size)
            print(Square.__x)
            print(Square.__y)

    def test_class(self):
        """Test class created is indeed Rectangle"""
        self.assertEqual(type(Square(1)), Square)

    def test_rectangle_instance_update_id(self):
        """ Test updating the value for id """
        r = Square(10)
        r.id = 91
        self.assertEqual(r.id, 91)

    def test_square_instance_update_size(self):
        """ Test a Square instance updating values for size """
        r = Square(4)
        r.size = 15
        self.assertEqual(r.size, 15)

    def test_area(self):
        """Test method: area"""
        s1 = Square(10)
        s4 = Square(5, 4)
        s2 = Square(2, 5, 7)
        s3 = Square(3, 7, 0, 12)

        self.assertEqual(s1.area(), 100)
        self.assertEqual(s2.area(), 4)
        self.assertEqual(s3.area(), 9)
        self.assertEqual(s4.area(), 25)

    def test_square_area_method_update(self):
        """ Test if area method can be updated """
        r = Square(8)
        self.assertEqual(r.size, 8)
        self.assertEqual(r.area(), 64)

        r.area = 17
        self.assertEqual(r.size, 8)
        self.assertEqual(r.area, 17)

    def test_square_area_method_with_arguments(self):
        """ Test if area method receives arguments """
        r = Square(9, 7)
        with self.assertRaises(TypeError):
            r.area(5)

    def test_display_size(self):
        """ Test a Square representation of size in stdout """
        r = Square(4)
        expected = "####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as printed:
            r.display()
            self.assertEqual(printed.getvalue(), expected)

    def test_display_all_attr(self):
        """ Test a Square representation size/x/y in stdout """
        r = Square(2, 1, 2)
        expected = "\n\n ##\n ##\n"
        with patch('sys.stdout', new=StringIO()) as printed:
            r.display()
            self.assertEqual(printed.getvalue(), expected)

    def test_str(self):
        """Test method: __str__"""
        s3 = Square(3, 7, 0, 12)
        self.assertEqual(str(s3), '[Square] (12) 7/0 - 3')

    def test_update(self):
        """Test method: update(*args)"""
        s3 = Square(3, 7, 0, 12)

        self.assertEqual(str(s3), '[Square] (12) 7/0 - 3')
        s3.update(1, 2, 3, 4)
        self.assertEqual(str(s3), '[Square] (1) 3/4 - 2')
        s3.update()
        self.assertEqual(str(s3), '[Square] (1) 3/4 - 2')
        s3.update(7)
        self.assertEqual(str(s3), '[Square] (7) 3/4 - 2')
        s3.update(7, 6)
        self.assertEqual(str(s3), '[Square] (7) 3/4 - 6')
        s3.update(7, 6, 5)
        self.assertEqual(str(s3), '[Square] (7) 5/4 - 6')
        s3.update(7, 6, 5, 4)
        self.assertEqual(str(s3), '[Square] (7) 5/4 - 6')

    def test_square_update_empty_arguments(self):
        """ Test update method without arguments """
        r = Square(9)
        self.assertFalse(r.update())

    def test_update_args_errors(self):
        """Test error *args"""
        s3 = Square(3, 7, 0, 12)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s3.update(7, 1, 2, "string")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s3.update(7, 1, 2, -99)

    def test_update_kwargs(self):
        """Test method: update(**kwargs)"""
        s3 = Square(3, 7, 0, 12)
        s3.update(id=7)
        self.assertEqual(str(s3), '[Square] (7) 7/0 - 3')
        s3.update(id=7, x=13, y=17, size=27)
        self.assertEqual(str(s3), '[Square] (7) 13/17 - 27')

    def test_update_kwargs_errors(self):
        """Test both valid and invalid *kwargs"""
        s3 = Square(3, 7, 0, 12)
        s3.update(nokey=555, invalid=777, testing=999, id=1111)
        self.assertEqual(str(s3), '[Square] (1111) 7/0 - 3')

    def test_to_dictionary(self):
        """Test method: to_dictionary"""
        s3 = Square(3, 7, 0, 12)
        s4 = Square(5, 4)
        s3dic = self.s3.to_dictionary()
        self.assertEqual(type(s3dic), dict)
        s4.update(**s3dic)
        self.assertEqual(str(s4), '[Square] (12) 7/0 - 3')

    def test_square_to_dictionary_arguments(self):
        """ Test if to_dictionary method receives arguments """
        r = Square(8)
        with self.assertRaises(TypeError):
            r_dict = r.to_dictionary(size=9)


if __name__ == "__main__":
    unittest.main()
