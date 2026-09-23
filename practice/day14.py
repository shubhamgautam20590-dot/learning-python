correct_password = "cyber123"
for attempt in range(3):
    user_password = input("Enter the password: ")
    if user_password == correct_password:
        print("Access granted.")
        break
    else:
        print("Incorrect password. Try again.")
        user_password = input("Enter the password: ")
if(attempt<3):
 print("Account locked due to too many failed attempts.")       