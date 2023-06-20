from view import launch_menu, message, select_creature_menu, select_part_1, select_part_2, select_part_3
from view import select_part_1_2, select_part_2_2, select_part_3_2
from view import text
from view.creature import human, enchanter, fury


def launch():
    while True:
        choice = launch_menu()
        match choice:
            case 'R':
                message(text.rules)
            case 'S':
                select_creature()
            case 'Q':
                break

def select_creature():
    while True:
        choice = select_creature_menu()
        match choice:
            case '1':
                print(human.specifications())
                select_human()
            case '2':
                enchanter.enchanter_ability()
                print(enchanter.specifications())
                select_enchanter()
            case '3':
                print(fury.specifications())
                select_fury()
            case 'Q':
                break

def select_human():
    message(text.action_cub)
    human.count_experience()
    print(human.specifications())
    human_history_part_1()

def select_enchanter():
    message(text.action_cub)
    enchanter.count_experience()
    print(enchanter.specifications())
    enchanter_history_part_1()

def select_fury():
    message(text.action_cub)
    fury.count_ability()
    print(fury.specifications())
    fury_history_part_1()

def human_history_part_1():
    while True:
        choice = select_part_1()
        match choice:
            case '0':
                message(text.part_1_1)
                human.subtraction_experience_1()
                print(human.specifications())
                human_history_part_2()
            case '1':
                message(text.part_1_2)
                human.subtraction_experience_2()
                print(human.specifications())
                human_history_part_2()
            case 'Q':
                break

def human_history_part_2():
    message(text.action_cub)
    human.count_experience()
    print(human.specifications())
    while True:
        choice = select_part_2()
        match choice:
            case '0':
                message(text.part_2_1)
                human.subtraction_experience_2()
                print(human.specifications())
                human_history_part_3()
            case '1':
                message(text.part_2_2)
                message(text.part_2_1)
                human.subtraction_experience_3()
                print(human.specifications())
                human_history_part_3()
            case 'Q':
                break

def human_history_part_3():
    message(text.action_cub)
    human.count_experience()
    print(human.specifications())
    while True:
        choice = select_part_3()
        match choice:
            case '0':
                message(text.part_3_1)
                human.subtraction_experience_3()
                print(human.specifications())
                human_end_history()
            case '1':
                message(text.part_3_2)
                human.subtraction_experience_5()
                print(human.specifications())
                human_end_history()
            case 'Q':
                break


def enchanter_history_part_1():
    while True:
        choice = select_part_1_2()
        match choice:
            case '0':
                message(text.part_1_1)
                enchanter.subtraction_manna_3()
                print(enchanter.specifications())
                enchanter_history_part_2()
            case '1':
                message(text.part_1_2)
                enchanter.subtraction_experience_2()
                print(enchanter.specifications())
                enchanter_history_part_2()
            case 'Q':
                break

def enchanter_history_part_2():
    message(text.action_cub)
    enchanter.count_experience()
    print(enchanter.specifications())
    while True:
        choice = select_part_2_2()
        match choice:
            case '0':
                message(text.part_2_1)
                enchanter.subtraction_manna_2()
                print(enchanter.specifications())
                enchanter_history_part_3()
            case '1':
                message(text.part_2_2)
                message(text.part_2_1)
                enchanter.subtraction_experience_3()
                print(enchanter.specifications())
                enchanter_history_part_3()
            case 'Q':
                break

def enchanter_history_part_3():
    message(text.action_cub)
    enchanter.count_experience()
    print(enchanter.specifications())
    while True:
        choice = select_part_3_2()
        match choice:
            case '0':
                message(text.part_3_1)
                enchanter.subtraction_experience_3()
                print(enchanter.specifications())
                enchanter_end_history()
            case '1':
                message(text.part_3_2)
                enchanter.subtraction_manna_4()
                print(enchanter.specifications())
                enchanter_end_history()
            case 'Q':
                break

def fury_history_part_1():
    while True:
        choice = select_part_1()
        match choice:
            case '0':
                message(text.part_1_1)
                fury.subtraction_experience_1()
                print(fury.specifications())
                fury_history_part_2()
            case '1':
                message(text.part_1_2)
                fury.subtraction_experience_2()
                print(fury.specifications())
                fury_history_part_2()
            case 'Q':
                break

def fury_history_part_2():
    message(text.action_cub)
    fury.count_ability()
    print(fury.specifications())
    while True:
        choice = select_part_2()
        match choice:
            case '0':
                message(text.part_2_1)
                fury.subtraction_experience_2()
                print(fury.specifications())
                fury_history_part_3()
            case '1':
                message(text.part_2_2)
                message(text.part_2_1)
                fury.subtraction_experience_3()
                print(fury.specifications())
                fury_history_part_3()
            case 'Q':
                break

def fury_history_part_3():
    message(text.action_cub)
    fury.count_ability()
    print(fury.specifications())
    while True:
        choice = select_part_3()
        match choice:
            case '0':
                message(text.part_3_1)
                fury.subtraction_experience_3()
                print(fury.specifications())
                fury_end_history()
            case '1':
                message(text.part_3_2)
                fury.subtraction_experience_5()
                print(fury.specifications())
                fury_end_history()
            case 'Q':
                break

def human_end_history():
    print(human.count_end())
    launch()

def enchanter_end_history():
    enchanter.count_manna_experience()
    print(enchanter.count_end())
    launch()

def fury_end_history():
    print(fury.count_end_fury())
    launch()