# This is Reva Adi's encode and main logic:
def encode(password):
    res = ""
    for num in range(len(password)):
        value = int(password[num])
        new_value = (value + 3) % 10
        res += str(new_value)
    return res


# Decoder function from Himal Bamzai-Wokhlu
# decodes 8-digit password
def decode(password):
    newString = ""
    for i in password:
        newString += str((int(i) + 10 - 3) % 10)
    return newString


def main():
    encode_decode_menu = True

    while encode_decode_menu:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit ")

        # menu selection based on user response
        menu_selection = int(input("Please enter an option:"))
        if menu_selection == 1:
            password_response = str(input("Please enter your password to encode:"))
            encoded_password = encode(password_response)
            print("Your password has been encoded and stored!")
        if menu_selection == 2:
            original_password = decode(encoded_password)
            print("The encoded password is " + encoded_password, end="")
            print(", and the original password is " + original_password + ".")
            print()
        if menu_selection == 3:
            quit()


if __name__ == "__main__":
    main()
