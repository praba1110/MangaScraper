import requests
import urllib
import bs4
import json
with open('mpdict.json', 'rb') as fp:
	mpdict = json.load(fp)
manga = raw_input('Enter the name of the manga that you want to download from (Note:If the name has spaces in it, replace the spaces with hyphens): ')
chapter = raw_input("Enter the chapter number that you want to download  : ")
url = 'http://www.mangapanda.com/'+str(mpdict[manga][0])+'-'+str(int(mpdict[manga][1])+int(chapter))+'-1/'+str(manga)+'/chapter-'+str(chapter)+'.html'
#this part the /bleach/ seems to not effect the url loading at all
h = {'User-Agent':'Mozilla/5.0'}
response = requests.get(url, headers=h)
soup = bs4.BeautifulSoup(response.text)
list = soup.select('option[value]')
link = [i['value'] for i in list]
for i in range(len(list)):
	pageres = requests.get('http://www.mangapanda.com'+link[i], headers=h)
	soup = bs4.BeautifulSoup(pageres.text)
	list = soup.select('img#img')
	name = list[0]['alt']
	imglink = list[0]['src']	
	urllib.urlretrieve(imglink, name+'.jpg')


