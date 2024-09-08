from seasons import check

def main():
    test_check()

def test_check():
    assert check("2000-12-31") == ("2000", "12", "31")
    assert check("20-12-31") == None
    assert check("2000-1-12") == None
    assert check("2000-12-1") == None


if __name__ == "__main__":
    main()
