from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import rasa_core
from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig
from rasa_core.run import serve_application
from rasa_core import config

logger = logging.getLogger(__name__)

def train_dialogue(domain_file = 'travel_domain.yml',
		    model_path = './models/dialogue',
		    training_data_file = './data/stories.md'):
	policies_var = config.load('policies.yml')
		
	agent = Agent(domain_file,policies = policies_var)
	training_data_var = agent.load_data(training_data_file)	
	agent.train(training_data_var,validation_split = 0.2)
	
	agent.persist(model_path)
	return agent
def run_travel_bot(serve_forever=True):
	interpreter_var = RasaNLUInterpreter('./models/nlu/default/travel_bot_nlu')
	action_endpoint_var = EndpointConfig(url="http://localhost:5055/webhook")
	agent = Agent.load('./models/dialogue', interpreter=interpreter_var, action_endpoint=action_endpoint_var)
	rasa_core.run.serve_application(agent ,channel='cmdline')
		
	return agent
	
if __name__ == '__main__':
	train_dialogue()
	run_travel_bot()
