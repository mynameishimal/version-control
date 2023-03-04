# name: Himal Bamzai-Wokhlu

def encode(intString):
    # encodes string integer input with a new string; each of the digits is 3 more
    newString = ""
    for i in intString:
        newString += str((int(i) + 3) % 10)
    return newString


def main():
    newString = ""
    # through newString variable, encoded password can be accessed
    chosenInt = 0
    while chosenInt != 3:
        # prints menu for encode, decode, and quit options
        print('Menu')
        print("-------------")
        print("1. Encode\n2. Decode\n3. Quit")
        print()
        print("Please enter an option: ", end="")
        chosenInt = int(input())
        if chosenInt < 3:
            # takes user input for password
            print("Please enter your password to encode: ", end="")
            password = input()
            if chosenInt == 1:
                newString = encode(password)
                print("Your password has been encoded and stored!")
                print()


main()
