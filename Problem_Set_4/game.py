import random

# Prompts the user for a level, n. If the user does not input a positive integer, the program should prompt again.
while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
    except:
        pass


# Randomly generates an integer between 1 and n, inclusive, using the random module.
randomizer = random.randint(1, n)

while True:
    try:
       guess = int(input("Guess: "))
       if guess > 0:
           if guess < randomizer:
                print("Too small!")
           elif guess > randomizer:
                print("Too large!")
           else:
                print("Just right!")
                break
    except:
        pass



