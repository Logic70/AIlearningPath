#coding=utf-8

import numpy as np

#np.array()创建数组
a1 = np.array([1,2,3])
m1 = np.array([[1,2],[3,4]])#这里注意，array的入参就一个，即使是多维数组，外面也要加一层[]
print(type(a1))
print("a1:",a1.shape,a1)
print("m1:",m1.shape,m1)



#np.zeros() / np.ones() 创建全0或全1数组

zeros_arr = np.zeros((3, 2))  # 3行2列全0数组
ones_arr = np.ones(5)         # 一维全1数组（长度5）
print("zeros_arr:",zeros_arr.shape,zeros_arr)
print("ones_arr:",ones_arr.shape,ones_arr)




#np.random.rand() 生成均匀分布的随机数组（范围[0,1)）
random_arr = np.random.rand(2, 3)  # 2行3列随机数组
#dtpye属性：数组中的数据类型
#shape属性：一个元组，x个元素就是x维数组，具体的值代表维度的某个维度的长度
print("random_arr:",random_arr.shape,random_arr.dtype,random_arr)
reshape_arr = random_arr.reshape(6,)#reshape函数可以改变数组的shape
print("reshape_arr:",reshape_arr.shape,reshape_arr.dtype,reshape_arr)



#np.arange()参考range函数，即创造一个从X到Y的数列
arange_arr = np.arange(10)
print("arange_arr:",arange_arr.shape,arange_arr.dtype,arange_arr)

#numpy中的bool类型
bool_arr = np.array([1,0,1,0,0],dtype=bool)
print("bool_arr:",bool_arr.shape,bool_arr.dtype,bool_arr)

#调整数据类型
bool_arr_x = bool_arr.astype("int8")
print("bool_arr_x:",bool_arr_x.shape,bool_arr_x.dtype,bool_arr_x)

#数组的计算
#数组与整数的计算，即数组中的每个元素与整数的计算
arange_arr_0 = arange_arr + 2
print("arange_arr + 2 = ",arange_arr_0)
arange_arr_1 = arange_arr * 2
print("arange_arr * 2 = ",arange_arr_1)
arange_arr_2 = arange_arr/2
print("arange_arr / 2 = ",arange_arr_2)
arange_arr_3 = arange_arr/0
print("arange_arr / 0 = ",arange_arr_3)
'''[nan inf inf inf inf inf inf inf inf inf] nan代表非数组，inf代表无穷'''
arange_arr_4 = arange_arr ** 3
print("arange_arr ** 3 = ",arange_arr_4)


#数组与数组的计算
#当数组与数组的shape相同时，同个位置的元素和同个位置的元素进行计算
a_2 = np.arange(0,12).reshape(3,4)
a_3 = np.arange(12,24).reshape(3,4)
a_1 = a_3 - a_2
a_5 = a_2 + a_3
a_6 = a_2 * a_3
print(
    "a_2 = ",a_2,"\n",
    "a_3 = ", a_3, "\n",
    "a_3 - a_2 = ", a_1, "\n",
    "a_3 + a_2 = ",a_5,"\n",
    "a_3 * a_2 = ", a_6, "\n",

)
#当数组与数组的shape不同时:加、减、数乘遵循如下规律
'''
1.对齐维度：首先从后往前（即从最右侧）比较两个数组的各个维度大小。这意味着如果两个数组的维度数不同，较小数组的形状会在其左侧补1，以匹配较大数组的维度数。
尺寸
2.兼容性检查：如果两个数组在某个维度上的大小相同，或者其中一个数组在该维度的大小为1，则这两个数组在该维度上是兼容的。
如果上述条件都不满足，即两个数组在某个维度上的大小既不相等也不包含1，则会抛出异常，表示无法广播。
'''
b_1 = np.arange(4).reshape(4,)
m_1 = a_2 + b_1
m_2 = a_2 - b_1
m_3 = a_2 * b_1
print(
    "a_2 = ", a_2, "\n",
    "b_1 = ",b_1,"\n",
    "a_2 + b_1 = ",m_1,"\n",
    "a_2 - b_1 = ", m_2, "\n",
    "a_2 * b_1 = ", m_3, "\n",
    )

#点积，也就是@，要求前列后行匹配，且不满足交换律
b_2 = np.arange(28).reshape(4,7)
print(
    "b_2 = ",b_2,"\n"
    "dot3 = ", np.dot(a_2,b_2),"\n",
    "dot4 = ",  a_2 @ b_2 , "\n"
)

#转置，行列角标互换

b_3 = b_2.T
print("b_2.T = ",b_3,"\n")


#统计计算
sum_1 = np.sum(b_2)#求和
mean_1 = np.mean(b_2)#求均值
std_1 = np.std(b_2)#标准差
min_1 = np.min(b_2)#最小值
max_1 = np.max(b_2)#最大值
print(
    "求和：",sum_1,"\n",
    "均值：", mean_1, "\n",
    "标准差：", std_1, "\n",
    "最大值：", max_1, "\n",
    "最小值：", min_1, "\n",

)
#分割,这里具体的数字均是三维空间中的角标

matrix = np.random.randint(0,10,size=(10,10,3),dtype="int8")
x_0 = matrix[0,:,:]#指代x=0的平面，也就是y和z组成的二维矩阵
x_1 = matrix[1,:,:]
y_5 = matrix[:,5,:]
x_2_y_3 = matrix[2,3,:]#x=2 和 y=3交织的线，也就是z轴下的线

print(
    "matrix = ",matrix,"\n",
    "x_0 = ",x_0,"\n",
    "x_1 = ",x_1,"\n",
    "y_5 = ", y_5, "\n",
    "x_2_y_3 = ", x_2_y_3, "\n",

)


#clip函数：np.clip(a, a_min, a_max) 会将数组 a 中的每个元素限制在 a_min 和 a_max 之间。如果某个元素小于 a_min，则将其设置为 a_min；如果某个元素大于 a_max，则将其设置为 a_max。

matrix[:,:,0] = np.clip(matrix[:,:,0] + 100,0,15)
print(matrix[:,:,0])






