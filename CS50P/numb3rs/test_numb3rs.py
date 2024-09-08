from numb3rs import validate

def main():
    test_validate()

def test_validate():
    assert validate('255.255.255.255') == True
    assert validate('512.512.512.512') == False
    assert validate('0.0.0.0') == True
    assert validate('257.255.1000.255') == False
    assert validate('cat') == False
    assert validate('1.1.1.1') == True
    assert validate('1.1.1') == False
    assert validate('1.1') == False
    assert validate('1') == False
