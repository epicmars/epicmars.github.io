#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Heap:
    def __init__(self, array, heap_size = None):
        if heap_size is not None:
            self.heap_size = heap_size
        else:
            self.heap_size = len(array)
        self.array = array

    @classmethod
    def left(cls, i):
        return (i << 1) + 1

    @classmethod
    def right(cls, i):
        return (i << 1) + 2

    @classmethod
    def parent(cls, i):
        return (i - 1) / 2

    @classmethod
    def swap(cls, A, i, j):
        temp = A[i]
        A[i] = A[j]
        A[j] = temp

class MaxHeap(Heap):
    def __init__(self, array, heap_size = None):
        Heap.__init__(self, array, heap_size)
        self.build()

    def build(self):
        for i in xrange(len(self.array)/2, -1, -1):
            self.max_heapify(i)
    
    def max_heapify(self, i):
        """
        heap: a max heap
        i: a heap node index
        """
        print i
        A = self.array
        heap_size = self.heap_size
        l = Heap.left(i)
        r = Heap.right(i)
        largest = i
        if l < heap_size and A[largest] < A[l]:
            largest = l
        if r < heap_size and A[largest] < A[r]:
            largest = r
        if largest != i:
            Heap.swap(A, i, largest)
            print i, self.array
            self.max_heapify(largest)

    def heap_sort(self):
        A = self.array
        for i in xrange(len(self.array) -1, -1, -1):
            Heap.swap(A, i, 0)
            self.heap_size -= 1
            self.max_heapify(0)

if __name__ == '__main__':
    array = [1, 14, 10, 8, 7, 4, 3, 2, 9, 16]
    max_heap = MaxHeap(array)
    max_heap.heap_sort()
    print max_heap.array
