import random


class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class LinkedList:
    def __init__(self):
        self.start = None

    def insertNode(self, data):
        newNode = Node(data)
        if self.start is None:
            self.start = newNode
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode

    def printList(self):
        if self.start is None:
            print(f'list is Empty !! Please insert node in it')
        else:
            temp = self.start
            while temp is not None:
                print(temp.data, end=' ')
                temp = temp.next
        print()

    def removeNode(self):
        if self.start is None:
            print(f'list is Empty !! Please insert node in it')
        else:
            temp = self.start
            temp = temp.next
            data = self.start.data
            self.start = temp
            del temp
            print(f'{data} is removed form list')

    def popList(self):
        if self.start is None:
            return 'list is empty'
        temp = self.start
        while temp.next is not None:
            pre = temp
            temp = temp.next
        data = temp.data
        del temp
        pre.next = None
        return f'{data} is popped form linked list'

    def reverse(self):
        cur = self.start
        pre = None
        while cur is not None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        self.start = pre

    def midOfList(self):
        if self.start is None:
            return 0
        first = self.start
        mid = self.start
        while first.next is not None:
            if first.next.next is None:
                first = first.next
            else:
                first = first.next.next
            mid = mid.next
        return mid.data

    def sizeOfList(self):
        if self.start is None:
            return 0
        size = 1
        temp = self.start
        while temp.next is not None:
            size += 1
            temp = temp.next
        return size


linkList = LinkedList()
for item in range(0, 10):
    ran = random.randint(0, 100)
    linkList.insertNode(ran)

linkList.printList()
print(linkList.popList())
print(f'{linkList.midOfList()} is Mid of list')
print(f'size of list is {linkList.sizeOfList()}')
linkList.printList()
linkList.reverse()
linkList.printList()
