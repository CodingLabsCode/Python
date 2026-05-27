def passwordthing():
    from random import choice as c
    from random import shuffle as s 
    from time import time as t
    from string import ascii_letters as letters, digits as numbers

    chars = letters + numbers + "!@£$%^&*_+=-§?></,.;;|"

    while True:
        user = input("Would You Like To Make A Password (y/n): ").lower()
        match user:
            case "y":
                password_length = int(input("How Long Do You Want The Password To Be: "))
                password = ""

                for i in range(password_length):password += c(chars)

                password_list = list(password)
                s(password_list)
                password = "".join(password_list)

                print(f"Your New Password Is {password}")
            case "n":
                print("GoodBye")
                exit()
        test_password = input("Would You Like To Test Your Password (y\n): ").lower()
        match test_password:
            case "y":
                print("Cracking Password")
                start = t()
                computer_guess = ""
                count = 16
                attepmts = 0
                while computer_guess != password:
                    computer_guess += c(chars)
                    count -= 1
                    attepmts += 1
                    if count == 0:
                        computer_guess = ""
                        count = 16
                        continue
                    end = t()
                finshed = f"""=== Results ===
                Password: {password}
                Attepmts: {attepmts}
                Time Taken: {end - start:.2f} Seconds"""
                print(finshed)
                again = input("Would You Like To Make Another Password (y/n): ")
                if again == "yes": continue
                else: print("GoodBye"); exit()
            case "n":
                print("GoodBye")
                exit()
