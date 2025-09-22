a = int(input())
b = int(input())
c = int(input())
m = 0
b = (b / 12) + 100
while a < c:
    m += 1
    a = a * b / 100
    print(f'{m} - {a:.2f}')