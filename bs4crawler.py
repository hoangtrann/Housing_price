import bs4 as bs
import urllib.request
import re
import time


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


def num_result():
    source_url = 'https://batdongsan.com.vn/ban-can-ho-chung-cu-tp-hcm/p'
    source = urllib.request.urlopen(source_url)
    soup = bs.BeautifulSoup(source, 'lxml')
    result_tag = soup.find('div', class_="Footer")
    for result in result_tag.find_all('span', class_="greencolor"):
        if hasNumbers(result.string):
            result = re.findall(r'\d+', str(result))
    if len(result) == 2:
        result = int(result[0]) * 1000 + int(result[1])
    elif len(result) == 1:
        result = int(result[0])
    print("There are {} results".format(result))
    return result


def main():
    source_url = 'https://batdongsan.com.vn/ban-can-ho-chung-cu-tp-hcm/p'
    source = urllib.request.urlopen(source_url)
    soup = bs.BeautifulSoup(source, 'lxml')

    results = num_result()
    pages = round(float(results)/20 + 0.5)
    print("There are {} Pages!".format(pages))
    # Create lists to store data, should I do this in case data is big?
    # These list will be store to memory which will end up really bad!
    Restate_titles = []
    Restate_prices = []
    Restate_areas = []
    Restate_locs = []
    Restate_dstamps = []
    # Crawl, each page at a time, then pause for 10s
    time_started = time.asctime()
    for p in range(1, pages + 1):
        source = urllib.request.urlopen(source_url + str(p))
        soup = bs.BeautifulSoup(source, 'lxml')
        main_soup = soup.find('div', class_='Main')  # only take main body

        s = main_soup.find_all('div', class_='p-title')
        for title in re.findall(r'title="(.*?)"', str(s)):
            Restate_titles.append(title)

        for price in main_soup.find_all('span', class_='product-price'):
            Restate_prices.append(price.string.split('\r\n')[0])

        for area in main_soup.find_all('span', class_='product-area'):
            Restate_areas.append(area.string.split('\r\n')[0])

        for loc in main_soup.find_all('span', class_='product-city-dist'):
            loc = loc.string.split('\r\n')[1].split(',')[0]
            Restate_locs.append(loc)

        for dstamp in main_soup.find_all('div', class_='floatright'):
            Restate_dstamps.append(dstamp.string.split('\r\n')[0])
        print("Crawled Page {}".format(p))
        time.sleep(5)

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
        logs = """Crawling started at {}.
Crawl Finished at {}, with {} results, as {} pages.
""".format(time_started, time.asctime(), results, pages)
        saveLog.write(logs)


if __name__ == '__main__':
    main()
# TODO: create a log file, records day and time executed, results, pages.
# Time finished
# create id for each to filter data
