T = int(input())
for _ in range(T):
    x, y, n = list(map(lambda a: int(a), input().split()))
    if x == y:
        print(n * x)
        continue
    
    out = [(n - k) * x + k * y for k in range(n + 1)]
    print(' '.join(list(map(lambda x: str(x), sorted(out)))))
