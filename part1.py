import pandas as pd # переименовали в pd для краткости

# Изучаем функции pandas
#df = pd.read_csv('World-happiness-report-2024.csv')
#print(df.head()) # выводим первые 5 (по умолчанию) строк из csv
#print(df.tail()) # выводит 5 строк с конца файла
#print(df.info()) # выводит инфу о дата фрейме
#print(df.describe()) # выводит статистическое описание данных
#print(df['Country name']) # выводим инфу по конкретному столбцу
#print(df[['Country name', 'Regional indicator']]) # выводим несколько столбцов
#print(df.loc[56]) # выводим инфу по строке 56
#print(df.loc[56, 'Healthy life expectancy']) # вывод значения конкретной ячейки
#print(df[df['Healthy life expectancy'] > 0.7]) # вывод данных конкретного столбца по условию

# Добавляем/удаляем данные
df = pd.read_csv('hh.csv')

#df['Test'] = [new for new in range(29)] # добавляем столбец Test и заполняем данными через цикл
#print(df)

#df.drop('Test', axis=1, inplace=True) # удаляем столбец Test, в axis 1/0 - удаляем столбец или строку
# inplace = True - изменения внести в исходный дата фрейм, False - оригина остается, возвращается измененный дата фрейм
#print(df)

df.drop(28, axis=0, inplace=True) # удаляем строку 28
print(df)