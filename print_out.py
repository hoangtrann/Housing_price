Titles = open('Data_Titles.txt', 'r')
Prices = open('Data_Prices.txt', 'r')
Areas = open('Data_Areas.txt', 'r')
Locs = open('Data_Locs.txt', 'r')

length = len(Titles)

for i in length:
    print(Titles[i].decode('utf8'), "    ", Prices[i].decode('utf8'), "    ", Areas[i].decode('utf8'), "    ", Locs[i].decode('utf8'))
