import sqlite3

def createDB():
	conn = sqlite3.connect('DB.sqlite')
	c = conn.cursor()



	# creating test table
	c.execute('''
	CREATE TABLE "test" (
		"ID"	INTEGER PRIMARY KEY,
		"VALUE"	TEXT NOT NULL UNIQUE)
		''')


	# inserting some test value
	c.execute('INSERT INTO test (VALUE) VALUES (\'some test value\')')
	

	conn.commit()

	conn.close()