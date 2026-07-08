import numpy as np
import time
import math

print("==========练习1 矩阵运算性能对比==========")
A = np.random.rand(1000, 2000)
B = np.random.rand(2000, 3000)

start = time.time()
np.dot(A, B)
time_dot = time.time() - start

# @运算符计时
start = time.time()
A @ B
time_at = time.time() - start

# np.matmul计时
start = time.time()
np.matmul(A, B)
time_matmul = time.time() - start
print("【矩阵乘法耗时（单轮秒数）】")
print(f"np.dot(A,B):    {time_dot:.4f} s")
print(f"A @ B:          {time_at:.4f} s")
print(f"np.matmul(A,B): {time_matmul:.4f} s")

# C、F序数组测速
arr_c = np.random.rand(1000, 1000)
arr_f = np.array(arr_c, order="F")
start = time.time()
arr_c.sum(axis=1)
t_c_row = time.time() - start
start = time.time()
arr_f.sum(axis=1)
t_f_row = time.time() - start
start = time.time()
arr_c.sum(axis=0)
t_c_col = time.time() - start
start = time.time()
arr_f.sum(axis=0)
t_f_col = time.time() - start
print("\n【C/F序数组求和耗时（单轮秒数）】")
print(f"C序-按行求和：{t_c_row:.4f} s | C序-按列求和：{t_c_col:.4f} s")
print(f"F序-按行求和：{t_f_row:.4f} s | F序-按列求和：{t_f_col:.4f} s")

# 内存复用计算 A²+2A+1
A_small = np.random.rand(1000, 1000)
res = np.empty_like(A_small)
temp_2A = np.empty_like(A_small)
np.multiply(A_small, A_small, out=res)
np.multiply(2, A_small, out=temp_2A)
np.add(res, temp_2A, out=res)
np.add(res, 1, out=res)
res_normal = A_small ** 2 + 2 * A_small + 1
print("\n【内存复用计算校验】")
print("两种计算结果是否完全一致：", np.allclose(res, res_normal))

print("\n==========练习2 金融数据分析实战==========")

# 对数收益率
prices = np.array([100, 102, 105, 103, 107])
returns = np.log(prices[1:] / prices[:-1])
print("1. 每日对数收益率：\n", returns)

# 移动平均线
np.random.seed(42)
price_100 = np.random.normal(loc=100, scale=5, size=100)
def get_ma(price_arr, window):
    weight = np.ones(window) / window
    return np.convolve(price_arr, weight, mode="valid")
ma5 = get_ma(price_100, 5)
ma20 = get_ma(price_100, 20)
print(f"\n2. MA5数组长度：{len(ma5)} | MA20数组长度：{len(ma20)}")

# 风险分析
ret_data = np.random.normal(loc=0.0005, scale=0.015, size=(1000, 252))
daily_std = ret_data.std(axis=1, keepdims=True)
annual_vol = daily_std * math.sqrt(252)
corr_matrix = np.corrcoef(ret_data)
print("\n3. 前5只股票年化波动率：\n", annual_vol[:5].ravel())
print("股票相关系数矩阵尺寸：", corr_matrix.shape)
