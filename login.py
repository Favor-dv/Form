from getpass import getpass
from validation import  *
import sqlite3

conn = sqlite3.connect('data.sqlite')
cur = conn.cursor()


username = input('Enter username: ')
password = getpass('Enter password: ')

parse = Validation(password)
print(parse.authenticate())

parser = Authentication(username)
print(parser.validate())

cur.execute('SELECT * FROM User ')
row = cur.fetchall()
#print(row)
for rows in row :
	for info in rows :
		print(info)
			
		if username and password not in rows   :
			print('Incorrect Username or Password')
			break

		else: 
			print ('Logging in .....')

cur.close()
