import random
import time

# Part 1: Selection Algorithms

def medianOfMedians(arr, k):
    """Deterministic selection algorithm using Median of Medians"""
    if len(arr) <= 5:
        return sorted(arr)[k]

    sublists = [arr[i:i+5] for i in range(0, len(arr), 5)]
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]
    pivot = medianOfMedians(medians, len(medians) // 2)

    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]

    if k < len(left):
        return medianOfMedians(left, k)
    elif k > len(left):
        return medianOfMedians(right, k - len(left) - arr.count(pivot))
    else:
        return pivot

def randomizedPartition(arr, left, right):
    """Helper function for Randomized Quickselect"""
    pivotIdx = random.randint(left, right)
    arr[right], arr[pivotIdx] = arr[pivotIdx], arr[right]
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i

def randomizedSelect(arr, left, right, k):
    """Randomized Quickselect algorithm"""
    if left == right:
        return arr[left]
    
    pivotIndex = randomizedPartition(arr, left, right)
    if k == pivotIndex:
        return arr[pivotIndex]
    elif k < pivotIndex:
        return randomizedSelect(arr, left, pivotIndex - 1, k)
    else:
        return randomizedSelect(arr, pivotIndex + 1, right, k)

# Performance Analysis for Selection Algorithms
def analyzeSelectionAlgorithms():
    print("\n=== Selection Algorithm Performance Analysis ===")
    sizes = [100, 500, 1000, 5000]
    for size in sizes:
        arr = [random.randint(1, 10000) for _ in range(size)]
        k = size // 2  # Find median
        
        startTime = time.time()
        medianOfMedians(arr, k)
        medianTime = time.time() - startTime

        startTime = time.time()
        randomizedSelect(arr[:], 0, size - 1, k)
        quickSelectTime = time.time() - startTime

        print(f"Array Size: {size} | Median of Medians: {medianTime:.6f}s | Quickselect: {quickSelectTime:.6f}s")

# ------------------------------
# Part 2: Data Structures
# ------------------------------

class CustomArray:
    """Custom Array Implementation"""
    def __init__(self, size):
        self.array = [None] * size
        self.size = size

    def insert(self, index, value):
        if 0 <= index < self.size:
            self.array[index] = value

    def access(self, index):
        return self.array[index] if 0 <= index < self.size else None

class Stack:
    """Stack Implementation using List"""
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop() if self.stack else "Stack Empty"

    def peek(self):
        return self.stack[-1] if self.stack else "Stack Empty"

class Queue:
    """Queue Implementation using List"""
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0) if self.queue else "Queue Empty"

    def front(self):
        return self.queue[0] if self.queue else "Queue Empty"

class Node:
    """Node Class for Linked List"""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Singly Linked List Implementation"""
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = newNode

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Performance Analysis for Data Structures
def analyzeDataStructures():
    print("\n=== Data Structure Operations Analysis ===")

    # Custom Array
    arr = CustomArray(10)
    arr.insert(2, 100)
    print(f"Array[2]: {arr.access(2)} (Expected: 100)")

    # Stack
    stack = Stack()
    stack.push(10)
    stack.push(20)
    print(f"Stack Top: {stack.peek()} (Expected: 20)")
    print(f"Stack Pop: {stack.pop()} (Expected: 20)")

    # Queue
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(15)
    print(f"Queue Front: {queue.front()} (Expected: 5)")
    print(f"Queue Dequeue: {queue.dequeue()} (Expected: 5)")

    # Linked List
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    print("Linked List (Before Deletion): ", end="")
    ll.traverse()
    ll.delete(2)
    print("Linked List (After Deletion): ", end="")
    ll.traverse()

# Run All Analyses
if __name__ == "__main__":
    analyzeSelectionAlgorithms()
    analyzeDataStructures()
