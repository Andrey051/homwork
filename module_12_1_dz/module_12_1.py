import requests
import numpy as np
import pandas as pd



address =  'https://api.github.com/events'
response = requests.get(address)
if response.status_code == 200:
    status = response.url
    print(f"Статус: {status}")
else:
    print("Ошибка при запросе")
print('-------------------------------------------------------------------------')
#--------------------------------------------------------------------------------


a = np.array([1, 2, 3, 4, 5, 6]) # создадим массив
three_up = (a >=3) # распечатаем все значения в массиве, от 3.
divisile_by_3 = a[a%3==0] # выберем элементы, делящиеся на 3
b = a.copy # Использование copy метода
sum_= np.sum(a)
max_ = np.max(a)
print(a)
print(a[three_up])
print(divisile_by_3)
print(sum_)
print(max_)
print("----------------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------

df = pd.read_fwf(r'D:\pythonProjectsForUniversity\pythonProject\module_12_1_dz\data.txt')
print(df.head())





