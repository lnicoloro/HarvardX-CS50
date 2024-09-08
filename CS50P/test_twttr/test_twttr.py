from twttr import shorten

def main():
    test_shorten()
    test_case()

def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"


def test_case():
    assert shorten('twitter') == 'twttr'
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('TwITteR') == 'TwTtR'


def test_numbers():
    assert shorten('123') == '123'


if __name__ == "__main__":
    main()

