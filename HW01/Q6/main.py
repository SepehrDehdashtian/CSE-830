T = int(input())

for _ in range(T):
    x, y = list(map(int, input().split()))

    # Finding number of multiples of 12 between x and y
    l_12 = x // 12 if x % 12 == 0 else x // 12 + 1
    u_12 = y // 12

    if u_12 or l_12:
        num_12 = u_12 - l_12 + 1

    # Finding number of perfect squares between x and y
    l_sq = int(x ** 0.5) if x ** 0.5 == int(x ** 0.5) else int(x ** 0.5) + 1
    u_sq = int(y ** 0.5)

    if u_sq or l_sq:
        num_sq = u_sq - l_sq + 1

    intersection = []

    for j in range(l_sq, u_sq + 1):
        if (j ** 2) % 12 == 0:
            intersection.append(j**2)
    
    num_12_sq = len(intersection)

    print(num_12, num_sq, num_12_sq)

