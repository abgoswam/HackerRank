import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-20, 21)
sigmoid = 1 / (1 + np.exp(-1 * x))

print(x)
print(sigmoid)

plt.plot(x, sigmoid)
plt.show()


def sigmoid_derivative(x):
    s1 = 1 / (1 + np.exp(-1 * x))
    s2 = (1 - s1)
    return s1*s2


sd = sigmoid_derivative(x)

plt.plot(x, sigmoid)
plt.plot(x, sd)
plt.show()




