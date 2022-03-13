res=[]
for item in range(2,12):
    for b in range(2,item):
        if not item%b==0:
            res.append(item)
print(res)
            