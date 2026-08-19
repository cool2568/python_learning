i=''
while(i!='q'):
    print("Enter your first number")
    first_number=input()
    first_number=float(first_number)

    print('give me operator')
    operator=input()

    print("Enter your second number")
    second_number=input()
    second_number=float(second_number)


    if operator=='*':
        multiply=first_number*second_number
        print('multiply',multiply)
        
    
    elif operator=='-':
        subtraction=first_number-second_number
        print('subtraction',subtraction)
    
    elif operator=='/':
        if(second_number==0):
            print('cant divisible by zer0')
        else:
            division=first_number/second_number
            print('division',division)
    
    elif operator=='+':
        addition=first_number+second_number
        print('addition',addition)

    else:
        print('invalid operatior')
    print("use q for quit press any button for start again")
    
    i=input()



