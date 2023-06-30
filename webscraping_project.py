# Working on google colab
!pip install bs4
!pip install requests
!pip install pandas

url = "https://www.worldometers.info/coronavirus/"

import requests

response = requests.get(url)
print(response)

print(type(response))

response.content

# Importing beautiful soup
from bs4 import  BeautifulSoup

soup=BeautifulSoup(response.content,'html.parser')
print(type(soup))

print(soup.prettify()[:5000])

soup.select('title')

world_data=soup.find('tbody').find_all('tr')
print(world_data)

# finding the data in the table, first identify the row using loop then again use loop to identify the column data in a row to get the desired the data of a row.
complete_data=[]
for i in range(8,len(world_data)):
  data=[]
  list_data=world_data[i].find_all('td')
  for col in list_data:
    data.append(col.getText())
  complete_data.append(data)

complete_data[5] # printing the required data of a index 5 row, it will optput the data of 6th row

# understanding lambda
def square_num(x):
  return x**2

square_num(2)

square_num1=lambda x:x**2   # lambda uses to make functions easily 
square_num1(4)

square_num1=lambda x:print(x)
num=square_num1(4)
print(num)

# using map function to get sqroot of the list items, lambda function made it easy to get the sq rood. finally type casting the output object to list.
# Map function

sample_list=[1,2,3,4,5]
list(map(lambda x:x**2,sample_list))

maped_data=list(map(lambda x:x[1:10]+[x[12]]+[x[14]],complete_data))

maped_data

print(maped_data[4])

Column_names=[
    'names'
    'total cases'
    'new_cases'
    'total_deaths'
    'new _deaths'
    'total_recovered'
    'new_recovered'
    'active_cases'
    'serious_cases'
    'total_tests'
    'populations'
]

import pandas as pd

df=pd.DataFrame(complete_data)
df.head() #first five data means head

df=pd.DataFrame(complete_data)
df.head(10) # 10 datas

df.tail()  # last five datas

df=pd.DataFrame(maped_data, columns=column_names) # giving column names
df.head()

df.to_csv('covid_data.csv') #save to csv

df.to_csv('covid_data_summary.csv') #save to csv

#read data

df_read = pd.read_csv('covid_data_summary.csv')
print(type(df_read))

df_read.isnull()

import seaborn as sns

sns.heatmap(df_read.isnull().T)  #plotting heatmap using seaborn