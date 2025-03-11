# 项目名称：
极坐标绘图项目

## 项目描述
本项目旨在通过绘制不同类型的曲线，帮助你掌握参数方程和极坐标绘图的技巧，加深对 NumPy 和 Matplotlib 的理解。

## 理论背景

### 1. 三角洲曲线
由参数方程定义：

  $$
 \begin{align*}
 x &= 2 \cos \theta + \cos 2\theta \\\\
 y &= 2 \sin \theta - \sin 2\theta
 \end{align*}
 $$ 

其中 $0 \leq \theta < 2\pi$.

### 2. 伽利略螺旋：
$r = \theta^2$，范围： $0 \leq \theta \leq 10\pi$
### 3. Fey's函数：
$r = e^{\cos\theta} - 2 \cos 4\theta + \sin^5 \frac{\theta}{12}$，范围： $0 \leq \theta \leq 24\pi$

**极坐标转换**：极坐标到笛卡尔坐标的转换：

 $$
 \begin{align*}
 &x = r\cos\theta \\\\
&y = r\sin\theta
 \end{align*}
 $$ 


## 项目要求

### 1. 基本功能实现
实现 `polar_plots.py` 文件中的以下函数：

1. `plot_deltoid(num_points=1000)`: 绘制三角洲曲线
2. `plot_galilean_spiral(num_points=1000)`: 绘制伽利略螺旋
3. `plot_feys_function(num_points=2000)`: 绘制Fey's函数

### 2. 具体要求
- 使用 NumPy 进行数值计算
- 使用 Matplotlib 进行绘图
- 每个图形都需要：
  - 适当的标题
  - 坐标轴标签
  - 合适的显示范围
  - 网格线（可选）
- 确保图形清晰美观

### 3. 输出要求
- 生成三个独立的图形
- 保存图形为PNG格式
- 合适的分辨率和大小

## 提示
1. 使用 `np.linspace()` 生成均匀分布的角度值
2. 注意参数方程中的三角函数计算
3. 使用 `plt.figure()` 创建新的图形窗口
4. 适当调整 `num_points` 以获得更平滑的曲线

## 评分标准
- 代码正确性（曲线计算准确）：40%
- 图形展示效果：30%
- 代码实现质量：20%
- 代码风格：10%
