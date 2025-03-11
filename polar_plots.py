import numpy as np
import matplotlib.pyplot as plt

def plot_deltoid(num_points=1000):
    """
    绘制三角洲曲线
    x = 2cos(θ) + cos(2θ)
    y = 2sin(θ) - sin(2θ)
    
    参数:
    num_points (int): 采样点数，默认1000
    """
    # TODO: 实现此函数
    pass

def plot_galilean_spiral(num_points=1000):
    """
    绘制伽利略螺旋
    r = θ²
    
    参数:
    num_points (int): 采样点数，默认1000
    """
    # TODO: 实现此函数
    pass

def plot_feys_function(num_points=2000):
    """
    绘制Fey's函数
    r = exp(cos(θ)) - 2cos(4θ) + sin⁵(θ/12)
    
    参数:
    num_points (int): 采样点数，默认2000
    """
    # TODO: 实现此函数
    pass

def save_plots():
    """
    生成并保存所有图形
    """
    # 设置图形大小和DPI
    plt.figure(figsize=(10, 8), dpi=100)
    
    # 绘制并保存三角洲曲线
    plot_deltoid()
    plt.savefig('deltoid.png')
    plt.close()
    
    # 绘制并保存伽利略螺旋
    plot_galilean_spiral()
    plt.savefig('galilean_spiral.png')
    plt.close()
    
    # 绘制并保存Fey's函数
    plot_feys_function()
    plt.savefig('feys_function.png')
    plt.close()

if __name__ == "__main__":
    save_plots()
