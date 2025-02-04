#coding=utf-8

import numpy as np

def Answer_1():
    '''
    任务：
    创建两个 2x3 的矩阵 A 和 B，分别用随机整数填充（范围 1-10），计算它们的和 C 与差 D。
    要求：
    使用 np.random.randint 生成矩阵
    输出结果时保留矩阵格式（避免展平）
    '''
    a = np.random.randint(1,11,size=(2,3))
    b = np.random.randint(1,11,size=(2,3))

    print(
        "a = ",a,"\n",
        "b = ",b,"\n",
        "c = ",a+b,"\n",
        "d = ",a-b,"\n"
        )
#Answer_1()

def Answer_2():
    '''
    计算以下结果：

    A 和 B 的点积

    A 的转置与 B 的点积

    B 的转置与 A 的点积

    验证：是否满足 （a @ b）T = bT @ aT

    '''
    a = np.array([[1,2],[3,4]])
    b = np.array([[5,6],[7,8]])

    x = a@b
    m1 = a.T@b
    m2 = b.T@a
    a1 = x.T
    b1 = b.T@a.T


    print(
        "a @ b = ",x,"\n",
        "a.T @ b = ",m1,"\n",
        "b.T @ a = ",m2,"\n",
        "(a@b)T = ",a1,"\n",
        "bT@aT = ",b1,"\n"
        )
    if np.allclose(a1,b1):
        print("验证成功，（a @ b）T = bT @ aT")
        return True

#Answer_2()

def Answer_3():
    '''
    任务：
    创建两个数组：

    arr1：形状 (3, 4) 的随机矩阵（范围 0-1）

    arr2：一维数组 [0.1, 0.2, 0.3, 0.4]

    实现以下操作：

    对 arr1 的每一行进行归一化（减去该行最小值，再除以该行最大值）题目描述的“归一化”实际是 Min-Max归一化，目的是将数据缩放到 [0,1] 区间
    归一化值 = （当前值 - 最小值）/（最大值-最小值）

    将 arr2 广播到与 arr1 相同形状后相加
    '''
    arr1 = np.random.rand(3,4)
    print(arr1)
    arr2 = np.array([0.1, 0.2, 0.3, 0.4])

    row_min = arr1.min(axis=1,keepdims=True)
    '''
    【关于axis】
    在Numpy中，axis参数的方向定义是关键：
    axis=0：纵向操作（沿行方向，跨行计算）  
    axis=1：横向操作（沿列方向，跨列计算）
    对于形状为 (3,4) 的矩阵 arr1，每行有4个元素。
    当执行 arr1.min(axis=1) 时，表示对每一行内的所有列元素求最小值，最终得到一个形状为 (3,) 的数组，包含每行的最小值。
    【关于keepdims】
    默认情况下，使用 min()、max() 等聚合函数会压缩维度，例如将形状 (3,4) 压缩为 (3,)。
    添加 keepdims=True 后，结果会保持原数组的维度结构，从 (3,) 变为 (3,1)，便于后续广播操作。
    '''
    row_max = arr1.max(axis=1,keepdims=True)


    normalized = (arr1 - row_min )/ (row_max - row_min)

    arr3 = normalized + arr2

    print(
        "arr1 = ",normalized,"\n",
        "arr2 = ",arr2,"\n",
        "arr3 = ",arr3,"\n"

        )
#Answer_3()

def Answer_4():
    '''
    任务（图像数据处理）：
    假设一个 RGB 图像用三维数组表示，形状为 (高度, 宽度, 3)，其中最后一个维度是红、绿、蓝通道。
    创建一个 256x256 的随机图像（值范围 0-255，数据类型 uint8）
    将所有红色通道的值增加 50（注意溢出问题，最大值保持 255）
    计算图像各通道的均值
    '''

    #创建随机图形
    pic = np.random.randint(0,256,size=(256,256,3),dtype="uint8")

    #增加红色通道值
    pic[:, :, 0] = np.clip(pic[:,:,0] + 50,0,256)

    mean_values = pic.mean(axis=(0, 1))  # 沿高度和宽度计算均值
    print("各通道均值（R, G, B）：", mean_values)

Answer_4()

    

    

