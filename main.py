"""
Скачайте любой датасет с сайта https://www.kaggle.com/datasets
Загрузите набор данных из CSV-файла в DataFrame.
Выведите первые 5 строк данных, чтобы получить представление о структуре данных.
Выведите информацию о данных (.info()) и статистическое описание (.describe()).
Определите среднюю зарплату (Salary) по городу (City) - используйте файл приложенный к дз - dz.csv

В поле сдачи домашнего задания приложите ссылку на репозиторий с кодом.
"""
import pandas as pd

df = pd.read_csv('champions.csv')
print(df.head())
print(df.info())
print(df.describe())
#print(df['Salary'].mean())

df2 = pd.read_csv('dz.csv')
print(df2.head(20))
df2.fillna(value={"City": "Х.З. (хочу знать)"}, inplace=True)
df.dropna(inplace=True)
group = df2.groupby('City')['Salary'].mean()
print(df2.head(20))
print(group)