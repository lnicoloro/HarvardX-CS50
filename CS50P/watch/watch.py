import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe.*><\/iframe>", s) and re.search(r"http(s)*:\/\/(www\.)*youtube\.com\/embed\/(?P<code>\w+)", s):
        url = re.search(r"http(s)*:\/\/(www\.)*youtube\.com\/embed\/(?P<code>\w+)", s)

        return "https://youtu.be/" + str(url.group('code'))
    else:
        return "None"








if __name__ == "__main__":
    main()