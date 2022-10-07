# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = input('Ingrese el conteo:')
count=int(count)
position = input('Introducir posición:')
position = int(position)

# Retrieve all of the anchor tags
tags = soup('a')
print('recuparando:',url)
l = range(count)
for x in l:
    search = tags[position-1].get('href', None)
    result= tags[position-1].contents[0]
    print('recuparando:',search)
    html = urllib.request.urlopen(search, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

print('recuparando: ',result)
