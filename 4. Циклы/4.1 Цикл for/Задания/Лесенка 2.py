n = int(input())
for i in range(n):
    g = n
    while g > i:
        print(g, end='')
        g -= 1
    print()
