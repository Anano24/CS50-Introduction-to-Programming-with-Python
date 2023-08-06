from um import count

def main():
    test_lower_case()
    test_word_with_um()
    test_spaces_surrounding()


def test_lower_case():
    assert count("Um, thanks, um...") == 2
    assert count("Um, thanks for the album.") == 1

def test_word_with_um():
    assert count("yummy") == 0


def test_spaces_surrounding():
    assert count("  um   ") == 1
    assert count("hello um world") == 1

if __name__ == "__main__":
    main()