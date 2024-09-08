from CS50P.calculator import square


def main():
    test_square()


def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0


def test_str():
    with pytest.raises(TypeError):
        square("cat")

## pytest will test all functions even if one fails
## run pytest in terminal
## pytest test_calculator.py




if __name__ == "__main__":
    main()