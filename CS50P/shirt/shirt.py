import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    command_line()

    try:
        image = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")
    size = shirt.size
    muppet = ImageOps.fit(image, size)
    muppet.paste(shirt, shirt)
    muppet.save(sys.argv[2])

def command_line():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if exe(splitext(sys.argv[1])) == False:
        sys.exit("Invalid input")
    if exe(splitext(sys.argv[2])) == False:
        sys.exit("Invalid output")

    if splitext(sys.argv[1])[1] != splitext(sys.argv[2])[1]:
        sys.exit("Input and output have different extensions")




def exe(file):
    if file[1] in [".png", ".jpg", ".jpeg"]:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
