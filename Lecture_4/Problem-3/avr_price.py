import logging


def get_average(ls):
    sum_of_prices = 0
    for price in ls:
        sum_of_prices += price
    if len(ls) > 0:
        return sum_of_prices / len(ls)
    else:
        return 0


def is_valid_number(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


kid = []
men = []
unisex = []
women = []

# with open('../catalog_sample.csv') as f:
with open('../catalog_full.csv') as file:
    for line_number, line in enumerate(file):
        content = line.split(',')
        if content and content[0] and len(content) == 7 and is_valid_number(content[-1]):
            if (content[-2].lower() == 'kid'):
                kid.append(float(content[-1]))
            elif (content[-2].lower() == 'men'):
                men.append(float(content[-1]))
            elif (content[-2].lower() == 'unisex'):
                unisex.append(float(content[-1]))
            else:
                women.append(float(content[-1]))
        else:
            logging.warning('Invalid line: {}'.format(line_number + 1))

print('Kids: {:.2f}'.format(get_average(kid)))
print('Mans: {:.2f}'.format(get_average(men)))
print('Unisex: {:.2f}'.format(get_average(unisex)))
print('Women: {:.2f}'.format(get_average(women)))
