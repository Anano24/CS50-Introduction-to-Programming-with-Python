# get user input
answer = input("What is the Answer to the great Question of Life, the Universe, and Everithing? ")

# print 'Yes' if the user inputs 42 or (case-insensitively) forty two or forty-two
if answer.strip() == "42":
    print("Yes")
elif answer.lower().strip() == "forty-two":
    print("Yes")
elif answer.lower().strip() == "forty two":
    print("Yes")
else:
    print("No")