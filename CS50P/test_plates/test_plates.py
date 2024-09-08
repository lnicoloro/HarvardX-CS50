from plates import is_valid

def main():
    test_length()
    test_start()
    test_middle()
    test_zero()


def test_length():
    assert is_valid("AA") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False


def test_start():
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("22") == False
    assert is_valid("2A") == False


def test_middle():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False


def test_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False


def test_punctuation():
    assert is_valid("CS!50") == False
    assert is_valid("CS.50") == False
    assert is_valid("CS 50") == False