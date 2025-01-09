#Скачайте любой датасет с сайта https://www.kaggle.com/datasets
#Загрузите набор данных из CSV-файла в DataFrame.
#Выведите первые 5 строк данных, чтобы получить представление о структуре данных.
#Выведите информацию о данных (.info()) и статистическое описание (.describe()).

import pandas as pd

df = pd.read_csv('tictactoe_games.csv')