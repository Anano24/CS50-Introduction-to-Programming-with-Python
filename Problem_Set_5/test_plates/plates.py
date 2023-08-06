def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s = s.lower().strip()
    if not s.isalnum():
        return False

    if len(s) < 2 or len(s) > 6:
        return False

    if not s[0:2].isalpha():
        return False

    for i in range(len(s)-1):
        if s[i].isdigit():
            if not s[i+1].isdigit():
                return False

    i = 0
    while i < len(s):
        if not s[i].isalpha():
            if s[i] == '0':
                return False
            else:
                break
        i += 1
    #if s[2] == "0":
        #return False
        
    for c in s:
        if c in [".", " ", "!", "?"]:
            return False

    return True


if __name__ == "__main__":
    main()