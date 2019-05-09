from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import wikipedia

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
		data = wikipedia.WikipediaPage(title=cityName).summary
		try:		
			print(data)
			import pdb;pdb.set_trace()			
			print("----------------XXXXXXXXXXXXX__________________")
			str_data = str(data)
			print(str_data)
			print('IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII')
			response =data
			dispatcher.utter_message(response)

			return [SlotSet('famous_place'),cityName]
		except Exception as ex:
			print("Encountred Exception :--"+str(ex))
			
