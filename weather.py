#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 10 - weather.py
# Fetch the weather forecast from the National Weather Service.

import sys, urllib, urllib2
from bs4 import BeautifulSoup

if len(sys.argv) < 2:
    print >>sys.stderr, 'usage: weather.py CITY, STATE'
    exit(2)

data = urllib.urlencode({'inputstring': ' '.join(sys.argv[1:])})
info = urllib2.urlopen('http://forecast.weather.gov/zipcity.php', data)
content = info.read()



# Solution #2
soup = BeautifulSoup(content)  # doctest: +SKIP
big = soup.find('td', 'big')
if big.font is not None:
    big = big.font
print 'Condition:', big.contents[0].string.strip()
temp = big.contents[3].string or big.contents[4].string  # can be either
print 'Temperature:', temp.replace('&deg;', ' ')
tr = soup.find('b', text='Humidity').parent.parent.parent
print 'Humidity:', tr('td')[1].string
print