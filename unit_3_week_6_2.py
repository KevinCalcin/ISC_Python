import urllib.request, urllib.parse, urllib.error
import json,ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = 'http://py4e-data.dr-chuck.net/json?'


address = input('Enter location:')
if len(address) < 1: quit()

url = serviceurl + urllib.parse.urlencode({'address':address, 'key': 42})

print('Retrieving:',url)


uh = urllib.request.urlopen(url,context = ctx)
data = uh.read().decode()

print('Retrieved:', len(data), 'characters')

try:
    js = json.loads(data)
    #print(data)
except:
    print('error')

place_id = js['results'][0]['place_id']
print('Place id:',place_id)
