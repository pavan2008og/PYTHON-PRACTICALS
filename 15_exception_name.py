class InvalidNameError(Exception):
    pass


def validate_name(name):
    if name.strip() == "":
        raise InvalidNameError("Name cannot be empty")
    if not name.replace(" ", "").isalpha():
        raise InvalidNameError("Name must contain only alphabets")
    return name.title()


try:
    name = input("Enter your name: ")
    print("Valid name:", validate_name(name))
except InvalidNameError as e:
    print("Error:", e)
finally:
    print("Program finished")
