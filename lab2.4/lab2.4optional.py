import math
import numpy as np
import matplotlib.pyplot as plt

# Функція обчислення cos(x) через ряд Тейлора
def taylor_cos(x, terms=10):
    result = 0
    for n in range(terms):
        result += ((-1)**n * x**(2*n)) / math.factorial(2*n)
    return result
# Массив кутів 
x = np.arange(-2*np.pi, 2*np.pi, 0.1)

# Обчислення значень косинуса
taylor_values = [taylor_cos(val, terms=10) for val in x]
true_values = np.cos(x)

# Побудова графіка
fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(x, true_values, label='np.cos(x)', color='blue')
ax.plot(x, taylor_values, label='Taylor approx (10 terms)', linestyle='--', color='red')

ax.set_title('Порівняння np.cos(x) з рядом Тейлора')
ax.set_xlabel('x')
ax.set_ylabel('cos(x)')
ax.legend()
ax.grid(True)

plt.show()










