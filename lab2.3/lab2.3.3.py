import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Створення часової осі 
time = np.linspace(0, 10, 100)
#прискорення 
acceleration = np.random.uniform(-5, 5, size=time.shape)

#Швидкість
velocity = np.cumsum(acceleration) * (time[1] - time[0])

#Позиція
position = np.cumsum(velocity) * (time[1] - time[0])

#DataFrame
df = pd.DataFrame({
    'Час': time,
    'Позиція': position,
    'Швидкість': velocity,
    'Прискорення': acceleration
})

#Середні значення
avg_velocity = df['Швидкість'].mean()
avg_acceleration = df['Прискорення'].mean()

print(f"Середня швидкість: {avg_velocity:.2f} м/с")
print(f"Середнє прискорення: {avg_acceleration:.2f} м/с²")

#Побудова графіків
plt.figure(figsize=(15, 10))

#Графік позиції
plt.subplot(3, 1, 1)
plt.plot(df['Час'], df['Позиція'], color='blue')
plt.title('Позиція тіла від часу')
plt.xlabel('Час (с)')
plt.ylabel('Позиція (м)')

# Графік швидкості
plt.subplot(3, 1, 2)
plt.plot(df['Час'], df['Швидкість'], color='green')
plt.title('Швидкість тіла від часу')
plt.xlabel('Час (с)')
plt.ylabel('Швидкість (м/с)')

# Графік прискорення
plt.subplot(3, 1, 3)
plt.plot(df['Час'], df['Прискорення'], color='red')
plt.title('Прискорення тіла від часу')
plt.xlabel('Час (с)')
plt.ylabel('Прискорення (м/с²)')

plt.tight_layout()
plt.show()
