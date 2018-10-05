import pandas as pd

Titles = open('Data_Titles.txt', mode='r', encoding='utf-8').read().split('\n')
Prices = open('Data_Prices.txt', mode='r', encoding='utf-8').read().split('\n')
Areas = open('Data_Areas.txt', mode='r', encoding='utf-8').read().split('\n')
Locations = open('Data_Locs.txt', mode='r', encoding='utf-8').read().split('\n')
Datestamp = open('Data_DStamps.txt', mode='r', encoding='utf-8').read().split('\n')

key = len(Titles)
List = []
for i in range(key):
    List.append((Titles[i], Prices[i], Areas[i], Locations[i], Datestamp[i]))

df = pd.DataFrame(List)
df.columns= ['Title', 'Price', 'Area', 'Location', 'Date']

search = df[df['Location'].str.match('Thủ Đức')]
print(search[['Price']])

