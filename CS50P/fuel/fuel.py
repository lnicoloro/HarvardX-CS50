def main():
    percent = get_percent()
    if percent <= 0.01:
        print('E')
    elif percent >= 0.99:
        print('F')
    else:
        percent = percent * 100
        whole, decimal = str(percent).split('.')
        print(f'{whole}%')





def get_percent():
    while True:
        try:
            fraction = input('Fraction: ')
            x, y = fraction.split('/')
            percent = int(x) / int(y)
            if percent > 1:
                pass
            else:
                return percent
        except (ValueError, ZeroDivisionError):
            pass



main()