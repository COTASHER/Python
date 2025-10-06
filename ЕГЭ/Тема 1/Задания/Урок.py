from itertools import permutations

table = '13 14 16 25 27 31 34 41 43 47 52 56 57 61 65 72 74 75'
graph = 'бв вб вг гв гж жг же еж дб бд да ад аб ба де ед ег ге'

for p in permutations('абвгдеж'):
    new_graph=table
    for i in range(1,8):
        new_graph=new_graph.replace(str(i),p[i-1])
    if set(new_graph.split()) == set(graph.split()):
        print(p)