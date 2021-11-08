import time
current_local = time.localtime()
current_local.tm_zone
count = 5


while count > 0:

        userName = input("Enter Username")
        if userName == "Python":
            password = input("Enter Password")
            if password == "Python@123":
                print("Login Successful")
                break
            else:
                count = count-1
                if count == 0:
                    print("Your account is locked for 24 hours")
                else:
                    print("Wrong Password Please try again. You have",count,"attempts left")

        else:
            count = count-1
            if count == 0:
                print("Your account is locked for 24 hours")

            else:
                print("Wrong Username Please try again. You have",count,"attempt left")



