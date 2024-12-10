#list
list1 = [1,2,3,[4,5,6],7,8,9,'blue',1+1]
list2 = list1[3]
list3 = list1[3][2]
list4 = list1[-1]
print(list1)
print(list2)
print(list3)
print(list4)
list1[1] = 'two'
print(list1[1])
print(len(list1))
for i in list1:
    print(i)

for i in range(0,len(list1),2):
    print(list1[i])

# list1.append(input("input a String: "))
# print(list1)
# list1.insert(2,input("input another String: "))
# print(list1)

del list1[0]
print(list1)
list4=[1,5,6,7,8,9,2,3,4]
list4.sort()
print(list4)
list4.reverse()
list4.remove(5)
list4.remove(1)
print(list4)
list4.pop()
print(list4)
list4.pop(2)
print(list4)
print(list4.index(8))

#dictionary
# 1. 字典的创建
# 使用大括号创建一个空字典
my_dict = {}
print("Empty dict:", my_dict)

# 创建并初始化字典（键值对形式）
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print("Initial dict (person):", person)

# 使用 dict() 函数创建字典
colors = dict(red=1, green=2, blue=3)
print("Colors dict:", colors)

# 使用可迭代对象创建字典（如列表的二元组）
pairs = [("one", 1), ("two", 2), ("three", 3)]
numbers = dict(pairs)
print("Numbers dict from list of tuples:", numbers)

# 2. 访问字典中的值
print("Name:", person["name"])  # 通过 key 访问
# print(person["country"])  # 若键不存在会报错 KeyError

# 使用 get() 方法可避免 KeyError，不存在则返回 None 或自定义默认值
country = person.get("country", "Unknown")
print("Country:", country)

# 3. 添加和修改字典项
person["age"] = 31  # 修改已有键的值
person["job"] = "Engineer"  # 新增键值对
print("Modified person dict:", person)

# 4. 删除字典项
del person["job"]
print("After deletion person dict:", person)

# pop() 方法会返回被删除的值
age_value = person.pop("age", None)
print("Popped age:", age_value)
print("After pop person dict:", person)

# 5. 字典的遍历
# 遍历键
print("Keys in person:")
for key in person:
    print(key, "->", person[key])

# 遍历值
print("Values in colors:")
for value in colors.values():
    print(value)

# 遍历键值对
print("Items in numbers:")
for key, value in numbers.items():
    print(key, "=", value)

# 6. 字典的一些常用方法
keys = person.keys()
values = person.values()
len = len(person)
items = person.items()
print("Keys:", list(keys))
print("Values:", list(values))
print("Items:", list(items))

# update() 用于批量更新或合并
person.update({"name": "Bob", "city": "Chicago"})
print("After update person dict:", person)

# clear() 清空字典
temp_dict = {"a": 1, "b": 2}
temp_dict.clear()
print("After clear:", temp_dict)

# 7. 判断键是否在字典中
if "name" in person:
    print("'name' key exists in person dict")

if "age" not in person:
    print("'age' key does not exist in person dict")

# 8. 字典与其他数据结构的转换
# 将字典的键转换为列表
person_keys_list = list(person.keys())
print("Person keys as list:", person_keys_list)

# 将字典的值转换为列表
person_values_list = list(person.values())
print("Person values as list:", person_values_list)

# 将字典的键值对转换为列表的二元组
person_items_list = list(person.items())
print("Person items as list of tuples:", person_items_list)

# 从键值对列表重新创建字典
new_person = dict(person_items_list)
print("New person dict from items list:", new_person)

# 9. 字典的浅拷贝与深拷贝
import copy
original = {"a": 1, "b": [1, 2, 3]}
shallow_copy = original.copy()  # 浅拷贝
deep_copy = copy.deepcopy(original)  # 深拷贝

original["b"][0] = 999  # 修改嵌套列表
print("Original:", original)
print("Shallow copy:", shallow_copy)  # 浅拷贝会受影响
print("Deep copy:", deep_copy)  # 深拷贝不受影响


#tuple
# 1. 创建元组
# 使用小括号创建空元组
empty_tuple = ()
print("Empty tuple:", empty_tuple)

# 创建包含多个元素的元组
numbers = (1, 2, 3, 4, 5)
print("Numbers tuple:", numbers)

# 元组中的元素可以是不同类型
mixed = (1, "apple", 3.14, [1,2], {"a":1})
print("Mixed tuple:", mixed)

# 使用逗号创建单元素元组时须加逗号，否则会被当作普通数字或字符串
single_element_tuple = (42,)
print("Single element tuple:", single_element_tuple)

# 可不使用小括号直接定义元组（解包时常用）
colors = "red", "green", "blue"
print("Colors tuple:", colors)

# 2. 访问元组元素
# 使用索引访问（索引从0开始）
print("First element of numbers:", numbers[0])
print("Last element of numbers:", numbers[-1])

# 3. 元组切片（类似列表切片）
print("Numbers slice [1:4]:", numbers[1:4])
print("Numbers slice [::2]:", numbers[::2])  # 间隔2个元素取一个

# 4. 元组是不可变的
# numbers[0] = 10  # 会报错：TypeError: 'tuple' object does not support item assignment

# 5. 元组解包（tuple unpacking）
a, b, c = ("cat", "dog", "mouse")
print("a:", a, "b:", b, "c:", c)

# 使用 * 运算符进行解包
first, *middle, last = (10, 20, 30, 40, 50)
print("first:", first, "middle:", middle, "last:", last)

# 6. 合并与重复元组
t1 = (1, 2, 3)
t2 = (4, 5)
t3 = t1 + t2  # 合并元组
print("Merged tuple:", t3)

t4 = t1 * 3  # 重复元组
print("Repeated tuple:", t4)

# 7. 成员操作符
print("Is 2 in t1?", 2 in t1)
print("Is 100 in t1?", 100 in t1)

# 8. 长度、最值、最小值、最大值
#print("Length of t1:", len(t1))
print("Min of t1:", min(t1))
print("Max of t1:", max(t1))

# 9. 元组与其他数据结构转换
my_list = [1, 2, 3]
my_tuple_from_list = tuple(my_list)
print("Tuple from list:", my_tuple_from_list)

# 将元组转换回列表
my_list_from_tuple = list(my_tuple_from_list)
print("List from tuple:", my_list_from_tuple)

# 将字符串转换为元组（元组中的每个元素将是单个字符）
string_tuple = tuple("hello")
print("Tuple from string:", string_tuple)

# 10. 遍历元组
for element in numbers:
    print("Element:", element)

# 11. 比较元组（字典序比较）
t5 = (1, 2, 3)
t6 = (1, 2, 4)
print("t5 < t6?", t5 < t6)  # 按元素依次比较，1=1，2=2，3<4 故 True

# 12. 使用元组作为字典键（元组是不可变的，可用作键）
coords = (10, 20)
my_dict = {coords: "Point A"}
print("Dict with tuple key:", my_dict)

# 13. 使用 enumerate() 获取序号和元素的元组
for index, value in enumerate(numbers):
    print("Index:", index, "Value:", value)

#Array
import array

# 1. 创建数组
# 创建一个整数数组 i f l d
int_arr = array.array('i', [1, 2, 3, 4, 5])
print("Integer array:", int_arr)

# 创建一个浮点数数组
float_arr = array.array('f', [1.0, 2.5, 3.3])
print("Float array:", float_arr)

# 创建空数组，然后逐个append
empty_arr = array.array('i')  # 创建一个空整数数组
empty_arr.append(10)
empty_arr.append(20)
print("Empty then appended:", empty_arr)

# 2. 访问数组元素
print("First element of int_arr:", int_arr[0])
print("Last element of int_arr:", int_arr[-1])

# 3. 修改数组元素
int_arr[0] = 100  # 将第一个元素修改为100
print("Modified int_arr:", int_arr)

# 4. 数组切片操作（与列表相似）
print("Slice int_arr [1:4]:", int_arr[1:4])
print("Slice float_arr [::2]:", float_arr[::2])

# 5. 添加和扩展数组
int_arr.append(6)        # 在末尾添加单个元素
print("After append:", int_arr)
int_arr.extend([7, 8])   # 使用 extend 添加可迭代对象中的多个元素
print("After extend:", int_arr)
int_arr.reverse()
int_arr.reverse()
# int_arr.sort()

# 6. 插入元素
int_arr.insert(1, 999)   # 在索引1处插入999
print("After insert:", int_arr)

# 7. 移除元素
int_arr.remove(999)      # 移除匹配的第一个元素999
print("After remove:", int_arr)

popped_value = int_arr.pop()  # 弹出末尾元素
print("After pop:", int_arr, "Popped value:", popped_value)

# 8. 获取数组长度
print("Length of int_arr:", len(int_arr))

# 9. 数组遍历
print("Iterating over int_arr:")
for x in int_arr:
    print(x, end=" ")
print()

# 10. 转换为列表
int_list = int_arr.tolist()
print("Converted to list:", int_list, "Type:", type(int_list))

# 11. 从文件中读取和写入数组（示例，仅演示写入和读取内存中的BytesIO）
import io
data_buffer = io.BytesIO()
int_arr.tofile(data_buffer)   # 将数组的二进制数据写入文件对象
data_buffer.seek(0)           # 将指针回到开头
new_arr = array.array('i')
new_arr.fromfile(data_buffer, len(int_arr))  # 从文件对象中读取数据到数组
print("New array read from buffer:", new_arr)

# 12. 使用 fromlist 将列表转换为数组
another_arr = array.array('i')
another_arr.fromlist([10, 20, 30])
print("Array created from list:", another_arr)

# 13. 数组的 count 和 index 方法
print("Count of '2' in another_arr:", another_arr.count(2))
print("Index of '20' in another_arr:", another_arr.index(20))

# in 2D
#list
# 创建一个二维列表，类似于矩阵
matrix_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("2D List:", matrix_list)

# 访问元素，比如第二行第三列 (行索引1，列索引2)
element = matrix_list[1][2]
print("Element at row 2, col 3 (0-based):", element)

# 修改元素
matrix_list[0][0] = 10
print("Modified 2D List:", matrix_list)

# 遍历二维列表
for row in matrix_list:
    for val in row:
        print(val, end=" ")
    print()

#tuple
# 创建一个二维元组（元组的元组）
matrix_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
print("2D Tuple:", matrix_tuple)

# 访问元素 (第三行第一列)
elem = matrix_tuple[2][0]
print("Element at row 3, col 1:", elem)

# 元组是不可变的，无法直接修改元素
# matrix_tuple[0][0] = 10  # 会报错：TypeError

# 若需要修改，只能通过转换为列表后再转换回元组
temp_list = [list(row) for row in matrix_tuple]
temp_list[0][0] = 10
matrix_tuple = tuple(tuple(row) for row in temp_list)
print("Modified 2D Tuple:", matrix_tuple)

# 遍历二维元组
for row in matrix_tuple:
    for val in row:
        print(val, end=" ")
    print()

#dictionary
# 创建一个字典的字典，类似于表格结构
# 可以将 "row1", "row2" 等作为行键，内部字典作为列数据
matrix_dict = {
    "row1": {"col1": 1, "col2": 2, "col3": 3},
    "row2": {"col1": 4, "col2": 5, "col3": 6},
    "row3": {"col1": 7, "col2": 8, "col3": 9}
}
print("2D Dict:", matrix_dict)

# 访问元素，比如 row2 的 col3
val = matrix_dict["row2"]["col3"]
print("Element (row2, col3):", val)

# 添加或修改元素
matrix_dict["row1"]["col1"] = 10
print("Modified 2D Dict:", matrix_dict)

# 添加新行
matrix_dict["row4"] = {"col1": 10, "col2": 11, "col3": 12}
print("After adding row4:", matrix_dict)

# 遍历字典
for row_key, cols in matrix_dict.items():
    print(row_key, end=": ")
    for col_key, value in cols.items():
        print(f"{col_key}={value}", end=" ")
    print()

# array
import array

# 创建几个一维数组，然后将它们放入列表中形成2D结构
row1 = array.array('i', [1, 2, 3])
row2 = array.array('i', [4, 5, 6])
row3 = array.array('i', [7, 8, 9])

two_d_array = [row1, row2, row3]
print("2D structure using array and list:", two_d_array)

# 访问元素 (例如第3行第2列)
elem = two_d_array[2][1]  # 行索引2的数组，列索引1的元素
print("Element (3rd row, 2nd col):", elem)

# 修改元素
two_d_array[0][0] = 10
print("Modified 2D structure:", two_d_array)

# 遍历
for arr in two_d_array:
    for value in arr:
        print(value, end=" ")
    print()


# a = 10
# b = 15
# c = 20
# max=max(a,b,c)

