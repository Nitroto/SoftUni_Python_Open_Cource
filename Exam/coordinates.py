import os


def is_correct_file(fname):
    return os.path.isfile(fname) and os.path.getsize(fname) > 0


def is_not_empty(s):
    return bool(s and s.strip())


def is_non_zero_file(fpath):
    return True if os.path.isfile(fpath) and os.path.getsize(fpath) > 0 else False


def is_correct_float(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


current_x = 0
current_y = 0
file_path = input()
error = False

if (is_correct_file(file_path)):
    with open(file_path, encoding='utf-8') as f:
        for line in f:
            line_data = line.strip()
            if (is_not_empty(line)):
                data = line.split()
                if (len(data) != 2):
                    break
                    error = True
                direction = data[0].lower()
                positions = 0
                if (is_correct_float(data[1])):
                    positions += float(data[1])
                else:
                    error = True
                    break
                if (direction == 'up'):
                    current_y += positions
                elif (direction == 'down'):
                    current_y -= positions
                elif (direction == 'left'):
                    current_x -= positions
                elif (direction == 'right'):
                    current_x += positions
                else:
                    error = True
                    break
    if (not error):
        print('X {:.3f}\nY {:.3f}'.format(current_x, current_y))
    else:
        print('INVALID INPUT')
else:
    print('INVALID INPUT')
