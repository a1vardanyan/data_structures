class Node:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None
        self.height = 1
 
 
class AVL_tree:
 
    def __init__(self):
        self.root = None
 
    def inserthelper(self, node, x):
        if node == None:
            return Node(x)
        if x >= node.value:
            node.right = self.inserthelper(node.right, x)
        if x < node.value:
            node.left = self.inserthelper(node.left, x)
        return self.balance(node)
 
    def insert(self, x):
        self.root = self.inserthelper(self.root, x)
 
    def height(self, node):
        if node == None:
            return 0
        return node.height
 
    def bfactor(self, node):
        if node == None:
            return 0
        return self.height(node.right) - self.height(node.left)
 
    def recalc_height(self, node):
        if node == None:
            return
        node.height = max(self.height(node.left), self.height(node.right)) + 1
 
    def right_rotation(self, q):
        p = q.left
        q.left = p.right
        p.right = q
        self.recalc_height(q)
        self.recalc_height(p)
        return p
 
    def left_rotation(self, p):
        q = p.right
        p.right = q.left
        q.left = p
        self.recalc_height(p)
        self.recalc_height(q)
        return q
 
    def balance(self, node):
        self.recalc_height(node)
        if self.bfactor(node) == 2:
            if self.bfactor(node.right) == -1:
                node.right = self.right_rotation(node.right)
            return self.left_rotation(node)
        if self.bfactor(node) == -2:
            if self.bfactor(node.left) == 1:
                node.left = self.left_rotation(node.left)
            return self.right_rotation(node)
        return node
 
    def find_biggest_element_from_left(self, node):
        if node.right == None:
            return node
        else:
            return self.find_biggest_element_from_left(node.right)
 
    def unlink_biggest_element_from_left(self, node):
        if node.right == None:
            return node.left
        else:
            node.right = self.unlink_biggest_element_from_left(node.right)
            return self.balance(node)
 
    def del_helper(self, node, x):
        if node == None:
            return
        elif node.value > x:
            node.left = self.del_helper(node.left, x)
        elif node.value < x:
            node.right = self.del_helper(node.right, x)
        elif node.value == x:
            if node.left == None:
                return node.right
            else:
                result = self.find_biggest_element_from_left(node.left)
                node.left = self.unlink_biggest_element_from_left(node.left)
                result.left = node.left
                result.right = node.right
                return self.balance(result)
        return self.balance(node)
 
    def deleting(self, x):
        self.root = self.del_helper(self.root, x)
 
    def find_element_helper(self, node, value):
        if node == None:
            return None
        if value == node.value:
            return value
        if value < node.value:
            return self.find_element_helper(node.left, value)
        else:
            return self.find_element_helper(node.right, value)
 
    def find_element(self, y):
        return self.find_element_helper(self.root, y)
 
 
 
avl = AVL_tree()
for i in range(100):
    avl.insert(i)
 
print(avl.find_element(20))
avl.deleting(20)
print(avl.find_element(20))
 
for i in range(40):
    avl.deleting(i)
 
for i in range(100, 10000):
    avl.insert(i)
 
print(avl.find_element(45))
