from hello import hello

## hello is not returning anything it is printing something
## change the function to return and print the result in main
## this is done to make the code more testable

## dont make test too complicated ( dont want tests for your tests)


def test_argument():
    for name in {'bob', 'john', 'joe'}:
        assert hello(name) == f"hello, {name}"


def test_default():
    assert hello() == "hello, world"