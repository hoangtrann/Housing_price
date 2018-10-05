import bs4 as bs
import urllib.request
import re
import time


# If any char of the string is number then hasNumbers return True
# This is for detecting the string which contains page results
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


# Find how many results there are, each page has 20 results
# then calculate the amout of pages to crawl
def num_result(source_url):
    source = urllib.request.urlopen(source_url)
    soup = bs.BeautifulSoup(source, 'lxml')
    result_tag = soup.find('div', class_="Footer")
    # Select source which contains number of result
    for result in result_tag.find_all('span', class_="greencolor"):
        if hasNumbers(result.string):
            result = re.findall(r'\d+', str(result))
    # Use re to take the number of result, format is 'XX,YYY'
    # result is a list, which usually has two items
    if len(result) == 2:
        # Which means, result = ['XX', 'YYY']
        result = int(result[0]) * 1000 + int(result[1])
    elif len(result) == 1:
        # result = ['YYY'] where XX = 0
        result = int(result[0])
    print("There are {} results".format(result))
    return result


def main():
    source_url = 'https://batdongsan.com.vn/ban-nha-dat-tp-hcm/p'
    source = urllib.request.urlopen(source_url)
    soup = bs.BeautifulSoup(source, 'lxml')

    results = num_result(source_url)
    pages = round(float(results)/20 + 0.5)
    print("There are {} Pages!".format(pages))

    # Stores data to list, this is bad when data can exceed the list limit
    # These list will be store to memory which will end up really bad!
    Restate_titles = []
    Restate_prices = []
    Restate_areas = []
    Restate_locs = []
    Restate_dstamps = []

    # Crawl each page at a time, then pause for to avoid damaging database
    time_started = time.asctime()
    for p in range(1, pages + 1):
        source = urllib.request.urlopen(source_url + str(p))
        soup = bs.BeautifulSoup(source, 'lxml')
        # Find main body of the source page
        main_soup = soup.find('div', class_='Main')

        # Title of the real estate project, store in class p-title
        s = main_soup.find_all('div', class_='p-title')
        for title in re.findall(r'title="(.*?)"', str(s)):
            Restate_titles.append(title)
        # Price of the real estate project, store in class_
        for price in main_soup.find_all('span', class_='product-price'):
            Restate_prices.append(price.string.split('\r\n')[0])
        # Square meter of the real estate project, store in class_
        for area in main_soup.find_all('span', class_='product-area'):
            Restate_areas.append(area.string.split('\r\n')[0])
        # Location of the real estate project, store in class_
        for loc in main_soup.find_all('span', class_='product-city-dist'):
            loc = loc.string.split('\r\n')[1].split(',')[0]
            Restate_locs.append(loc)
        # Posting Date of the real estate project, store in class_
        for dstamp in main_soup.find_all('div', class_='floatright'):
            Restate_dstamps.append(dstamp.string.split('\r\n')[0])
        print("Crawled Page {}".format(p))
        time.sleep(3)

    with open('Data_Titles.txt', mode='wt', encoding='utf-8') as saveTitles:
        for title in Restate_titles:
            saveTitles.write(title + '\n')

    with open('Data_Prices.txt', mode='wt', encoding='utf-8') as savePrices:
        for price in Restate_prices:
            savePrices.write(price + '\n')

    with open('Data_Areas.txt', mode='wt', encoding='utf-8') as saveAreas:
        for area in Restate_areas:
            saveAreas.write(area + '\n')

    with open('Data_Locs.txt', mode='wt', encoding='utf-8') as saveLocs:
        for loc in Restate_locs:
            saveLocs.write(loc + '\n')

    with open('Data_DStamps.txt', mode='wt', encoding='utf-8') as saveDStamps:
        for dstamp in Restate_dstamps:
            saveDStamps.write(dstamp + '\n')

    with open('Log.txt', mode='wt') as saveLog:
        logs = """
        Crawling started at {}.
        Crawl Finished at {}, with {} results, as {} pages.
        """.format(time_started, time.asctime(), results, pages)
        saveLog.write(logs)


if __name__ == '__main__':
    main()
# create index for each data
