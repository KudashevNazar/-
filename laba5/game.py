# Лаба 5: RPG "Алхімік". Запуск: python main.py

import config
import endings
from crafting import can_craft, craft
from inventory import Inventory
from ingredients import TYPES, create_ingredients, give_daily
from input_utils import ask_number
from potions import create_potions
from shop import sell_menu


def show_recipes(potions, ing_inv, ing_types):
    print("\n--- Рецепти (+ означає, що можна зварити зараз) ---")
    number = 1
    for potion in potions:
        mark = " "
        if can_craft(ing_inv, potion, ing_types):
            mark = "+"
        print(f" {mark}{number}. {potion['name']}: {', '.join(potion['recipe'])} -> {potion['price']} зол.")
        number += 1


def craft_menu(potions, ing_inv, potion_inv, ing_types):
    available = []
    for potion in potions:
        if can_craft(ing_inv, potion, ing_types):
            available.append(potion)
    if len(available) == 0:
        print("З наявних інгредієнтів нічого зварити не можна.")
        return
    print("\n--- Можна зварити ---")
    number = 1
    for potion in available:
        print(f"  {number}. {potion['name']} ({', '.join(potion['recipe'])}) -> {potion['price']} зол.")
        number += 1
    choice = ask_number("Що варити (0 - назад): ", 0, len(available))
    if choice != 0:
        craft(ing_inv, potion_inv, available[choice - 1], ing_types)


def play():
    ingredients = create_ingredients()
    potions = create_potions(list(TYPES.keys()))

    # словники для швидкого пошуку
    ing_types = {}  # назва інгредієнта -> тип
    for item in ingredients:
        ing_types[item["name"]] = item["type"]
    prices = {}  # назва зілля -> ціна
    for potion in potions:
        prices[potion["name"]] = potion["price"]

    ing_inv = Inventory("Інгредієнти", config.INGREDIENT_SLOTS, config.INGREDIENT_STACK)
    potion_inv = Inventory("Зілля", config.POTION_SLOTS, config.POTION_STACK)
    gold = config.START_GOLD
    day = 1

    print(endings.INTRO)
    give_daily(ing_inv, ingredients, config.START_INGREDIENTS)

    while True:
        got, lost = give_daily(ing_inv, ingredients, config.DAILY_INGREDIENTS)
        print(f"\n=== День {day}/{config.MAX_DAYS} | Золото: {gold}/{config.GOAL_GOLD} ===")
        print("Сьогодні видано:", ", ".join(got))
        if len(lost) > 0:
            print("Не вмістилось (втрачено):", ", ".join(lost))

        day_over = False
        while not day_over:
            print("\n1. Інвентар  2. Рецепти  3. Варити  4. Завершити день  0. Вихід")
            choice = ask_number("> ", 0, 4)
            try:
                if choice == 1:
                    ing_inv.show()
                    potion_inv.show()
                elif choice == 2:
                    show_recipes(potions, ing_inv, ing_types)
                elif choice == 3:
                    craft_menu(potions, ing_inv, potion_inv, ing_types)
                elif choice == 4:
                    print("\n--- Кінець дня: час продати зілля ---")
                    gold = sell_menu(gold, potion_inv, prices)

                    text = endings.no_money_for_rent(gold)
                    if text is None:
                        gold -= config.DAILY_RENT
                        print("Оренда: -", config.DAILY_RENT, "зол. Залишилось:", gold)
                        text = endings.check_end(day, gold)
                    if text is not None:
                        print("\n" + text)
                        return
                    day += 1
                    day_over = True
                else:
                    print("Вихід з гри.")
                    return
            except Exception as error:
                print("Сталася помилка:", error)


def main():
    try:
        play()
    except (KeyboardInterrupt, EOFError):
        print("\nГру перервано.")


main()