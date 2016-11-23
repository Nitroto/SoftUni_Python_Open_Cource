import os


def is_correct_file(fname):
    return os.path.isfile(fname)


def is_not_empty(s):
    return bool(s and s.strip())


file_name_exchange = input()
file_name_amounts = input()

data = {}
print()
if (is_correct_file(file_name_exchange) and is_correct_file(file_name_amounts)):
    with open(file_name_exchange, encoding='utf-8') as f:
        print(f)
        for line in f:
            input_data = line.strip()
            if is_not_empty(input_data):
                currency_data = input_data.split()

                if (currency_data[0] not in data):
                    data[currency_data[0]] = 0
                data[currency_data[0]] = float(currency_data[1])

    with open(file_name_amounts, encoding='utf-8') as f:
        for line in f:
            input_data = line.strip()
            if is_not_empty(input_data):
                currency_data = input_data.split()
                currency = currency_data[1]
                if (currency in data):
                    quantity = float(currency_data[0])
                    value = quantity / data[currency]
                    print('{:.2f}'.format(value))
                else:
                    print('INVALID INPUT')
