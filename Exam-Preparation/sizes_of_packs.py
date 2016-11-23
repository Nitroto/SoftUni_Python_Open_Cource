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


def can_fit(w1, h1, d1, w2, h2, d2):
    if ((w1 > w2) and (h1 > h2) and (d1 > d2)):
        return True
    if ((w1 > w2) and (h1 > d2) and (d1 > h2)):
        return True
    if ((h1 > w2) and (w1 > h2) and (d1 > d2)):
        return True
    if ((h1 > w2) and (d1 > h2) and (w1 > d2)):
        return True
    if ((d1 > w2) and (w1 > h2) and (h1 > d2)):
        return True
    if ((d1 > w2) and (h1 > h2) and (w1 > d2)):
        return True


input_w = input()
input_h = input()
input_d = input()
file_name = input()

if (is_valid_number(input_d) and is_valid_number(input_h) and is_valid_number(input_d) and is_correct_file(file_name)):
    w = float(input_w)
    h = float(input_h)
    d = float(input_d)
    with open(file_name, encoding='utf-8') as f:
        for line in f:
            line_data = line.strip()
            if (is_not_empty(line_data)):
                medicament_data = line_data.split(',')
                medicament_name = medicament_data[0]
                if (is_valid_number(medicament_data[1]) and is_valid_number(medicament_data[2]) and is_valid_number(
                        medicament_data[3])):
                    first_side = float(medicament_data[1])
                    second_side = float(medicament_data[2])
                    third_side = float(medicament_data[3])
                if (can_fit(w, h, d, first_side, second_side, third_side)):
                    print(medicament_name)

else:
    print('INVALID INPUT')
