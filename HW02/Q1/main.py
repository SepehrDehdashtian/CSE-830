N = int(input())

id2votes = dict()

max_id = None

for _ in range(N):
    ID = int(input())

    if ID in id2votes:
        id2votes[ID] += 1
    else:
        id2votes[ID] = 1
        if max_id is None:
            max_id = ID

    if id2votes[ID] > id2votes[max_id]:
        max_id = ID

print(max_id)