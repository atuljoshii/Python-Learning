pin = int(input("Enter YOur Pin Of YOur ATM"))
AvailableBalance = 50000
name = "Atul Joshi"

if(pin==261226):
        print("Your Name Is",name)
        print("Your Available Balance",AvailableBalance)
        widrwall = (input("Do You Want To Widrall Monry yes/no "))
        if(widrwall=="yes"):
                    ammount = int(input("Enter The Ammount you Want To Widerwal"))
                if amount <= available_balance:
                    available_balance -= amount
                    print("Withdrawal successful!")
                    print("Your Available Balance is:", available_balance)
                else:
                    print("Insufficient balance.")
        elif(widrwall=="no"):
                    print("Thankyou For Visiting......")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")        
else:
print("Your Enterd Wrong pin ")

pin = int(input("Enter Your ATM PIN: "))
available_balance = 50000
name = "Atul Joshi"

if pin == 261226:
    print("Your Name is:", name)
    print("Your Available Balance is:", available_balance)

    withdrawal = input("Do you want to withdraw money? (yes/no): ").lower()

    if withdrawal == "yes":
        amount = int(input("Enter the amount you want to withdraw: "))
        
        if amount <= available_balance:
            available_balance -= amount
            print("Withdrawal successful!")
            print("Your Available Balance is:", available_balance)
        else:
            print("Insufficient balance.")
    
    elif withdrawal == "no":
        print("Thank you for visiting.")
    
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
else:
    print("You entered the wrong PIN.")



    

    
        

