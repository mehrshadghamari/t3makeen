try:
    a=int(input(' enter your tempreture in C  '))
    b=a*9/5+32
    if a<-273 :
     raise SyntaxError('invalid tempreture')
    else:
        print(b)
except  SyntaxError as e :
    print(e)






