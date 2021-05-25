""" 4. Create a login page backend to ask users to enter the username and password. Make sure to
ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
should not be more than 3 times. """

print("Welcome to the login page:")
name=input("Please enter the username: ")
password=input("Please enter the password: ")
counter=1
while counter<=3:
    repassword=input("RE Type the password: ")
    if password==repassword:
        print("Sucsess")
        break
    else:
        print("Password does not match")
        counter+=1
        #repassword=input("Please enter the right password :")
if counter==4:
    print("Sorry! 3 Attempts done")
       
        
