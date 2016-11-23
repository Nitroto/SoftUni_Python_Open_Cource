import csv
import os

import datetime


def is_correct_file(fname):
    return os.path.isfile(fname) and os.path.getsize(fname) > 0

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
data = {}
cities = set()
if (is_correct_file(file_path)):
    with open(file_path, encoding='utf-8') as f:
        input_data = csv.reader(f)
        for row in input_data:
            if (len(row) != 0):
                line = row[0].split('-')
                if (len(row) != 3 or not is_valid_date(line[0], line[1], line[2]) or not is_correct_float(row[2])):
                    error = True
                    break
                date = datetime.datetime(int(line[0]), int(line[1]), int(line[2]))
                city = row[1]
                cities.add(city)
                temperature = float(row[2])
                if (date not in data):
                    data[date] = set()
                data[date].add(city)
    data_sorted = sorted(data.items(), key=lambda x: x[0], reverse=False)
    all_availeble = True
    if (not error):
        for d in data_sorted:
            current_cities = d[1]
            missing = cities - current_cities
            current_date = d[0]
            if(len(missing)>0):
                print('{:%Y-%m-%d},{}'.format(current_date, ','.join(sorted(missing))))
                all_availeble = False
        if(all_availeble):
            print('ALL DATA AVAILABLE')
    else:
        print('INVALID INPUT')
else:
    print('INVALID INPUT')
