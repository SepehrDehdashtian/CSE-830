
N = int(input())

a = [int(a_i) for a_i in input().split()]

while sum(a):
    print(len(a))
    min_a = min(a)
    a = list(map(lambda x: x - min_a, a))
    while 0 in a:
        a.remove(0)




