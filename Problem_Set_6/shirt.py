import sys
from PIL import Image, ImageOps
from os.path import splitext


def main():
    check_argument()

    try:
        image = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")
    size = shirt.size
    muppet = ImageOps.fit(image, size)
    muppet.paste(shirt, shirt)
    muppet.save(sys.argv[2])


def check_argument():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])

    if check_extention(file1[1]) == False:
        sys.exit("Invalid input")
    if check_extention(file2[1]) == False:
        sys.exit("Invalid output")
    if file1[1].lower() != file2[1].lower():
        sys.exit("Input and output have different extensions")


def check_extention(file):
    if file in [".jpg", ".jpeg", ".png"]:
        return True
    return False



if __name__ == "__main__":
    main()