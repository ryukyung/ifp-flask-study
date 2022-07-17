import sqlite3
database = sqlite3.connect("TestDB.db")

cur = database.cursor()
cur.execute('''CREATE TABLE ANIMATION(
    TITLE TEXT,
    CHARACTER TEXT,
    STARTYEAR INTEGER)
''')
cur.execute("INSERT INTO ANIMATION VALUES('짱구는 못말려', '짱구', 1990)")
cur.execute("INSERT INTO ANIMATION VALUES('도라에몽','도라에몽',1969)")
database.commit()
database.close()
