import pandas as pd

# Работа с некорректными данными
df = pd.read_csv('animal.csv')
print(df)

# Заменяем значения NaN на другие (в данном случае на 0)
#df.fillna(0, inplace=True)
#print(df)

# Удаляем строки с Nan (не рекомендуется)
df.dropna(inplace=True)
print(df)
