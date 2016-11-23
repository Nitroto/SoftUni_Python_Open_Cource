def is_not_empty(s):
    return bool(s and s.strip())


input_string = input()
max_count = 0
max_character = 'a'
letters = []
if is_not_empty(input_string):
    for letter in input_string:
        character = letter
        if (character not in letters):
            letters.append(character)
            count = input_string.count(character)

            if(count>max_count):
                max_count = count
                max_character = character

    print(max_character)
else:
    print('INVALID INPUT')


