from bitarray import bitarray
from mmh3 import hash

class BloomFilter:
    def __init__(self, size, num_hash):
        self.size = size
        self.num_hash = num_hash
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, item):
        for i in range(self.num_hash):
            digest = hash(item, i) % self.size
            self.bit_array[digest] = 1

    def check(self, item):
        for i in range(self.num_hash):
            digest = hash(item, i) % self.size
            if self.bit_array[digest] == 0:
                return False
        return True

# Parameters for the Bloom filter
bloom_size = 1 * 8 * 10**6  # 16MB
num_hash = 3 

bloom = BloomFilter(bloom_size, num_hash)


# Add to the bloom filter
M = int(input())  
for _ in range(M):
    value = input().strip()
    bloom.add(value)

# Checking encounter
N = int(input())
encountered = 0

for _ in range(N):
    value = input().strip()
    if bloom.check(value):
        encountered += 1



print(encountered)
