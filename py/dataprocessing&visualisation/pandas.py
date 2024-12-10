#series
import pandas as pd

# 创建Series
# (1) 从列表创建
ser = pd.Series([10, 20, 30, 40])
print("Series from list:\n", ser)

# (2) 自定义索引
ser_with_index = pd.Series([10, 20, 30], index=['a', 'b', 'c'], name="MySeries")
print("\nSeries with custom index:\n", ser_with_index)

# (3) 从字典创建
data_dict = {'a': 10, 'b': 20, 'c': 30}
ser_from_dict = pd.Series(data_dict)
print("\nSeries from dictionary:\n", ser_from_dict)

# (4) 从标量创建
scalar_series = pd.Series(5, index=['x', 'y', 'z'])
print("\nSeries from scalar:\n", scalar_series)

# Series 运算
ser_a = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
ser_b = pd.Series([4, 5, 6], index=['a', 'b', 'd'])
# 自动对齐索引进行运算
print("\nAddition of two Series:\n", ser_a + ser_b)

# dataframe
# 创建DataFrame
# (1) 从字典创建
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print("\nDataFrame from dictionary:\n", df)

# (2) 自定义行索引
df_with_index = pd.DataFrame(data, index=['ID1', 'ID2', 'ID3'])
print("\nDataFrame with custom index:\n", df_with_index)

# (3) 从列表创建
df_from_list = pd.DataFrame([[1, 'A'], [2, 'B'], [3, 'C']], columns=['Number', 'Letter'])
print("\nDataFrame from list:\n", df_from_list)

# (4) 从字典的列表创建
dict_list = {
    'Product': ['Apple', 'Banana', 'Orange'],
    'Price': [10, 15, 20]
}
df_from_dict_list = pd.DataFrame(dict_list)
print("\nDataFrame from dictionary of lists:\n", df_from_dict_list)

# DataFrame 运算
# 数值列的算术运算
df_calc = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print("\nElement-wise addition:\n", df_calc['A'] + df_calc['B'])

# 按列操作
df_calc['C'] = df_calc['A'] * 2
print("\nNew column added:\n", df_calc)

print("Head of DataFrame:\n", df.head())  # 显示前5行
print("Tail of DataFrame:\n", df.tail())  # 显示后5行
print("Summary info of DataFrame:")
df.info()  # 显示列信息
print("Describe DataFrame:\n", df.describe())  # 显示数值列统计信息

# 按列选择
print("\nSelect a single column:\n", df['Name'])
print("\nSelect multiple columns:\n", df[['Name', 'Age']])

# 按行选择
print("\nSelect rows by index position (iloc):\n", df.iloc[0:2])  # 前两行
print("\nSelect rows by index label (loc):\n", df_with_index.loc['ID1':'ID2'])  # 按索引范围

# 条件选择
print("\nRows where Age > 25:\n", df[df['Age'] > 25])


# 修改单元格
df.loc[0, 'Age'] = 26
print("\nModified DataFrame:\n", df)

# 添加新列
df['Salary'] = [50000, 60000, 70000]
print("\nDataFrame with new column:\n", df)

# 删除列
df = df.drop('Salary', axis=1)
print("\nDataFrame after dropping column:\n", df)

# 删除行
df = df.drop(1, axis=0)
print("\nDataFrame after dropping row:\n", df)

# 检查缺失值
print("\nCheck for missing values:\n", df.isnull())

# 填充缺失值
df['Age'] = df['Age'].fillna(30)

# 删除缺失值
df = df.dropna()

# 修改列数据类型
df['Age'] = df['Age'].astype(float)

# 分组并聚合
grouped = df.groupby('City').mean()  # 按城市分组，计算每组的均值
print("\nGrouped and aggregated DataFrame:\n", grouped)

# file
# 读取 CSV 文件
df_csv = pd.read_csv('example.csv')  # 文件路径
print("\nDataFrame from CSV file:\n", df_csv)

# 读取 Excel 文件
df_excel = pd.read_excel('example.xlsx', sheet_name='Sheet1')
print("\nDataFrame from Excel file:\n", df_excel)

# 读取 JSON 文件
df_json = pd.read_json('example.json')
print("\nDataFrame from JSON file:\n", df_json)

# 读取 SQL 数据库
import sqlite3
conn = sqlite3.connect('example.db')
df_sql = pd.read_sql_query("SELECT * FROM table_name", conn)
print("\nDataFrame from SQL database:\n", df_sql)

# 写入 CSV 文件
df.to_csv('output.csv', index=False)

# 写入 Excel 文件
df.to_excel('output.xlsx', index=False, sheet_name='Sheet1')

# 写入 JSON 文件
df.to_json('output.json', orient='records', lines=True)

# 写入 SQL 数据库
df.to_sql('table_name', conn, if_exists='replace', index=False)


#data manipulation
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 27, 22, 32],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# 选择单列
print("\nSelect single column:\n", df["Name"])

# 选择多列
print("\nSelect multiple columns:\n", df[["Name", "City"]])

# 按行索引号选择（iloc）
print("\nSelect first two rows:\n", df.iloc[:2])

# 按行标签选择（loc）
df.index = ["A", "B", "C", "D"]
print("\nSelect rows by index label:\n", df.loc[["A", "C"]])

# 根据条件过滤
filtered = df[df["Age"] > 25]
print("\nRows where Age > 25:\n", filtered)

# 多条件过滤
filtered = df[(df["Age"] > 25) & (df["City"] == "Los Angeles")]
print("\nRows where Age > 25 and City == 'Los Angeles':\n", filtered)

# 修改单个值
df.loc["A", "Age"] = 30
print("\nDataFrame after modifying a value:\n", df)

# 添加新列
df["Salary"] = [50000, 60000, 55000, 70000]
print("\nDataFrame after adding a new column:\n", df)

# 修改列的值
df["Age"] += 1
print("\nDataFrame after modifying 'Age' column:\n", df)

# 删除列
df = df.drop("Salary", axis=1)
print("\nDataFrame after dropping column 'Salary':\n", df)

# 删除行
df = df.drop("B", axis=0)
print("\nDataFrame after dropping row 'B':\n", df)


#merge
data = {
    "Department": ["HR", "HR", "IT", "IT", "Finance", "Finance"],
    "Employee": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"],
    "Salary": [50000, 60000, 75000, 80000, 65000, 70000]
}
df_group = pd.DataFrame(data)

# 按部门分组，计算每个部门的平均工资
grouped = df_group.groupby("Department")["Salary"].mean()
print("\nAverage Salary by Department:\n", grouped)

# 按部门分组，计算每个部门的总工资和员工人数
grouped = df_group.groupby("Department").agg({"Salary": "sum", "Employee": "count"})
grouped = grouped.rename(columns={"Salary": "Total Salary", "Employee": "Employee Count"})
print("\nGrouped Data with Aggregation:\n", grouped)

#合并两个
df1 = pd.DataFrame({
    "Employee": ["Alice", "Bob", "Charlie"],
    "Department": ["HR", "IT", "Finance"]
})
df2 = pd.DataFrame({
    "Employee": ["Alice", "Bob", "Charlie"],
    "Salary": [50000, 60000, 75000]
})

# 合并（类似 SQL 的 JOIN）
merged = pd.merge(df1, df2, on="Employee")
print("\nMerged DataFrame:\n", merged)

# 按列连接
df3 = pd.DataFrame({
    "Bonus": [5000, 7000, 6000]
})
concatenated = pd.concat([merged, df3], axis=1)
print("\nConcatenated DataFrame along columns:\n", concatenated)

# 按行连接
df4 = pd.DataFrame({
    "Employee": ["David"],
    "Department": ["Marketing"],
    "Salary": [65000]
})
concatenated_rows = pd.concat([merged, df4], ignore_index=True)
print("\nConcatenated DataFrame along rows:\n", concatenated_rows)

# 按工资升序排序
sorted_df = merged.sort_values(by="Salary", ascending=True)
print("\nSorted DataFrame by Salary (ascending):\n", sorted_df)

# 按多列排序
sorted_df = merged.sort_values(by=["Department", "Salary"], ascending=[True, False])
print("\nSorted DataFrame by Department (ascending) and Salary (descending):\n", sorted_df)

data = {
    "Department": ["HR", "HR", "IT", "IT", "Finance", "Finance"],
    "Year": [2021, 2022, 2021, 2022, 2021, 2022],
    "Salary": [50000, 60000, 75000, 80000, 65000, 70000]
}
df_pivot = pd.DataFrame(data)

# 创建透视表
pivot_table = df_pivot.pivot_table(values="Salary", index="Department", columns="Year", aggfunc="mean")
print("\nPivot Table:\n", pivot_table)

# 将宽表转换为长表（melt）
melted = pd.melt(pivot_table.reset_index(), id_vars=["Department"], var_name="Year", value_name="Salary")
print("\nMelted DataFrame (Long format):\n", melted)

# 将长表转换回宽表（pivot）
pivoted = melted.pivot(index="Department", columns="Year", values="Salary")
print("\nPivoted DataFrame (Wide format):\n", pivoted)

#缺失值处理
df_missing = pd.DataFrame({
    "A": [1, 2, None, 4],
    "B": [None, 2, 3, 4]
})
print("\nDataFrame with Missing Values:\n", df_missing)
print("\nMissing values check:\n", df_missing.isnull())

# 使用均值填充
df_missing["A"] = df_missing["A"].fillna(df_missing["A"].mean())
print("\nDataFrame after filling missing values in 'A' with mean:\n", df_missing)

# 删除包含缺失值的行
df_no_missing = df_missing.dropna()
print("\nDataFrame after dropping rows with missing values:\n", df_no_missing)


