import unittest
from unittest.mock import patch
import numpy as np
import matplotlib.pyplot as plt
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from celestial_coordinate_conversion import celestial_coordinate_transformation

class TestCelestialCoordinateTransformation(unittest.TestCase):
    def setUp(self):
        # 设置测试用的天体坐标数据
        self.test_ra = np.array([0.0, 90.0, 180.0, 270.0, 360.0])
        self.test_dec = np.array([-30.0, 0.0, 30.0, 60.0, 90.0])
        
        # 设置测试用的观测时间
        self.test_times = Time(['2024-01-01 00:00:00', '2024-01-01 12:00:00', 
                              '2024-01-02 00:00:00'], scale='utc')
        
        # 设置测试用的观测地点
        self.test_lat = 53.48
        self.test_lon = 10.0

    @patch('matplotlib.pyplot.show')
    def test_function_execution(self, mock_show):
        """测试函数是否能够正常执行"""
        celestial_coordinate_transformation()
        mock_show.assert_called_once()

    @patch('matplotlib.pyplot.figure')
    @patch('matplotlib.pyplot.show')
    def test_plot_creation(self, mock_show, mock_figure):
        """测试是否创建了正确大小的图表"""
        celestial_coordinate_transformation()
        mock_figure.assert_called_with(figsize=(10, 6))

    def test_coordinate_conversion(self):
        """测试坐标转换的正确性"""
        # 创建测试用的天体坐标
        coords = SkyCoord(ra=self.test_ra, dec=self.test_dec, unit='deg')
        
        # 创建观测地点
        location = EarthLocation(lat=self.test_lat*u.deg, lon=self.test_lon*u.deg)
        
        # 计算期望的地平坐标
        altaz_frame = AltAz(obstime=self.test_times[0], location=location)
        expected_altaz = coords.transform_to(altaz_frame)
        
        # 验证转换后的坐标是否在合理范围内
        self.assertTrue(all(expected_altaz.az.deg >= 0))
        self.assertTrue(all(expected_altaz.az.deg <= 360))
        self.assertTrue(all(expected_altaz.alt.deg >= -90))
        self.assertTrue(all(expected_altaz.alt.deg <= 90))

    def test_input_validation(self):
        """测试输入数据的有效性"""
        # 验证赤经范围
        self.assertTrue(all(self.test_ra >= 0))
        self.assertTrue(all(self.test_ra <= 360))
        
        # 验证赤纬范围
        self.assertTrue(all(self.test_dec >= -90))
        self.assertTrue(all(self.test_dec <= 90))
        
        # 验证观测地点的有效性
        self.assertTrue(-90 <= self.test_lat <= 90)
        self.assertTrue(-180 <= self.test_lon <= 180)

if __name__ == '__main__':
    unittest.main()
