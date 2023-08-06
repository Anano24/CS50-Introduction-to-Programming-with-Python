# get user input
camelCase = input("camelCase: ")

# print "snake_case"
print("snake_case: ", end="")

# loop through every letter
for c in camelCase:
    if c.isupper():
        print("_" + c.lower(), end="")
    else:
        print(c, end="")

print()
