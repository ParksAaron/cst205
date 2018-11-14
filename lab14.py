from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

url = "https://loremflickr.com/"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(urlopen(req).read(), features="lxml")
images = soup.findAll('img')
print(images[0]['src'])
hdr = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
req = Request("https://loremflickr.com/" + images[0]['src'], headers = hdr)
r = urlopen(req)
image = np.asarray(bytearray(r.read()), dtype="uint8")
image = cv2.imdecode(image, cv2.IMREAD_COLOR)
#LOREN IPSUM FLICKR