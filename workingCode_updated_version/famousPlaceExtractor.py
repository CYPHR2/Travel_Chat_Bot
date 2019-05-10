import json
import random

def getFamousPlaces(cityName):
	path="JSONFiles/"+cityName.lower()+".json"
	
	with open(path) as f:
		data = json.load(f)

	famousPlaces = []
	for d in data[cityName.lower()]:
		famousPlaces.append(d['placeName'])
	
	places = []
	for  i in range(10):
		k = random.choice(famousPlaces)
			
		places.append(k)
		
		famousPlaces.remove(k)

	for i in range(len(places)):
		places[i] = places[i][4:].lstrip()

	return places
