"""
数据清洗与预处理 - Titanic数据集
实现：缺失值处理、类型转换、重复删除
输出：清洗后的数据文件（位于 output/ 目录）
"""

import pandas as pd
import numpy as np
import os

# 获取当前脚本所在目录，并构建绝对路径
base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, 'data', 'train.csv')
output_dir = os.path.join(base_dir, 'output')
os.makedirs(output_dir, exist_ok=True)

# -------------------------- 1. 读取数据 --------------------------
df = pd.read_csv(data_path)
print("原始数据形状:", df.shape)
print("\n前5行预览:\n", df.head())

# -------------------------- 2. 缺失值处理 --------------------------
# 2.1 Age: 中位数填充
df['Age'].fillna(df['Age'].median(), inplace=True)

# 2.2 Embarked: 众数填充
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# 2.3 Cabin: 缺失率过高，直接删除
df.drop('Cabin', axis=1, inplace=True)

print("\n缺失值处理完成，剩余缺失值:\n", df.isnull().sum())

# -------------------------- 3. 数据类型转换 --------------------------
# 3.1 Sex: 编码为数值
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# 3.2 Age: 转为整数
df['Age'] = df['Age'].astype(int)

# 3.3 Embarked: 转为类别型
df['Embarked'] = df['Embarked'].astype('category')

# 3.4 可选：提取称呼（Title）作为新特征（示例）
df['Title'] = df['Name'].apply(lambda x: x.split(',')[1].split('.')[0].strip())
df['Title'] = df['Title'].map({'Mr': 0, 'Miss': 1, 'Mrs': 2, 'Master': 3, 'Dr': 4, 'Rev': 5, 'Col': 6, 'Major': 7, 'Mlle': 8, 'Countess': 9, 'Ms': 10, 'Lady': 11}).fillna(9).astype(int)

# -------------------------- 4. 重复记录处理 --------------------------
duplicates = df.duplicated().sum()
if duplicates > 0:
    df.drop_duplicates(inplace=True)
    print(f"删除 {duplicates} 条重复记录")

# -------------------------- 5. 保存清洗后数据 --------------------------
output_path = os.path.join(output_dir, 'titanic_cleaned.csv')
df.to_csv(output_path, index=False)
print("\n清洗后数据形状:", df.shape)
print("清洗后数据已保存至:", output_path)
print("\n清洗后数据描述:\n", df.describe(include='all'))