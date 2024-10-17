Medical_cause=input("Do you have a Medical cause? Yes or no?:")
atendant=int(input("Enter your atendance percentage:"))

if Medical_cause == 'Yes':
    print("You are allowed.")
else:
    if atendant>=75:
        print("You are allowed.")
    else:
        print("You are not allowed.")