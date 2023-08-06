
def main():
    fraction = input("Fraction: ")
    fraction_converted = convert(fraction)
    print(gauge(fraction_converted))



def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            new_x = int(x)
            new_y = int(y)
            z = new_x / new_y
            if z <= 1:
                p = round(z * 100)
                return p
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            pass


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"



if __name__ == "__main__":
    main()


