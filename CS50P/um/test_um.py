from um import count

def main():
    test_count()


def test_count():
    assert count('um') == 1
    assert count('um.') == 1
    assert count('Um') == 1
    assert count('um hello um') == 2
    assert count('Um hell um') == 2
    assert count('cat') == 0
    assert count('bum') == 0


if __name__ == "__main__":
    main()