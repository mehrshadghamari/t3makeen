b=0
d=10
for i in range(6,b,-1):
    a=" "*i
    a=a+("#"*(b+1))
    b+=2
    print(a)
    if i==1:
        for j in range(1,d):
            c=" "*(j+1)
            c=c+("#"*(d-1))
            d-=2
            print(c)
