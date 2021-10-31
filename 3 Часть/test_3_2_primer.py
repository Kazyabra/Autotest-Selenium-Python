import unittest


class TestAbs(unittest.TestCase):

    def test_abs1(self):
        self.assertEqual(abs(-42), 42, 'Тут ожидалось положительное число')

    def test_abs2(self):
        self.assertEqual(abs(-42), -42, 'Пример проваленного теста, типа "тут ожидалось отрицательное число"')


if __name__ == "__main__":
    unittest.main()
