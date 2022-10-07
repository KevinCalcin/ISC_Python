import urllib.request, urllib.parse, urllib.error
import json

while True:
    address = input('Enter location:')
    if len(address) < 1: break

    print('Retrieving:',address)


    uh = urllib.request.urlopen(address)
    data = uh.read().decode()

    print('Retrieved:', len(data), 'characters')

    js = json.loads(data)
    sum = 0
    count = 0
    for user in js['comments']:
        sum = sum + int(user['count'])
        count = count+1

    print('Count:', count)
    print('Sum:', sum)
