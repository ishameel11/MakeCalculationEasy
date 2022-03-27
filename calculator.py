print("                            CALCULATOR                            \n")

while True:
    print("Choose your choice from below 1, 2, 3, 4, 5, 6: ")
    print("1. +\t", "2. -\t", "3. *\t", "4. ÷\t", "5. %\t")
    print()
    print("                 6. ||||EXIT||||")
    your_choice = int(input("Enter your choice: "))

    if your_choice in (1, 2, 3, 4, 5, 6):
        no1 = float(input('Write 1st no.: '))
        no2 = float(input('Write 2nd no.: '))
        
    if your_choice == 1:
        Add = no1 + no2
        print("Result: ", Add)
    elif your_choice == 2:
        Sub = no1 - no2
        print("Result: ", Sub)
    elif your_choice == 3:
        Multi = no1 * no2
        print("Result: ", Multi)
    elif your_choice == 4:
        Div = no1/no2
        print("Resultt: ", Div)
    elif your_choice == 5:
        Modulus = no1%no2
        print("Result: ", Modulus)
    elif your_choice == 6:
        print("Exit from the calculator")
        
        break
