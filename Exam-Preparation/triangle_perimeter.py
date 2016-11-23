import math


def is_valid_number(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


input_a = input()
input_b = input()
input_c = input()

if (is_valid_number(input_a) and is_valid_number(input_b) and is_valid_number(input_c)):
    a = float(input_a)
    b = float(input_b)
    c = float(input_c)

    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))

    print('{:.2f}'.format(s))
else:
    print('INVALID INPUT')
