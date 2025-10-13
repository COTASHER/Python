# Решение

print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f=(x or not y)<=(w==z)
                f1=(x or not y)==(w<=z)
                print(x,y,z,w,f,f1)

answer = 'ywxz'

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 11, answer, '7379de4777f5748aa568b8d0bf8c3795'))