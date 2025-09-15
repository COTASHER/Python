# Функция, выводящая на экран последовательность целых чисел от begin до end
def print_seq(begin, end):
    for i in range(begin, end + 1):
        print(i, end=' ')
    print()


# Функция, суммирующая последовательность целых чисел от begin до end
def sum_seq(begin, end):
    s = 0
    for i in range(begin, end + 1):
        s += i
    return s

f = 5
print_seq(f, 45)
print(sum_seq(f, 45))
print_seq(1, 45)
print(sum_seq(1, 45))
print_seq(50, 100)
print(sum_seq(50, 100))
