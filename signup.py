from getpass import getpass
from validation import  *
import sqlite3

conn = sqlite3.connect('data.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS User 
	(id INTEGER PRIMARY KEY, username TEXT, password TEXT) ''')


username = input('Enter username: ')
password = getpass('Enter password: ')

parse = Validation(password)
print(parse.authenticate())

parser = Authentication(username)
print(parser.validate())

parse_4 = parse and parser

if parse_4 :
	cur.execute('INSERT OR IGNORE INTO User (username, password) VALUES (?,?)', (username, password) )
	conn.commit()

else :
	quit()


cur.execute('SELECT * FROM User WHERE id != (select max(id)) ')
row = cur.fetchall()
#print(row)
for rows in row :
	for info in rows :
		try :

			if username not in info :
				pass

			else:
				cur.execute('DELETE FROM User WHERE username = ?', (username, ) )
				conn.commit()
				print('Username already taken try again')
				break
	 
		except : 
			con_password = getpass('Confirm password: ')

			if  password == con_password :
				print('Signing in ......')
				break

			else:
				cur.execute('DELETE FROM User WHERE password = ?', (password, ) )
				conn.commit()
				print ('Password not matched')
				
cur.close()
