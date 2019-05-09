import mysql.connector
import csv

mydb = mysql.connector.connect(
		host='localhost',
		user='root',
		passwd='kprateek09',
	)

mycursor = mydb.cursor()
mycursor.execute('DROP DATABASE IF EXISTS ChatBot')
mycursor.execute('CREATE DATABASE IF NOT EXISTS ChatBot')
mycursor.execute('USE ChatBot')
mydb.commit()

# Create table for tickets
mycursor.execute('DROP TABLE IF EXISTS AIR_TICKETS')

mycursor.execute('CREATE TABLE IF NOT EXISTS AIR_TICKETS (code varchar(5),ddate DATE, ffrom varchar(20),fto varchar(20),deptime DATETIME,arritime DATETIME,price varchar(5))')
mydb.commit()

# Add data to the tables
def fill_database(filename):
	with open(filename) as csvF:
		csvFile = list(csv.reader(csvF))

	query = "INSERT INTO AIR_TICKETS values( %s, %s, %s, %s, %s, %s, %s)"

	for row in csvFile:
		row[4] = ' '.join((row[1],row[4]))
		row[5] = ' '.join((row[1],row[5]))
		mycursor.execute(query,row)

	mydb.commit()


fill_database('tickets.csv')