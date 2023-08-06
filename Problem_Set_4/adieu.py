import inflect


p = inflect.engine()

dict_names = []

while True:
    try:
        name = input("Name: ").title()
        dict_names.append(name)
    except EOFError:
        print()
        break

mylist = p.join(dict_names)
print(f"Adieu, adieu, to {mylist}")