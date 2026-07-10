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

# 1.5 loc推荐原因
print("推荐loc的原因：loc基于行列标签匹配，不受索引重排、数据删改影响；iloc仅依赖数字下标，索引错乱后会取错数据，业务场景loc稳定性与可读性更强。\n")

print("==================== 任务2：构造订单结算指标 ====================")
# 基于原表生成新表analysis，向量化新增结算字段
analysis = orders.assign(
    gross_amount = lambda x: x['quantity'] * x['unit_price'],
    member_discount = lambda x: np.where(x['member_level'] == '金卡', 0.10, np.where(x['member_level'] == '银卡', 0.05, 0.00)),
    payable_amount = lambda x: (x['gross_amount'] * (1 - x['member_discount']) * (1 - x['coupon_rate'])).round(2),
    shipping_fee = lambda x: np.where(x['payable_amount'] >= 1000, 0, 20),
    final_amount = lambda x: (x['payable_amount'] + x['shipping_fee']).round(2)
)
show_cols = ['order_id','gross_amount','member_discount','payable_amount','shipping_fee','final_amount']
print("结算指标前8行：")
print(analysis[show_cols].head(8))
print("解释：使用assign不修改原始数据，全部向量化运算，依次计算货值、会员折扣、优惠应付、运费、最终实付金额并保留两位小数。\n")

print("==================== 任务3：复杂条件筛选重点跟进订单 ====================")
# 定义3个独立布尔条件
cond1 = (analysis['region'] == '华东') | (analysis['region'] == '华南')
cond2 = analysis['final_amount'] >= 700
cond3 = (analysis['quantity'] >= 2) | (analysis['member_level'] == '金卡')
mask = cond1 & cond2 & cond3

# 筛选、指定列、金额降序
target_orders = analysis.loc[mask, ['order_id','region','product','quantity','member_level','final_amount']].sort_values('final_amount', ascending=False)
print("重点跟进订单：")
print(target_orders)
print("&、|两侧加括号原因：&、|优先级高于比较运算符，不加括号会优先执行位运算，逻辑判断失效；括号隔离每个独立条件保证逻辑正确。")
print("解释：筛选华东南、实付≥700、满足量大或金卡任一条件的高价值订单，按成交金额从高到低排序。\n")

print("==================== 任务4：封装订单等级函数 + pipe调用 ====================")
def add_order_level(df):
    df_copy = df.copy()
    df_copy['order_level'] = np.where(df_copy['final_amount'] >= 2000, '战略订单', np.where(df_copy['final_amount'] >= 1000, '重点订单', '普通订单'))
    return df_copy

leveled_orders = analysis.pipe(add_order_level)
level_count = leveled_orders['order_level'].value_counts()
print("各订单等级数量：")
print(level_count)
print("解释：函数内部拷贝数据不污染原入参，嵌套np.where完成三级分级，pipe链式调用后统计各类订单总量。\n")

print("==================== 任务5：单条方法链生成区域经营报表 ====================")
region_report = (
    analysis
    .pipe(add_order_level)
    .query("final_amount >= 500")
    .groupby(['region', 'order_level'], as_index=False)
    .agg(
        order_count=('order_id', 'count'),
        quantity_sum=('quantity', 'sum'),
        revenue_sum=('final_amount', 'sum'),
        revenue_mean=('final_amount', 'mean')
    )
    .sort_values('revenue_sum', ascending=False)
)
print("区域分层经营报表：")
print(region_report)
print("解释：全程无额外中间变量，链式完成分级、低金额过滤、地区+订单等级双层分组聚合，按总营收降序输出经营汇总。\n")

print("==================== 任务6：经营诊断分析 ====================")
# 6.1 找出成交金额最高销售
sales_total = leveled_orders.groupby('salesperson')['final_amount'].sum().reset_index()
top_sales = sales_total.loc[sales_total['final_amount'].idxmax()]
top_name = top_sales['salesperson']
top_total = round(top_sales['final_amount'], 2)

# 6.2 该销售金额最高地区
sales_region = leveled_orders[leveled_orders['salesperson'] == top_name].groupby('region')['final_amount'].sum().reset_index()
top_region = sales_region.loc[sales_region['final_amount'].idxmax()]
r_name = top_region['region']
r_amount = round(top_region['final_amount'], 2)

# 6.3 地区营收占比
ratio = round(r_amount / top_total * 100, 2)

# 输出诊断结果
print(f"销冠销售人员：{top_name}")
print(f"个人总成交金额：{top_total}")
print(f"核心贡献地区：{r_name}")
print(f"该地区成交金额：{r_amount}")
print(f"核心地区营收贡献率：{ratio}%")
print("业务结论：该销售人员业绩高度集中于单一核心区域，可持续深耕该区域市场，同时拓展其他区域降低业绩依赖风险。")
