import pandas as pd
import matplotlib.pyplot as plt

# Завантаження CSV-файлу
data = pd.read_csv("/company_sales_data.csv")

month = data['month_number']
face_cream = data['facecream']
face_wash = data['facewash']

# Побудова гістограми
plt.bar(month - 0.2, face_cream, width=0.4, label='Face Cream sales data', color='skyblue')
plt.bar(month + 0.2, face_wash, width=0.4, label='Face Wash sales data', color='orange')

# Налаштування графіка
plt.title('Facewash and facecream sales data')
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.xticks(month)
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()