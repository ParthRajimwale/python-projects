while True:
    inpt=float(input("Please enter a number: "))
    inpt1=float(input("Please enter another number: "))
    inpt2=input("Please enter the operation you want to perform from the following -(+,-,*,/,Use Powers): ")
    if inpt2=="+":
        b=inpt+inpt1
        print("The sum of the numbers is - ",b)
    elif inpt2=="-":
        c=inpt-inpt1
        print("The difference of the numbers is - ",c)
    elif inpt2=="*":
        d=inpt*inpt1
        print("The product of the numbers is - ",d)
    elif inpt2=="/":
        if inpt1==0:
            print("Denominator cannot be 0,please try again")
        else:
             e=inpt/inpt1
             print("The quotient is - ",e)
    elif inpt2=="Use Powers":
        f=inpt**inpt1
        print("The number",inpt,"raised to the power",inpt1,"is",f)
    else:
        print("Please enter the operation in exact words as given in the above brackets and try again")
    x=input("Do you want to continue?(Yes/No): ")
    if x.lower()=="no":
        break
    

    

    
