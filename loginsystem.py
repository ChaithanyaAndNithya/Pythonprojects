# This program will take the user's user id and password.
#He/she can log in again any number of times.
#This program will also be able to take multiple users's info


infodic = dict()
x = 0
while x == 0:
    exit = input("If you want to exit this program, type 'exit', otherwise, type 'continue': ")
    if exit == "exit" :
        break
    elif exit == "continue" :
        print("Thank you")
    elif exit != "exit" or exit != "continue" :
        print("please enter type in one of the words above")
        continue
    userid = input("Enter your userid: ")
    userpass = input("Enter your password: ")
    if userid not in infodic :
        infodic[userid] = userpass
        print("Thank you for signing up!")
    elif userid in infodic :
        if userpass == infodic[userid] :
            print("Access granted\nThank you for logging in!")
        else :
            print("Access denied")
