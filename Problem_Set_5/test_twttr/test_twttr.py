from twttr import shorten

# Test letters upper and lower cases
def test_upper_lower_case():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("Anano Robakidze") == "nn Rbkdz"

# Test numbers
def test_numbers():
    assert shorten("1347") == "1347"

# Test punctuation
def test_punctuation():
    assert shorten("!?,.") == "!?,."