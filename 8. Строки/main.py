# Использование функции строковой count
print('Hello world'.count('l')) # 3

# Использование функции zfill
print('12340'.zfill(10)) # 000012340

# Использование функции strip
print('   Hello world    '.strip()) # 'Hello world'
print('   Hello world    '.rstrip()) # '   Hello world'
print('   Hello world    '.lstrip()) # 'Hello world    '

# В функцию strip можно передать символы, которые нужно удалить
print('...Hello world...'.strip('.')) # 'Hello world'
print('...Hello world...'.lstrip('.')) # 'Hello world...'
print('...Hello world...'.rstrip()) # '...Hello world'

# Использование функции join
print('-'.join(['a', 'b', 'c'])) # a-b-c
