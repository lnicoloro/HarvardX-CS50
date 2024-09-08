from bank import value

def main():
    test_zero()
    test_twenty()
    test_hundred()


def test_zero():
    assert value("hello bob") == 0
    assert value("Hello") == 0
    assert value("HeLlO Bob") == 0


def test_twenty():
    assert value("Hi") == 20
    assert value("hey") == 20




def test_hundred():
    assert value("What's up?") == 100
    assert value("good morning") == 100
