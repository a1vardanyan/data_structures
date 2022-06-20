class Node:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class binary_tree:
    
    def __init__(self):
        self.root = None
    
    def add_element_helper(self, node, value):
        if node == None:
            return Node(value)
        if value <= node.value:
            node.left = self.add_element_helper(node.left, value)
        else:
            node.right = self.add_element_helper(node.right, value)
        return node
        
    def add_element(self, x):
        self.root = self.add_element_helper(self.root, x)
    
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
            return node
    
    def deleting_element_helper(self, node, value):
        if value == node.value:
            if node.left == None:
                return node.right
            else:
                result = self.find_biggest_element_from_left(node.left)
                node.left = self.unlink_biggest_element_from_left(node.left)
                result.left = node.left
                result.right = node.right
                return result
        if value < node.value:
            node.left = self.deleting_element_helper(node.left, value)
        else:
            node.right = self.deleting_element_helper(node.right, value)
        return node
    
    def deleting_element(self, z):
        self.root = self.deleting_element_helper(self.root, z)   
