exclusions = ['van', 'von', 'fon', 'der', 'bin', 'd-r', 'д-р', 'phd', 'prof']  # and others

name = input('Enter your name: ').split()

elements = len(name)
initials = ''

if elements > 0:
    for word in name:
        if word not in exclusions and '.' not in word:
            initials += word[0] + '.'
    print(initials)

if len(initials) < 1:
    print('Incorrect name!')
