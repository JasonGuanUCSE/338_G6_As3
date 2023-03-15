import random
import time
import matplotlib.pyplot as plt


#Inefficient implementation

def search(arr, x):
  for i in range(len(arr)):
    if arr[i] == x:
      return i
  return -1

#Efficient implementation
def binary_search(arr, x):
  low = 0
  high = len(arr) - 1
  while low <= high:
    mid = (low + high) // 2
    if arr[mid] < x:
      low = mid + 1
    elif arr[mid] > x:
      high = mid - 1
    else:
      return mid
  return -1



arr = sorted([random.randint(1, 10000) for _ in range(1000)])

results1 = []
results2 = []
for i in range(100):
    x = random.randint(1, 10000)
    start_time = time.time()
    search(arr, x)
    results1.append(time.time() - start_time)
    start_time = time.time()
    binary_search(arr, x)
    results2.append(time.time() - start_time)

plt.hist(results1, bins=20, alpha=0.5, label='linear search')
plt.hist(results2, bins=20, alpha=0.5, label='binary search')
plt.legend(loc='upper right')
plt.show()

print('Average time for linear search:', sum(results1) / len(results1))
print('Average time for binary search:', sum(results2) / len(results2))
