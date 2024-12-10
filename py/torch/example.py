#logistic or sigmod sample
import torch
import matplotlib.pyplot as plt

x = torch.linspace(-10,10,100)

y = torch.sigmoid(x)

plt.plot(x.numpy(), y.numpy(), color='purple')
plt.xlabel('Input')
plt.ylabel('Output')
plt.title('Logistic Activation Function')
plt.show()

# tanh
z = torch.tanh(x)
plt.plot(x.numpy(), z.numpy(), color='blue')
plt.xlabel('Input')
plt.ylabel('Output')
plt.title('Tanh Activation Function')
plt.show()

#relu
w = torch.tanh(x)
plt.plot(x.numpy(), w.numpy(), color='green')
plt.xlabel('Input')
plt.ylabel('Output')
plt.title('Relu Activation Function')
plt.show()