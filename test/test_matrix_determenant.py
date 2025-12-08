import unittest
from matrix_function import determinant

class TestDeterminant(unittest.TestCase):
    def test_empty_matrix(self):
        """Определитель пустой матрицы — 1 по соглашению."""
        self.assertEqual(determinant([]), 1)

    def test_1x1_matrix(self):
        """Определитель матрицы 1x1."""
        self.assertEqual(determinant([[5]]), 5)
        self.assertEqual(determinant([[0]]), 0)
        self.assertEqual(determinant([[-3]]), -3)

    def test_2x2_matrix(self):
        """Определитель матрицы 2x2."""
        matrix = [[2, 1],
                  [3, 4]]
        self.assertEqual(determinant(matrix), 2*4 - 1*3)

        matrix2 = [[1, 2],
                   [2, 1]]
        self.assertEqual(determinant(matrix2), 1*1 - 2*2)

    def test_3x3_matrix(self):
        """Определитель матрицы 3x3, проверено вручную."""
        matrix = [[2, 1, 3],
                  [1, 3, 2],
                  [3, 2, 1]]
        self.assertEqual(determinant(matrix), -18)

    def test_identity_matrix(self):
        """Определитель единичной матрицы всегда 1."""
        i3 = [[1, 0, 0],
              [0, 1, 0],
              [0, 0, 1]]
        self.assertEqual(determinant(i3), 1)

        i4 = [[1, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 1, 0],
              [0, 0, 0, 1]]
        self.assertEqual(determinant(i4), 1)

    def test_singular_matrix(self):
        """Определитель вырожденной матрицы равен 0."""
        matrix = [[1, 2, 3],
                  [2, 4, 6],
                  [1, 1, 1]]  # первые две строки линейно зависимы
        self.assertEqual(determinant(matrix), 0)

    def test_upper_triangular_matrix(self):
        """Определитель верхне треугольной матрицы — произведение диагонали."""
        matrix = [[2, 3, 4],
                  [0, 5, 6],
                  [0, 0, 7]]
        self.assertEqual(determinant(matrix), 2 * 5 * 7)

    def test_negative_determinant(self):
        """Матрица с отрицательным определителем."""
        matrix = [[0, 1],
                  [1, 0]]
        self.assertEqual(determinant(matrix), -1)

    def test_large_matrix(self):
        """Тест на 4x4 матрице (проверка рекурсии)."""
        matrix = [[1, 0, 2, -1],
                  [3, 0, 0, 5],
                  [2, 1, 4, -3],
                  [1, 0, 5, 0]]
        det = determinant(matrix)
        # Проверим, что не возникает ошибок и результат — число
        self.assertIsInstance(det, int)
        # Можно вычислить вручную или через numpy для сверки, если нужно

if __name__ == '__main__':
    unittest.main()
