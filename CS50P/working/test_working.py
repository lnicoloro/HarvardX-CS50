from working import convert
import pytest


def main():
    test_time()
    test_hour()
    test_minute()

def test_time():
    with pytest.raises(ValueError):
        convert("9 AM - 5")

    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("6:45 AM to 3:22 PM") == "06:45 to 15:22"

def test_hour():
    with pytest.raises(ValueError):
        convert("15 AM to 18 PM")


def test_minute():
    with pytest.raises(ValueError):
        convert("9:70 PM to 5:80 PM")