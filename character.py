import random as r
from logic import *
import random
from termcolor import colored

class Char:

    def __init__(self):
        self.attack = 8
        self.hp = 75
        self.shield = 5


class Enemy:
    def __init__(self):
        self.e_attack = 5
        self.e_hp = 60
        self.e_shield = 10

class Inventory:
    def __init__(self, weapon, armor):
        self.weapons = weapon
        self.armors = armor

    def add_weapon(self, weapon):
        self.weapons.append(weapon)
        print(colored(f"Вы получили {weapon}", 'red'))
        if len(self.weapons) > 1:
            print("You also have a second weapon.")
            while True:
                choice = input("Do you want to switch weapons? (yes/no): ")
                if choice.lower() == "yes":
                    self.weapons.remove(self.weapons[0])
                    self.weapons.remove(self.weapons[1])
                    self.weapons.append(Inventory.get_weapon())
                    self.weapons.append(Inventory.get_weapon())
                    break
                elif choice.lower() == "no":
                    break
                else:
                    print("Invalid choice. Please try again.")
                    continue
    
    def add_armor(self, armor):
        self.armors.append(armor)
        print(colored(f"Вы получили {armor}", 'red'))
        if len(self.armors) > 1:
            print("You also have a second armor.")
            while True:
                choice = input("Do you want to switch armors? (yes/no): ")
                if choice.lower() == "yes":
                    self.armors.remove(self.armors[0])
                    self.armors.remove(self.armors[1])
                    self.armors.append(Inventory.get_armor())
                    self.armors.append(Inventory.get_armor())
                    break
                elif choice.lower() == "no":
                    break
                else:
                    print("Неправильный ввод. Попробуйте ещё раз")
                    continue

    def get_weapon(self):
        weapon = ["Меч", "Топор", "Жезл", "Кинжал"]
        return random.choice(weapon)
    
    def get_armor(self):
        armor = ["Кожанная броня", "Кольчуга", "Железный нагрудник", "Щит"]
        return random.choice(armor)

    def display_inventory(self):
        if self.weapons[0] == None:
            print("Инвентарь пуст")
        else:
            print("Инвентарь:")
            if self.weapons:
                print(f"Оружие: {self.weapons[0]}")
            if self.armors:
                print(f"Броня: {self.armors[0]}")

    def equip(self):
        global max_hp

        if self.weapons[0] == None:
            print("Оружие не экиперовано")
            
        elif self.weapons[0] == "Меч":
            p.attack += 10
        elif self.weapons[0] == "Топор":
            p.attack += 15
        elif self.weapons[0] == "Жезл":
            p.attack += 5
        elif self.weapons[0] == "Кинжал":
            p.attack += 20
        
        if self.armors[0] == "Кожанная броня":
            p.shield += 1
            p.hp += 25
        elif self.armors[0] == "Кольчуга":
            p.shield += 2
            p.hp += 35
        elif self.armors[0] == "Железный нагрудник":
            p.shield += 3
            p.hp += 45
        elif self.armors[0] == "Щит":
            p.shield += 2
            p.hp += 15

def restore():
    p.hp = 75
    e.e_hp = 60
    return p.hp, e.e_hp

weapon = []
armor = []

inv = Inventory(weapon, armor)
p = Char()
e = Enemy()
