import logging


def is_valid_number(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


count = 0
sum_of_prices = 0

# with open('../catalog_sample.csv') as f:
with open('../catalog_full.csv') as file:
    for line_number, line in enumerate(file):
        content = line.split(',')
        if content and content[0] and len(content) == 7 and is_valid_number(content[-1]):
            sum_of_prices += float(content[-1])
            count += 1
        else:
            logging.warning('Invalid line: {}'.format(line_number + 1))
if (count > 0):
    average = sum_of_prices / count
    print('{:.2f}'.format(average))
else:
    print('No prices')
