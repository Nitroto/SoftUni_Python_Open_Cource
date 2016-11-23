import os


def is_correct_file(fname):
    return os.path.isfile(fname)


def is_not_empty(s):
    return bool(s and s.strip())


def contains_in_key(char, word):
    try:
        word.index(char)
        return True
    except ValueError:
        return False


def convert_string_to_list(str):
    string_as_list = []
    for letter in str:
        string_as_list.append(letter)
    return string_as_list


file_path = input()
key_word = input()
key_word_as_list = convert_string_to_list(key_word)
anagrams = []

if (is_correct_file(file_path)):
    with open(file_path, encoding='utf-8') as f:
        for line in f:
            anagram = False
            current = line.strip()
            if (is_not_empty(current)):
                current_word = convert_string_to_list(current)
                if (len(current_word) == len(key_word_as_list) and current != key_word):
                    anagram = True
                    temp_list = convert_string_to_list(key_word)
                    for letter in current_word:
                        if (contains_in_key(letter, temp_list)):
                            index = temp_list.index(letter)
                            temp_list[index] = '@'
                        else:
                            anagram = False
            if (anagram):
                anagrams.append(current)
    if (len(anagrams) > 0):
        sorted_anagrams = sorted(anagrams, key=str.lower)
        for word in sorted_anagrams:
            print(word)
    else:
        print('NO ANAGRAMS')
else:
    print('INVALID INPUT')
