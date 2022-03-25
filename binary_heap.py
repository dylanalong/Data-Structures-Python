from math import floor
from pickle import NONE

class min_heap:
    def __init__(self, init_size) -> None:
        self.arr = [NONE] * init_size
        self.size = 0

    def resize(self):
        temp = [NONE]*len(self.arr)
        self.arr = self.arr + temp 
    
    def left_child(self, index) -> int:
        return index*2
    
    def right_child(self, index) -> int:
        return index*2+1

    def parent(self, index) -> int:
        return floor(index/2)

    def swap(self, index1, index2):
        self.arr[index1], self.arr[index2] = self.arr[index2], self.arr[index1]

    def insert(self, value):
        if self.size >= len(self.arr)-1:
            self.resize()
        index = self.size+1
        self.arr[index] = value
        while index > 1 and value < self.arr[self.parent(index)]:
            self.swap(self.parent(index), index)
            index = self.parent(index)
        self.size += 1

    def delete(self):
        min = self.arr[1]
        self.swap(1, self.size)
        self.size -= 1
        self.heapify(1)
        return min
    
    def heapify(self, index):
        min = NONE
        left = self.left_child(index)
        right = self.right_child(index)
        if left <= self.size and right <= self.size:
            if self.arr[left] < self.arr[right]:
                min = left
            else:
                min = right
        elif left <= self.size:
            if self.arr[left] < self.arr[index]:
                min = left
        if min != NONE:
            self.swap(index, min)
            self.heapify(min)
            

if __name__ == '__main__':
    heap = min_heap(10)
    heap.insert(20)
    heap.insert(15)
    heap.insert(30)
    heap.insert(10)
    heap.insert(5)
    heap.insert(8)
    heap.insert(3)
    min = heap.delete()
    min = heap.delete()
    print("hello")