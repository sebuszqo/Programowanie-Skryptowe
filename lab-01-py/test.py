import main
import unittest
# python3 -m unittest test.py

class Test_TestSum(unittest.TestCase):
    def test_sum_integer_integer(self): # 2 int .
        self.assertEqual(main.sum(2, 2), 4)

    def test_sum_integer_float(self):   # int + float .
        self.assertEqual(main.sum(2, 1.5), 3.5)

    def test_sum_integer_string(self): # int + string . dopiero po zmianie string --> float
        self.assertEqual(main.sum(2, '2'), 4)

    def test_sum_string_string(self):   # string + string . dopiero po zmianie string --> float
        self.assertEqual(main.sum('2.1', '2.0'), 4.1)

    def test_sum_fraction_fraction(self):  # fraction + fraction . zamiana 4/5 --> 0.8
        self.assertEqual(main.sum(7/5, 3/5), 2)

    def test_sum_complex_int(self):  # complex + int --> . po dodaniu if z complex ( rzeczywista, urojona)
        self.assertEqual(main.sum(complex(15, 7), -13), complex(2,7))
    
    def test_sum_integer_wrong_number_in_string(self): # int + string --> . dopiero po asserRaises - ValueError
        with self.assertRaises(ValueError):
            self.assertEqual(main.sum(2,'Ala ma kota'), 2)
    
    def test_sum_integer_list(self): # int + array --> . dopiero po asserRaises - TypeError
        with self.assertRaises(TypeError):
            self.assertEqual(main.sum(1, [2, 3]), 1)

    
   

if '__name__' == '__main__':
    unittest.main()