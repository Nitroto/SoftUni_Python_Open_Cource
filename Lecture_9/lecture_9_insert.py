import sqlite3

connection = sqlite3.connect('./data/sales-example.db', isolation_level=None)
print('Connected')

item_key = input('Въведете ключ на артикула: ')
item_key = item_key.strip()

category_name = input('Въведете име на категория: ')
category_name = category_name.strip()

cursor = connection.cursor()
cursor.execute("insert into catalog (item_key, category) value (?,?)", [item_key, category_name])
results = cursor.fetchall()
print(results)
