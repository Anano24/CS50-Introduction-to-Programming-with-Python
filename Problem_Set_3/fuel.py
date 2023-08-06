
while True:
    fraction = input("Fraction: ")
    try:
        x, y = fraction.split("/")
        new_x = int(x)
        new_y = int(y)
        z = new_x / new_y
        if z <= 1:
            break
    except (ValueError, ZeroDivisionError):
        pass

p = round(z * 100)
if p <= 1:
    print("E")
elif p >= 99:
    print("F")
else:
    print(f"{p}%")




