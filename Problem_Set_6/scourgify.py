import sys
import csv

def main():
    write_new_list()


def write_new_list():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
        try:
            students = []
            with open(sys.argv[1], "r") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    name_split = row["name"].split(",")
                    students.append({"first" : name_split[1].lstrip(), "last" : name_split[0], "house" : row["house"]})
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")

        with open(sys.argv[2], "w") as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writerow({"first" : "first", "last" : "last", "house" : "house"})
            for rows in students:
                writer.writerow({"first" : rows["first"], "last" : rows["last"], "house" : rows["house"]})



if __name__ == "__main__":
    main()