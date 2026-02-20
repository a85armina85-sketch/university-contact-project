from random import *


def meno():
    print("----------------------------------meno--------------------------------")
    print("1.easy")
    print("2.Elementary")
    print("3.hard")
    print("-"*80)


def choose_level():
    while True:
        try:
            level = int(input("enter level(1_3)="))
            return level
        except ValueError as v:
            print(f"error={v}")


def setting_level(level):
    if level == 1:
        return 10, 3
    elif (level == 2):
        return 50, 5
    elif (level == 3):
        return 100, 6


def input_javab():
    while True:
        try:
            javab = int(input("enter answer="))
            return javab
        except ValueError as v:
            print(f"error={v}")


def main():
    list1 = []
    meno()
    level = choose_level()
    max_number, talash = setting_level(level)
    answer = randint(1, max_number)
    while talash > 0:
        javab = input_javab()
        list1.append(javab)
        talash -= 1
        if javab == answer:
            print("wow")

            c = input("aya mikhoi adameh bdi?")

            if c.lower() in ('g', 'y'):
                answer = randint(1, max_number)
                # این خط برای این است که تلاش ها بعد از برد ریست شود
                talash = setting_level(level[1])
            else:
                print("finish")
                break
        elif (javab > answer):
            print("javab to maximum ast")
        elif (javab < answer):
            print("javab to minimum ast")
        if talash > 0:
            print(f"talash baghy={talash}")
    print("you lost")
    print(f"javabs to={list1}")
    print(f"javab man={answer}")


main()
