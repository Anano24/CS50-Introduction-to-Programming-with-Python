from plates import is_valid


def test_true():
    assert is_valid("cs") == True
    assert is_valid("CS") == True
    assert is_valid("CS50") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("AAA222") == True


def test_false():
    assert is_valid("CS05") == False
    assert is_valid("PI3.14") == False
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("123") == False
    assert is_valid("AAA22B") == False
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("PI 34") == False
