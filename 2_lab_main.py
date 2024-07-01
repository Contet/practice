import numpy as np
import matplotlib.pyplot as plt
y1 = [1, 2]
y2 = [2, 3]
y3 = [3, 4]

# y(x) = sin(x) * (x ** 2), x  = [0; 20; 0.01]

X  = np.arange(0, 20, 0.01)
Y = np.sin(X) * (X ** 2)

plt.plot(Y)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.show()