#Todd McMillan
def encode(pass_wd):
    pass_w = list(pass_wd)
    pass_w_new = ""
    for num in pass_w:
        num = int(num) + 3
        pass_w_new += str(num)
    return pass_w_new



def main():
    program = True
    pass_wd = ""
    pass_w_new = ""
    while program:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = int(input("Please enter an option: "))
        if option == 1:
           pass_wd = input("Please enter your password to encode: ")
           pass_w_new = encode(pass_wd)
           print("Your password has been encoded and stored!")

        elif option == 2:
            print(f"The encoded password is {pass_w_new}, and the original password is {decode(pass_w_new)}.")

        elif option == 3:
            program = False




if __name__ == '__main__':
    main()
