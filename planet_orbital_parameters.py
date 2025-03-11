import numpy as np
from scipy.constants import G, year

# 行星半长轴数据（单位：m）
a = np.array([57.9e9, 108.21e9, 149.60e9, 227.92e9, 778.57e9, 1433.53e9, 2872.46e9, 4495.06e9])
# 行星质量数据（单位：kg）
m = 1e24 * np.array([0.33011, 4.8675, 5.9723, 0.64171, 1898.19, 568.34, 86.813, 102.413])
# 太阳质量（单位：kg）
M = 1.989e30
# 行星名称
planet_names = ['水星', '金星', '地球', '火星', '木星', '土星', '天王星', '海王星']


def calculate_orbital_parameters():
    """
    计算行星的轨道周期和轨道速度，并将结果整理成字典。

    返回:
        dict: 一个字典，键为行星名称，值为一个包含轨道周期（年）和轨道速度（km/s）的元组。
    """
    # TODO: 计算轨道周期（单位：s）
    P = None
    # TODO: 将轨道周期转换为年
    P_yr = None
    # TODO: 计算轨道速度（单位：m/s）
    v = None
    # TODO: 将轨道速度转换为 km/s
    v_km_s = None

    result = {}
    for i in range(len(planet_names)):
        result[planet_names[i]] = (P_yr[i], v_km_s[i])

    return result
if __name__ == "__main__":
    # 获取计算结果
    results = calculate_orbital_parameters()
    
