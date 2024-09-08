from hello import hello

def test_argument():
    for name in {'bob', 'john', 'joe'}:
        assert hello(name) == f"hello, {name}"


def test_default():
    assert hello() == "hello, world"