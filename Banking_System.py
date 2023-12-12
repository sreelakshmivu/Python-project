# Project : Banking System
from Customers import Customer as c
customers= c()
num=customers.display()
if num==1:
    user = input("User name:")
    pwd = input("Password:")
    customer_login=c()
    acc_no=customer_login.c_login(user, pwd)
    if acc_no!=False:
        balance = customer_login.show_account(acc_no)
        action = input("Enter 'D' for debit /'C' for credit:")
        amount = float(input("Enter the amount:"))
        if action == 'D':
            new_balance = customer_login.withdraw_amount(acc_no,amount,balance)
            print("Your balance amount in account:", new_balance)
        if action == 'C':
            new_balance = customer_login.deposit_amount(acc_no,amount,balance)
            print("Your balance amount in account:", new_balance)
        customer_login.customer_exit()
    else:
        customer_login.exit()
elif num==2:
    print("\t\t\t!!! User Registration Form !!!")
    name=input("Enter your full name:")
    email=input("email id:")
    user=input("User name:")
    password=input("Password:")
    profile_password=input("Enter profile password for security:")
    acc_no=int(input("Enter account number:"))
    balance=float(input("Enter your balance:"))
    new_customer=c()
    new_customer.add_new_customer(name,email,user,password,profile_password,acc_no,balance)
    print("Submit")
    print("\t\t\t* You successfully registered")
    print("\t\t** Now you can login to your account!!")
    n=new_customer.display()
    if n==1:
        user=input("User name:")
        pwd=input("Password:")
        acc_no=new_customer.c_login(user,pwd)
        if acc_no != False:
            balance=new_customer.show_account(acc_no)
            action=input("Enter 'D' for debit /'C' for credit:")
            amount=float(input("Enter the amount:"))
            if action=='D':
                new_balance=new_customer.withdraw_amount(acc_no,amount,balance)
                print("Your balance amount in account:",new_balance)
            if action=='C':
                new_balance=new_customer.deposit_amount(acc_no,amount,balance)
                print("Your balance amount in account:", new_balance)
            new_customer.customer_exit()
        else:
            new_customer.exit()
    elif n==2:
        print("Already exist")
    else:
        print("Enter valid option")
else:
    print("Enter Valid Option.")