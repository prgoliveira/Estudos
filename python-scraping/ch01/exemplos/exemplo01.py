from cgitb import html
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup


try:
    html = urlopen('https://pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
else:
    print('It Worked')

bs = BeautifulSoup(html.read(), 'html5lib')

print(bs)
