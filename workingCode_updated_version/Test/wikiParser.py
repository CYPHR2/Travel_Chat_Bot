from wikipedia import WikipediaPage

with open('places.txt','r') as f:
	data = f.read().split('\n')
	#print(data)

dataDict = {}

for i, eachPlaces in enumerate(data):
	d = None
	try:
		d = WikipediaPage(title=eachPlaces)
		print(" Data for {} exists".format(eachPlaces))
	except:
		print(" Data for {} does not exist".format(eachPlaces))
		d = None

	dataDict[eachPlaces] = d


	if i>10:
		break

print(dataDict)
