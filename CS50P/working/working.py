import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    format = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)
    if format:
        parts = format.groups()
        if int(parts[1]) > 12 or int(parts[5]) > 12:
            raise ValueError

        start = meridiam(parts[1], parts[2], parts[3])
        end = meridiam(parts[5], parts[6], parts[7])
        return start + " to " + end
    else:
        raise ValueError


def meridiam(hour, minute, m):
    hour = int(hour)
    if m == "PM":
        if hour == 12:
            hour = 12
        else:
            hour = hour + 12
    else:
        if hour == 12:
            hour = 0
        else:
            hour = hour
    hour = str(hour)

    if minute == None:
        minute = ":00"
        time = f"{hour.zfill(2)}{minute}"
    else:
        time = f"{hour.zfill(2)}:{minute}"

    return time

if __name__ == "__main__":
    main()