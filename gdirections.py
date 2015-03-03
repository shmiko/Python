#Python Get Directions Script
from googlemaps import Client
from HTMLParser import HTMLParser
from sys import argv
gmaps = Client('AIzaSyCDyuMEpvjNHZS8ACf1rJPhxMOODrfJyL4')

#create googlemaps object
#mapService = Client(api_key)

#from http://stackoverflow.com/questions/753052/
#answer submitted by user Eloff
class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

#Get Directions from googlemaps
directions = gmaps.directions(argv[1],argv[2]) #('texarkana','atlanta')

#print each step in directions to console
#print int(directions['Directions'])#['Routes']['seconds'][0]['Steps']
#for step in directions:#['Directions']['Routes'][0]['Steps']:
#	print step[u'html_instructions']
for step in directions[0]['legs'][0]['steps']:#['seconds'][0]['Steps']:
  print strip_tags(step['html_instructions'])

#output to text file
with open('directions.txt','w') as f:
  for step in directions[0]['legs'][0]['steps']:#['seconds'][0]['Steps']:
    f.write(strip_tags(step['html_instructions']+'\r\n'))