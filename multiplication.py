def jadval(num):
    print(' ', *list(range(1, num+1)), sep='  ')
    for i in range(1, num+1):
        print(i, end=' ')
        for j in range(1, num+1):
            print(f'{i*j: >2}', end=' ')
        print()

num = int(input())
jadval(num)
