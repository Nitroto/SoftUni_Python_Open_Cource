import os
import math


def is_correct_file(fname):
    return os.path.isfile(fname) and os.path.getsize(fname) > 0


def is_not_empty(s):
    return bool(s and s.strip())


def is_correct_float(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


conversation_factor = 0.001
rakia = input()
file_path = input()
containers = {}
error = False
has_any = False
current_number = 1
if (is_correct_file(file_path) and is_correct_float(rakia) and float(rakia) > 0):
    with open(file_path, encoding='utf-8') as f:
        for line in f:
            line_data = line.strip()
            if (is_not_empty(line_data)):
                data = line_data.split(',')
                if (len(data) != 3 or not is_correct_float(data[1]) or not is_correct_float(data[2])):
                    error = True
                    break
                name = data[0]
                r = float(data[1])
                h = float(data[2])
                if (r <= 0 or h <= 0):
                    error = True
                    break
                current_volume = math.pi * (r * r * h) * conversation_factor

                if (current_volume >= float(rakia)):
                    if (name not in containers):
                        containers[data[0]] = current_volume
                        has_any = True
    if (not error):
        if (has_any):
            sorted_containers = sorted(containers.items(), key=lambda x: x[1])
            print('{}'.format(sorted_containers[0][0]))
        else:
            print('NO SUITABLE CONTAINER')
    else:
        print('INVALID INPUT')
else:
    print('INVALID INPUT')
