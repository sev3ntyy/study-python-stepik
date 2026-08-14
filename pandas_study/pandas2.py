import pandas as pd

data = {
    'Имя': ['Аня', 'Борис', 'Света', 'Иван'],
    'Возраст': [23, 34, 29, 24],
    'Город': ['Москва', 'Питер', 'Новосибирск', 'Екатеринбург']
}

df = pd.DataFrame(data)

filtered_df = df[df['Возраст'] > 25]
print(filtered_df)
