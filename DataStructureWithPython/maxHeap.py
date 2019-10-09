import random


class MaxHeap:
    def __init__(self, collection=None):
        self.heap = []
        if collection is not None:
            for el in collection:
                self.push(el)

    def push(self, el):
        self.heap.append(el)
        self._shiftUp(len(self.heap) - 1)

    def _shiftUp(self, idx):
        parent_idx = idx // 2
        if parent_idx < 0:
            return
        elif self.heap[idx] > self.heap[parent_idx]:
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            return self._shiftUp(parent_idx)
        else:
            return

    def popNode(self):
        self.heap[0], self.heap[len(self.heap) - 1] = self.heap[len(self.heap) - 1], self.heap[0]
        el = self.heap.pop()
        self._shiftDown()
        return el

    def _shiftDown(self, idx=0):
        child_idx = idx * 2 + 1
        if child_idx >= len(self.heap):
            return
        if child_idx + 1 < len(self.heap) and self.heap[child_idx + 1] > self.heap[child_idx]:
            child_idx += 1
        if self.heap[child_idx] > self.heap[idx]:
            self.heap[idx], self.heap[child_idx] = self.heap[child_idx], self.heap[idx]
            return self._shiftDown(child_idx)

        return
    def printHeap(self):
        return self.heap

    def ranInsert(self, max_range=1000, node=20):
        for k in range(0, node):
            rand = random.randint(1, max_range)
            self.push(rand)

    def heap_sort(self):
        ret = []
        for i in range(len(self.heap)):
            ret.append(self.popNode())
        return ret


heap = MaxHeap([])
heap.ranInsert()
print(f'heap before  sort:->')
print(heap.printHeap())
print(f'heap after sort:->')
print(heap.heap_sort())