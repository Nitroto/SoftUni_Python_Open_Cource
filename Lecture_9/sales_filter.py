import sqlite3

DB = './data/sales-imported.db'

city_name = input('Въведете град: ')

with sqlite3.connect(DB, isolation_level=None) as connection:
    cursor = connection.cursor()
    cursor.execute('select id, item_key from catalog')
    catalog_id_to_item_key_mapping = {}
