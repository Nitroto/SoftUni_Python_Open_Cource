import csv
import os


def is_correct_file(fname):
    return os.path.isfile(fname)


def is_not_empty(s):
    return bool(s and s.strip())


file_path = input()
temps = []
opened_time = []
if (is_correct_file(file_path)):
    with open(file_path, encoding='utf-8') as f:
        input_data = csv.reader(f)
        prev_temp = 0
        for row in input_data:
            row_data = tuple(row)
            temps.append(row_data)
        prev_temp = float(temps[0][1])
        for row in temps:
            current_temp = float(row[1])
            diff = current_temp - prev_temp
            prev_temp = current_temp
            if (diff >= 4.0):
                opened_time.append(row[0])
        if (len(opened_time) > 0):
            for time in opened_time:
                print(time)
        else:
            print('BAH')
else:
    print('INVALID INPUT')
