def main():
    answer = input("What time is it? ")
    # Call the converted function
    time = convert(answer)

    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")


# convert a time
def convert(time):
    hours, minute = time.split(":")
    time = float(minute)/60 + float(hours)
    return time



if __name__ == "__main__":
    main()