import re

name = input('Name: ').strip()

## capturing the .+ on either side of the comma
matches = re.search(r"^(.+), *(.+)$", name)

## if matches are found (input is in last, first format)
if matches:
    name = matches.group(2) + " " + matches.group(1)
    # last = matches.group(1)
    # first = matches.group(2)
    # name = f"{first} {last}"
    ## re.search returns something else in group(0) so for this functino start counting at 1


print(name)