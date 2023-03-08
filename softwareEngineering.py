# name: Himal Bamzai-Wokhlu

def encode(intString):
    # encodes string integer input with a new string; each of the digits is 3 more
    newString = ""
    for i in intString:
        newString += str((int(i) + 3) % 10)
    return newString

# This is Reva Adi's decoder function
def decode(password):
    res = ""
    for num in range(len(password)):
        value = int(password[num])
        new_value = (value + 3) % 10
        res += str(new_value)
    return res

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
        if chosenInt == 1:
            print("Please enter your password to encode: ", end="")
            password = input()
            newString = encode(password)
            print("Your password has been encoded and stored!")
            print()
        if chosenInt == 2:
            old_password = decode(newString)
            print("The encoded password is " + newString, end="")
            print(", and the original password is " + old_password + ".")
            print()
        if chosenInt == 3:
            quit()



main()

'''
        if chosenInt < 3:
            # takes user input for password
            print("Please enter your password to encode: ", end="")
            password = input()
'''