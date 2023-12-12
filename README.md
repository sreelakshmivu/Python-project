# Python Mini-Project

Video link

https://drive.google.com/file/d/1Yh17BuEvAht5mMbfDn1y3FBnDlxf9aST/view?usp=sharing

Banking System using Python

Introduction:

Python program represents a simple banking system implemented using object-oriented programming (OOP) concepts. The system includes a Customer class with methods for account management, such as creating new customer accounts, logging in, checking account details, depositing and withdrawing funds, and logging out. The program uses a text file, "Customer_Details.txt," to store customer data in a JSON format.
      
Explanation of the Code:

Customer Class:

The Customer class contains class-level attributes for customer details and methods for various banking operations.
The display method presents a menu for users to log in or sign up.
The add_new_customer method adds a new customer to the system and updates the customer details file.
The show_account method displays account details based on the account number.
The c_login method handles customer login authentication.
The withdraw_amount and deposit_amount methods update account balances for withdrawals and deposits, respectively.
The customer_exit and exit methods handle user logout and program exit.

Banking System Execution:

The program creates an instance of the Customer class and displays the main menu.
If the user chooses to log in (option 1), the program prompts for a username and password, authenticates the user, and performs withdrawal or deposit operations.
If the user chooses to sign up (option 2), the program collects necessary information, creates a new customer account, and allows the user to log in immediately.
The program handles logout (press 'l') and exit (press 'e') operations.

Usage Example:

Users can log in with existing credentials, view their account details, and perform transactions.
New users can sign up, providing their details, and then log in to access their accounts.

Output:

The program outputs prompts and messages for user interactions, such as login success, balance updates, successful registration, and logout messages.
User input is used to navigate through the menu options and perform banking operations.
