n = int(input('Enter the number: '))
print("Pattern 2\n")
i = 1
while i <= n:
    j = n
    while j > i:
        # display space
        print(' ', end= ' ')
        j -= 1
    print('* ', end= ' ')
    k = 1
    while k < 2 * (i - 1):
        print(' ', end= ' ')
        k += 1
    if i == 1:
        print()
    else:
        print('* ')
    i += 1

i = n - 1
while i >= 1:
    j = n
    while j > i:
        print(' ', end= ' ')
        j -= 1
    print('* ', end= ' ')
    k = 1
    while k < 2 * (i - 1):
        print(' ', end= ' ')
        k += 1
    if i == 1:
        print( )
    else:
        print('*')
    i -= 1