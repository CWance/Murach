def main():
    full_name = get_full_name()
    password = get_password()
    email = get_email()
    phone = get_phone()

    first_name = get_first_name(full_name)
    print(f"Hi {first_name}, thanks for creating an account.")


def get_full_name():
    while True:
        name = input("Enter full name:       ").strip()
        if " " in name:
            return name
        else:
            print("You must enter your full name.")


def get_first_name(full_name):
    index1 = full_name.find(" ")
    first_name = full_name[:index1]
    return first_name


def get_password():
    while True:
        digit = False
        cap_letter = False
        password = input("Enter password:        ").strip()
        for char in password:
            if char.isdigit():
                digit = True
            elif char.isupper():
                cap_letter = True
        if digit == False or cap_letter == False or len(password) < 8:
            print(f"Password must be 8 characters or more \n"
                  f"with at least one digit and one uppercase letter.")
        else:
            return password

def get_email():
    while True:
        email = input("Enter email address:   ")
        email = email.lower()
        if "@" in email:
            if email.endswith(".com"):
                return email
        print("Please enter a valid email address.")

def get_phone():
    while True:
        phone = input("Enter phone number:   ")
        temp = ""
        for i in phone:
            if i.isdigit():
                temp += i
        phone = temp
        if len(phone) == 10:
            return phone
        print("Please enter a 10-digit phone number.")

if __name__ == "__main__":
    main()
