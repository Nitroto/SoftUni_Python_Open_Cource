import os


def is_correct_file(fname):
    return os.path.isfile(fname)


def is_not_empty(s):
    return bool(s and s.strip())


def is_valid_number(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


code = input()
file_name = input()
lowest_value = float('inf')
cheapest_city = ''

if (is_correct_file(file_name)):
    with open(file_name, encoding='utf-8') as f:
        for line in f:
            line_data = line.strip()
            if (is_not_empty(line_data)):
                data = line_data.replace('"', '').split(',')
                if (is_valid_number(data[-1])):
                    code_of_product = data[0]
                    if (code_of_product == code):
                        value = float(data[-1])
                        city = data[2]
                        if (value < lowest_value):
                            lowest_value = value
                            cheapest_city = city
else:
    print('INVALID INPUT')

print(cheapest_city)
