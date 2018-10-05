from bs4 import BeautifulSoup
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()

soup = BeautifulSoup(sauce, 'lxml')

#print(soup.find_all('p'))
for paragraph in soup.find_all('p'):
	print(paragraph.string)