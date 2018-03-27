
# from urllib2 import urlopen as webopen	# request to use URL
import requests
from bs4 import BeautifulSoup as soup  			# This library is required for Beautiful Soup.
 
myurl = 'https://www.amazon.in/gp/bestsellers/books'
# target url for scraping

page = requests.get(myurl)	#opens up connection with net
html_code = page.text		#reads all the data into the variable


page_soup = soup(page.text , "html.parser")				#soup page as html doc.

# print(page_soup)
for link in page_soup.findAll('div',{'class': 'zg_itemWrapper'}):
	
	temp = link.div.a.div.img["alt"]
	print(temp)
	for x in link.findAll("a" , {"class" : "a-size-small a-link-child"}):
		print(x.text) 
	con = link.findAll("span", {"class" : "a-icon-alt"})
	print((con[0]).text + "\n")


			
