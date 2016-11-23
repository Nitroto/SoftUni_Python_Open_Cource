import csv
import os

import datetime


def is_correct_file(fname):
    return os.path.isfile(fname) and os.path.getsize(fname) > 0


def is_not_empty(s):
    return bool(s and s.strip())


def is_valid_date(y, m, d):
    try:
        datetime.datetime(int(y), int(m), int(d))
        return True
    except ValueError:
        return False


def is_correct_float(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


file_path = input()
error = False
items = {}
cities = {}
if (is_correct_file(file_path)):
    with open(file_path, encoding='utf-8') as f:
        input_data = csv.reader(f)
        for row in input_data:
            if (len(row) != 0):
                if (len(row) != 5):
                    error = True
                    break
                item_id = row[0]
                city = row[2]
                if (item_id not in items):
                    items[item_id] = set()
                items[item_id].add(city)
    for item in items:
        if (len(items[item]) == 1):
            value = list(items[item])[0]
            if (value not in cities):
                cities[value] = set()
            cities[value].add(item)
    sorted_cities = sorted(cities.items(), key=lambda x: x[0])

    if (not error):
        if(len(sorted_cities)>0):
            for city in sorted_cities:
                print('{},{}'.format(city[0], ','.join(sorted(city[1]))))
        else:
            print('NO UNIQUE SALES')
    else:
        print('INVALID INPUT')
else:
    print('INVALID INPUT')
