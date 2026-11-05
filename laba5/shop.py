# Продаж зілль наприкінці дня

from input_utils import ask_number


def sell_one_kind(gold, potion_inv, prices, name, amount):
    """Продає amount зілль з назвою name. Повертає нову суму золота."""
    if potion_inv.remove(name, amount):
        earned = prices[name] * amount
        print(f"  Продано {name} x{amount} за {earned} зол.")
        return gold + earned
    print("  Не вистачає зілль!")
    return gold


def sell_menu(gold, potion_inv, prices):
    """Меню ринку. Повертає суму золота після продажу."""
    while True:
        names = []
        for slot in potion_inv.slots:
            if slot[0] not in names:
                names.append(slot[0])
        if len(names) == 0:
            print("Зілль для продажу немає.")
            return gold

        print("\n=== Ринок ===")
        number = 1
        for name in names:
            print(f"  {number}. {name} x{potion_inv.count(name)} - {prices[name]} зол./шт.")
            number += 1
        print("  A. Продати все")
        print("  0. Завершити торгівлю")

        answer = input("Що продати (номер / A / 0): ").strip().lower()
        try:
            if answer == "a":
                for name in names:
                    gold = sell_one_kind(gold, potion_inv, prices, name, potion_inv.count(name))
                return gold
            number = int(answer)
            if number == 0:
                return gold
            name = names[number - 1]  # якщо номер хибний - буде IndexError
            how_many = ask_number("  Скільки штук: ", 1, potion_inv.count(name))
            gold = sell_one_kind(gold, potion_inv, prices, name, how_many)
        except (ValueError, IndexError):
            print("  Некоректний вибір.")