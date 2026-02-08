from random import *


def meno():
    print("----------------------------------meno--------------------------------")
    print("1.asan")
    print("2.motevased")
    print("3.sakht")
    print("-"*80)


def choose_level():
    while True:
        try:
            level = int(input("enter level="))
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
            javab = int(input("enter javab="))
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
            if c == 'g':
                answer = randint(1, max_number)
            else:
                print("finish")
                break
        elif (javab > answer):
            print("javab to maximum ast")
        elif (javab < answer):
            print("javab to maximum ast")
        if talash > 0:
            print(f"talash baghy={talash}")
    print(f"javabs to={list1}")
    print(f"javab man={answer}")


main()
