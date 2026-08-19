def calculation(first_number,operator,second_number):

    if operator=='*':
        return first_number*second_number
       
        
    
    elif operator=='-':
        subtraction=first_number-second_number
        return subtraction
    
    elif operator=='/':
        if(second_number==0):
            return None
        else:
            return first_number/second_number
  
    elif operator=='+':
        return first_number+second_number

    else:
        return None
    


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

    result=calculation(first_number,operator,second_number)
    if result is None:print("Invalid")
    else:
        print(result)
    i=input()