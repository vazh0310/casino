#!/usr/bin/env python3
from random import randint
import os
import platform
import config

def welcome():
    print("Добро пожаловать в казино!")

def is_right_system():
    if os.name == 'nt':
        print("Данное ПО не может работать на Windows. Пожалуйста, установите Linux.")
        return False
    elif os.name in ['posix', 'unix'] or platform.system() in ['Linux', 'FreeBSD']:
        if 'microsoft' in platform.release():
            print("Слушай, а ловко ты это придумал, я даже в начале и не понял.\nДанное ПО не может работать под WSL. Пожалуйста, установите настоящий Linux.")
            return False
        else:
            print(f"{platform.system()} - хороший выбор!")
            return True
    else:
        print("Ты под чем работаешь, дурень?!?")
        return False

def casino(money):
    rolled = randint(config.min_num, config.max_num)
    if rolled < money:
        print("Вы проиграли...")
    elif rolled > money:
        print(f"Вы выиграли {rolled} денег!")
    elif rolled == money:
        print("Счет не изменился.")
    elif rolled == config.max_num:
        print("МЕГА-ВЫИГРЫШ! Вы выиграли максимально возможную сумму!")
    else:
        print("Что? Что? ЧТО-О-О-О-О-О-О? Это что такое?")

def play_casino():
    money_set = int(input("Ваша ставка? "))
    if money_set:
        casino(money_set)
        retry = input("Продолжить? (Y/n) ")
        if retry.lower() in ['y', 'yes', 'д', 'да']:
            play_casino()
        else:
            return True
    else:
        print("Ставку поставь!")
        play_casino()
        
def main():
    if is_right_system():
        print("Добро пожаловать. Снова")
        try:
            play_casino()
        except Exception as e:
            print(f"Произошла ошибка {e}.")
        finally:
            print("Возвращайтесь!")
    else:
        exit()

if __name__ == '__main__':
    main()
