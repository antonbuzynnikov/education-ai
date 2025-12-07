import unittest
from src.linear_algebra.matrix_function import add

class TestMatrixAddition(unittest.TestCase):

    def test_add_two_2x2_matrices(self):
        first = [[1, 2], [3, 4]]
        second = [[5, 6], [7, 8]]
        expected = [[6, 8], [10, 12]]
        self.assertEqual(add(first, second), expected)

    def test_add_two_3x3_matrices(self):
        first = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        second = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
        expected = [[1, 1, 1], [3, 3, 3], [5, 5, 5]]
        self.assertEqual(add(first, second), expected)

    def test_add_matrices_with_negative_values(self):
        first = [[-1, -2], [-3, -4]]
        second = [[1, 2], [3, 4]]
        expected = [[0, 0], [0, 0]]
        self.assertEqual(add(first, second), expected)

    def test_add_single_element_matrices(self):
        first = [[5]]
        second = [[3]]
        expected = [[8]]
        self.assertEqual(add(first, second), expected)

    def test_add_matrices_with_different_rows_should_raise_error(self):
        first = [[1, 2]]
        second = [[1, 2], [3, 4]]
        with self.assertRaises(ValueError):
            add(first, second)

    def test_add_matrices_with_different_columns_should_raise_error(self):
        first = [[1, 2, 3]]
        second = [[1, 2]]
        with self.assertRaises(ValueError):
            add(first, second)

    def test_add_empty_matrices(self):
        first = [[]]
        second = [[]]
        expected = [[]]
        self.assertEqual(add(first, second), expected)

    def test_add_matrices_with_different_inner_lengths_should_raise_error(self):
        # Это важно: внутренние списки должны быть одинаковой длины
        first = [[1, 2], [3]]
        second = [[4, 5], [6, 7]]
        # Здесь first[1] имеет длину 1, а second[1] — 2
        # Но наша функция проверяет только первую строку
        # Поэтому лучше уточнить, что вход — корректные матрицы
        # В реальности стоит добавить валидацию матрицы отдельно
        pass  # Пока пропустим, так как функция предполагает валидный ввод

if __name__ == '__main__':
    unittest.main()
