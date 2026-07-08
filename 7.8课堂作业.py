import numpy as np
print("====================练习1：数组创建与形状操作====================")
arr = np.random.randint(0, 10, size=(3, 4))
print("原始(3,4)数组：")
print(arr)
reshaped_arr = arr.reshape(4, 3).T
print("\nreshape(4,3)后转置：")
print(reshaped_arr)
filtered_arr = arr[arr > 5]
print("\n大于5的元素数组：")
print(filtered_arr)

print("\n====================练习2：索引与切片====================")
arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("原数组：\n", arr2)
part_row2 = arr2[1, 0:3]
print("\n第2行1~3列：", part_row2)
col_all = arr2[:, 2]
print("全部行第3列：", col_all)
odd_line = arr2[::2, :]
print("\n奇数行：\n", odd_line)
print("\n用法对比：")
print("arr[:, 2] → 提取全部行的第3列，输出一维数组")
print("arr[::2, :] → 步长2取行，保留全部列，输出二维子数组")

print("\n====================练习3：矢量化运算与聚合函数====================")
A = np.random.randint(1, 10, size=(2, 3))
B = np.random.randint(1, 10, size=(2, 3))
elem_mult = A * B
mat_mult = A @ B.T
print("数组A：\n", A)
print("数组B：\n", B)
print("逐元素乘法 A*B：\n", elem_mult)
print("矩阵乘法 A@B.T：\n", mat_mult)

mat_sum = np.array([[1, 2], [3, 4]])
sum_col = np.sum(mat_sum, axis=0)
sum_row = np.sum(mat_sum, axis=1)
print("\n求和矩阵：\n", mat_sum)
print("列求和 axis=0：", sum_col)
print("行求和 axis=1：", sum_row)

num_list = np.array([1.2, 3.5, 2.8])
mean_res = np.mean(num_list)
std_res = np.std(num_list)
round_res = np.round(num_list)
print("\n数组[1.2, 3.5, 2.8]")
print("均值：", mean_res)
print("标准差：", std_res)
print("四舍五入结果：", round_res)

print("\n====================练习4：综合应用====================")
rand_float = np.random.rand(10)
min_r = rand_float.min()
max_r = rand_float.max()
norm = (rand_float - min_r) / (max_r - min_r) * 100
print("原始0~1随机浮点数组：\n", rand_float)
print("归一化0~100数组：\n", norm)

cumsum_out = np.cumsum(norm)
cummax_out = np.maximum.accumulate(norm)
print("\n累计和 cumsum：\n", cumsum_out)
print("累计最大值 cummax：\n", cummax_out)
