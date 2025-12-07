import unittest
import matrix_function as mf


class MatrixMultiplyUnitTest(unittest.TestCase):
    def test_valid_matrices_2x2(self):
        """Тест умножения двух 2x2 матриц."""
        a = [[1, 2], [3, 4]]
        b = [[5, 6], [7, 8]]
        expected = [[19, 22], [43, 50]]
        self.assertEqual(mf.multiply(a, b), expected)

    def test_valid_matrices_2x3_and_3x2(self):
        """Тест умножения матриц 2x3 и 3x2."""
        a = [[1, 2, 3], [4, 5, 6]]
        b = [[7, 8], [9, 10], [11, 12]]
        expected = [[58, 64], [139, 154]]
        self.assertEqual(mf.multiply(a, b), expected)

    def test_valid_matrices_1x2_and_2x1(self):
        """Тест умножения матриц 1x2 и 2x1 (результат — 1x1)."""
        a = [[2, 3]]
        b = [[4], [5]]
        expected = [[23]]
        self.assertEqual(mf.multiply(a, b), expected)

    def test_invalid_dimensions(self):
        """Тест ошибки при несовпадении размеров (2x3 и 2x2)."""
        a = [[1, 2, 3], [4, 5, 6]]
        b = [[7, 8], [9, 10]]
        with self.assertRaises(ValueError) as context:
            mf.multiply(a, b)
        self.assertIn('Количество столбцов первой матрицы должно совпадать', str(context.exception))

    def test_empty_first_matrix(self):
        """Тест с пустой первой матрицей."""
        a = []
        b = [[1, 2], [3, 4]]
        with self.assertRaises(ValueError):
            mf.multiply(a, b)

    def test_empty_second_matrix(self):
        """Тест с пустой второй матрицей."""
        a = [[1, 2]]
        b = []
        with self.assertRaises(ValueError):
            mf.multiply(a, b)

    def test_first_matrix_with_empty_row(self):
        """Тест, если первая матрица содержит пустую строку."""
        a = [[], [1, 2]]
        b = [[3], [4]]
        with self.assertRaises(ValueError):
            mf.multiply(a, b)

    def test_inconsistent_rows_in_first_matrix(self):
        """Тест, если строки первой матрицы разной длины."""
        a = [[1, 2], [3, 4, 5]]  # Несогласованные строки
        b = [[6], [7], [8]]
        with self.assertRaises(ValueError):  # Это вызовет IndexError при выполнении
            mf.multiply(a, b)

    def test_single_element_matrices(self):
        """Тест умножения 1x1 матриц."""
        a = [[3]]
        b = [[4]]
        expected = [[12]]
        self.assertEqual(mf.multiply(a, b), expected)

    def test_multiply_by_zero_matrix(self):
        """Тест умножения на нулевую матрицу."""
        a = [[1, 2], [3, 4]]
        b = [[0, 0], [0, 0]]
        expected = [[0, 0], [0, 0]]
        self.assertEqual(mf.multiply(a, b), expected)

    def test_multiply_with_negative_numbers(self):
        """Тест с отрицательными числами."""
        a = [[-1, 2], [3, -4]]
        b = [[5, -6], [-7, 8]]
        expected = [[-19, 22], [43, -50]]
        self.assertEqual(mf.multiply(a, b), expected)

    def test_rectangular_result(self):
        """Тест прямоугольной результирующей матрицы (1x3 * 3x1 -> 1x1)."""
        a = [[1, 2, 3]]
        b = [[4], [5], [6]]
        expected = [[32]]
        self.assertEqual(mf.multiply(a, b), expected)


if __name__ == '__main__':
    unittest.main()
