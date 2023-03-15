import heapq
import random
import timeit
import matplotlib.pyplot as plt

#Efficient Implementation
class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.index = 0

    def insert(self, priority, data):
        heapq.heappush(self.queue, (-priority, self.index, data))
        self.index += 1

    def extract_max(self):
        return heapq.heappop(self.queue)[-1]



# create a list of 1000 random integers
data = [random.randint(0, 1000) for i in range(1000)]

# inefficient implementation
pq_inefficient = PriorityQueue()
for d in data:
    pq_inefficient.insert(d, d)


# efficient implementation
pq_efficient = PriorityQueue()
for d in data:
    pq_efficient.insert(d, d)

# measure time to extract max element for the inefficient implementation
time_inefficient = []
for i in range(100):
    start_time = timeit.default_timer()
    pq_inefficient.extract_max()
    end_time = timeit.default_timer()
    time_inefficient.append(end_time - start_time)

# measure time to extract max element for the efficient implementation
time_efficient = []
for i in range(100):
    start_time = timeit.default_timer()
    pq_efficient.extract_max()
    end_time = timeit.default_timer()
    time_efficient.append(end_time - start_time)

# plot the distribution of measured values
plt.hist(time_inefficient, bins=20, alpha=0.5, label='Inefficient')
plt.hist(time_efficient, bins=20, alpha=0.5, label='Efficient')
plt.legend(loc='upper right')
plt.show()

# print the aggregate of measured values
print('Inefficient: Min time: {:.8f}, Avg time: {:.8f}'.format(min(time_inefficient), sum(time_inefficient) / len(time_inefficient)))
print('Efficient: Min time: {:.8f}, Avg time: {:.8f}'.format(min(time_efficient), sum(time_efficient) / len(time_efficient)))