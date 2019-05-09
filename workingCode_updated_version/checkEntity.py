import wikipedia

def checkEntity(name):
	# Check for city name
	cityFile = 'cities.txt'
	placeFile = 'places.txt'
	with open(cityFile) as f:
		data = f.read().lower().split('\n')
		if(name.lower() in data):
			return 1

	with open(placeFile) as f:
		data = f.read().lower().split('\n')
		if(name.lower() in data):
			return 2

	return 0


def getCityInfo(Name):
	return wikiepedia.WikipediaPage(title=Name).summary
	
