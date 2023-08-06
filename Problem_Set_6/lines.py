import sys


def main():
    check_command_line_arg()

    try:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    count = 0
    for line in lines:
        if not (line.isspace() or line.lstrip().startswith("#")):
            count += 1
    print(count)


def check_command_line_arg():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")


if __name__ == "__main__":
    main()