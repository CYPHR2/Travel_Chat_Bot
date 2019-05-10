from fuzzywuzzy import fuzz
import operator

with open('places.txt') as f:
	data = f.read().split('\n')

dataDict = {}

user = input(">> ")

for each  in data:
	dataDict[each] = fuzz.ratio(each.lower(),user.lower())

dataFinal = sorted(dataDict.items(), key=operator.itemgetter(1))
	
print(dataFinal[-1])
