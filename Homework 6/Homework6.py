from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
html = urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")

lst = []

for tag in soup.find_all(class_ = "comments"):
    lst.append(tag.get_text())

list_of_numbers = list(map(int, lst))
print(sum(list_of_numbers))
