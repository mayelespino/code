import heapq

heap = []
heapq.heappush(heap, (1, 'one'))
heapq.heappush(heap, (10, 'ten'))
heapq.heappush(heap, (5,'five'))

for x in heap:
	print(x,end='')
print

heapq.heappop(heap)
print("\n","-"*10)
for x in heap:
	print(x,end='')
print
print("\n","-"*10)
# the smallest
print(heap[0])