#nlu_model
from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Metadata,Interpreter


def train_nlu(data,config_file,model_dir):
	training_data = load_data(data)
	trainer  = Trainer(config.load('config_spacy.yml'))
	trainer.train(training_data)
	model_directory = trainer.persist(model_dir,fixed_model_name = 'travel_bot_nlu_1')


#example for testing the given tokenization of the sentence after the NLP models are created:
def run_nlu():
	interpreter = Interpreter.load('./models/nlu/default/travel_bot_nlu_1')
	print(interpreter.parse(u"what is Kerala .what is weather in kerala"))
	print("tainnnnnx")
if __name__ == '__main__':
	train_nlu('./data/nlu.md','config_spacy.yml','./models/nlu')
	run_nlu()
