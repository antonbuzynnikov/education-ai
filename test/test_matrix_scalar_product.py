import unittest
from matrix_function import scalar_product

class TestScalarProduct(unittest.TestCase):

    def test_scalar_product_positive(self):
        """Тест умножения матрицы на положительный скаляр."""
        matrix = [[1, 2], [3, 4]]
        scalar = 2
        expected = [[2, 4], [6, 8]]
        result = scalar_product(matrix, scalar)
        self.assertEqual(result, expected)

    def test_scalar_product_negative(self):
        """Тест умножения матрицы на отрицательный скаляр."""
        matrix = [[1, -2], [3, 4]]
        scalar = -1
        expected = [[-1, 2], [-3, -4]]
        result = scalar_product(matrix, scalar)
        self.assertEqual(result, expected)

    def test_scalar_product_zero(self):
        """Тест умножения матрицы на ноль."""
        matrix = [[1, 2], [3, 4]]
        scalar = 0
        expected = [[0, 0], [0, 0]]
        result = scalar_product(matrix, scalar)
        self.assertEqual(result, expected)

    def test_scalar_product_fraction(self):
        """Тест умножения матрицы на дробный скаляр."""
        matrix = [[2, 4], [6, 8]]
        scalar = 0.5
        expected = [[1.0, 2.0], [3.0, 4.0]]
        result = scalar_product(matrix, scalar)
        self.assertEqual(result, expected)

    def test_single_element_matrix(self):
        """Тест матрицы 1x1."""
        matrix = [[5]]
        scalar = 3
        expected = [[15]]
        result = scalar_product(matrix, scalar)
        self.assertEqual(result, expected)

    def test_empty_matrix(self):
        """Тест пустой матрицы (допустимо, если все строки одинаковой длины)."""
        matrix = [[], []]
        scalar = 5
        expected = [[], []]
        result = scalar_product(matrix, scalar)
        self.assertEqual(result, expected)

    def test_invalid_matrix_mismatched_rows(self):
        """Тест некорректной матрицы (разная длина строк)."""
        matrix = [[1, 2], [3, 4, 5]]
        scalar = 2
        with self.assertRaises(ValueError) as context:
            scalar_product(matrix, scalar)
        self.assertEqual(str(context.exception), 'Матрица некорректна: строки имеют разную длину')


if __name__ == '__main__':
    unittest.main()