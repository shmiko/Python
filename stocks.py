import urllib
import re

symbol_list = ["aapl","spy","goog","nflx"]
#https://au.finance.yahoo.com/q?s=appl&ql=1
i = 0

while i < len(symbol_list):
    url = "https://au.finance.yahoo.com/q?s=" + symbol_list[i] + "&ql=1"
    #print url
    htmlfile = urllib.urlopen(url)
    htmltext = htmlfile.read()
    #print htmltext
    regex = '<span id="yfs_l84_' + symbol_list[i] + '">(.+?)</span>'
    pattern = re.compile(regex)
    #print pattern
    price = re.findall(pattern,htmltext)
    print "The price of ", symbol_list[i], " is ", price
    i +=1





