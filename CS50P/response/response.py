import validators


if validators.email(input("What's your address? ")):
        print("Valid")
else:
      print('Invalid')