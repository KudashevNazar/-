# Варіння зілль

from input_utils import ask_number


def count_by_type(inventory, ing_types):
    """Скільки інгредієнтів кожного типу є в інвентарі."""
    result = {}
    for slot in inventory.slots:
        type_name = ing_types[slot[0]]
        result[type_name] = result.get(type_name, 0) + slot[1]
    return result


def can_craft(inventory, potion, ing_types):
    """True, якщо для рецепта є інгредієнти кожного потрібного типу."""
    try:
        have = count_by_type(inventory, ing_types)
        for type_name in potion["recipe"]:
            if have.get(type_name, 0) < 1:
                return False
        return True
    except KeyError:
        return False


def craft(ing_inv, potion_inv, potion, ing_types):
    """Варить зілля: гравець обирає інгредієнт для кожного типу з рецепта."""
    chosen = []
    print("\nВаримо:", potion["name"])
    for type_name in potion["recipe"]:
        options = []
        for slot in ing_inv.slots:
            if ing_types[slot[0]] == type_name and slot[0] not in options:
                options.append(slot[0])
        print(f" Оберіть інгредієнт типу '{type_name}' (0 - скасувати):")
        number = 1
        for name in options:
            print(f"  {number}. {name} (є {ing_inv.count(name)})")
            number += 1
        choice = ask_number(" > ", 0, len(options))
        if choice == 0:
            print("Варіння скасовано.")
            return
        chosen.append(options[choice - 1])

    if potion_inv.free_space(potion["name"]) < 1:
        print("Немає місця в інвентарі зілль! Спочатку продайте зілля.")
        return

    for name in chosen:
        ing_inv.remove(name, 1)
    potion_inv.add(potion["name"], 1)
    print("Зварено:", potion["name"], "!")