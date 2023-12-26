class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2

    def left(self, index):
        return (index * 2) + 1

    def right(self, index):
        return (index * 2) + 2

    # here in insertion heapify process is already done.(if we are using extraction heapify has to be done)
    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1
        while current != 0 and self.heap[self.parent(current)] > self.heap[current]:
            self.heap[current], self.heap[self.parent(current)] = (
                self.heap[self.parent(current)],
                self.heap[current],
            )
            current = self.parent(current)

    def heapify(self, index):
        r = self.right(index)
        l = self.left(index)
        small = index

        if l < len(self.heap) and self.heap[l] < self.heap[small]:
            small = l

        if r < len(self.heap) and self.heap[r] < self.heap[small]:
            small = r

        if small != index:
            self.heap[small], self.heap[index] = self.heap[index], self.heap[small]
            self.heapify(small)

    def extract_min(self):
        if self.heap is None:
            return None
        elif len(self.heap) == 1:
            return self.heap.pop()
        else:
            value = self.heap[0]
            self.heap[0] = self.heap.pop()
            self.heapify(0)
            return value

    def heap_sort(self):
        sorted_array = []
        while self.heap:
            sorted_array.append(self.extract_min())
        return sorted_array



h1 = MinHeap()
h1.insert(10)
h1.insert(20)
h1.insert(30)
h1.insert(40)
h1.insert(50)
h1.insert(3)
h1.insert(4)
h1.insert(6)

print("Min Heap:")
print(h1.heap)

print("\nExtracting minimum element:")
print(h1.extract_min())

print("\nHeap after extraction:")
print(h1.heap)

print("\nHeap Sort:")
print(h1.heap_sort())



#Que: To appply heap sort we have to apply for 


