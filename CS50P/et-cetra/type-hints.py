## type hint a hint that n should be an int
## mypy will understand that n: int means n should be an int
def meow(n: int):
    for _ in range(n):
        print("meow")



number: int = int(input("> "))
meow(number)


## runing "mypy type-hint.py" in command console will show the error with type hint