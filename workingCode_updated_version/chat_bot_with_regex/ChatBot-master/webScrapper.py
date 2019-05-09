from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
from urllib.request import Request
import os

def webScrapper():
	urlStart = "https://www.holidify.com/places/" 
	urlEnd = "/sightseeing-and-things-to-do.html"

	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

	with open('cities.txt') as cities:
		citiesList = cities.read().split('\n')
		citiesList.remove(citiesList[-1])

	places = citiesList

	dirName = "FamousPlaces"

	try:
		os.mkdir(dirName)
		print(f"Directory {dirName} created")
	except:
		print(f"Directory {dirName} already exists")

	htmlDirName = "HTMLFiles"

	try:
		os.mkdir(htmlDirName)
		print(f"Directory {htmlDirName} created")
	except:
		print(f"Directory {htmlDirName} already exists")


	# Start retrieving html files
	os.chdir(htmlDirName)
	for p in places:
		# Complete URL to parse
		myUrl = urlStart + p + urlEnd
		# If the above one doesnt work then use just urlStart + p
		print("================Started parsing "+p+"======================")
		print("getting html for "+p)
		try:
			req = Request(myUrl, headers=headers)
			htmlObject = uReq(req)
		except:
			# Just use https://holidify.com/places as the url
			try:
				req = Request(myUrl+p, headers=headers)
				htmlObject = uReq(req)
			except:
				print('The HTML page is not available for '+p)
				# if the html is not found then skip this city
				continue

		htmlFile = htmlObject.read()
		text = htmlFile.decode('utf-8')
		print("saving the html file")
		with open(p+'.html', 'w+') as myHTML:
			myHTML.write(text)		
		print('file '+p+'.html saved');
		
	# Go back to previous directory
	os.chdir('..')


