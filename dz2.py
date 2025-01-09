#Определите среднюю зарплату (Salary) по городу (City) - используйте файл приложенный к дз - dz.csv

import pandas as pd

df = pd.read_csv('dz.csv')
df.fillna({'Salary': 0}, inplace=True)
group = df.groupby('City')['Salary'].mean()
print('Убираем NaN в зарплате:')
print(df)
print()
print('Средняя зарплата по городам:')
print(group)