import numpy as np
import matplotlib.pyplot as plt
# Масив 25x25 
arr = np.random.rand(25, 25)
print("Мінімум:", arr.min())
print("Максимум:", arr.max())

# Матриця 6x6 зі значеннями 1-5 
mat = np.zeros((6, 6), dtype=int)
for i in range(1, 6):
    mat[i, i-1] = i
print("\nМатриця під діагоналлю:\n", mat)

# Множення матриць
a = np.random.randint(1, 10, (5, 3))
b = np.random.randint(1, 10, (3, 2))
result = np.dot(a, b)
print("\nРезультат множення:\n", result)

# Масив з 20 елементів — зміна знаку 10 та 16 елементів
arr20 = np.random.randint(-10, 10, 20)
print("\nДо зміни:", arr20)
arr20[9:16] *= -1
print("Після зміни знаку:", arr20)
from numpy import linalg as LA
# Матриця Коші C[i][j] = 1 / (x[i] - y[j])
x = np.linspace(1, 10, 10)
y = np.linspace(11, 20, 10)
C = 1 / np.subtract.outer(x, y)
det = LA.det(C)
print("\nВизначник матриці Коші:", det)

# Пошук екстремумів функції
x_vals = np.linspace(-10, 10, 1000)
y_vals = np.sin(x_vals) + 0.1 * x_vals**2
max_idx = np.argmax(y_vals)
min_idx = np.argmin(y_vals)
print("\nМаксимум при x =", x_vals[max_idx], "→", y_vals[max_idx])
print("Мінімум при x =", x_vals[min_idx], "→", y_vals[min_idx])
import matplotlib.pyplot as plt
def f(x, y):
    return y * (1 - 2*x)

# Параметри
x0, y0 = 0, 1
h = 0.1
x_end = 2
n = int((x_end - x0)/h)

# Ініціалізація
x_vals = [x0]
y_euler = [y0]

# Метод Ейлера
x = x0
y = y0
for _ in range(n):
    y += h * f(x, y)
    x += h
    x_vals.append(x)
    y_euler.append(y)

# Аналітичне рішення
x_exact = np.linspace(0, 2, 100)
y_exact = np.exp(x_exact - x_exact**2)

# Побудова графіка
plt.plot(x_vals, y_euler, 'o-', label='Метод Ейлера')
plt.plot(x_exact, y_exact, '-', label='Аналітичне')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Порівняння: Ейлер vs Аналітичне')
plt.grid(True)
plt.show()
