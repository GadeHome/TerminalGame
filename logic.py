import random as r
from character import *
from main import *
from termcolor import colored
import os, time

atk = '1'
blk = '2'
abt = '3'
ptn = '4'
show_inv = '5'
run = '6'

cnt_floor = 1
dif = 0

weapon = inv.get_weapon()
armor = inv.get_armor()

floor = True

def game_logic():
    global floor
    floor = True
    print(colored("НАЧАЛО ВОСХОЖДЕНИЯ", 'cyan'))

    while floor == True:

        print("\nВведите '1' чтобы начать битву")
        print("Введите '2' чтобы открыть инвентарь")
        print("Введите '3' чтобы просмотреть характеристики героя")
        print("Введите '4' чтобы узнать текущий этаж")
        print("Введите '5' чтобы выйти\n")

        command = input("Введите действие: ")

        if command == stats:
            os.system('cls')
            print(colored(f'Атака: {p.attack}, здоровье: {p.hp}, защита: {p.shield}', 'yellow'))
        elif command == battle:
            progress_save()
            os.system('cls')
            fight()
            break
        elif command == inventory:
            os.system('cls')
            if cnt_floor <= 2:
                print(colored("Инвентарь пуст", 'green'))
            elif cnt_floor > 2:
                inv.display_inventory()
        elif command == status_floor:
            os.system('cls')
            print(cnt_floor)
        elif command == '5':
            os.system('cls')
            print("\nВыход из игры")
            quit()



def after_lose():
    global cnt_floor
    if lost_choose == 'y':
        os.system('cls')
        cnt_floor = 1
        restore()
        fight()
    elif lost_choose == 'n':
        os.system('cls')
        quit()
    else:
        os.system('cls')
        print("Неверный ввод, автоматический перезапуск")
        restore()
        fight()

inventory_equiped = None

def attack():

    if fstep % 2 == 1:
        e.e_hp -= p.attack * (1 - (e.e_shield / 100))
        e.e_hp = round(e.e_hp, 2)
    elif fstep % 2 == 0:
        p.hp -= e.e_attack * (1 - (p.shield / 100))
        p.hp = round(p.hp, 2)
    else:
        main_menu()

    return print(f'Ваше здоровье: {p.hp}, Здоровье врага: {e.e_hp}')

def block():
    p.hp += 20
    p.hp = round(p.hp, 2)
    return print(f'Вы получаете щит. Ваше здоровье: {p.hp}')

def ability():
    if fstep % 2 == 1:
        e.e_hp -= (p.attack * 1.5) * (1 - (e.e_shield / 100))
        e.e_hp = round(e.e_hp, 2)
    elif fstep % 2 == 0:
        p.hp -= e.e_attack * (1 - (p.shield / 100))
        p.hp = round(p.hp, 2)
    else:
        fight()
    return print(f'Ваше здоровье: {p.hp}, Здоровье врага: {e.e_hp}')
     

cnt_potion = 3
def potion_use():
    global cnt_potion

    if cnt_potion > 0:
        p.hp += 50
        if p.hp > max_hp:
            p.hp = max_hp
        cnt_potion -= 1
        print(colored('Вы использовали зелье. Ваше здоровье восстановлено', 'green'))
    else:
        print(colored("Зелье закончилось", 'green'))
    return p.hp


def safe_zone():
    global floor
    global cnt_potion
    global cnt_floor

    print(colored("\nВы находите пару случайных предметов\n", 'green'))
    print(colored("Запас зелей востановлен", 'yellow'))
    cnt_potion = 3

    choose = input("\nХотите продолжить? (y/n): ")
    if choose == 'y':
        cnt_floor +=1
        next_fight()
    elif choose == 'n':
        os.system('cls')
        print(colored("Ваше приключение на этом закончено. Вы остались в безопасной зоне навсегда", 'yellow'))
        quit()

    return cnt_potion




def fight_run():
    global run_choose
    run_choose = input("Вы уверены что хотите сбежать? (y/n): ")
    if run_choose == 'y':
        os.system('cls')
        print(colored("Вы сбежали. Ваши приключения на этом закончились. Вы встретили свой конец в холодном подвале башни\n\n", 'yellow'))
        quit()
    elif run_choose == 'n':
        os.system('cls')
        print(colored("\n\nВы продолжили бой", 'yellow'))
        fight()
    else:
        os.system('cls')
        print("Неверный ввод, автоматический перезапуск")
        restore()
        fight()


def progress_save():
    with open('save.txt', 'w') as f:
        f.write(f'floor_status={cnt_floor}\ninventory_status={inventory_equiped}\n')

def load_save():
    global cnt_floor, inventory_equiped
    try:
        with open('save.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                key, value = line.strip().split('=')
                globals()[key] = value
            print(f'Сохранение загружено. Текущий этаж: {floor_status}. Инвентарь: {inventory_status}')
            cnt_floor = floor_status
            inventory_equiped = inventory_status
            upgrade_dif()
            game_logic()
    except FileNotFoundError:
        print("Сохранение не найдено\n")
        game_logic()


def upgrade_dif():
    global dif, cnt_floor, max_hp

    dif = 0
    dif += 0.02 * int(cnt_floor)
    
    restore()
    max_hp = p.hp
    e.e_hp += e.e_hp*dif
    e.e_attack += e.e_attack*dif
    e.e_shield += e.e_shield*dif

    dif = 0
    return e.e_attack, e.e_shield, e.e_hp

def next_fight():

    global cnt_floor
    global floor
    global max_hp

    progress_save()
    if cnt_floor == 3:
        inv.add_weapon(weapon)
        inv.add_armor(armor)
    if cnt_floor == 5:
        print(colored("\n\nВы дошли до безопасного этажа", 'yellow'))
        safe_zone()
    elif cnt_floor == 10:
        print(colored("\n\nВы дошли до конца башни", 'yellow'))
        boss_fight()
    elif cnt_floor == 11:
        print(colored("\n\nВЫ ПРОШЛИ БАШНЮ", 'yellow'))
        quit()
    else:
        upgrade_dif()
        if cnt_floor >= 3:
            p.attack = 8
            inv.equip()
            max_hp = p.hp
        print(colored("\n\nПереход на следующий этаж\n", 'blue'))
        fight_floor = True
        while fight_floor:
            fight()

def boss_stats():

    e.e_hp = 250
    e.e_attack = 15
    e.e_shield = 8
    return e.e_attack, e.e_shield, e.e_hp

def boss_fight():
    global cnt_floor
    global floor

    boss_stats()
    print(colored("\n\nВЫ ВСТРЕТИЛИ БОССА\n", 'yellow'))
    print(colored(f'Здоровье босса: {e.e_hp}\n', 'red'))

    fight()

def battle_choose():
    print("\nВведите '1' чтобы аттаковать")
    print("Введите '2' чтобы блокировать")
    print("Введите '3' чтобы использовать заклинание " + colored(f"(осталось {2 - cnt_power_attack})", 'green'))
    print("Введите '4' чтобы использовать зелье" + colored(f"(осталось {cnt_potion})", 'green'))
    print("Введите '5' чтобы открыть инвентарь")
    print("Введите '6' чтобы сбежать\n")


def fight():
    global fstep
    global lost_choose
    global cnt_floor
    global cnt_power_attack, cnt_block
    global max_hp

    fstep = 0
    fight_floor = True
    cnt_power_attack = 0
    cnt_block = 0
    max_hp = p.hp

    progress_save()

    print(colored(f'Текущий этаж: {cnt_floor}', 'green'))
    print(colored(f'Ваше здоровье: {p.hp}, Здоровье врага: {e.e_hp}', 'yellow'))

    while True:
        fstep += 1
        if  fstep % 2 == 1:
            battle_choose()
            action = input("\nЧто ты выберешь: ")
            if action == atk:
                print(colored("\n\nВаш ход: атака", 'light_green'))
                attack()
            elif action == blk:
                if cnt_block < 1:
                    cnt_block += 1
                    print(colored("\n\nВаш ход: защита", 'light_green'))
                    block()
                else:
                    print(colored("\n\nВы уже использовали защиту", 'red'))
                    continue
            elif action == abt:
                if cnt_power_attack < 2:
                    cnt_power_attack += 1
                    print(colored("\n\nВаш ход: заклинание", 'light_green'))
                    ability()
                else:
                    print(colored("\n\nВы уже использовали максимальное кол-во заклинаний", 'red'))
                    continue
            elif action == ptn:
                print(colored("\n\nВаш ход: использование зелья\n", 'light_green'))
                potion_use()
            elif action == show_inv:
                fstep = 0
                if cnt_floor < 3:
                    print(colored("Инвентарь пуст", 'green'))
                elif cnt_floor >= 3:
                    inv.display_inventory()
                    continue
            elif action == run:
                print(colored("\n\nВаш ход: выход из боя", 'light_green'))
                fight_run()

        elif fstep % 2 == 0:
            if action == blk:
                print(colored("\n\nХод врага", 'light_red'))
                attack()
            else:    
                print(colored("\n\nХод врага", 'light_red'))
                attack()

        max_hp = 75

        if p.hp <= 0:
            print(colored("\nПОРАЖЕНИЕ\n", 'red'))
            fight_floor = 'lose'
            

        elif e.e_hp <= 0:
            print(colored("\nПОБЕДА\n", 'light_yellow'))
            fight_floor = 'victory'

        if fight_floor == 'victory':
            cnt_floor += 1
            upgrade_dif()
            return next_fight()
    
        elif fight_floor == 'lose':
            print("Поражение\n\n")
            print(colored("Вы хотите начать с начала? y/n: ", 'yellow'))
            lost_choose = input()
            return after_lose()