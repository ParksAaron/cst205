from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

url = "http://www.thrashermagazine.com/"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(urlopen(req).read())
images = soup.findAll('img')
for image in images:
    print(image['src'])
