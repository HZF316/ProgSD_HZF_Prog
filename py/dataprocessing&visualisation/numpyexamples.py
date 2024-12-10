import numpyexamples as np

# 1. 创建数组
arr_from_list = np.array([1, 2, 3, 4, 5])  # 从列表创建一维数组
print("1D array:", arr_from_list)

arr_from_tuple = np.array((10, 20, 30))    # 从元组创建数组
print("Array from tuple:", arr_from_tuple)

arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])             # 创建二维数组
print("2D array:\n", arr_2d)

# 使用内置函数创建数组
zeros_arr = np.zeros((2, 3))               # 创建元素全为0的数组
ones_arr = np.ones((2, 3))                 # 创建元素全为1的数组
eye_arr = np.eye(3)                       # 创建单位矩阵
arange_arr = np.arange(0, 10, 2)          # 类似于 range，创建等差序列
linspace_arr = np.linspace(0, 1, 5)        # 在指定范围线性分布的数值
print("Zeros array:\n", zeros_arr)
print("Ones array:\n", ones_arr)
print("Identity matrix:\n", eye_arr)
print("Arange array:", arange_arr)
print("Linspace array:", linspace_arr)

# 2. 数组属性
print("Shape of arr_2d:", arr_2d.shape)
print("Data type of arr_from_list:", arr_from_list.dtype)
print("Size of arr_2d:", arr_2d.size)
print("Number of dimensions of arr_2d:", arr_2d.ndim)

# 3. 切片与索引
print("Element at (0, 1) in arr_2d:", arr_2d[0, 1])
print("First row of arr_2d:", arr_2d[0, :])
print("First column of arr_2d:", arr_2d[:, 0])
# 修改元素
arr_2d[1, 2] = 99
print("Modified 2D array:\n", arr_2d)

# 高级索引
index_arr = np.array([2, 0, 1])
sample_arr = np.array([10, 20, 30])
print("Advanced indexing:", sample_arr[index_arr])  # 根据index_arr选取元素

# 布尔索引
bool_mask = arr_from_list > 2
print("Boolean mask:", bool_mask)
print("Elements > 2:", arr_from_list[bool_mask])

# 4. 基本算术运算
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print("a+b:", a + b)
print("a-b:", a - b)
print("a*b:", a * b)
print("a/b:", a / b)

# 标量运算自动广播
print("a*2:", a * 2)

# 5. 通用函数（ufunc）
print("sin(a):", np.sin(a))
print("sqrt(a):", np.sqrt(a))
print("log(a):", np.log(a))

# 6. 矩阵与线性代数操作
mat1 = np.array([[1, 2],
                 [3, 4]])
mat2 = np.array([[5, 6],
                 [7, 8]])

print("Matrix multiplication:\n", np.dot(mat1, mat2))
print("Element-wise multiplication:\n", mat1 * mat2)
print("Matrix transpose:\n", mat1.T)
print("Matrix inverse:\n", np.linalg.inv(mat1))
print("Matrix determinant:", np.linalg.det(mat1))

# 7. 广播机制
# 不同形状的数组进行算术运算时自动沿特定维度扩展
arr_broadcast = np.array([[1], [2], [3]])  # shape (3,1)
vec = np.array([10, 20, 30])               # shape (3,)
# 在计算中 vec 会被视为 shape(1,3)，然后与arr_broadcast匹配
# 实际广播结果是arr_broadcast变成(3,3)和vec变成(3,3)
# arr_broadcast = [[1],[2],[3]] -> [[1,1,1],[2,2,2],[3,3,3]]
# vec = [10,20,30] -> [[10,20,30]]
# 最终运算形状为(3,3)
print("Broadcast result:\n", arr_broadcast + vec)

# 8. 形状操作
arr_reshaped = np.arange(1, 13).reshape((3, 4))  # 重塑数组为3行4列
print("Reshaped array:\n", arr_reshaped)
arr_flattened = arr_reshaped.flatten()
print("Flattened array:", arr_flattened)

# 9. 聚合操作
print("Sum of arr_2d:", arr_2d.sum())
print("Mean of arr_2d:", arr_2d.mean())
print("Max of arr_2d:", arr_2d.max())
print("Min of arr_2d:", arr_2d.min())
print("Row-wise sum of arr_2d:", arr_2d.sum(axis=1))
print("Column-wise mean of arr_2d:", arr_2d.mean(axis=0))

# 10. 排序与搜索
unsorted_arr = np.array([3, 1, 2])
sorted_arr = np.sort(unsorted_arr)
print("Sorted array:", sorted_arr)
print("Original array unchanged:", unsorted_arr)
unsorted_arr.sort()  # 就地排序
print("In-place sorted array:", unsorted_arr)

# 搜索元素
print("Index of element '2' in unsorted_arr:", np.where(unsorted_arr == 2))

# 11. 过滤数据
data = np.array([10, 15, 20, 25, 30])
filtered_data = data[data > 20]  # 过滤出大于20的元素
print("Filtered data:", filtered_data)

# 12. 随机数生成
np.random.seed(0)  # 设置随机种子以复现结果
rand_arr = np.random.rand(3, 3)    # 生成0~1之间的随机数
rand_int = np.random.randint(0, 10, size=(3,3))
print("Random array (float):\n", rand_arr)
print("Random array (int):\n", rand_int)
print("Shuffle a list in place:")
arr_for_shuffle = np.arange(10)
np.random.shuffle(arr_for_shuffle)
print(arr_for_shuffle)

# 13. 与 Python 原生数据结构的转换
list_from_arr = arr_from_list.tolist()
print("Converted to list:", list_from_arr)
arr_from_list_again = np.array(list_from_arr)
print("Converted back to array:", arr_from_list_again)

# 14. 文件读写
# 保存数组到文本文件
np.savetxt("data.txt", arr_2d, delimiter=",")
# 从文本文件加载数据
loaded_data = np.loadtxt("data.txt", delimiter=",")
print("Loaded data from file:\n", loaded_data)

# 保存为二进制格式（.npy）
np.save("data.npy", arr_2d)
loaded_npy = np.load("data.npy")
print("Loaded data from .npy file:\n", loaded_npy)

# 总结：
# 本示例展示了 NumPy 的基本使用方法，包括数组创建、索引切片、广播、线性代数、统计分析、排序过滤、随机数生成以及文件读写等常用操作。
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

# 1. 基本算术运算（逐元素运算）
print("a + b:", a + b)     # [11, 22, 33]
print("a - b:", a - b)     # [-9, -18, -27]
print("a * b:", a * b)     # [10, 40, 90]
print("a / b:", a / b)     # [0.1, 0.1, 0.1]
print("a ** 2:", a ** 2)   # [1, 4, 9]

# 2. 标量与数组的运算（广播）
print("a * 2:", a * 2)     # [2, 4, 6]

# 创建一个二维数组
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

# 3. 矩阵相乘(点乘与元素级乘法的区别)
print("Element-wise multiply A*B:\n", A * B)
# [[5, 12],
#  [21, 32]]

# 矩阵乘法（点积）
print("Matrix multiplication np.dot(A, B):\n", np.dot(A, B))
# [[19, 22],
#  [43, 50]]

# 4. 通用函数（ufunc）的使用（如sin, cos, exp, sqrt等）
x = np.array([0, np.pi/2, np.pi])
print("sin(x):", np.sin(x))   # [0, 1, 0]
print("exp(a):", np.exp(a))   # 对a中每个元素求e的幂
print("sqrt(a):", np.sqrt(a)) # 对a中每个元素开平方

# 5. 聚合运算
print("sum of a:", np.sum(a))         # 1+2+3=6
print("mean of b:", np.mean(b))       # (10+20+30)/3 = 20
print("max of A:", np.max(A))         # 最大值为4
print("min of A:", np.min(A))         # 最小值为1

# 6. 条件筛选与布尔掩码
cond = a > 1    # [False, True, True]
print("a > 1:", a[cond])  # [2, 3]

# 7. 广播（更复杂的例子）
# 假设有一个二维数组和一维数组进行加法，会自动进行广播
C = np.array([[1, 2, 3],
              [4, 5, 6]])
d = np.array([10, 20, 30])
print("C + d:\n", C + d)
# [[11, 22, 33],
#  [14, 25, 36]]

# 8. 排序
unsorted_arr = np.array([3, 1, 5, 2, 4])
sorted_arr = np.sort(unsorted_arr)
print("sorted_arr:", sorted_arr)  # [1, 2, 3, 4, 5]

# 9. 累积操作
print("cumulative sum of a:", np.cumsum(a)) # [1, 3, 6]

# 10. 矩阵行列操作
print("Column-wise sum of C:", np.sum(C, axis=0))  # 对每列求和 [5,7,9]
print("Row-wise mean of C:", np.mean(C, axis=1))   # 对每行求平均 [2,5]

A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

# 1. 元素级乘法（Element-wise）
# 使用 * 号，对应元素相乘
elementwise = A * B
# elementwise = [[1*5, 2*6],
#                [3*7, 4*8]]
# elementwise = [[5, 12],
#                [21,32]]

print("元素级乘法结果：\n", elementwise)

# 2. 矩阵点乘（Matrix Multiplication）
# 使用 np.dot(A, B) 或者 A.dot(B) 或者 A @ B 都可以实现矩阵乘法。
dot_product = np.dot(A, B)
# 矩阵乘法规则：(2x2) · (2x2) = (2x2)
# dot_product[0,0] = 1*5 + 2*7 = 19
# dot_product[0,1] = 1*6 + 2*8 = 22
# dot_product[1,0] = 3*5 + 4*7 = 43
# dot_product[1,1] = 3*6 + 4*8 = 50
# dot_product = [[19, 22],
#                [43, 50]]

print("矩阵点乘结果 (np.dot)：\n", dot_product)

# 使用 @ 运算符（Python 3.5+）：
at_product = A @ B
print("矩阵点乘结果 (@ 符号)：\n", at_product)

A.T
tr=np.trace(A)
inx=np.linalg.inv(A)

import numpyexamples as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# 沿轴0（对于一维数组即水平）拼接
concatenated = np.concatenate((arr1, arr2))
print("Concatenate 1D:", concatenated)  # [1 2 3 4 5 6]

# 对二维数组沿axis=0拼接（垂直方向）
arr3 = np.array([[1, 2],
                 [3, 4]])
arr4 = np.array([[5, 6],
                 [7, 8]])
concatenated_2d_axis0 = np.concatenate((arr3, arr4), axis=0)
print("Concatenate along axis=0:\n", concatenated_2d_axis0)
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

# 对二维数组沿axis=1拼接（水平方向）
concatenated_2d_axis1 = np.concatenate((arr3, arr4), axis=1)
print("Concatenate along axis=1:\n", concatenated_2d_axis1)
# [[1 2 5 6]
#  [3 4 7 8]]


arr5 = np.array([1, 2, 3])
arr6 = np.array([4, 5, 6])

vertical_stack = np.vstack((arr5, arr6))
print("vstack:\n", vertical_stack)
# [[1 2 3]
#  [4 5 6]]

horizontal_stack = np.hstack((arr5, arr6))
print("hstack:", horizontal_stack)
# [1 2 3 4 5 6]

# 对二维数组一样适用
vertical_stack_2d = np.vstack((arr3, arr4))
print("2D vertical stack:\n", vertical_stack_2d)
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

horizontal_stack_2d = np.hstack((arr3, arr4))
print("2D horizontal stack:\n", horizontal_stack_2d)
# [[1 2 5 6]
#  [3 4 7 8]]


arr7 = np.array([1, 2, 3])
arr8 = np.array([4, 5, 6])

stacked = np.stack((arr7, arr8), axis=0)
print("stacked along new axis=0:\n", stacked)
# [[1 2 3]
#  [4 5 6]]
print("stacked shape:", stacked.shape)  # (2, 3)

# 沿axis=1堆叠，会将数组从(3,)->(3,2)的形状
stacked_axis1 = np.stack((arr7, arr8), axis=1)
print("stacked along new axis=1:\n", stacked_axis1)
# [[1 4]
#  [2 5]
#  [3 6]]
print("stacked_axis1 shape:", stacked_axis1.shape) # (3, 2)



import numpyexamples as np

arr = np.arange(1, 13)
print("Original 1D array:", arr)

# 将一维数组分割成三个等长的部分
split_arr = np.split(arr, 3)  # 分成3份，每份长度为4
for i, part in enumerate(split_arr):
    print(f"Part {i}:", part)
# Part 0: [1 2 3 4]
# Part 1: [5 6 7 8]
# Part 2: [ 9 10 11 12]

# 二维数组示例
arr2d = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8]])
print("Original 2D array:\n", arr2d)

# 沿axis=1(水平方向)分割为两部分（要求等长分割）
left, right = np.split(arr2d, 2, axis=1)
print("Left part:\n", left)
print("Right part:\n", right)


arr = np.arange(1, 10)
print("Original array:", arr)

# 分成4部分，即使不能等分，也会尝试分割
split_arr = np.array_split(arr, 4)
for i, part in enumerate(split_arr):
    print(f"Part {i}:", part)
# 可能分为 [1 2 3], [4 5], [6 7], [8 9]


arr2d = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8]])

# 水平分割为两部分（列方向分割）
left, right = np.hsplit(arr2d, 2)
print("Left part (hsplit):\n", left)
print("Right part (hsplit):\n", right)

# 垂直分割为两部分（行方向分割）
top, bottom = np.vsplit(arr2d, 2)
print("Top part (vsplit):\n", top)
print("Bottom part (vsplit):\n", bottom)

arr3d = np.array([[[ 1,  2,  3],
                   [ 4,  5,  6]],

                  [[ 7,  8,  9],
                   [10, 11, 12]]])

print("Original 3D array:\n", arr3d)

# 沿深度方向分割成3个单独的 2D 数组
d1, d2, d3 = np.dsplit(arr3d, 3)
print("After dsplit:\n")
print("d1:\n", d1)
print("d2:\n", d2)
print("d3:\n", d3)


#slicing
import numpyexamples as np

# 创建一个一维数组
arr = np.arange(10)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Original 1D array:", arr)

# 基础切片语法：arr[start:end:step]
# start 默认是0，end默认是数组长度，step默认是1
print("arr[2:5]:", arr[2:5])      # 取索引2到4的元素，即[2, 3, 4]
print("arr[:4]:", arr[:4])        # 从开头到索引3，即[0, 1, 2, 3]
print("arr[5:]:", arr[5:])        # 从索引5到结束，即[5, 6, 7, 8, 9]
print("arr[::2]:", arr[::2])      # 每隔2个取一个，即[0, 2, 4, 6, 8]

# 对切片的修改会影响原数组的数据，因为切片返回的是视图（view）
sub_arr = arr[2:5]  # sub_arr现在是 arr 的一个视图
sub_arr[0] = 100
print("Modified sub_arr:", sub_arr)   # [100, 3, 4]
print("arr after sub_arr modification:", arr)
# arr 也变了，现在 arr[2] = 100

# 若想复制一份独立的数据副本，而不是视图，可以用copy()
copy_arr = arr[2:5].copy()
copy_arr[0] = 200
print("copy_arr:", copy_arr)   # [200, 3, 4]
print("arr after copy_arr modification:", arr)  # arr不变

# 二维数组切片
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
print("Original 2D array:\n", arr2d)

# 切片选取一块子区域
print("arr2d[0:2, 1:3]:\n", arr2d[0:2, 1:3])
# 取第0、1行 和 第1、2列的元素：
# [[2, 3],
#  [5, 6]]

# 行列的不同切片组合
print("First row:", arr2d[0, :])     # 第0行的所有元素 [1, 2, 3]
print("First column:", arr2d[:, 0])  # 第0列的所有元素 [1, 4, 7]

# 使用步长切片二维数组
print("arr2d[:, ::2]:\n", arr2d[:, ::2])
# 所有行，每隔2列取一列：
# [[1, 3],
#  [4, 6],
#  [7, 9]]

# 切片赋值
arr2d[1:, 1:] = 0
print("arr2d after slice assignment:\n", arr2d)
# 从第1行第1列开始的子块置0
# [[1, 2, 3],
#  [4, 0, 0],
#  [7, 0, 0]]