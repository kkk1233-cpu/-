"""
空气质量数据分析与可视化 - Beijing PM2.5
实现：时间序列处理、缺失插值、统计指标、相关性、季节性可视化
输出：图表保存至 output/air_quality_plots/ 目录
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 设置路径
base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, 'data', 'PRSA_data_2010.1.1-2014.12.31.csv')
plot_dir = os.path.join(base_dir, 'output', 'air_quality_plots')
os.makedirs(plot_dir, exist_ok=True)

# 设置中文字体（如需显示中文，请取消注释并设置字体）
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False

# -------------------------- 1. 读取数据与日期处理 --------------------------
df = pd.read_csv(data_path)
df['datetime'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])
df.set_index('datetime', inplace=True)
print("数据形状:", df.shape)
print("\n前5行:\n", df.head())

# -------------------------- 2. 缺失值处理（线性插值） --------------------------
print("\n插值前缺失值统计:\n", df.isnull().sum())
df['pm2.5'] = df['pm2.5'].interpolate(method='linear', limit_direction='both')
print("插值后pm2.5缺失值:", df['pm2.5'].isnull().sum())

# -------------------------- 3. 统计指标与相关性 --------------------------
num_cols = ['pm2.5', 'DEWP', 'TEMP', 'PRES', 'Iws', 'Is', 'Ir']
stats = df[num_cols].describe()
print("\n数值列统计描述:\n", stats)

corr = df[num_cols].corr()
print("\n相关性矩阵:\n", corr)

# 热力图
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('空气质量指标相关性热力图')
plt.tight_layout()
plt.savefig(os.path.join(plot_dir, 'correlation_heatmap.png'), dpi=150)
plt.close()

# -------------------------- 4. 时间序列聚合与季节性分析 --------------------------
# 添加时间维度
df['year'] = df.index.year
df['month'] = df.index.month
df['quarter'] = df.index.quarter

# 聚合
monthly_mean = df.groupby('month')['pm2.5'].mean()
quarterly_mean = df.groupby('quarter')['pm2.5'].mean()
yearly_mean = df.groupby('year')['pm2.5'].mean()

print("\n月度平均PM2.5:\n", monthly_mean)
print("\n季度平均PM2.5:\n", quarterly_mean)
print("\n年度平均PM2.5:\n", yearly_mean)

# -------------------------- 5. 可视化 --------------------------
# 5.1 月度变化折线图
plt.figure(figsize=(10,4))
monthly_mean.plot(kind='line', marker='o')
plt.title('PM2.5月度平均变化')
plt.xlabel('月份')
plt.ylabel('PM2.5浓度 (μg/m³)')
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(plot_dir, 'monthly_trend.png'), dpi=150)
plt.close()

# 5.2 年度变化柱状图
plt.figure(figsize=(8,4))
yearly_mean.plot(kind='bar')
plt.title('PM2.5年度平均变化')
plt.xlabel('年份')
plt.ylabel('PM2.5浓度')
plt.tight_layout()
plt.savefig(os.path.join(plot_dir, 'yearly_trend.png'), dpi=150)
plt.close()

# 5.3 温度与PM2.5散点图
plt.figure(figsize=(8,6))
plt.scatter(df['TEMP'], df['pm2.5'], alpha=0.3, s=1)
plt.xlabel('温度 (℃)')
plt.ylabel('PM2.5浓度')
plt.title('温度与PM2.5散点关系')
plt.tight_layout()
plt.savefig(os.path.join(plot_dir, 'temp_scatter.png'), dpi=150)
plt.close()

# 5.4 季度箱线图
plt.figure(figsize=(8,6))
sns.boxplot(x='quarter', y='pm2.5', data=df)
plt.title('不同季度PM2.5分布')
plt.xlabel('季度')
plt.ylabel('PM2.5浓度')
plt.tight_layout()
plt.savefig(os.path.join(plot_dir, 'quarterly_boxplot.png'), dpi=150)
plt.close()

print("\n所有图表已保存至:", plot_dir)