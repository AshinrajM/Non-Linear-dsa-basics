# BST(Binary Search Tree) is type of tree with maximum of two nodes as child also the node in the left side
# of root will be smaller than root and node in right will be greater than root


class BST:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, data):
        if self.key is None:
            self.key = BST(data)
            return

        if data < self.key:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BST(data)
            return "added on left"

        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BST(data)
            return "added on right"

    def PreOrderTraversal(self):
        if self.key is None:
            return " preorder traversal completed"
        print(self.key)
        if self.left:
            self.left.PreOrderTraversal()
        if self.right:
            self.right.PreOrderTraversal()
        return " Pre completed"

    def InOrderTraversal(self):
        if self.key is None:
            return " Inorder traversal completed"
        if self.left:
            self.left.InOrderTraversal()
        print(self.key)
        if self.right:
            self.right.InOrderTraversal()
        return "In completed"

    def PostOrderTraversal(self):
        if self.key is None:
            return "PostOrder Traversal completed"
        if self.left:
            self.left.PostOrderTraversal()
        if self.right:
            self.right.PostOrderTraversal()
        print(self.key)

        return "Post Completed"

    def LevelOrder(self):
        current = self
        queue = []
        result = []
        queue.append(current)

        while len(queue) > 0:
            current = queue.pop(0)
            result.append(current)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result

    def Search(self, element):
        if self.key == element:
            print("found")
            return
        if element < self.key:
            if self.left:
                self.left.Search(element)
            else:
                print("Not found")
        else:
            if self.right:
                self.right.Search(element)
            else:
                print("Not found")

    def DeleteNode(self, element):
        if self.key is None:
            print("No element is present")
            return
        elif self.key > element:
            if self.left:
                self.left = self.left.DeleteNode(element)
            else:
                print("not available")
        elif self.key < element:
            if self.right:
                self.right = self.right.DeleteNode(element)
            else:
                print("not found")
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp
            if self.right is None:
                temp = self.left
                self = None
                return None
            node = self.right
            while node.left:
                node = node.left
            self.key = node.key
            self.right = self.right.DeleteNode(node.key)
        return self

    def MinNode(self):
        if self.key is None:
            return None
        min = self.key
        while self.left:
            min = self.left.key
            self.left=self.left.left
        print("smallest",min)

    def MaxNode(self):
        if self.key is None:
            return None
        max=self.key
        while self.right:
            max=self.right.key
            self.right=self.right.right
        print("Maximum",max)


n = BST(65)
n.insert(78)
n.insert(46)
n.insert(344)
n.insert(34)
n.insert(56)
# n.PreOrderTraversal()
# print("========")
# n.InOrderTraversal()
# print("========")
# n.Search(34)
# n.DeleteNode(46)
# n.LevelOrder()
# n.Search(34)
# n.InOrderTraversal()
n.MinNode()
n.MaxNode()
