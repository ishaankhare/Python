from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = 'https://www.amazon.in/s?k=playstation+5&crid=2WSYOPMYQHFZU&sprefix=playstation%2Caps%2C227&ref=nb_sb_ss_ts-doa-p_1_11'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'

#headers for your request
HEADERS = ({ 'User-Agent': f'{user_agent}', 'Accept-Language': 'en-US, en;q=0.5'})

#returns the html code for the URL in bytes
webpage = requests.get(URL, headers=HEADERS)

print(webpage)

#parse the bytes html code using bs
full_webpage = BeautifulSoup(webpage.content, "html.parser")

#extract the product links
all_links = full_webpage.findAll('a', attrs={'class': "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})

individual_link = all_links[0].get('href')

#construct the urls
base_url = 'https://www.amazon.in'
product_url = base_url + individual_link


#navigate to the product url and obtain the html doc
product_webpage = BeautifulSoup(requests.get(product_url, headers=HEADERS).content, 'html.parser')

#extract information the same way as above.





