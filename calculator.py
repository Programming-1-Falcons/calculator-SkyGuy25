while True:
    print ("Welcome to the Calculator, just follow instructions below to calculate")
    Rn1 = False
    print("+ - Addition")
    print("- - Subtraction")
    print("* - Multiplication")
    print("/ - Division")
    print("** - Power/Exponent")
    Num1 = eval(input("Please enter your First number: "))
    Op = input("Please enter your Operation type: ")
    Num2 = int(input("Please enter your Second number: "))



    if Op == "+":
        Ans = Num1 + Num2
    elif Op == "-":
        Ans = Num1 - Num2
    elif Op == "*":
        Ans = Num1 * Num2
    elif Op == "/":
        Ans = Num1 / Num2
    elif Op == "**":
        Ans = Num1 ** Num2

    
    print(str(Num1) + " " + Op + " " +str(Num2)+" = "+ str(Ans))
