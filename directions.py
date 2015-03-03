#Python Get Directions Script
from googlemaps import GoogleMaps

#create googlemaps object
mapService = GoogleMaps()

#Get Directions from googlemaps
directions = mapService.directions('texarkana','atlanta')

#print each step in directions to console

for step in directions['Directions']['Routes'][0]['Steps']:
	print step['descriptionHtml']