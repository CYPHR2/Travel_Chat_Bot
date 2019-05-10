from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.actions import Action
from rasa_core.events import SlotSet

class ActionTravel(Action):
	def name(self):
		return 'action_travel'
	def run(self,dispatcher,tracker,domain):
		from apixu.client import ApixuClient
		api_key = '92ee3cfdbca94b0707aba0c190805190305'
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
		
		
