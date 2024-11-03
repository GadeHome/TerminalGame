import random as r
from termcolor import colored, cprint
import time
import os

from logic import *
from character import *


market = "shop"
status_floor = "4"
stats = "3"
inventory = "2"
battle = "1"

ex = "4"
faq = "3"
save = "2"
start = "1"

def intro():
    os.system('cls')
    print(colored(r" ______  __                                                                      __", 'yellow'))                     
    print(colored(r"/\__  _\/\ \                         __          __                             /\ \__", 'yellow'))                  
    print(colored(r"\/_/\ \/\ \ \___      __       _ __ /\_\    ____/\_\    ___      __         ____\ \ ,_\    __     _ __", 'yellow')) 
    print(colored(r"   \ \ \ \ \  _ `\  /'__`\    /\`'__\/\ \  /',__\/\ \ /' _ `\  /'_ `\      /',__\\ \ \/  /'__`\  /\`'__\ ", 'yellow'))
    print(colored(r"    \ \ \ \ \ \ \ \/\  __/    \ \ \/ \ \ \/\__, `\ \ \/\ \/\ \/\ \L\ \    /\__, `\\ \ \_/\ \L\.\_\ \ \/ ", 'yellow'))
    print(colored(r"     \ \_\ \ \_\ \_\ \____\    \ \_\  \ \_\/\____/\ \_\ \_\ \_\ \____ \   \/\____/ \ \__\ \__/.\_\\ \_\ ", 'yellow'))
    print(colored(r"      \/_/  \/_/\/_/\/____/     \/_/   \/_/\/___/  \/_/\/_/\/_/\/___L\ \   \/___/   \/__/\/__/\/_/ \/_/ ", 'yellow'))
    print(colored(r"                                                                 /\____/", 'yellow'))                              
    print(colored(r"                                                                 \_/__/", 'yellow'))  

    print(colored("~~Главное меню~~\n", attrs=["bold"]))
    print(colored("1. Начать восхождение", 'blue', attrs=['bold']))
    print(colored("2. Запустить сохранение"))
    print(colored("3. Справочник"))
    print(colored("4. Выход\n\n"))


def main_menu(): #основная механика игры
    global status
    intro()
    s = input("Введите число от 1 до 4: ")
    status = s
    return main_choose()

def main_choose():
    if status == start:
        print(colored("\nНачало восхождения\n", 'red', attrs=["bold"]))
        story()

    elif status == save:
        print("\nПоиск сохранения\n")
        load_save()

    elif status == faq:
        print(colored("РПГ игра про рыцаря и его восхождение по башне\n", 'yellow'))
        game_logic()
        
    elif status == ex:
        print("\n\nВыход из игры")
        quit()

    elif status == battle:
        print("\nВведите '1' чтобы аттаковать")
        print("Введите '2' чтобы блокировать")
        print("Введите '3' чтобы использовать заклинание")
        print("Введите '4' чтобы использовать зелье")
        print("Введите '5' чтобы сбежать\n")

    elif status == market:
        print("\nВведите '1' для выбора предмета")
        print("Введите '2' чтобы продать предметы")
        print("Введите '3' чтобы уйти\n")
    else:
        print("\nвведено неправильное число, попробуйте ещё раз\n")
        main_menu()

def story():
    global i
    loading = [
    'Где я?',
    'Что это за место?',
    'Боже, я ничего не помню. Как я тут оказался!?',
    'Ладно, не паниковать, надо выбираться отсуда',
    'Боже! Как же тут темно. Стоп. Здесь что-то есть. Похоже это лестницу. Кажется это единсвтенный путь выбраться отсюда.\n'
    ]
    os.system('cls') 
    i = 0
    
    for value in loading:
        print(value)
        time.sleep(0.4)
        i += 1
        if i == len(loading):
            game_logic()
            break

def market_choose():
    print("\nВведите '1' для выбора предмета")
    print("Введите '2' чтобы продать предметы")
    print("Введите '3' чтобы уйти\n")

if __name__ == '__main__':
    main_menu()
