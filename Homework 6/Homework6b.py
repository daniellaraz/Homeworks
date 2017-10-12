from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
html = urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")

for link in soup.find_all('a'):
    print(link.get('href'))
#lst = []
#i = 0
#count = 7
#while i < count:
'''
tags = soup('a')
for tag in tags:
#    print('TAG: ', tag)
    print('URL: ', tag.get('href', None))
    print('URL: at position 18', tag.get('href', ))
    #print('Contents: ', tag.contents[0])
    #print('Attrs: ', tag.attrs)
#all_links = soup.find_all("a")
#all_links[3]
'''
#use beautiful soup to read in the position 3 link
