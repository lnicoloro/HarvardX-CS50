## takes alot of code just to format and valid an email (more than this)
# email = input('Email: ').strip()
# username, domain = email.split("@")
# if username and domain.endswith('.edu'):
#     print('Valid')
# else:
#     print('Invalid')

## a regular expression is just a pattern

## regular expression symbols
## . - any character
## * - zero or more repetitions
## + - one or more repetitions
## ? - zero or one repetitions
## {m} - m repititions (number of characters)
## {m,n} - range of m to n repetitions (range of characters)
## ^ - match the start of the string
## $ - match the end of the string
## [] - look specifically for characters within the square brackets
## [^] - cannot match any of the characters within the square brackets
## \d - decimal digit (0-9)
## \D - not a decimal digit
## \s - whitespace charaters (space or tab)
## \S - not a whitespace charater
## \w - word character, includes numbers and underscore (a-z and A-Z and 0-9 and _)
## \W - not a word character
## A|B - either A or B
## ( ) - a group (can group multiple like: A or B or C or D)
##(?: ) - non capturing version of grouping


## regular expression flags
## re.IGNORECASE - ingnores case
## re.MULTILINE - hanldes multiple lines of input
## re.DOTALL - . will recongize new lines as well (\n)





## use of the regular expression library
## .+ means something to the left and something to the right of the @
## ..* == .+ (..* means repeating characters repeating 0 or more times)
## \ will tell the re.search that the following character is not a regular expression (in this case the '.')
## r will tell python to read it as a raw string (not formatted)
## ^ match at the start of the string
## $ means match at the end of the string
## [^@] means any character but '@' is ok
## [a-z] means the range of characters a to z
## [a-zA-Z1-9_] a-z, A-Z, 1-9, and _ are all ok
## (com|net|org|edu) means com or net or org or edu
## flags are the third argument of re.search allow to configure the call to re.search
## (\w\.)? the ? means that there can be 0 or more repetitions of what is in the ()   (allows for subdomains: @cs50.harvard.edu)
## (\w|\.) means either a word character or a '.'


import re
email = input('Email: ').strip()

if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.(com|net|org|edu)$", email, re.IGNORECASE):
    print('Valid')
else:
    print('Invalid')


## re.match(pattern, string, flag=0)    will match a regular expression from the start (automatically includes ^ at the start)
## re.fullmatch(pattern, string, flag=0)    will match a regular expression from the start to the end (automatically includes ^ and $)