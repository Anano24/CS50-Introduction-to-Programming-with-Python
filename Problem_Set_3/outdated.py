months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date = input("Date: ")
    try:
        month, day, year = date.split("/")
        month = month.replace(" ","")
        year = year.replace(" ","")
        if(int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
            break
    except:
        try:
            m, d, year = date.split(" ")
            for i in range(len(months)):
                if m == months[i]:
                    month = i + 1
                    break
                else:
                    continue

            if not d.endswith(","):
                continue
            day = d.replace(",", "")
            if(int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
                break
        except:
            print()
            pass

print(f"{year}-{int(month):02}-{int(day):02}")

