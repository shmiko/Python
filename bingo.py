#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (C) 2009 HalOtis Marketing
# written by Matt Warren
# http://halotis.com/
 
import urllib,urllib2
 
from BeautifulSoup import BeautifulSoup
 
def bing_grab(query):
 
    address = "http://www.bing.com/search?q=%s" % (urllib.quote_plus(query))
    request = urllib2.Request(address, None, {'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'} )
    urlfile = urllib2.urlopen(request)
    page = urlfile.read(200000)
    urlfile.close()
 
    soup = BeautifulSoup(page)
    links =   [x.find('a')['href'] for x in soup.find('div', id='results').findAll('h3')]
 
    return links
 
if __name__=='__main__':
    # Example: Search written to file
    links = bing_grab('halotis')
    print(links)