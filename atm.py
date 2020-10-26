database = {
    'shaloo28': {
        'name': 'shaloo',
        'age': 29,
        'email': 'justmailmesh56@gmail.com',
        'password': 'loo@98',
        'amount': 50000
    },

    'Jenny78': {
        'name': 'Jenny',
        'age': 25,
        'email': 'jenny44@gmail.com',
        'password': 'nny@55',
        'amount': 70000
    }

}

enter = int(input('Enter your choice : \n1. Sign in \n2. Sign up \n3. Exit'))
    
if enter == 1:
    username = input('Enter username : ')
    if username not in database.keys():
        print('Username not Exist')
        enter = int(input('Enter your choice : \n1. Sign in \n2. Sign up \n3. Exit'))

        username = input('Enter username : ')
    password = input('Enter password :')



    if username in database.keys():
        if password == database[username]['password']:
            print(f"Welcome {database[username]['name']}")
            def main():
                print('Choices : \n1. Check balance \n2. Deposit Balance \n3. Withdrawal \n4. Logout')

            def deposit(amt):
                (database[username]['amount'])=(database[username]['amount'])+amt
                print('Account is credited by : ', str(amt))
                print('Current Balance : ', int(database[username]['amount']))



            def withdrawal(amt):
                if amt < database[username]['amount']:
                    database[username]['amount']= database[username]['amount'] - amt
                    print("Collect your cash : " + str(amt))
                    print('Current Balance : ', int(database[username]['amount'])+amt-amt)
                else:
                    print("Sorry, Insufficient Fund..")

            while True:
                main()
                ch = int(input("Enter Your Choice: "))
                if ch == 1:
                    print("Current Balance : ", database[username]['amount'])

                elif ch == 2:
                    deposit(int(input("Enter Amount: ")))

                elif ch == 3:
                    withdrawal(int(input("Enter Amount: ")))

                else:
                    exit()


        print('Password Not Found!')


    else :
        exit()


elif enter == 2:
    username=input('Enter your username : ')
    name=input('Enter your name : ')
    age=int(input('Enter your age : '))
    email=input('Enter email ID : ')
    password=input('Enter password : ')
    amount=int(input('Enter amount : '))
    print('Username successfully created')

else:

    passwrd = input(('Will you like to forgot password(f), change password(c) or exit(e)? '))
    if passwrd == 'c':
        username=input('Enter username: ')
        if username in database.keys():
            passwrd = input('Enter password you want to create : ')
            print('Password successfully changed !')
        else:
            print('Username not Found')
            pass

    if passwrd == 'f':
         username=input('Enter username: ')
         email = input('Enter email ID :')
         if database[username]['email'] == email:
             pswrd = input('Type Password : ')
             confirm = input('Confirm Password : ')
             if pswrd == confirm :
                 print('Password successfully generated')
             else:
                 print('Password mismatched')
                 pswrd = input('Type Password : ')
                 confirm = input('Confirm Password : ')
                 if pswrd == confirm:
                     print('Password successfully generated')


         else:
             print('Email ID does not exist')



    else:
        print('Thank You')
    exit()








