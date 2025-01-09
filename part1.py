import pandas as pd # переименовали в pd для краткости

df = pd.read_csv('World-happiness-report-2024.csv')
#print(df.head()) # выводим первые 5 (по умолчанию) строк из csv
#print(df.tail()) # выводит 5 строк с конца файла
#print(df.info()) # выводит инфу о дата фрейме
#print(df.describe()) # выводит статистическое описание данных
#print(df['Country name']) # выводим инфу по конкретному столбцу
#print(df[['Country name', 'Regional indicator']]) # выводим несколько столбцов
#print(df.loc[56]) # выводим инфу по строке 56
#print(df.loc[56, 'Healthy life expectancy']) # вывод значения конкретной ячейки
#print(df[df['Healthy life expectancy'] > 0.7]) # вывод данных конкретного столбца по условию