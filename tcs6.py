b=0
d=8
for i in range(8,b,-1):
    a=" "*i
    a=a+("#"*(b+1))
    b+=1
    print(a)
    if i==1:
        for j in range(1,d):
            c=" "*(j+1)
            c=c+("#"*(d-1))
            d-=1
            print(c)
