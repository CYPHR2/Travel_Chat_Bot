import mysql.connector
import json
import random
import os


mydb = mysql.connector.connect(
		host='localhost',
		user='root',
		passwd='kprateek09',
	)

mycursor = mydb.cursor()

def getData(cityName):
	realPath = os.getcwd()
	with open(realPath+'\\JSONFiles\\'+cityName.lower()+'.json') as jsonFile:
		jsonData = json.load(jsonFile)

	index = []
	data = jsonData[cityName.lower()]
	for i in range(5):
		k = random.randint(0,len((jsonData[cityName.lower()])))
		if k not in index:
			index.append(k)
			placeName = data[k]['placeName'][4:].lstrip()
			placeDesc = data[k]['placeDesc']
			print("="*80)
			print(placeName+'--->')
			print(placeDesc)
			print("="*80)


def famousPlace(placeName):
	
	cwd = os.getcwd()
	jsonFileNames = os.listdir(cwd+"\\JSONFiles\\")

	for filename in jsonFileNames:
		with open(cwd+"\\JSONFiles\\"+filename) as file:
			data = json.load(file)
			for row in data[list(data.keys())[0]]:
				if(row['placeName'][4:].lower().lstrip() == placeName.lower()):
					print(row['placeDesc'])
			

#famousPlace('jawaharlal nehru planetarium')
	


