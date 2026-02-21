list1 = []


def menu():
    print("--------menu-------------")
    print("1.add item")
    print("2.remove item")
    print("3.show item")
    print("4.count item")
    print("5.exit")
    print("6.sort items")
    print("7.clear items")


def add_item():
    while True:
        try:
            name = input("enter name=")
        except ValueError as v:
            print(f"error={v}")
        if name in list1:
            print(f"{name}tekrari ast ")
        else:
            list1.append(name)
            print(f"add{name} in list")
            break


def remove_item():
    while True:
        try:
            name = input("enter name=")
        except ValueError as v:
            print(f"error={v}")
        if name in list1:
            list1.remove(name)
            print(f"{name} remov as list")
            break
        else:
            print("no found")
            break


def show_item():
    print(list1)


def count_item():
    print(f"count items={len(list1)}")


def sort_item():
    list1.sort()
    print("is sort list")
    print(list1)


def clear_items():
    list1.clear()
    print("clear items")


def main():
    menu()
    while True:
        try:

            num = int(input("choose meno="))
        except ValueError as v:
            print(f"error={v}")
            continue
        if num == 1:
            add_item()
        elif num == 2:
            remove_item()
        elif num == 3:
            show_item()
        elif num == 4:
            count_item()
        elif num == 5:
            print("bye")
            break
        elif num == 6:
            sort_item()
        elif num == 7:
            clear_items()


main()
