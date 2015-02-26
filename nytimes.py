import urlparse
import urllib
from bs4 import BeautifulSoup

target_urls = "http://shmik.com"
html_page = "options.html"

url_stack = [target_urls] #stack of urls
visited_urls = [target_urls] #history of urls



data = []

while len(url_stack) > 0:
    # do something here to find the necessary values
    #print "Tagret URL is ", url_stack[0]
    htmltext = ""
    try:
      htmltext = urllib.urlopen(url_stack[0]).read()
    except:
      print "No Good", url_stack[0]
    soup = BeautifulSoup(htmltext)
    url_stack.pop(0)
    print len(url_stack)
    for tag in soup.findAll('a', href=True):
    #    data.append(tag[0])
      #print soup.findAll('a', href=True)
      tag['href'] = urlparse.urljoin(target_urls,tag['href'])
      #print tag['href']
      if target_urls in tag['href'] and tag['href'] not in visited_urls:
        url_stack.append(tag['href'])
        visited_urls.append(tag['href'])

print visited_urls




