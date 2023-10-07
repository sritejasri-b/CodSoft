def cal():
    while True:
        num1 = int(input("Enter 1st number: "))
        num2 = int(input("Enter 2nd number: "))
        print("Choose any arithmetic operation below to be performed ")
        print("1.Enter 1 for Addition\n2.Enter 2 for Subtraction\n3.Enter 3 for Multiplication\n4.Enter 4 forDivision")
        choice = int(input("Enter choice: "))

        while 1 <= choice <= 4:
            if choice == 1:
                print("Addition:", num1 + num2)
            elif choice == 2:
                print("Subtraction:", num1 - num2)
            elif choice == 3:
                print("Multiplication:", num1 * num2)
            elif choice == 4:
                if num2 == 0:
                    print("Division by zero is not allowed.")
                else:
                    print("Division:", num1 / num2)
            else:
                print("Invalid choice")
            choice = int(input("Enter any other operation on same numbers: "))

        print("Do you want to enter again?\n1. Yes\t2. No")
        ch = int(input("Enter your choice: "))
        if ch == 2:
            print("Thank you 😊")
            break

cal()




