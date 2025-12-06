import unittest

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
    
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(0, 5), 0)
    
    #def test_fail_example(self):
        # Этот тест упадёт для демонстрации
       # self.assertEqual(add(2, 2), 5)  # Намеренная ошибка

if __name__ == '__main__':
    unittest.main()
