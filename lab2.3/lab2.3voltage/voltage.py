import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Читання Excel-файлу
df = pd.read_excel("/voltage.xlsx")

U = df['Voltage_1 (1)']       
I = df['abs(col(Current11))']

Uabs = np.abs(U)
Iabs = np.abs(I)

# Підготовка даних
X1, Y1 = Uabs, Iabs
X2, Y2 = 1/Uabs, Iabs/Uabs
X3, Y3 = 1/Uabs, Iabs/(Uabs**2)
X4, Y4 = Uabs**0.5, Iabs/Uabs

# Графік через log10
def plot_log(x, y, title, xlabel, ylabel):
    plt.figure()
    plt.plot(np.log10(x), np.log10(y), 'o-')
    plt.title(title)
    plt.xlabel(f"log10({xlabel})")
    plt.ylabel(f"log10({ylabel})")
    plt.grid(True)
    plt.show()

# Побудова графіків
plot_log(X1, Y1, "Омічна провідність", "U", "I")
plot_log(X2, Y2, "Інжекційна провідність", "1/U", "I/U")
plot_log(X3, Y3, "Фаулер-Нордгейм", "1/U", "I/U²")
plot_log(X4, Y4, "Пула-Френкеля", "√U", "I/U")

# Пошук екстремумів
print("Макс струм:", Iabs.max(), "Мін струм:", Iabs.min())
print("Макс напруга:", Uabs.max(), "Мін напруга:", Uabs.min())
