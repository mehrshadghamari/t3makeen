for i in range(7,0,-1):
    a="#"*i
    print(a)
    if i==1:
        for j in range(1,8):
            b="#"*j
            print(b)
e=8
m=1
for k in range(e,16):
    f=" "*k
    f=f+("#"*(e))
    e-=1
    print(f)
    if k==15:
        for h in range(15,8,-1):
            g=" "*h
            g=g+("#"*m)
            m+=1
            print(g)





