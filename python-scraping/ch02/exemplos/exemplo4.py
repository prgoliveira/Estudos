from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


html = urlopen('https://pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(), 'html5lib')
images = bs.find_all('img', {'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')})
for image in images:
    print(image['src'])
