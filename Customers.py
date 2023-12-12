import json
class Customer:
    customers={}
    name=""
    email=""
    username=""
    password=""
    pro_password=""
    account_no=0
    balance=0

    def display(self):
        print("########################################################################")
        print("\t\t\t\t!!!\t Welcome to State Bank\t!!!")
        print("\t\tPersonal Banking Account")
        print("***\tLogin!! **\tPress 1")
        print("***\tNew user? Sign Up!! **\tPress 2")
        num = int(input("*\tEnter your option:"))
        return num

    def add_new_customer(self,name,email,username,password,pro_password,acc_no,balance):
        self.name=name
        self.email=email
        self.username=username
        self.password=password
        self.pro_password=pro_password
        self.account_no=acc_no
        self.balance=balance
        self.customers.update({f'{self.account_no}':
                                {f"{"name"}":f"{self.name}",
                                 f"{"email"}":f"{self.email}",
                                 f"{"username"}":f"{self.username}",
                                 f"{"password"}":f"{self.password}",
                                 f"{"pro_password"}":f"{self.pro_password}",
                                 f"{"balance"}":self.balance}
                               })
        with open("Customer_Details","a") as c_file:
            c_data=str(self.customers)
            c_file.write("\n"+c_data)

    def show_account(self,acc_no):
        with open("Customer_Details","r") as cus_file:
            customer_data=cus_file.read()
            each_customer=customer_data.strip().split('\n')
            # process each line separately
            for line in each_customer:
                # Replace single quotes with double quotes to make it a valid JSON string
                line= line.replace("'", "\"")
                # Convert the string line to a dictionary
                customers=json.loads(line)
                for i in customers.keys():
                    if i==acc_no:
                        print("Account Number:",i)
                        print("Account Holder Name:", customers.get(i).get("name"))
                        print("Balance:", customers.get(i).get("balance"))
                        return customers.get(i).get("balance")
    def c_login(self,user,pwd):
        with open("Customer_Details","r") as cus_file:
            customer_data=cus_file.read()
            each_customer=customer_data.strip().split('\n')
            #process each line seperately
            for line in each_customer:
                # Replace single quotes with double quotes to make it a valid JSON string
                line= line.replace("'", "\"")
                # Convert the string line to a dictionary
                customers=json.loads(line)
                for i in customers.keys():
                    if customers.get(i).get("username")==user and customers.get(i).get("password") ==pwd:
                        print("\t\t\t\t\tYou are successfully logged in!")
                        return i
        print("Incorrect password or username")
        return False

    def withdraw_amount(self,acc_no,amount,balance):
        with open("Customer_Details","r") as cus_file:
            customer_data=cus_file.read()
        each_customer=customer_data.strip().split('\n')
        modify_data = []
        for line in each_customer:
            line= line.replace("'", "\"")
            customers=json.loads(line)
            if acc_no in customers:
                balance -= amount
                customers[acc_no]["balance"]=balance
            modify_data.append(json.dumps(customers))
        with open("Customer_Details", "w") as n_file:
            for line in modify_data:
                line = line.replace("\"", "'")
                n_file.write(line+"\n")
        return balance

    def deposit_amount(self, acc_no,amount,balance):
        with open("Customer_Details","r") as cus_file:
            customer_data=cus_file.read()
        each_customer=customer_data.strip().split('\n')
        modify_data = []
        for line in each_customer:
            line= line.replace("'", "\"")
            customers=json.loads(line)
            if acc_no in customers:
                balance += amount
                customers[acc_no]["balance"]=balance
            modify_data.append(json.dumps(customers))
        with open("Customer_Details", "w") as n_file:
            for line in modify_data:
                line = line.replace("\"", "'")
                n_file.write(line+"\n")
        return balance

    def customer_exit(self):
        n = input("Press L:")
        if n.lower() == "l":
            print("########################################################")
            print("\t\t\t* You are successfully logged out.")
    def exit(self):
        n = input("Press e:")
        if n.lower() =="e" :
            print("########################################################")
            print("\t\t\t* Try again.")

