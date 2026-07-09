import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# ==================== 第1部分：NumPy数组基础操作 ====================
print("=" * 50)
print("第1部分：NumPy数组基础操作")
print("=" * 50)

arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.arange(1, 13).reshape(3, 4)
arr_3d = np.random.randint(0, 10, size=(2, 3, 4))

print("一维数组:", arr_1d)
print("二维数组:\n", arr_2d)
print("三维数组:\n", arr_3d)

print("\n--- 索引切片示例 ---")
print("二维数组第2行:", arr_2d[1])
print("第2行前3列:", arr_2d[1, :3])
print("所有行第2列:", arr_2d[:, 1])
print("三维数组第1个矩阵:\n", arr_3d[0])
print("三维数组第2层前2行后2列:\n", arr_3d[1, :2, -2:])

print("\n--- 形状变换 ---")
reshaped = arr_2d.reshape(2, 6)
transposed = arr_2d.T
flattened = arr_3d.flatten()
print("原始形状:", arr_2d.shape)
print("reshape(2,6):\n", reshaped)
print("转置:\n", transposed)
print("三维数组展平:", flattened)

print("\n--- 矩阵运算 ---")
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("加法:\n", A + B)
print("矩阵乘法:\n", A @ B)
print("逐元素乘:\n", A * B)

np.random.seed(77)
data = np.random.randn(1000)
print("\n--- 随机数据统计 ---")
print(f"均值: {data.mean():.4f}, 标准差: {data.std():.4f}")
print(f"最小值: {data.min():.4f}, 最大值: {data.max():.4f}")
print(f"中位数: {np.median(data):.4f}")
print(f"25%分位数: {np.percentile(data, 25):.4f}")
print(f"75%分位数: {np.percentile(data, 75):.4f}")

# ==================== 第2部分：金融数据分析实战 ====================
print("\n" + "=" * 50)
print("第2部分：金融数据分析实战 (模拟数据)")
print("=" * 50)

np.random.seed(999)
n_days = 252
n_stocks = 5
mu = 0.00042
sigma = 0.021
daily_returns = np.random.randn(n_days, n_stocks) * sigma + mu
price_paths = 100 * np.exp(np.cumsum(daily_returns, axis=0))

stock_colors = ["#2980b9","#e67e22","#27ae60","#c0392b","#8e44ad"]
plt.figure(figsize=(12, 5))
for i in range(n_stocks):
    plt.plot(price_paths[:, i], label=f'股票 {i+1}', c=stock_colors[i], lw=1.8)
plt.title('模拟股票价格走势（一年）', fontsize=16)
plt.xlabel('交易日', fontsize=13)
plt.ylabel('价格', fontsize=13)
plt.legend(fontsize=12)
plt.grid(alpha=0.35)
plt.tight_layout()
plt.show()

log_returns = np.diff(np.log(price_paths), axis=0)
annual_ret = log_returns.mean(axis=0) * 252
annual_vol = log_returns.std(axis=0) * np.sqrt(252)
print("股票年化收益率:", np.round(annual_ret, 4))
print("股票年化波动率:", np.round(annual_vol, 4))

price = price_paths[:, 0]
ma5 = np.convolve(price, np.ones(5)/5, mode='valid')
ma20 = np.convolve(price, np.ones(20)/20, mode='valid')

plt.figure(figsize=(12, 5))
plt.plot(price, label='价格', c="#3498db", alpha=0.75, lw=2)
plt.plot(np.arange(4, len(price)), ma5, label='5日移动平均', c="#f39c12", lw=2.2)
plt.plot(np.arange(19, len(price)), ma20, label='20日移动平均', c="#229954", lw=2.2)
plt.title('移动平均线（股票1）', fontsize=16)
plt.xlabel('交易日', fontsize=13)
plt.ylabel('价格', fontsize=13)
plt.legend(fontsize=12)
plt.grid(alpha=0.35)
plt.tight_layout()
plt.show()

simple_returns = np.diff(price_paths, axis=0) / price_paths[:-1]
cov_matrix = np.cov(simple_returns, rowvar=False)
corr_matrix = np.corrcoef(simple_returns, rowvar=False)

print("\n年化协方差矩阵 (×100):\n", np.round(cov_matrix * 252 * 100, 4))
print("\n相关系数矩阵:\n", np.round(corr_matrix, 4))

weights = np.ones(n_stocks) / n_stocks
port_var = weights @ cov_matrix @ weights * 252
port_vol = np.sqrt(port_var)
print(f"\n等权重投资组合年化波动率: {port_vol:.4f}")

plt.figure(figsize=(7, 6))
im = plt.imshow(cov_matrix, cmap='Blues', interpolation='none')
plt.colorbar(im, label='协方差')
plt.title('日收益率协方差矩阵', fontsize=15)
plt.xticks(range(n_stocks), [f'股票{i+1}' for i in range(n_stocks)], fontsize=11)
plt.yticks(range(n_stocks), [f'股票{i+1}' for i in range(n_stocks)], fontsize=11)
plt.tight_layout()
plt.show()
