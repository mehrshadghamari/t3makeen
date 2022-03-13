for i in 1, 2, 3, 4, 5:
    if i == 4:
        end = ''
    else:
        end = '\n'
    print('#' * (5 - i) + ' ' * (i - 1) * 2 + '#' * (5 - i), end=end)

for i in 1, 2, 3, 4:
    print('#' * i + ' ' * (4 - i) * 2 + '#' * i)