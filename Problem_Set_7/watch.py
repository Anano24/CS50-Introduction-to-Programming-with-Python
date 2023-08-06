import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    iframe_match = re.search(r"<iframe.*?src=\".*?(youtube\.com/embed/)(\w+)\".*?></iframe>", s)
    if iframe_match:
           split_url = iframe_match.groups()
           return "https://youtu.be/" + split_url[1]




if __name__ == "__main__":
    main()