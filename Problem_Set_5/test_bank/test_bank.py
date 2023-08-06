from bank import value

def test_return_zero():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0

def test_return_20():
    assert value("h") == 20
    assert value("H") == 20
    assert value("Hi") == 20
    assert value("hey man") == 20
    assert value("HOW ARE YOU?") == 20

def test_return_100():
    assert value("Anano") == 100
    assert value("Whats up?") == 100
    assert value("GOOD MORNING!") == 100
