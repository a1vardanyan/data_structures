#Task 2: List of size N is a binary heap with maximum priotiry. For log(N) change it to min priority.

class binary_heap():
    'min priority'
    def __init__(self):
        self.capacity = 1
        self.data = [0 for i in range(self.capacity)]
        self.size = 0
    def get_max1(self):
        if self.size > 0:
            temp = self.data.copy()
            temp.reverse()
            temp_full = [-i for i in temp if i != 0]
            heap_max = binary_heap()
            for k in temp_full:
                heap_max.add_element(k)
            heap_max_correct = [-i for i in heap_max.check() if i != 0]
            return heap_max_correct[0]
        return None
    def get_max2(self):
        if self.size > 0:
            temp = self.data.copy()
            temp = temp[:self.size]
            sorted_value = self.quicksort(0, self.size-1, temp)
            return sorted_value[-1]
        return None
    def max_priority(self):
        if self.size > 0:
            temp = self.data.copy()
            temp.reverse()
            temp_full = [-i for i in temp if i != 0]
            heap_max = binary_heap()
            for k in temp_full:
                heap_max.add_element(k)
            heap_max_correct = [-i for i in heap_max.check()]
            return heap_max_correct
        return None
    def get_min(self):
        if self.size > 0:
            return self.data[0]
        return None
    def shift_down(self, i):    
        min_children = i
        if 2*i + 1 < self.size and self.data[2*i + 1] < self.data[min_children]:
            min_children = 2*i + 1
        if 2*i + 2 < self.size and self.data[2*i + 2] < self.data[min_children]:
            min_children = 2*i + 2
        if i != min_children:
            self.data[min_children], self.data[i] = self.data[i], self.data[min_children]
            self.shift_down(min_children)        
    def extract_min(self):
        if self.size > 0:
            min_data = self.data[0]
            self.data[0], self.data[self.size-1] = self.data[self.size-1], 0
            self.size -= 1
            self.shift_down(0)
        return min_data
    def resize(self, new_capacity):
        self.capacity = new_capacity
        self.data += [0 for i in range(self.capacity)]
    def shift_up(self, i):
        if i <= 0:
            return
        parent = (i - 1) // 2
        if self.data[i] < self.data[parent]:
            self.data[i], self.data[parent] = self.data[parent], self.data[i]
        self.shift_up(parent)
    def add_element(self, element):
        if self.size >= self.capacity:
            self.resize(2*self.capacity)
        self.data[self.size] = element
        self.size += 1
        self.shift_up(self.size - 1)
    def check(self):
        return self.data
    def partition(self, l, r, nums):
        pivot, ptr = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
        nums[ptr], nums[r] = nums[r], nums[ptr]
        return ptr
    def quicksort(self, l, r, nums):
        if len(nums) == 1:
            return nums
        if l < r:
            pi = self.partition(l, r, nums)
            self.quicksort(l, pi-1, nums)
            self.quicksort(pi+1, r, nums)
        return nums

#Given
N = 10
import numpy as np
X = [np.random.randint(1,100) for j in range(N)]
heap_min = binary_heap()
for i in range(len(X)):
    heap_min.add_element(X[i])
print(heap_min.get_max1())
print(heap_min.get_max2())
print(heap_min.max_priority())
print(heap_min.check())
