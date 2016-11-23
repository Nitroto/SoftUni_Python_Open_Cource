from math import ceil


def is_valid_number(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


coverage = 1.76

input_w = input()
input_h = input()

if(is_valid_number(input_w) and is_valid_number(input_h)):
    w = float(input_w)
    h = float(input_h)
    surface = w * h
    print('{}'.format(ceil(surface/coverage)))
