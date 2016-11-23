import sqlite3

connection = sqlite3.connect('./data/sales-example.db')
print('Connected')

category_name = input('Въведете категория: ')
category_name = category_name.strip()

cursor = connection.cursor()
cursor.execute("select * from catalog where category = ?", [category_name])
results = cursor.fetchall()
print(results)
