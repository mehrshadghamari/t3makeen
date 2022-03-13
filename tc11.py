a=input("enter a choice...sang,kaghaz,gheichi  ")
b=input("enter a choice...sang,kaghaz,gheichi  ")
if a=="sang" and b=="kaghaz" :
    print("b won the game...")

elif a=="sang" and b=="gheichi" :
    print("a won the game...")

elif a=="sang" and b=="sang" :
    print("a and b equal...")

elif a=="kaghaz" and b=="kaghaz" :
    print("a and b equal...")

elif a=="kaghaz" and b=="gheichi" :
    print("b won the game...")

elif a=="kaghaz" and b=="sang" :
    print("a won the game...")

elif a=="gheichi" and b=="kaghaz":
    print("a won the game...")

elif a=="gheichi" and b=="gheichi":
    print("a and b equal...")

elif a=="gheichi" and b=="sang" :
    print("b won the game...")
else:
    print(" THE GAME IS NOT TRUE...")

