import heapq

li = []
heapq.heapify(li)
heapq.heappush(li, 10)
heapq.heappush(li, 20)
heapq.heappush(li, 1)
print(li)
print(heapq.heappop(li))
print(li)
