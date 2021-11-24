import unittest
import score

class MyTestCase(unittest.TestCase):
    def test_normal(self):
        # запускаем тестируемую функцию
        result = score.get_score('34X7/')
        # проверяем что она вернула
        self.assertEqual(result, f'Количество очков для результатов 34X7/ - 42')

    def test_only_x(self):
        # запускаем тестируемую функцию
        result = score.get_score('xxxxx')
        # проверяем что она вернула
        self.assertEqual(result, f'Количество очков для результатов XXXXX - 100')

    def test_only_X(self):
        # запускаем тестируемую функцию
        result = score.get_score('XXXXXX')
        # проверяем что она вернула
        self.assertEqual(result, f'Количество очков для результатов XXXXXX - 120')

    def test_only_number(self):
        # запускаем тестируемую функцию
        result = score.get_score('123454')
        # проверяем что она вернула
        self.assertEqual(result, f'Количество очков для результатов 123454 - 19')

    def test_whith_missing(self):
        # запускаем тестируемую функцию
        result = score.get_score('-23/54')
        # проверяем что она вернула
        self.assertEqual(result, f'Количество очков для результатов -23/54 - 26')

    def test_whith_missing_2(self):
        # запускаем тестируемую функцию
        result = score.get_score('-2-/54')
        # проверяем что она вернула
        self.assertEqual(result, f'Количество очков для результатов -2-/54 - 26')

    def test_big_sum(self):
        # запускаем тестируемую функцию
        result = score.get_score('-25/59')
        # проверяем что она вернула
        self.assertRaises(BaseException)

    def test_no_number(self):
        # запускаем тестируемую функцию
        # проверяем что она вернула
        with self.assertRaises(BaseException):
            score.get_score('/x/45')

    def test_error_count(self):
        with self.assertRaises(BaseException):
            score.get_score('12525')

    def test_letters(self):
        with self.assertRaises(BaseException):
            score.get_score('aa1a')





if __name__ == '__main__':
    unittest.main()
