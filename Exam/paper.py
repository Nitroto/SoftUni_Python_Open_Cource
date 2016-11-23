import math

loses = 0.098


def is_correct_float(str):
    try:
        float(str)
        if (float(str) > 0.0):
            return True
        else:
            return False
    except ValueError:
        return False


input_sheet = input()
input_h = input()
input_w = input()
input_d = input()

if (is_correct_float(input_sheet) and is_correct_float(input_h) and is_correct_float(input_w) and is_correct_float(
        input_d)):
    sheet = float(input_sheet)
    h = float(input_h)
    w = float(input_w)
    d = float(input_d)
    total_array = 2 * ((h * d) + (h * w) + (w * d))
    needed = total_array * (1 + loses)
    sheets_needed = needed / sheet
    sheets = math.ceil(sheets_needed)
    print(sheets)
else:
    print('INVALID INPUT')
