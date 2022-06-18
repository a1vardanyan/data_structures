class binary_heap:
    'min priority'
    def __init__(self):
        self.data = [0 for i in range(1)]
        self.size = 0
        self.capacity = 1
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
            self.resize(self, 2*self.capacity)
        self.data[self.size] = element
        self.size += 1
        self.shift_up(self.size - 1)
    def check(self):
        print(self.data)
        
un_list = [5, 9, 100, 14, 2, 10, 19]
bh = binary_heap()
for i in un_list:
    bh.add_element(i)
bh.check()
print(bh.get_min())
bh.check()
print(bh.extract_min())
