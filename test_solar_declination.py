import unittest
import numpy as np
from calculate_solar_declination import (
    calculate_declination_loop,
    calculate_declination_vector
)

class TestSolarDeclination(unittest.TestCase):
    def setUp(self):
        """设置测试数据"""
        self.test_days = [0, 79, 172, 266, 356]  # 1月1日、春分、夏至、秋分、冬至
        self.expected_values = [
            -23.0706,  # 1月1日
            0.0,       # 春分
            23.44,     # 夏至
            0.0,       # 秋分
            -23.44     # 冬至
        ]
        self.tolerance = 0.01  # 允许的误差范围

    def test_loop_calculation(self):
        """测试循环计算方法"""
        results = calculate_declination_loop(self.test_days)
        for result, expected in zip(results, self.expected_values):
            self.assertAlmostEqual(result, expected, delta=self.tolerance)

    def test_vector_calculation(self):
        """测试数组运算方法"""
        results = calculate_declination_vector(self.test_days)
        for result, expected in zip(results, self.expected_values):
            self.assertAlmostEqual(result, expected, delta=self.tolerance)

    def test_methods_consistency(self):
        """测试两种方法的结果是否一致"""
        loop_results = calculate_declination_loop(self.test_days)
        vector_results = calculate_declination_vector(self.test_days)
        for loop_result, vector_result in zip(loop_results, vector_results):
            self.assertAlmostEqual(loop_result, vector_result, delta=0.0001)

if __name__ == '__main__':
    unittest.main()
