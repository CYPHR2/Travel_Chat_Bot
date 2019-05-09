import json
import os

allFiles = os.listdir('JSONFiles')

try:
	os.mkdir('DataFiles')
except:
	print('Directory already exists')

for eachCity in allFiles:
	cityName = eachCity.split('.')[0]
	with open('JSONFiles/'+eachCity) as jsonDoc:
		data = json.load(jsonDoc)
		dataCity = data[cityName]
		with open('DataFiles/'+cityName+'_f','w') as f:
			for x in dataCity:
				placeName = x['placeName'][4:].lstrip()
				stra = "- Tell me about "
				strb = "- Give me information about "
				strc = "- Info about "
				strd = "- Say about "
				str2 = " ["+placeName+"](famous_place)"
				finalString = stra+str2+"\n"	
				f.write(finalString)
				finalString = strb+str2+"\n"	
				f.write(finalString)
				finalString = strc+str2+"\n"	
				f.write(finalString)
				finalString = strd+str2+"\n"	
				f.write(finalString)
