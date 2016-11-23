first_text = input('First text: ')
second_text = input('second text: ')

index = first_text.find(second_text)

if index == -1:
    print(first_text)
else:
    print(first_text[index + len(second_text):])
