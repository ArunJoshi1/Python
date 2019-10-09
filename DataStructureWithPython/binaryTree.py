import random


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(node.right, data)
        else:
            print(f'{data} is already in the list')

    def inOrder(self):
        if self.root is None:
            print(f'tree is empty')
        else:
            self._inOrder(self.root)

    def _inOrder(self, node):
        if node is not None:
            print(f'{node.data} ')
            self._inOrder(node.left)
            self._inOrder(node.right)

    def height(self):
        if self.root is not None:
            size = self._height(self.root)
            print(f'{size} is height of tree')
        else:
            print(f'height of tree is {0}')

    def _height(self, node, curheight = 0):
        if node is None:
            return curheight
        left_height = self._height(node.left, curheight + 1)
        right_height = self._height(node.right, curheight + 1)
        return max(left_height, right_height)

    def findNode(self, key):
        if self.root is not None:
            return self._findNode(self.root, key)
        else:
            return f'tree is empty'

    def _findNode(self, node, key):
        if node.data == key:
            return True
        elif node.data > key and node.left is not None:
            return self._findNode(node.left, key)
        elif node.data < key and node.right is not None:
            return self._findNode(node.right, key)
        else:
            return False

    def deleteLeaf(self):
        if self.root is None:
            print("Tree is empty")
            return None
        else:
            self._deleteLeaf(self.root)

    def _deleteLeaf(self, node):
        if node is None:
            return None
        if node.left is None and node.right is None:
            return None
        node.left = self._deleteLeaf(node.left)
        node.right = self._deleteLeaf(node.right)
        return node


def ranRun(tree, max_ran=20, max_size=10):
    for num in range(max_size):
        ran = random.randint(0, max_ran)
        tree.insert(ran)


bTree = BinaryTree()
# ranRun(bTree)
lst = []
for item in lst:
    bTree.insert(item)
bTree.inOrder()
bTree.height()
print(bTree.findNode(10))
bTree.deleteLeaf()
bTree.inOrder()
