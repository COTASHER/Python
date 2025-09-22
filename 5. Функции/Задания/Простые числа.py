def is_simple(number):
    current = 2
    while current < number:
        if number % current == 0:
            return False
        current += 1
    return True

n = int(input())
num = 1
while n > 0:
    if is_simple(num):
        print(num, end=' ')
        n -= 1
    num += 1