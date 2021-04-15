from _datetime import datetime
from numpy.random import seed
from numpy.random import randint



allowedNames = ['seyi', 'montero', 'jason']
allowedPassword = ['passwordseyi', 'passwordmontero', 'passwordjason']
accountnum = []

#This function is incharge of login
def login():
    name = input("what is your name \n")
    if (name in allowedNames):
        password = input("input your password \n")
        userid = allowedNames.index(name)
        if (password == allowedPassword[userid]):
            print("Welcome %s" % name)
            print(datetime.now())
            print('here are the available options')
            print('1.Widraw ')
            print('2.deposit')
            print('3.Complain')
            Selectoption = int(input('select an option\n'))
            if Selectoption == 1:
                Widraw = int(input("How much would you like to withdraw?\n"))
                print('take your cash %d' % Widraw)
            elif Selectoption == 2:
                Deposit = int(input(" How much would you like to deposit?\n"))
                print('current balance %d' % Deposit)
            elif Selectoption == 3:
                Complain = input('What issue will you like to report? \n')
                print("Thank you for contacting us\n")

        else:
            print("password incorrect")

    else:
        print("incorrect name please make sure you have created an account in our system\n")


#This function is in charge or registering the user
def Register():
    UserName = input("input your name]\n")
    if UserName in allowedNames:
            print('username already exist place use another username\n')
    else:
        allowedNames.append(UserName)
        Newpassword = str(input('create your new password\n'))
        confirm =str(input('confirm password\n'))

        if Newpassword!= confirm:
           print('The passwords do not match\n')

        else:

            allowedPassword.append(Newpassword)
            print('Account succesfully created\n')
            # seed random number generator
            seed(1)
            # generate The Users Account number
            AccountNumber = randint(0, 5, 10)
            print('Here is your AccountNumber')
            print(AccountNumber)



print('Welcome to The Atm')
print('1.Login')
print('2.Register')

Reply=int(input('Reply'))

if Reply==1:
    login()

elif Reply==2:
    Register()





