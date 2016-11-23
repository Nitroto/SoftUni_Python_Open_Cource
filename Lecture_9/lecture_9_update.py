import sqlite3

connection = sqlite3.connect('./data/sales-example.db', isolation_level=None)
print('Connected')

category_id = input('Въведете ID на категория: ')
category_id = category_id.strip()

category_name = input('Въведете ново име на категория: ')
category_name = category_name.strip()

cursor = connection.cursor()
cursor.execute("update catalog set category = ? where id = ?", [category_name, category_id])
results = cursor.fetchall()
print(results)
