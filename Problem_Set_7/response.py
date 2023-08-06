from validator_collection import validators, checkers, errors


def main():
    input_email = input("What's your email address?: ")
    try:
        email_validate = validators.email(input_email)
        print("Valid")
    except errors.EmptyValueError:
        print("Invalid")
    except errors.InvalidEmailError:
        print("Invalid")

if __name__ == "__main__":
    main()


