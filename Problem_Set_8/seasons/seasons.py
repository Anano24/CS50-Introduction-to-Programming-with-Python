
from datetime import date
import inflect
import sys


p = inflect.engine()

def main():
    try:
        time = date.fromisoformat(input("Date of Birth: "))
    except:
        sys.exit("Invalid date")

    print(date_into_minutes(time))


def date_into_minutes(my_birthday):
    today = date.today()
    time_to_birthday = 0
    if my_birthday < today:
        time_to_birthday = (today - my_birthday) * 24 * 60
        words = p.number_to_words(time_to_birthday.days, andword="")

    return words.capitalize() + " minutes"

if __name__ == "__main__":
    main()

