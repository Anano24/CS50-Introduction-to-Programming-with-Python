import random
import cowsay

class Pig:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} is in {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name not in ["Nifnifi", "Nafnafi", "Nufnufi"]:
            raise ValueError("Invalid name")
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["house of straw", "house of sticks", "house of bricks"]:
            raise ValueError("Invalid name")
        self._house = house


    @classmethod
    def choose_pig(cls):
        try:
            cowsay.pig("Hello!")
            n = int(input("This is the Three Little Pigs short story.\nChoose a pig's number to see their story:\n1. Nifnifi\n2. Nafnafi\n3. Nufnufi\n"))
            if n not in [1, 2, 3]:
                raise ValueError()
            return n
        except ValueError:
            print("Please enter a valid choice (1, 2, or 3)")
            return cls.choose_pig()



class Nifnifi(Pig):
    def __init__(self, name, house):
        super().__init__(name, house)


    def about_pig(self):
        print(f"I am {self.name} 🐷 and live in the {self.house}.")


    def wolf_destroy_house(self):
        story = f'''One starlit night a wolf 🐺 came out looking for food.
- Little pig, little pig, let me come in.
- Oh no, not by the hair on my chinny chin chin!
The big bad wolf huffed and puffed and blew the house down in minutes!💥
👀 Seeing this {self.name} run to his brother's house.
If you want to see the end of this story, try 'Nufnufi'!'''
        print(story)

class Nafnafi(Nifnifi):
    def __init__(self, name, house):
        super().__init__(name, house)


class Nufnufi(Nifnifi):
    def __init__(self, name, house):
        super().__init__(name, house)


    def wolf_end_story(self):
        story ='''One starlit night a wolf 🐺 came out looking for food.
- Little pig, little pig, let me come in.
- Oh no, not by the hair on my chinny chin chin!
The big bad wolf tried to huff and puff and blow the house down, but he couldn't.
The house of bricks was very strong and pigs were safe inside.
The wolf tried to enter through the chimney.
If you want that the wolf fall into a big pot of water answer this 3 questions:
'''
        print(story)


    @classmethod
    def simulate_round(cls):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        count_tries = 1
        while count_tries <=3:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == (x + y):
                    return True
                else:
                    count_tries += 1
                    print ("EEE")
            except:
                count_tries += 1
                print ("EEE")
        print(f"{x} + {y} = {x + y}")
        return False

    @classmethod
    def simulate_game(cls):
        count_round = 1
        while count_round <= 3:
            response = cls.simulate_round()
            count_round += 1
        return response



def main():
    get_pig = Pig.choose_pig()
    if  get_pig == 1:
        nifnifi = Nifnifi("Nifnifi", "house of straw")
        nifnifi.about_pig()
        nifnifi.wolf_destroy_house()
    elif get_pig == 2:
        nafnafi = Nafnafi("Nafnafi", "house of sticks")
        nafnafi.about_pig()
        nafnafi.wolf_destroy_house()
    elif get_pig == 3:
        nufnufi = Nufnufi("Nufnufi", "house of bricks")
        nufnufi.about_pig()
        nufnufi.wolf_end_story()
        nufnufi.simulate_game()
        print("The wolf fall into a big pot of water!\nThe three little pigs lived happily ever after!")





if __name__ =="__main__":
    main()

