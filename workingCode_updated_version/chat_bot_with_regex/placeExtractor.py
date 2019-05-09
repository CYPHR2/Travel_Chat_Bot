
import json
import os

allFiles = os.listdir('JSONFiles')

with open('places.txt','w') as f:
	for eachCity in allFiles:
		cityName = eachCity.split('.')[0]
		with open('JSONFiles/'+eachCity) as jsonDoc:
			data = json.load(jsonDoc)
			dataCity = data[cityName]
			for x in dataCity:
				placeName = x['placeName'][4:].lstrip()+"\n"
				f.write(placeName)
