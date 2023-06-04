initial_amount=2000 #in dollor
choice=input("""
     Enter \" BAL \" for checking Bank Balance.
     Enetr \" Withdraw \" for withdrawal of money.
     Enter \" Help\" for other service..
""")
if choice=="Bal":
    print("Your Account Balance is {:.2f} dollors".format(initial_amount))
    print("---Your Request is Successfully completed.---")
    print("------Thank you-----")
elif choice=="Withdraw":
    x = float(input("Enter your withdraw amount: "))
    if x>=initial_amount-0.5:
        print("Kindly check your Balance amount.\n Because your withdraw money is greater than your Main Account balance ")
    else:
        y = x + 0.5
        initial_amount = initial_amount - y
        print("your transaction is successfully completed.")
        print("Now your Bank Balance is {:.2f} dollor".format(initial_amount))
else:
    print("for more information visit our website. ")






