import unittest
import numpy as np
from numpy_array_exercise import (
    find_power_with_six, 
    first_ten_powers,
    create_frame_matrix,
    create_number_matrix,
    create_multiplication_matrix,
    create_special_matrix
)

class TestNumpyPowerExercise(unittest.TestCase):
    def test_find_power_with_six(self):
        """测试2^i末尾为6的i值查找函数"""
        result = find_power_with_six()
    
        # 检查返回类型是否为numpy数组
        self.assertIsInstance(result, np.ndarray)
            
        # 检查是否包含了所有满足条件的数
        all_valid = np.array([i for i in range(1, 100) if str(2**i)[-1] == '6'])
        np.testing.assert_array_equal(sorted(result), sorted(all_valid))

    def test_first_ten_powers(self):
        """测试2的前10次幂计算函数"""
        result = first_ten_powers()
        
        # 检查返回类型是否为numpy数组
        self.assertIsInstance(result, np.ndarray)
        
        # 检查数组长度是否为10
        self.assertEqual(len(result), 10)
        
        # 检查计算结果是否正确
        expected = np.array([2**i for i in range(10)])
        np.testing.assert_array_equal(result, expected)

    def test_create_frame_matrix(self):
        """测试框架矩阵创建函数"""
        result = create_frame_matrix()
        
        # 检查矩阵大小
        self.assertEqual(result.shape, (10, 10))
        
        # 检查边框是否都是1
        self.assertTrue(np.all(result[0:2, :] == 1))  # 上边框
        self.assertTrue(np.all(result[-2:, :] == 1))  # 下边框
        self.assertTrue(np.all(result[:, 0:2] == 1))  # 左边框
        self.assertTrue(np.all(result[:, -2:] == 1))  # 右边框
        
        # 检查内部是否都是0
        self.assertTrue(np.all(result[2:-2, 2:-2] == 0))

    def test_create_number_matrix(self):
        """测试数字矩阵创建函数"""
        result = create_number_matrix()
        
        # 检查矩阵大小
        self.assertEqual(result.shape, (10, 10))
        
        # 检查边框是否都是-1
        self.assertTrue(np.all(result[0, :] == -1))  # 上边框
        self.assertTrue(np.all(result[-1, :] == -1))  # 下边框
        self.assertTrue(np.all(result[:, 0] == -1))  # 左边框
        self.assertTrue(np.all(result[:, -4:] == -1))  # 右边框
        
        # 检查内部数字是否正确
        expected_numbers = np.arange(40).reshape(8, 5)
        self.assertTrue(np.all(result[1:-1, 1:6] == expected_numbers))

    def test_create_multiplication_matrix(self):
        """测试乘法表矩阵创建函数"""
        result = create_multiplication_matrix()
        
        # 检查矩阵大小
        self.assertEqual(result.shape, (3, 5))
        
        # 检查矩阵内容
        expected = np.array([[i * j for j in range(5)] for i in range(3)])
        np.testing.assert_array_equal(result, expected)

    def test_create_special_matrix(self):
        """测试特殊矩阵创建函数"""
        result = create_special_matrix()
        self._test_matrix_shape(result)
        self._test_matrix_diagonal(result)
        self._test_matrix_non_diagonal(result)
        self._test_matrix_type(result)
        self._test_matrix_symmetry(result)

    def _test_matrix_shape(self, matrix):
        """测试矩阵形状是否正确"""
        self.assertEqual(matrix.shape, (11, 11))

    def _test_matrix_diagonal(self, matrix):
        """测试对角线元素是否正确"""
        expected_diagonal = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5]
        np.testing.assert_array_equal(np.diag(matrix), expected_diagonal)

    def _test_matrix_non_diagonal(self, matrix):
        """测试非对角线元素是否都为1"""
        # 创建一个全1矩阵
        ones = np.ones((11, 11))
        # 将对角线元素设置为期望值
        np.fill_diagonal(ones, [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5])
        # 比较整个矩阵
        np.testing.assert_array_equal(matrix, ones)

    def _test_matrix_type(self, matrix):
        """测试返回值类型是否为numpy数组"""
        self.assertIsInstance(matrix, np.ndarray)
        self.assertTrue(np.issubdtype(matrix.dtype, np.number))

    def _test_matrix_symmetry(self, matrix):
        """测试对角线是否对称"""
        diagonal = np.diag(matrix)
        self.assertTrue(np.array_equal(diagonal[:5], diagonal[-5:][::-1]))
        self.assertEqual(diagonal[5], 0)

if __name__ == '__main__':
    unittest.main()
