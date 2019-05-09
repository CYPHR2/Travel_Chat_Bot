# ChatBot
This is the final year group project. We are building a generative based travel agent chatbot.

## cities.txt 
Contains the names of the cities which need to be parsed.

## webScrapper.py 
webScrapper() - Reads the cities.txt file and then scrapes the data from holidify.com website and saves the html files.

## parser.py 
parser\_function(): This function parses the html files and then generates json files which contain the famous places in cities with their description.

getCity(cityName): This function takes in a cityName as an argument and returns a dictionary of famous places in that city if it exits or else will print data not found error if the data for that city does not exists i.e, the json file for that city does not exist
