print("Basic ATM Machine")

total_amount = 100000
correct_pin = 1234


card = input("Enter Your Card")
if card != "":
    print("Haven't entered your card propely")
    exit()


language = input("Select Your Language(Hindi/English)")
if language not in ["Hindi", "English"]:
    print("Invalid Language")
    exit()
print("Card accepted and Language selected")

pin = int(input("Enter the pin"))
if pin == correct_pin:
    print("Select the option from menu")

    while True:
        print("1 Check Balance")
        print("2 Withdrawl")
        print("3 Deposit")
        print("4 Pin Change")

        choice = int(input("Enter the choice"))  # what user want to do

        if choice == 1:  # user want to check balance
            print("Your current balance is :", total_amount)
            continue

        elif choice == 2:  # user want to make a withdrwal
            account_type = input("Enter account type")
            if account_type in ["Current", "Savings"]:
                print("Select the amount in multiple of 500.")

                amount = int(input("Enter the amount"))
                if amount % 500 != 0:
                    print("Invalid selection")
                    continue
                if amount <= total_amount:
                    print("Withdrawl Successful")
                    total_amount -= amount
                    print("Your current account balance is :", total_amount)
                    continue

                else:
                    print("Invalid amount")

            else:
                print("Invalid account type")
                continue

        elif choice == 3:  # user want to deposit money
            deposit = int(input("Enter the amount to deposit:"))
            total_amount += amount
            print("Your current Balance is :", total_amount)
            continue

        elif choice == 4:  # user want to update pin
            old_pin = int(input("Enter four digit old Pin"))
            if old_pin == correct_pin:
                pass
            else:
                print("Invalid Pin")
                continue
            new_pin = int(input("Enter four digit new pin"))
            varify_pin = int(input("Enter four digit new Pin"))
            if new_pin == varify_pin:
                print("Your pin changed successfully.")
                correct_pin = new_pin
                continue
            else:
                print("Incorrect Pin")
                continue

        else:
            print("invalid choice")
            break
else:
    print("Invalid Pin")
    exit()
