T = int(input())

for _ in range(T):
    n, m, c = list(map(lambda a: int(a), input().split()))
    
    miles = 0
    frag = 0
    
    while n // m + frag // c > 0:
        miles += n // m # miles from remaining leaves
        miles += frag // c # miles from fragments

        frag -= frag // c * (c - 1) # remaining fragments
        frag += n // m # fragments from the current wings

        n -= n // m * m # remaining leaves

    print(miles)