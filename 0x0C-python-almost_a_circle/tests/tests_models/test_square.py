import unittest
import pep8
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
        """ Test if base module is documented """
        self.assertTrue(square.__doc__)

    def test_class_documentation(self):
        """ Test if Base class is documented """
        self.assertTrue(Square.__doc__)

    def test_id(self):
        """Test ids given"""
        self.assertTrue(Square(10), self.id == 10)
        self.assertTrue(Square(5, 4), self.id == 2)
        self.assertTrue(Square(2, 5, 7), self.id == 3)
        self.assertTrue(Square(3, 7, 0, 12), self.id == 3)

    def test_default_attributes(self):
        """Test attributes given"""
        self.assertTrue(self.s3.id is not None)
        self.assertTrue(self.s3.width == 3)
        self.assertTrue(self.s3.height == 3)
        self.assertTrue(self.s3.size == 3)
        self.assertTrue(self.s3.x == 7)
        self.assertTrue(self.s3.y == 0)

    def test_width(self):
        """Test width attribute"""
        self.assertEqual(self.s1.width, 10)
        self.assertEqual(self.s2.width, 2)
        self.assertEqual(self.s3.width, 3)
        self.assertEqual(self.s4.width, 5)

        """Test width attribute value validations"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-2)
            Square(-2.5)
            Square(0)

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
        self.assertEqual(self.s1.height, 10)
        self.assertEqual(self.s2.height, 2)
        self.assertEqual(self.s3.height, 3)
        self.assertEqual(self.s4.height, 5)

    def test_size(self):
        """Test height attribute"""
        self.assertEqual(self.s2.size, 2)
        self.assertEqual(self.s3.size, 3)
        self.assertEqual(self.s4.size, 5)

    def test_x(self):
        """Test x attribute"""
        self.assertEqual(self.s2.x, 5)
        self.assertEqual(self.s3.x, 7)
        self.assertEqual(self.s4.x, 4)

        """Test x attribute value validations"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(10, -5)
            Square(10, -2.5)

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
        self.assertEqual(self.s2.y, 7)
        self.assertEqual(self.s3.y, 0)

        """Test y attribute value validations"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(10, 2, -3)
            Square(10, 2, -5.2)

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

    def test_invalid_args(self):
        """Test wrong amount of attributes given"""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5, 6, 7)
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

    def test_area(self):
        """Test method: area"""
        self.assertEqual(self.s1.area(), 100)
        self.assertEqual(self.s2.area(), 4)
        self.assertEqual(self.s3.area(), 9)
        self.assertEqual(self.s4.area(), 25)

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
        self.assertEqual(str(self.s3), '[Square] (12) 7/0 - 3')
        self.s3.update(1, 2, 3, 4)
        self.assertEqual(str(self.s3), '[Square] (1) 3/4 - 2')
        self.s3.update()
        self.assertEqual(str(self.s3), '[Square] (1) 3/4 - 2')
        self.s3.update(7)
        self.assertEqual(str(self.s3), '[Square] (7) 3/4 - 2')
        self.s3.update(7, 6)
        self.assertEqual(str(self.s3), '[Square] (7) 3/4 - 6')
        self.s3.update(7, 6, 5)
        self.assertEqual(str(self.s3), '[Square] (7) 5/4 - 6')
        self.s3.update(7, 6, 5, 4)
        self.assertEqual(str(self.s3), '[Square] (7) 5/4 - 6')

        """Test error *args"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.s3.update(7, 1, 2, "string")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            self.s3.update(7, 1, 2, -99)

        """Test method: update(**kwargs)"""
        self.s3.update(id=7)
        self.assertEqual(str(self.s3), '[Square] (7) 2/4 - 1')
        self.s3.update(id=7, x=13, y=17, size=27)
        self.assertEqual(str(self.s3), '[Square] (7) 13/17 - 27')

        """Test both valid and invalid *kwargs"""
        self.s3.update(nokey=555, invalid=777, testing=999, id=1111)
        self.assertEqual(str(self.s3), '[Square] (1111) 13/17 - 27')

    def test_to_dictionary(self):
        """Test method: to_dictionary"""
        s3dic = self.s3.to_dictionary()
        self.assertEqual(type(s3dic), dict)
        self.s4.update(**s3dic)
        self.assertEqual(str(self.s4), '[Square] (12) 7/0 - 3')


if __name__ == "__main__":
    unittest.main()
