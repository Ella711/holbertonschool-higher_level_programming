import unittest
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):

    def setUp(self):
        self.r1 = Rectangle(10, 2, 5, 4)
        self.r2 = Rectangle(2, 5, 7, 3)
        self.r3 = Rectangle(3, 7, 0, 0, 12)
        self.r4 = Rectangle(3, 4)

    def tearDown(self):
        pass

    def test_id(self):
        self.assertTrue(Rectangle(10, 2, 5, 4), self.id == 10)
        self.assertTrue(Rectangle(2, 5, 7, 3), self.id == 2)
        self.assertTrue(Rectangle(3, 7, 0, 0, 12), self.id == 3)
        self.assertTrue(Rectangle(3, 4), self.id == 3)

    def test_default_attributes(self):
        """Test attributes given"""
        self.assertTrue(self.r4.id is not None)
        self.assertTrue(self.r4.width == 3)
        self.assertTrue(self.r4.height == 4)
        self.assertTrue(self.r4.x == 0)
        self.assertTrue(self.r4.y == 0)

    def test_width(self):
        """Test width attribute"""
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r3.width, 3)

        """Test width attribute value validations"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-2, 10)
            Rectangle(-2.5, 10)
            Rectangle(0, 10)

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
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r2.height, 5)
        self.assertEqual(self.r3.height, 7)

        """Test height attribute value validations"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)
            Rectangle(10, -2.5)
            Rectangle(10, 0)

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
        self.assertEqual(self.r1.x, 5)
        self.assertEqual(self.r2.x, 7)
        self.assertEqual(self.r3.x, 0)

        """Test x attribute value validations"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -5)
            Rectangle(10, -2.5)

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
        self.assertEqual(self.r1.y, 4)
        self.assertEqual(self.r2.y, 3)
        self.assertEqual(self.r3.y, 0)

        """Test y attribute value validations"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 5, -3)
            Rectangle(10, 2, -5.2)

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

    def test_invalid_args(self):
        """Test wrong amount of attributes given"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6, 7)
        with self.assertRaises(TypeError):
            Rectangle(1)
            Rectangle()
            Rectangle(None)

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
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r2.area(), 10)
        self.assertEqual(self.r3.area(), 21)

    def test_str(self):
        """Test method: __str__"""
        self.assertEqual(str(self.r3), '[Rectangle] (12) 0/0 - 3/7')

    def test_update(self):
        """Test method: update(*args)"""
        self.assertEqual(str(self.r3), '[Rectangle] (12) 0/0 - 3/7')
        self.r3.update(1, 2, 3, 4, 5)
        self.assertEqual(str(self.r3), '[Rectangle] (1) 4/5 - 2/3')
        self.r3.update()
        self.assertEqual(str(self.r3), '[Rectangle] (1) 4/5 - 2/3')
        self.r3.update(7)
        self.assertEqual(str(self.r3), '[Rectangle] (7) 4/5 - 2/3')
        self.r3.update(7, 5)
        self.assertEqual(str(self.r3), '[Rectangle] (7) 4/5 - 5/3')
        self.r3.update(7, 5, 4)
        self.assertEqual(str(self.r3), '[Rectangle] (7) 4/5 - 5/4')
        self.r3.update(7, 5, 4, 3, 2)
        self.assertEqual(str(self.r3), '[Rectangle] (7) 3/2 - 5/4')

        """Test error *args"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.r3.update(7, 1, 2, 3, "string")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            self.r3.update(7, 1, 2, 3, -99)

        """Test method: update(**kwargs)"""
        self.r3.update(id=7)
        self.assertEqual(str(self.r3), '[Rectangle] (7) 3/2 - 1/2')
        self.r3.update(id=7, x=13, y=17, width=27)
        self.assertEqual(str(self.r3), '[Rectangle] (7) 13/17 - 27/2')

        """Test both valid and invalid *kwargs"""
        self.r3.update(nokey=555, invalid=777, testing=999, id=1111)
        self.assertEqual(str(self.r3), '[Rectangle] (1111) 13/17 - 27/2')

    def test_to_dictionary(self):
        """Test method: to_dictionary"""
        r3dic = self.r3.to_dictionary()
        self.assertEqual(type(r3dic), dict)
        self.r4.update(**r3dic)
        self.assertEqual(str(self.r4), '[Rectangle] (12) 0/0 - 3/7')


if __name__ == "__main__":
    unittest.main()
