import unittest
import numpy as np
from scipy.constants import G, year
from planet_orbital_parameters import calculate_orbital_parameters

# 行星半长轴数据（单位：m）
a = np.array([57.9e9, 108.21e9, 149.60e9, 227.92e9, 778.57e9, 1433.53e9, 2872.46e9, 4495.06e9])
# 行星质量数据（单位：kg）
m = 1e24 * np.array([0.33011, 4.8675, 5.9723, 0.64171, 1898.19, 568.34, 86.813, 102.413])
# 太阳质量（单位：kg）
M = 1.989e30
# 行星名称
planet_names = ['水星', '金星', '地球', '火星', '木星', '土星', '天王星', '海王星']


class TestPlanetOrbitalParameters(unittest.TestCase):
    def test_calculate_orbital_parameters(self):
        result = calculate_orbital_parameters()
        self.assertEqual(len(result), len(planet_names))

        for planet in planet_names:
            P_yr, v_km_s = result[planet]
            # 手动计算预期结果
            P_expected = 2 * np.pi * np.sqrt(a[planet_names.index(planet)] ** 3 / (G * (M + m[planet_names.index(planet)])))
            P_yr_expected = P_expected / year
            v_expected = 2 * np.pi * a[planet_names.index(planet)] / P_expected
            v_km_s_expected = v_expected / 1000

            # 检查计算结果是否在合理误差范围内
            self.assertTrue(np.isclose(P_yr, P_yr_expected, rtol=1e-3))
            self.assertTrue(np.isclose(v_km_s, v_km_s_expected, rtol=1e-3))


if __name__ == '__main__':
    unittest.main()
