import pandas as pd

data = {
    'Имя': ['Аня', 'Борис', 'Света', None],
    'Возраст': [23, None, 29, 24],
    'Город': ['Москва', 'Питер', None, 'Екатеринбург']
}

df = pd.DataFrame(data)
print(df.isnull())

df['Город'] = df['Город'].fillna('Неизвестно')
df['Возраст'] = df['Возраст'].fillna(0)
df['Имя'] = df['Имя'].fillna("Нет имени")
print(df)