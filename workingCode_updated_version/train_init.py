from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import logging
from rasa_core import config
from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

if __name__ == '__main__':
	logging.basicConfig(level='INFO')
	policies_var = config.load("policies.yml")	

	policies_var[0] = KerasPolicy(epochs=2)

	agent = Agent('travel_domain.yml', policies = policies_var)
	
	#training_data_file = './data/stories.md'
	training_data = agent.load_data('./data/stories.md')
	model_path = './models/dialogue'
	
	agent.train(training_data,validation_split = 0.2)
			
	agent.persist(model_path)
