while True:
    num=float(input("enter a number:"))

    operators ={
        "add": '+',
        "sub": '-',
        "div": '/',
        "mult": '*',
           }

    operator=operators
    operator=input("chose your operator add: '+' , sub: '-' , div: '/' , mult: '*' , :")

    num2=float(input("enter a number: "))

    if operator == '/'and num2 == 0:
        print("division by zero is not allowed")
        continue 

    if operator == '+':
        print(num+num2)
    elif operator == '-':
        print(num-num2)
    elif operator =='*':
        print(num*num2)
    elif operator == '/':
        print(num/num2)
    elif operator == 'e':
        break
    else:
        print("invalid operator")

    exit=input("do you want exit yes/no:")
    if exit =='yes':
        print("thank you")
        break
    elif exit=='no':
        continue
        
