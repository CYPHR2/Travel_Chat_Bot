import re
import spacy
import mysql.connector
import cities
import os
import json
import nltk
import numpy as np

GREETINGS = ['Hi', 'Hello']
FLIGHTS = ['flight','airplane','ticket',]
CUR_CITY = 'BANGALORE'
CITIES = []
FAMOUS_PLACES_DICT = {}
FAMOUS_PLACES = {}
ATT = ['famous','place','tourist','attractions','info','about']
BOT = 'BOT: {0}'

# use database

mydb = mysql.connector.connect(
		host='localhost',
		user='root',
		passwd='kprateek09',
		db='ChatBot',
	)

mycursor = mydb.cursor()

def createPlacesList():
	cwd = os.getcwd()
	jsonFileNames = os.listdir(cwd+"\\JSONFiles\\")

	for filename in jsonFileNames:
		with open(cwd+"\\JSONFiles\\"+filename) as file:
			data = json.load(file)
			cityName = list(data.keys())[0]
			for row in data[cityName]:
				placeName = row['placeName'][4:].lower().lstrip()
				placeDesc = row['placeDesc']
				FAMOUS_PLACES_DICT[cityName] = (placeName, placeDesc)
				FAMOUS_PLACES[placeName] = cityName
	

def getFamousPlace(user_input):

	ui = user_input
	print(ui)
	print(ui.split(' '))
	if(len(ui.split(' ')) == 1):
		d = ' '.join(list(FAMOUS_PLACES.keys())).split(' ')
		k = []
		for x in d:
			k.append(nltk.edit_distance(ui.lower(), x))

		x_1 = np.argmin(np.asarray(k))
		matchedPlaces = []
		for each in list(FAMOUS_PLACES.keys()):
			if(re.search(d[x_1],each,re.I)):
				matchedPlaces.append(each)
		if(len(matchedPlaces)>1):
			print("We have found the following matches based on your keyword, Choose the appropeiate one: ")
			inputChoice = 0
			for i, z in enumerate(matchedPlaces): 
				print(str(i+1)+'.'+z)
			inputChoice = int(input())-1

			if(inputChoice > len(matchedPlaces)-1):
				print('Wrong Choice')
				return

			key = matchedPlaces[inputChoice]
			print(cities.famousPlace(key))
		else:
			print(cities.famousPlace(matchedPlaces[0]))


	else:
		print(cities.famousPlace(ui))
		

def createCitiesList():
	cwd = os.getcwd()
	cities = os.listdir(cwd+"\\JSONFiles\\")

	for c in cities:
		cityName = c.split('.')[0].upper()	
		CITIES.append(cityName)



def processFlight(user_input):
	c = re.findall('|'.join(CITIES), user_input, re.I)
	if len(c) == 1:
		return (CUR_CITY, c[0].upper())
	elif len(c) == 2:
		return (c[0].upper(),c[1].upper())

def getTickets(a, b):
	query = "SELECT * FROM AIR_TICKETS where ffrom=%s and fto=%s"
	table = []
	mycursor.execute(query,(a,b))
	for row in mycursor:
		table.append(row)

	return table

def main():
	while(True):
		user_input = input('USER: ')

		# First check for greeting
		if(re.search('|'.join(GREETINGS), user_input, re.I)):
			response = 'Hi This is BiBot'
			print(BOT.format(response))

		
		else:
			# In else, check for airplane tickets
			if(re.search('|'.join(FLIGHTS), user_input, re.I)):
				# Return flight tickets
				resp = processFlight(user_input)
				response = getTickets(*resp)
				print(BOT.format('Here are the flights from {0} to {1}'.format(resp[0],resp[1])))
				print(response)
			# Famous places
			elif(re.search('|'.join(ATT),user_input,re.I)):	
				famousP = re.search('|'.join(list(FAMOUS_PLACES.keys())).lower(), user_input, re.I)
				#print(famousP.group(0))
				if(famousP != None):
					print('Here is some info about '+famousP.group(0))
					print(getFamousPlace(famousP.group(0)))
					return
				cityName = re.search('|'.join(CITIES),user_input,re.I)
				#print(cityName)
				if(cityName):
					print(cityName.group(0))
					cities.getData(cityName.group(0))
					return


createCitiesList()
createPlacesList()
#print(FAMOUS_PLACES)
main()
#d = list(FAMOUS_PLACES.keys())
#d = '|'.join(d)
#print(re.search(d,'Tell me about Cubbon Park',re.I).group(0)[0])
#getFamousPlace('Cubbon Park')
