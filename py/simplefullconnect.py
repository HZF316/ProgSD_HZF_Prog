import torch
import torch.nn as nn
import torch.optim as optim

# 定义一个简单的全连接网络（MLP）
class SimpleFCNet(nn.Module):
    def __init__(self, input_size=10, hidden_size=20, output_size=1):
        super(SimpleFCNet, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)  # 第一层线性层
        self.relu = nn.ReLU()                          # ReLU激活函数
        self.fc2 = nn.Linear(hidden_size, output_size) # 输出层

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

# 假设我们有一些随机输入数据和对应的目标值
# 这里的输入是一个形状为 (batch_size, input_size) 的张量
batch_size = 5
input_size = 10
hidden_size = 20
output_size = 1

# 随机生成输入数据和标签
x = torch.randn(batch_size, input_size)  # 输入数据
y = torch.randn(batch_size, output_size) # 目标值（回归任务中可随机生成连续值）

# 实例化网络、定义损失函数和优化器
model = SimpleFCNet(input_size, hidden_size, output_size)
criterion = nn.MSELoss()      # 均方误差损失函数 (适合回归任务)
optimizer = optim.SGD(model.parameters(), lr=0.01)  # 随机梯度下降优化器

# 前向传播
predictions = model(x)  # 模型预测输出

# 计算损失
loss = criterion(predictions, y)

# 将梯度清零
optimizer.zero_grad()

# 反向传播计算梯度
loss.backward()

# 更新参数
optimizer.step()

# 打印当前损失
print("Current loss:", loss.item())