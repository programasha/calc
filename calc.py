while True:
    s= input()
    if s== "exit":
        break
    num1, op, num2 = s.split(' ')
    num1= int(num1)
    num2= int(num2)
    if op== '+':
        print(num1 + num2)
    elif op== '-':
        print(num1 - num2)
    elif op== '*':
        print(num1 * num2)
    elif op== '/':
        if num2 ==0:
            print("DO NOT DIVIDE BY ZERO!!!")
        else:
            print(num1 / num2)
    elif op=='^':
        print(num1 ** num2)
    elif op=='%':
        print(num1 % num2)
    elif op== 'r':
        print(num1 ** (1/num2))

    
