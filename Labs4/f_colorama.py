from colorama import Fore, Style, init

def colored_text(text):
    init()
    return f"{Fore.GREEN}{text}{Style.RESET_ALL}"