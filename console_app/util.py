calculate_discount = lambda price, percent: price - (price * percent / 100)


def transaction_generator(transactions):
    for index, (stock , timestamp) in enumerate(transactions):
        yield f"{index}. Stock change: {stock}, Time: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}"

def get_valid_integer(message):
    while True:
        value = input(message)
        try:
            return int(value)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_valid_float(message):
    while True:
        value = input(message)
        try:
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a valid number.")