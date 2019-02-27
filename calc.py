while True:
    s= input()
    s.split(' ')
    if s[1]== '+':
        print(int(s[0]) + int(s[2]))
    elif s[1]== '-':
        print(int(s[0])- int(s[2]))
    elif s[1]== '*':
        print(int(s[0])*int(s[2]))
    elif s[1]== '/':
        print(int(s[0])/int(s[2]))
    elif s[1]=='^':
        print(int(s[0])**int(s[2]))

    
