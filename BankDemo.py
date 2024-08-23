class Bank:

    def openAccount(self,cname,acno,balance):
        self.cname=cname
        self.acno=acno
        self.balance=balance
        print("Hello ",self.cname,", Your Account Number: ",self.acno," Is Opened with ",self.balance," Rs. ")
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
        else:
            print("Sorry Your Need Another ",amount-self.balance," Rs to withdraw ",amount)
    def checkBalance(self):
        print("Your Current Balance Is : ",self.balance)

b1=Bank()
cname=input("Enter Your Name : ")
acno=input("Enter Your Account Number : ")
bal=float(input("Enter your balance : "))
b1.openAccount(cname,acno,bal)

while True:
    print("*"*40)
    print("1.Depoit")
    print("2.Withdraw")
    print("3.Check Balance")
    print("4.Exit")
    print("*"*40)
    choice=int(input("Enter your Choice : "))
    print("*"*40)
    if choice==1:
        amount=int(input("Enter Amount to Deposited : "))
        b1.deposit(amount)
        print("*"*40)
    elif choice==2:
        amount=int(input("Enter Amount to Withdraw : "))
        b1.withdraw(amount)
        print("*"*40)
    elif choice==3:
        b1.checkBalance()
    elif choice==4:
        print("Thank Your for using our Services")
        print("*"*40)
    else:
        print("Invalid Choice.Please Try Again")
        
    
    
