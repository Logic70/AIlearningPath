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
#shape属性：
print("random_arr:",random_arr.shape,random_arr.dtype,random_arr)


#np.arange()参考range函数，即创造一个从X到Y的数列
arange_arr = np.arange(10)
print("arange_arr:",arange_arr.shape,arange_arr.dtype,arange_arr)

#numpy中的bool类型
bool_arr = np.array([1,0,1,0,0],dtype=bool)
print("bool_arr:",bool_arr.shape,bool_arr.dtype,bool_arr)

#调整数据类型
bool_arr_x = bool_arr.astype("int8")
print("bool_arr_x:",bool_arr_x.shape,bool_arr_x.dtype,bool_arr_x)
