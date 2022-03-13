a=int(input('1 adad dar nazar begir '))
for i in range(1,10):
    b=int(input('hads bezanid'))
    if b>a:
        print('adad kochik tar hads bezan')
    elif b<a:
        print('adad bozorg tar hads bezan')
    elif b==a:
        print('hads dorost bod')
        break
if a!=b:
    print('  forsat tamam shod natonesti hads bezani')
