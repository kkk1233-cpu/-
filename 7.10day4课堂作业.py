import numpy as np
import pandas as pd

# 全局设置浮点数保留两位小数、显示全部列
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: f'{x:.2f}')

# 原始订单数据
orders = pd.DataFrame({
    'order_id': [f'O{number}' for number in range(1001, 1019)],
    'region': ['华东','华北','华南','华东','西南','华北','华南','华东','西南','华北','华东','华南','西南','华东','华北','华南','华东','西南'],
    'product': ['机械键盘','无线鼠标','显示器','扩展坞','机械键盘','显示器','无线鼠标','显示器','扩展坞','机械键盘','无线鼠标','扩展坞','显示器','机械键盘','扩展坞','显示器','无线鼠标','机械键盘'],
    'category': ['外设','外设','显示设备','配件','外设','显示设备','外设','显示设备','配件','外设','外设','配件','显示设备','外设','配件','显示设备','外设','外设'],
    'quantity': [2,3,1,4,5,2,6,1,3,2,8,2,1,3,5,2,4,6],
    'unit_price': [289,129,1299,399,289,1299,129,1299,399,289,129,399,1299,289,399,1299,129,289],
    'member_level': ['金卡','普通','银卡','金卡','银卡','普通','金卡','银卡','普通','金卡','银卡','金卡','普通','银卡','金卡','金卡','普通','银卡'],
    'coupon_rate': [0.05,0.00,0.08,0.10,0.05,0.00,0.12,0.05,0.00,0.08,0.10,0.05,0.00,0.12,0.05,0.08,0.00,0.10],
    'salesperson': ['小林','小周','小陈','小林','小赵','小周','小陈','小林','小赵','小周','小林','小陈','小赵','小林','小周','小陈','小林','小赵']
})

print("==================== 任务1：快速理解数据 ====================")
# 1.1 输出行数、列数、所有列名
row_cnt, col_cnt = orders.shape
print(f"数据行数：{row_cnt}，列数：{col_cnt}")
print("所有列名：", orders.columns.tolist())
print("解释：数据集共18条订单、9个字段，涵盖订单、地区、商品、价格、会员、销售等维度。\n")

# 1.2 单列、多列选取并打印类型
single_col = orders['region']
multi_cols = orders[['order_id','product','quantity']]
print("region单列类型：", type(single_col))
print("三列组合类型：", type(multi_cols))
print("解释：单列取出为Series一维序列，多列选取为DataFrame二维表格。\n")

# 1.3 iloc取第4～8行、前4列（索引3:8，左闭右开）
iloc_slice = orders.iloc[3:8, 0:4]
print("iloc切片结果：")
print(iloc_slice)
print("解释：iloc按数字下标定位，提取索引3至7共5行、前4个基础字段。\n")

# 1.4 loc筛选华东订单，指定三列展示
east_df = orders.loc[orders['region'] == '华东', ['order_id','product','member_level']]
print("华东订单loc筛选结果：")
print(east_df)
print("解释：loc通过布尔条件筛选地区，仅展示指定的订单ID、商品、会员等级三列。\n")
