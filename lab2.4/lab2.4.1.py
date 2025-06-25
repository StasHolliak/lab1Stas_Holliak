import numpy as np
import matplotlib.pyplot as plt

# Дані для графіків
x1 = np.linspace(0.1, 10, 100)
y1 = np.log(x1)

x2 = np.linspace(0, 2 * np.pi, 100)
y2 = 2 * np.sin(x2)
y3 = 2 * np.cos(x2) + 5

# Створення фігури
plt.figure(figsize=(12, 6))

# Графік 1: y = log(x)
plt.subplot(1, 3, 1)
plt.plot(x1, y1, label='y = log(x)', color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графік y = log(x)')
plt.legend()

# Графік 2: y = 2sin(x)
plt.subplot(1, 3, 2)
plt.plot(x2, y2, label='y = 2sin(x)', color='green')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графік y = 2sin(x)')
plt.legend()

# Графік 3: y = 2cos(x) + 5
plt.subplot(1, 3, 3)
plt.plot(x2, y3, label='y = 2cos(x) + 5', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графік y = 2cos(x) + 5')
plt.legend()

# Відображення графіків
plt.tight_layout()
plt.show()
