import sqlite3
import random
conn = sqlite3.connect('zadaca_1.db')
cursor = conn.cursor()
cursor.execute('''create table if not exists zadaca(ident integer, 
name text, 
opis text, 
status text)''')

ident = random.randint(1000000, 1000000000)
name = 'Gory'
opis = 'Posetit Gory'
status = 'vipolneno!!!'

cursor.execute('''insert into zadaca(ident, name, opis, status) values (?,?,?,?)''', (ident, name, opis, status))
conn.commit()
conn.close()