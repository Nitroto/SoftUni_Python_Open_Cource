text = input('Input string: ')

if 10 > len(text):
    print(text)
else:
    print(text[0:10] + '...')
