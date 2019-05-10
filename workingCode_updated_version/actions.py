from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import wikipedia
import famousPlaceExtractor as F
from fuzzywuzzy import fuzz
import operator

#def spellCheck(dispatcher,keyword):
#	with open('Test/places.txt') as f:
#		data = f.read().split('\n')
#	dataDict = {}
#	for each  in data:
#		dataDict[each] = fuzz.ratio(each.lower(),keyword.lower())
#	dataFinal = sorted(dataDict.items(), key=operator.itemgetter(1))
#
#	top5 = dataFinal[-5:]
#	if(top5[-1][1] == 100):
#		return keyword
#	else:
#		dispatcher.utter_message('Did you mean {}'.format(top5[-1][0]))
#		x = input("--> ")
#		if(x.lower() == 'y' or x.lower() == 'yes'):
#			return top5[-1][0]
#	
#	
#		else :
#			dispatcher.utter_message('Please choose one: ')
#			for a in top5[-5:]:
#				dispatcher.utter_message(a)
#			return keyword

class ActionTravel(Action):
	def name(self):
		return 'action_travel'
	def run(self,dispatcher,tracker,domain):
		from apixu.client import ApixuClient
		api_key = '92ee3cfdbca94baba0c190805190305'
		client = ApixuClient(api_key)
		
		loc = tracker.get_slot('location_state')
		current = client.gerCurrentWeather(q = loc)
		
		country = current['location']['country']
		city = current['location']['name']
		condition = current['current']['condition']['text']
		temperature_c = current['current']['temp_c']
		humidity = current['current']['humidity']
		wind_mph = current['current']['wind_mph']

		response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(condition, city, temperature_c, humidity, wind_mph)
						
		dispatcher.utter_message(response)
		return [SlotSet('location',loc)]
		
class ActionGetInfo(Action):
	def name(self):
		return 'get_infoX'
	
	def run(self, dispatcher, tracker, domain):		
		cityName = tracker.get_slot('famous_place')
		#cityName = spellCheck(dispatcher,cityName)
		#print(cityName)
		data = wikipedia.WikipediaPage(title=cityName).summary
		try:		
			#print(data)
			response = data
			dispatcher.utter_message(response)
			#return [SlotSet('famous_place_city'),cityName]
			return []
		except Exception as ex:
			print("Encountred Exception :--"+str(ex))
			

class GetFamousPlaces(Action):
	def name(self):
		return "get_famous_place"

	def run(self, dispatcher, tracker, domain):		
		cityName = tracker.get_slot('famous_places_2')
		dispatcher.utter_message(F.getFamousPlaces(cityName))
		return []
