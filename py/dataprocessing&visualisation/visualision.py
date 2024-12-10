import matplotlib.pyplot as plt
import numpy as np

#lineplot折线
x = np.linspace(0, 10, 100)  # 生成 0 到 10 的 100 个点
y = np.sin(x)

plt.plot(x, y, label='sin(x)')  # 绘制曲线
plt.title("Line Plot Example")  # 图标题
plt.xlabel("X Axis")            # X轴标签
plt.ylabel("Y Axis")            # Y轴标签
plt.legend()                    # 显示图例
plt.grid()                      # 显示网格
plt.show()                      # 显示图表


#散点 scatter
x = np.random.rand(50)  # 生成50个随机点
y = np.random.rand(50)
sizes = np.random.rand(50) * 100  # 点的大小
colors = np.random.rand(50)       # 点的颜色

plt.scatter(x, y, s=sizes, c=colors, alpha=0.7, cmap='viridis')  # alpha 控制透明度
plt.title("Scatter Plot Example")
plt.colorbar()  # 添加颜色条
plt.show()

#Bar plot柱状
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 8, 5]

# 水平柱状图
plt.bar(categories, values, color='skyblue')
plt.title("Bar Plot Example")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# 垂直柱状图
plt.barh(categories, values, color='orange')
plt.title("Horizontal Bar Plot Example")
plt.show()

#直方Histogram
data = np.random.randn(1000)  # 生成1000个正态分布的随机数

plt.hist(data, bins=20, color='purple', alpha=0.7)  # bins 指定柱子数量
plt.title("Histogram Example")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

#饼图pie chart
sizes = [15, 30, 45, 10]
labels = ['Category A', 'Category B', 'Category C', 'Category D']
explode = [0, 0.1, 0, 0]  # 突出显示第二块

plt.pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%', startangle=140)
plt.title("Pie Chart Example")
plt.show()

#box plot箱型
data = [np.random.randn(100) for _ in range(4)]  # 生成4组随机数据

plt.boxplot(data, labels=['Group 1', 'Group 2', 'Group 3', 'Group 4'])
plt.title("Box Plot Example")
plt.xlabel("Groups")
plt.ylabel("Values")
plt.show()

# subplot
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.subplot(2, 1, 1)  # 创建第一个子图 (2行1列，第1个子图)
plt.plot(x, y1, label="sin(x)")
plt.legend()

plt.subplot(2, 1, 2)  # 创建第二个子图 (2行1列，第2个子图)
plt.plot(x, y2, label="cos(x)", color='red')
plt.legend()

plt.tight_layout()  # 自动调整子图之间的间距
plt.show()

#网格子图
fig, axs = plt.subplots(2, 2, figsize=(8, 6))  # 创建2x2网格的子图
x = np.linspace(0, 10, 100)

axs[0, 0].plot(x, np.sin(x), color='blue')
axs[0, 0].set_title("sin(x)")

axs[0, 1].plot(x, np.cos(x), color='orange')
axs[0, 1].set_title("cos(x)")

axs[1, 0].plot(x, np.tan(x), color='green')
axs[1, 0].set_title("tan(x)")

axs[1, 1].plot(x, -np.sin(x), color='red')
axs[1, 1].set_title("-sin(x)")

plt.tight_layout()
plt.show()


#style
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, color='purple', linestyle='--', linewidth=2, marker='o', markersize=5)
plt.title("Custom Style Example")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(color='gray', linestyle=':', linewidth=0.5)
plt.show()


print(plt.style.available)  # 查看可用样式
plt.style.use('ggplot')  # 使用 'ggplot' 样式

x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x), label="sin(x)")
plt.plot(x, np.cos(x), label="cos(x)")
plt.legend()
plt.title("Styled Plot Example")
plt.show()


#savex = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title("Save Plot Example")
plt.savefig("plot_example.png", dpi=300, bbox_inches='tight')  # 保存为高分辨率 PNG 图像
plt.show()