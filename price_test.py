import bs4 as bs
import urllib.request
# import re

############ Main Program ############################################
# Source url for page's navigation, p1-px
source_url = 'https://batdongsan.com.vn/tags/ban/chung-cu-tphcm/p'
# open the url, define number of result (to identify number of page)
source = urllib.request.urlopen(source_url)
# take source of the first page
soup = bs.BeautifulSoup(source, 'lxml')

# TODO create table to store data

# Start crawling
real_estate_prices = []  # 2 types, net, and each square meter
real_estate_areas = []
real_estate_locs = []
real_estate_datestamps = []
main_soup = soup.find('div', class_='Main')  # only take main body

# Price for each
for price in main_soup.find_all('span', class_='product-price'):
    real_estate_prices.append(price.string)
    # print(price.string)
for area in main_soup.find_all('span', class_='product-area'):
    real_estate_areas.append(area.string)
    # print(area.string)

for loc in main_soup.find_all('span', class_='product-city-dist'):
    real_estate_locs.append(loc.string)
    # print(loc.string)
for dstamp in main_soup.find_all('div', class_='floatright'):
    real_estate_datestamps.append(dstamp.string)


print(real_estate_datestamps[0].split('\r\n')[1])
