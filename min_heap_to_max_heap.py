#Task 2: List of size N is a binary heap with maximum priotiry. For log(N) change it to min priority.
#Given
N = 10
import numpy as np
X = [np.random.randint(1,100) for j in range(N)]
heap_min = binary_heap()
for i in range(len(X)):
    heap_min.add_element(X[i])
y = heap_min.check()
#Min heap to max heap
y.reverse()
y = np.array(y)*(-1)
z = [i for i in y if i != 0]
heap_max = binary_heap()
for i in z:
    heap_max.add_element(i)
heap_max = np.array(heap_max.check())*(-1)
heap_max
