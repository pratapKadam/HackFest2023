n = int(input('Enter the number: '))
i = 0
print("\n\nPattern 1\n")
while i <= n - 1:
    j = 0
    while j < i:
        print('', end= ' ')
        j=j+ 1
    k = i
    while k <= n - 1:
        print('*', end= ' ')
        k =k+ 1
    print()
    i=i+ 1

i = n-1
while i >= 0:
    j = 0
    while j < i:
        print('', end= ' ')
        j=j+1
    k = i
    while k <=  n - 1:
        print('*', end= ' ')
        k=k+1
    print('')
    i=i-1
