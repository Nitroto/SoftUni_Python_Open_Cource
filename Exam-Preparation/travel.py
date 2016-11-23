import os


def is_correct_file(fname):
    return os.path.isfile(fname)


def is_not_empty(s):
    return bool(s and s.strip())


def is_valid_number(number):
    try:
        int(number)
        return True
    except ValueError:
        return False


file_path = input()
total_time_in_minutes = 0
if (is_correct_file(file_path)):
    with open(file_path, encoding='utf-8') as f:
        for line in f:
            line_data = line.strip()
            if (is_not_empty(line_data)):
                data = line_data.split(',')
                if (is_valid_number(data[0]) and is_valid_number(data[1]) and is_valid_number(data[2])):
                    start = int(data[0])
                    end = int(data[1])
                    speed = int(data[2])
                    distance = (end - start) + 1
                    total_time_in_minutes += (distance / speed * 60)
else:
    print('INVALID INPUT')

hours = int(total_time_in_minutes / 60)
minutes = int(total_time_in_minutes % 60)
in_decimal = total_time_in_minutes / 60

print('{:.2f}'.format(in_decimal))
