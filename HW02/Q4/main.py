import heapq

N = int(input())

instructions = [tuple(map(int, input().split())) for _ in range(N)]

instructions.sort()

current_time = 0 
total_wait_time = 0
heap = []
idx = 0  

while heap or idx < N:
    while idx < N and instructions[idx][0] <= current_time:
        heapq.heappush(heap, (instructions[idx][1], instructions[idx][0]))  # (Li, Ti)
        idx += 1

    if heap:
        li, ti = heapq.heappop(heap)
        current_time += li 
        # Calculate wait time
        total_wait_time += current_time - ti  
    else:
        current_time = instructions[idx][0]

print(total_wait_time // N)