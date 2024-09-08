from datetime import date
import sys, re, inflect

p = inflect.engine()


def main():
    birth = input('Date of Birth: ')
    try:
        year, month, day = check(birth)
    except:
        sys.exit('Invalid Birthday')

    birth = date(int(year), int(month), int(day))
    diff = date.today() - birth
    minutes = p.number_to_words(diff.days * 24 * 60, andword="")
    print(f"{minutes.capitalize()} minutes")



def check(birth):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth):
        year, month, day = birth.split('-')
        if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
            return year, month, day


if __name__ == "__main__":
    main()