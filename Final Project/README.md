
# ___Three Little Pigs - Python Game___

#### Video Demo: <https://youtu.be/sIqHumpbXWI>

## __Definition__

This Python code is a simple text-based game based on the classic children's story "The Three Little Pigs." The game allows you to interact with three little pigs and experience different scenarios based on the choices you make.

Project structure :
 - project.py
 - test_project.py
 - requirements.txt
 - README.md

 ## __Libraries__
 __RANDOM__: This module implements pseudo-random number generators for various distributions.. [(Readmore)](https://docs.python.org/3/library/random.html)

__COWSAY__: The cowsay library in Python is a fun and humorous tool that generates ASCII art of a cow with a speech bubble containing a message provided by the user. It's based on the original cowsay Unix command-line program, which has been recreated as a Python library for users to incorporate the playful ASCII art into their Python scripts and programs. [(Readmore)](https://pypi.org/project/cowsay/#description)

## **Installing Libraries**
there is a a requirements.txt file that has all the libraries used.

and simply can be install by this pip command:

```pip install -r requirements.txt```

## __Usage__

```python project.py```
```
  ______
| Hello! |
  ======
      \
       \
        \
         \
                   ,.
                  (_|,.
                  ,' /, )_______   _
              __j o``-'        `.'-)'
              (")                 \'
              `-j                |
                `-._(           /
                   |_\  |--^.  /
                  /_]'|_| /_)_/
                      /_]'  /_]'
This is the Three Little Pigs short story.
Choose a pig's number to see their story:
1. Nifnifi
2. Nafnafi
3. Nufnufi
```
After that, the user can select a pig 1, 2, or 3. If the user selects '1' hi/she can see the story about 'Nifnifi'.

```
I am Nifnifi 🐷 and live in the house of straw.
One starlit night a wolf 🐺 came out looking for food.
- Little pig, little pig, let me come in.
- Oh no, not by the hair on my chinny chin chin!
The big bad wolf huffed and puffed and blew the house down in minutes!💥
👀 Seeing this Nifnifi run to his brother's house.
If you want to see the end of this story, try 'Nufnufi'!
```
If you want to see the end of this story, try 3 - 'Nufnufi!'.

__Nifnifi__ (House of Straw): The first pig's house is made of straw, and you will experience an encounter with the big bad wolf.

__Nafnafi__ (House of Sticks): The second pig's house is made of sticks, and you will also face the big bad wolf.

__Nufnufi__ (House of Bricks): The third pig's house is made of bricks. You will try to trap the wolf by answering three simple math questions.

__Note:__ When prompted to answer questions, you must provide the correct answer within three attempts; otherwise, the wolf will succeed.

Have fun playing the game! 🐷🐺

## __coding__

project.py is my first experience in Object-Oriented programming.

the project contains 4 classes including the main function.
### class Pig:
- Description: This is the base class representing a generic pig character in the game.
- Attributes:
    - __name__: A string representing the pig's name. It can only be one of three specific names: "Nifnifi," "Nafnafi," or "Nufnufi."
    - __house__: A string representing the pig's house type. It can only be one of three specific types: "house of straw," "house of sticks," or "house of bricks."
- Methods:
    - __ __init____ __(self, name, house)__: The constructor method to initialize the name and house attributes.
    - __ __str____ __(self)__: A special method that returns a string representation of the pig's name and house.
    - __name.setter__: A property setter method to validate and set the pig's name.
    - __house.setter__: A property setter method to validate and set the pig's house.
    - __choose_pig()__: A class method that lets the user choose one of the three pigs and returns their selection.


### class Nifnifi(Pig):
- Description: This class represents the pig named "Nifnifi" with a house made of straw. It is a subclass of the _Pig_ class.
- Methods:
    - __ __init____ __(self, name, house)__: The constructor method to initialize the pig's name and house using the parent class's constructor.
    - __about_pig()__: A method to display information about the pig and its house.
    - __wolf_destroy_house()__: A method that narrates an encounter with the big bad wolf, leading to the destruction of the house made of straw.


### class Nafnafi(Nifnifi):
- Description: This class represents the pig named "Nafnafi" with a house made of sticks. It is a subclass of the _Nifnifi_ class, which itself is a subclass of the _Pig_ class.
- Methods:
    - __ __init____ __(self, name, house)__: The constructor method to initialize the pig's name and house using the parent classes' constructors.


### class Nufnufi(Nifnifi):
- Description: This class represents the pig named "Nufnufi" with a house made of bricks. It is a subclass of the _Nifnifi_ class, which itself is a subclass of the _Pig_ class.
- Methods:
    -  __ __init____ __(self, name, house)__: The constructor method to initialize the pig's name and house using the parent classes' constructors.
    - __wolf_end_story()__: A method that narrates an encounter with the big bad wolf, but the house made of bricks remains strong. The player needs to answer three math questions to trap the wolf successfully.
    - __simulate_round()__: A class method that simulates a round of math questions for the player to answer.
    - __simulate_game()__: A class method that simulates the entire game, asking three rounds of math questions, with the wolf eventually being trapped.


### Author : Anano Robakidze


