import numpy as np
import pandas as pd

# Матриця коефіцієнтів
A = np.array([
    [1, -4,  3, -1],
    [1,  2,  5, -1],
    [2, -3,  0,  4],
    [-1, -2, -3, -4]
])

# Порожній список для результатів
results = []

# Перебираємо a 
for a in range(-30, 31):
    b = np.array([a, 2, 5, -5], dtype=float)  
    try:
        x = np.linalg.solve(A, b)
        results.append([a, *x])
    except np.linalg.LinAlgError:
        results.append([a, None, None, None, None])

#DataFrame
df = pd.DataFrame(results, columns=['a', 'x1', 'x2', 'x3', 'x4'])
print(df)
