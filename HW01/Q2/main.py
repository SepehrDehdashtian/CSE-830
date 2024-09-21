num_tests = int(input())

for test_idx in range(num_tests):
    line = input().split()
    S = int(line[0]) # Starting bet
    k = int(line[1]) # Number of rounds

    for i in range(k):
        if S % 2 == 0:
            S = (S - 99) * 3
        else:
            S = (S - 15) * 2
        
        while S < 0:
            S += 1000000

        while S > 1000000:
            S -= 1000000

    print(S)

