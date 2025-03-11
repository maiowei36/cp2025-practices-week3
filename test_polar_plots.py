import unittest
from unittest.mock import patch
import numpy as np
import matplotlib.pyplot as plt
from polar_plots import (
    plot_deltoid,
    plot_galilean_spiral,
    plot_feys_function
)

class TestPolarPlots(unittest.TestCase):
    def setUp(self):
        """设置测试环境"""
        self.test_points = 100

    def test_plot_creation(self):
        """测试是否正确创建了所有必要的图形元素"""
        with patch('matplotlib.pyplot.plot') as mock_plot:
            with patch('matplotlib.pyplot.title') as mock_title:
                with patch('matplotlib.pyplot.xlabel') as mock_xlabel:
                    with patch('matplotlib.pyplot.ylabel') as mock_ylabel:
                        # 测试三角洲曲线
                        plot_deltoid(self.test_points)
                        mock_plot.assert_called()
                        mock_title.assert_called()
                        mock_xlabel.assert_called()
                        mock_ylabel.assert_called()

    def test_deltoid_calculation(self):
        """测试三角洲曲线的计算结果"""
        with patch('matplotlib.pyplot.plot') as mock_plot:
            plot_deltoid(self.test_points)
            args, _ = mock_plot.call_args
            # 修改这里，正确获取x和y值
            x_values, y_values = args[0], args[1]
            
            # 验证点数
            self.assertEqual(len(x_values), self.test_points)
            self.assertEqual(len(y_values), self.test_points)
            
            # 验证特定点的值（θ = 0时）
            self.assertAlmostEqual(x_values[0], 3.0)  # 当θ = 0时，x = 3
            self.assertAlmostEqual(y_values[0], 0.0)  # 当θ = 0时，y = 0

    def test_galilean_spiral_calculation(self):
        """测试伽利略螺旋的计算结果"""
        with patch('matplotlib.pyplot.plot') as mock_plot:
            plot_galilean_spiral(self.test_points)
            args, _ = mock_plot.call_args
            # 修改这里，正确获取x和y值
            x_values, y_values = args[0], args[1]
            
            # 验证点数
            self.assertEqual(len(x_values), self.test_points)
            self.assertEqual(len(y_values), self.test_points)
            
            # 验证值域
            r_values = np.sqrt(x_values**2 + y_values**2)
            theta_max = 10 * np.pi
            self.assertLessEqual(max(r_values), theta_max**2)

    def test_feys_function_calculation(self):
        """测试Fey's函数的计算结果"""
        with patch('matplotlib.pyplot.plot') as mock_plot:
            plot_feys_function(self.test_points)
            args, _ = mock_plot.call_args
            # 修改这里，正确获取x和y值
            x_values, y_values = args[0], args[1]
            
            # 验证点数
            self.assertEqual(len(x_values), self.test_points)
            self.assertEqual(len(y_values), self.test_points)
            
            # 验证值是否有限
            self.assertTrue(np.all(np.isfinite(x_values)))
            self.assertTrue(np.all(np.isfinite(y_values)))

    def test_input_validation(self):
        """测试输入参数验证"""
        # 测试负数点数
        with self.assertRaises(ValueError):
            plot_deltoid(-100)
        
        # 测试零点数
        with self.assertRaises(ValueError):
            plot_galilean_spiral(0)
        
        # 测试非整数点数
        with self.assertRaises(TypeError):
            plot_feys_function(10.5)

if __name__ == '__main__':
    unittest.main()
