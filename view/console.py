from view.text import *

def launch_menu():
    print(message(launch))
    while True:
        choice = input(input_launch)
        if choice == 'R' or choice == 'S' or choice == 'Q':
            return str(choice)
        print(message(input_error))

def select_creature_menu():
    print(message(select_entity))
    choise = input(input_launch)
    if choise == '1' or choise == '2' or choise == '3' or choise == 'Q':
        return str(choise)
    print(message(input_error))

def select_part_1():
    print(message(part_1))
    print(message(action_1))
    while True:
        choice = input(input_launch)
        if choice == '0' or choice == '1' or choice == 'Q':
            return choice
        print(message(input_error))

def select_part_2():
    print(message(part_2))
    print(message(action_2))
    while True:
        choice = input(input_launch)
        if choice == '0' or choice == '1' or choice == 'Q':
            return choice
        print(message(input_error))

def select_part_3():
    print(message(part_3))
    print(message(action_3))
    while True:
        choice = input(input_launch)
        if choice == '0' or choice == '1' or choice == 'Q':
            return choice
        print(message(input_error))

def select_part_1_2():
    print(message(part_1))
    print(message(action_1_2))
    while True:
        choice = input(input_launch)
        if choice == '0' or choice == '1' or choice == 'Q':
            return choice
        print(message(input_error))

def select_part_2_2():
    print(message(part_2))
    print(message(action_2_2))
    while True:
        choice = input(input_launch)
        if choice == '0' or choice == '1' or choice == 'Q':
            return choice
        print(message(input_error))

def select_part_3_2():
    print(message(part_3))
    print(message(action_3_2))
    while True:
        choice = input(input_launch)
        if choice == '0' or choice == '1' or choice == 'Q':
            return choice
        print(message(input_error))

def message(message: str):
    lenth = len(message)
    print('\n' + '☼' * 100)
    print(message)
    print('☼' * 100 + '\n')