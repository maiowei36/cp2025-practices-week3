import numpy as np

def find_power_with_six():
    """
    找出所有满足条件的i值(0<i<100)，使得2^i的最后一位数字是6
    
    返回:
    numpy.ndarray: 包含所有满足条件的i值的数组
    """
    # TODO: 实现此函数
    return np.arange(4,100,4)  #由于所有满足条件的i值都是4的倍数，所以直接在100范围内以4为步长就找到满足条件的i值
print(fimd_power_with_six())

def first_ten_powers():
    """
    计算2的前10次幂
    
    返回:
    numpy.ndarray: 包含2的0次幂到9次幂的数组
    """
    # TODO: 实现此函数
    return np.array([2**i for i in range(10)])  #计算2的0到10次幂，返回为数组
print(first_ten_powers())
    
    
def create_frame_matrix():
    """
    创建一个10x10的框架矩阵，边框为1，内部为0
    
    返回:
    numpy.ndarray: 10x10的框架矩阵
    """
    # TODO: 实现此函数
    a=np.ones((10,10))  #创建一个元素都为1的10*10矩阵
    a[1:-1,1:-1]=np.zeros((8,8))  #将该矩阵除边框外的元素替换为0
    return a
print(create_frame_matrix())

def create_number_matrix():
    """
    创建一个10x10的数字矩阵，边框为-1，内部为0-39的数字
    
    返回:
    numpy.ndarray: 10x10的数字矩阵
    """
    # TODO: 实现此函数
    a=np.zeros((10,10))-1  #创建元素都为-1的10*10矩阵
    a[1:-1, 1:-1] = np.random.randint(0, 40, size=(8, 8))  #将边框内的元素替换为0到40间的随机数
    #a[3:8,1:-1]=np.arange(40).reshape(5,8)  #将矩阵能的5*8矩阵替换为0到40的数
    return a
print(create_number_matrix())

def create_multiplication_matrix():
    """
    创建一个3×5的矩阵，其中A[i,j] = i × j
    要求使用数组广播实现
    
    返回:
    numpy.ndarray: 3×5的矩阵
    """
    # TODO: 实现此函数
    i=np.arange(3)[:,np.newaxis]  #行索引（3，1）
    j=np.arange(5)[np.newaxis,:]  #列索引（1，5）
    A=np.multiply(i,j)  #广播乘法
    return A
print(create_multiplication_matrix())

def create_special_matrix():
    """
    创建一个特殊的11×11矩阵，其中每个元素都是1
    对角线上的元素为[5,4,3,2,1,0,1,2,3,4,5]
    要求使用数组广播实现
    
    返回:
    numpy.ndarray: 11×11的矩阵
    """
    # TODO: 实现此函数
    a=np.arange(11)[:,np.newaxis]  #行索引（11，1）
    b=np.arange(11)[np.newaxis,:]  #列索引（1，11）
    return np.where(a==b,np.abs(a-5),1)  #将对角线元素替换为i-5的绝对值，其他元素为1
print(create_special_matrix())
