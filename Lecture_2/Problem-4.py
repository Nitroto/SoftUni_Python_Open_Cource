user_input = input('Input price: ')


def is_valid_number(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


prices = []
while user_input != 'stop':
    if is_valid_number(user_input):
        prices.append(float(user_input))
    user_input = input('Input price: ')

if len(prices) > 0:
    minimum = min(prices)
    maximum = max(prices)

    while minimum in prices:
        prices.remove(minimum)

    while maximum in prices:
        prices.remove(maximum)

    total = sum(prices)

    average = float(total / len(prices))
    print(average)
