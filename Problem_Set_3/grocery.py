
grocery = {}

while True:
    try:
        item = input().lower()
        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1
    except EOFError:
        print()
        for k in sorted(grocery.keys()):
            print(grocery[k], k.upper())
        break