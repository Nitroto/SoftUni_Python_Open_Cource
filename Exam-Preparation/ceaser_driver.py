normal_alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
    'X',
    'Y', 'Z']


def is_valid_number(number):
    try:
        a = int(number)
        if (a >= 0):
            return True
    except ValueError:
        return False


def generate_drivers_alpfabet(key):
    firstPart = normal_alphabet[key:]
    secondPart = normal_alphabet[:key]
    drivers_alphabet = firstPart + secondPart
    return drivers_alphabet


def is_correct_char(char):
    try:
        normal_alphabet.index(char)
        return True
    except ValueError:
        return False


key = input()
message = input()
value_A = ord('A')
value_Z = ord('Z')

if (is_valid_number(key)):
    value = int(key) % len(normal_alphabet)
    key_value = value
    drivers_alphabet = generate_drivers_alpfabet(key_value)
    output = ''
    for letter in message:
        # print(letter)
        if (is_correct_char(letter)):
            index = normal_alphabet.index(letter)
            output += drivers_alphabet[index]
            # print(drivers_alphabet[index])
        else:
            output += letter

    print(output)
else:
    print('INVALID INPUT')
