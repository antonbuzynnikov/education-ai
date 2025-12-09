import unittest

from matrix_function import matrix_rank_and_basis_minor

class TestMatrixRankAndBasisMinor(unittest.TestCase):

    def test_empty_matrix(self):
        """Тест: пустая матрица"""
        matrix = []
        minor, rows, cols, rank = matrix_rank_and_basis_minor(matrix)
        self.assertEqual(rank, 0)
        self.assertEqual(minor, 0)
        self.assertEqual(rows, [])
        self.assertEqual(cols, [])

    def test_single_zero_element(self):
        """Тест: матрица 1x1 с нулём"""
        matrix = [[0]]
        minor, rows, cols, rank = matrix_rank_and_basis_minor(matrix)
        self.assertEqual(rank, 0)
        self.assertEqual(minor, 0)
        self.assertEqual(rows, [])
        self.assertEqual(cols, [])

    def test_single_nonzero_element(self):
        """Тест: матрица 1x1 с ненулевым элементом"""
        matrix = [[5]]
        minor, rows, cols, rank = matrix_rank_and_basis_minor(matrix)
        self.assertEqual(rank, 1)
        self.assertEqual(rows, [0])
        self.assertEqual(cols, [0])
        self.assertEqual(minor, 5)

    def test_2x2_full_rank(self):
        """Тест: матрица 2x2 полного ранга"""
        matrix = [[1, 2], [3, 4]]
        minor, rows, cols, rank = matrix_rank_and_basis_minor(matrix)
        self.assertEqual(rank, 2)
        self.assertEqual(rows, [0, 1])
        self.assertEqual(cols, [0, 1])
        expected_det = 1*4 - 2*3  # -2
        self.assertEqual(minor, expected_det)

    def test_2x2_rank_1(self):
        """Тест: матрица 2x2 ранга 1"""
        matrix = [[1, 2], [2, 4]]  # вторая строка — удвоение первой
        minor, rows, cols, rank = matrix_rank_and_basis_minor(matrix)
        self.assertEqual(rank, 1)
        self.assertEqual(len(rows), 1)
        self.assertEqual(len(cols), 1)
        # Базисный минор должен быть ненулевым и выбираться из первого ненулевого элемента
        # Например, если выбран [0,0], то minor = 1
        self.assertIn(rows[0], [0, 1])
        self.assertIn(cols[0], [0, 1])
        self.assertNotEqual(minor, 0)

    def test_3x3_full_rank(self):
        """Тест: матрица 3x3 полного ранга"""
        matrix = [[1, 0, 2], [3, 1, 0], [2, 0, 5]]
        minor, rows, cols, rank = matrix_rank_and_basis_minor(matrix)
        self.assertEqual(rank, 3)
        self.assertEqual(sorted(rows), [0, 1, 2])
        self.assertEqual(sorted(cols), [0, 1, 2])
        # Проверим, что минор — это определитель всей матрицы
        expected_det = 1*(1*5 - 0*0) - 0 + 2*(3*0 - 1*2)  # 5 - 4 = 1
        self.assertEqual(minor, expected_det)

    def test_3x3_rank_2(self):
        """Тест: матрица 3x3 ранга 2"""
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # строки линейно зависимы
        minor, rows, cols, rank = matrix_rank_and_basis_minor(matrix)
        self.assertEqual(rank, 2)
        self.assertEqual(len(rows), 2)
        self.assertEqual(len(cols), 2)
        # Проверим, что минор ненулевой
        self.assertNotEqual(minor, 0)
        # Проверим, что выбранные строки и столбцы в пределах размера
        for r in rows:
            self.assertIn(r, [0, 1, 2])
        for c in cols:
            self.assertIn(c, [0, 1, 2])

    def test_matrix_with_zero_column(self):
        """Тест: матрица с нулевым столбцом"""
        matrix = [[0, 1], [0, 2]]
        minor, rows, cols, rank = matrix_rank_and_basis_minor(matrix)
        self.assertEqual(rank, 1)
        self.assertEqual(cols, [1])  # должен выбрать ненулевой столбец
        self.assertNotEqual(minor, 0)

    def test_rank_0_matrix(self):
        """Тест: матрица 2x2 из нулей"""
        matrix = [[0, 0], [0, 0]]
        minor, rows, cols, rank = matrix_rank_and_basis_minor(matrix)
        self.assertEqual(rank, 0)
        self.assertEqual(minor, 0)
        self.assertEqual(rows, [])
        self.assertEqual(cols, [])

    def test_non_square_matrix_full_rank(self):
        """Тест: прямоугольная матрица 2x3, полный ранг (2)"""
        matrix = [[1, 0, 2], [0, 1, 3]]
        minor, rows, cols, rank = matrix_rank_and_basis_minor(matrix)
        self.assertEqual(rank, 2)
        self.assertEqual(len(rows), 2)
        self.assertEqual(len(cols), 2)
        self.assertNotEqual(minor, 0)

    def test_non_square_matrix_tall(self):
        """Тест: прямоугольная матрица 3x2, полный ранг (2)"""
        matrix = [[1, 2], [3, 4], [5, 6]]
        minor, rows, cols, rank = matrix_rank_and_basis_minor(matrix)
        self.assertEqual(rank, 2)
        self.assertEqual(len(rows), 2)
        self.assertEqual(len(cols), 2)
        self.assertNotEqual(minor, 0)


if __name__ == '__main__':
    unittest.main()