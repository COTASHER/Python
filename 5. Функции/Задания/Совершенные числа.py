def is_perfect(number):
    summ = 0
    current = 1
    while current < number:
        if number % current == 0:
            summ += current
        current += 1
    return summ == number

n = int(input())
num = 2
while n > 0:
    if is_perfect(num):
        print(num, end=' ')
        n -= 1
    num += 1
