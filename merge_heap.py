class binary_heap():
    'min priority'
    def __init__(self):
        self.capacity = 1
        self.data = [0 for i in range(self.capacity)]
        self.size = 0
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
 
import numpy as np

def mergeheap(Y, N):
    bh = binary_heap()
    final_list = []
    sorted_list = []

    for i in range(N):
        bh.add_element(Y[i][0])
        del Y[i][0]
    final_list.append(bh.extract_min())

    while any(len(i) > 0 for i in Y):
        if len(Y[final_list[-1][1]]) == 0:
            for i in Y:
                if len(i) != 0:
                    list_num = i[0][1]
                    break
        else:
            list_num = final_list[-1][1]
        bh.add_element(Y[list_num][0])
        del Y[list_num][0]
        final_list.append(bh.extract_min())


    while bh.check()[0] != 0:
        final_list.append(bh.extract_min())
    for j in range(len(final_list)):
        sorted_list.append(final_list[j][0])
    return sorted_list
  
#example
M = 8
N = 10
X = [[(np.random.randint(1,1000),j) for i in range(M)] for j in range(N)]
X = np.sort(X,1)
Y = [[tuple(X[j][i]) for i in range(M)] for j in range(N)]

len(mergeheap(Y, N))
