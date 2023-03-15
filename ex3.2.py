import json
import time
import matplotlib.pyplot as plt
import requests


#Load the array and the list of search tasks.
data_url = 'https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment3/ex2data.json'
tasks_url = 'https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment3/ex2tasks.json'

data = requests.get(data_url).json()
arr = data


tasks = requests.get(tasks_url).json()


def binary_search(arr, x, start, end, mid):
    if start > end:
        return False

    if arr[mid] == x:
        return True

    if arr[mid] > x:
        return binary_search(arr, x, start, mid - 1, (start + mid - 1) // 2)

    return binary_search(arr, x, mid + 1, end, (mid + 1 + end) // 2)



results = []

for task in tasks:
    x = task
    times = []
    best_time = float('inf')
    best_midpoint = None

    for i in range(len(arr)):
        start_time = time.time()
        binary_search(arr, x, 0, len(arr) - 1, i)
        end_time = time.time()
        elapsed_time = end_time - start_time

        times.append(elapsed_time)

        if elapsed_time < best_time:
            best_time = elapsed_time
            best_midpoint = i

    results.append({
        'x': x,
        'times': times,
        'best_midpoint': best_midpoint
    })


#Plot
for result in results:
    x = result['x']
    times = result['times']
    best_midpoint = result['best_midpoint']

    plt.scatter([best_midpoint], [min(times)], color='green', s=50, marker='o')
    plt.scatter(range(len(times)), times, color='blue', s=5, alpha=0.5)
    plt.title(f'Search for {x}')
    plt.xlabel('Midpoint')
    plt.ylabel('Time (seconds)')
    plt.show()


