from seasons import date_into_minutes
from datetime import date



def test_date_into_minutes():
    my_birthday = date(2021, 6, 30)
    assert date_into_minutes(my_birthday) ==  "One million, one hundred four thousand, four hundred eighty minutes"
    my_birthday = date(1998, 3, 24)
    assert date_into_minutes(my_birthday) ==  "Thirteen million, three hundred forty-three thousand forty minutes"

