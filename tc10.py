import random
a=int(input('adad entekhab kon  '))
for i in range(1,10):
    b=int(random.randrange(1,101))
    if b>a:
        print(f'adad hads zade shode{b} adad kochik tar hads bezan')
    elif b<a:
        print(f'adad hads zade shode{b} adad bozorg tar hads bezan')
    elif b==a:
        print(f'adad hads zade shode{b} hads dorost bod')
        break
if a!=b:
    print('  forsat tamam shod natonesti hads bezani')
    print(f'adad entekhab shode {a} bod')
