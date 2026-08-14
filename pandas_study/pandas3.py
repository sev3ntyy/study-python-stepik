import pandas as pd 

arrays = [
    ['Россия','Россия','США','США'],
    ['Москва','Питер','Нью-Йорк','Лос-Анджелес']
]
index = pd.MultiIndex.from_arrays(arrays, names={'Страна','Город'})

data = {
    'Население': [12.5,5.4,8.4,4.0],
    'Площадь (км²)': [2511 , 1439 ,789,503] 
}

df_multi = pd.DataFrame(data,index=index)
print(df_multi)