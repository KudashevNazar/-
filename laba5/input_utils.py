# Безпечне введення чисел


def ask_number(text, low, high):
    """Питає число від low до high, поки гравець не введе правильно."""
    while True:
        try:
            number = int(input(text))
            if number < low or number > high:
                raise ValueError
            return number
        except ValueError:
            print("  Введіть число від", low, "до", high)