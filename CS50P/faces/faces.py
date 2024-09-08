def convert(input):
    converted = input.replace(":)", "🙂")
    converted = converted.replace(":(", "🙁")
    return converted


text = input("")

new = convert(text)

print(new)





