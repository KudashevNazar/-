from f_requests import get_status
from f_numpy import array_stats
from f_pandas import make_dataframe
from f_matplotlib import save_plot
from f_rich import print_table
from f_colorama import colored_text
from f_pyfiglet import banner
from f_emoji import add_emoji
from f_faker import fake_person
from f_tqdm import progress
from f_random import random_numbers
from f_math import circle_area
from f_datetime import current_time
from f_json import save_json
from f_os import list_files


def main():
    print(banner("Lab 4"))
    print(colored_text("Старт програми: " + current_time()))
    print(add_emoji("Python це круто :thumbs_up:"))

    nums = random_numbers()
    print("Числа:", nums)
    print("Статистика:", array_stats(nums))
    print("Площа кола r=5:", round(circle_area(5), 2))

    df = make_dataframe(["Оля", "Іван", "Марія"], [19, 21, 20])
    print_table(df)

    person = fake_person()
    print("Фейкова людина:", person)
    save_json(person)

    save_plot(nums)
    print("HTTP статус:", get_status("https://example.com"))

    progress()
    print("Файли в папці:", list_files())


if __name__ == "__main__":
    main()