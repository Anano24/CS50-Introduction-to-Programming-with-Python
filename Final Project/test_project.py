from project import Pig, Nifnifi
import unittest
from unittest.mock import patch
from io import StringIO


class PigTest(unittest.TestCase):
    def test_valid_pig_instance(self):
        pig = Pig("Nifnifi", "house of straw")
        self.assertEqual(pig.name, "Nifnifi")
        self.assertEqual(pig.house, "house of straw")

    def test_invalid_pig_instance(self):
        with self.assertRaises(ValueError):
            Pig("invalid_pig", "invalid_house")


class NifnifiTest(unittest.TestCase):
    def test_about_pig(self):
        nifnifi = Nifnifi("Nifnifi", "house of straw")
        expected_output = "I am Nifnifi 🐷 and live in the house of straw.\n"
        with patch("sys.stdout", new=StringIO()) as fake_out:
            nifnifi.about_pig()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_wolf_destroy_house(self):
        nifnifi = Nifnifi("Nifnifi", "house of straw")
        expected_output = """One starlit night a wolf 🐺 came out looking for food.
- Little pig, little pig, let me come in.
- Oh no, not by the hair on my chinny chin chin!
The big bad wolf huffed and puffed and blew the house down in minutes!💥
👀 Seeing this Nifnifi run to his brother's house.
If you want to see the end of this story, try 'Nufnufi'!\n"""
        with patch("sys.stdout", new=StringIO()) as fake_out:
            nifnifi.wolf_destroy_house()
            self.assertEqual(fake_out.getvalue(), expected_output)


