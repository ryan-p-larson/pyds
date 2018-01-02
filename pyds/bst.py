# Ryan Larson
#
#
# bst.py

class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.height = 1
        self.parent = None

class BST(object):
    def __init__(self, root=None):
        self.root = root
        self.size = 1 if root else 0

    ## traversals!
    def traverse_pre_iter(self):
        order = []
        stack = []

        if self.root is None:
            return order
        else:
            stack.append(self.root)

        while stack:
            node = stack.pop()
            order.append(node.data)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return order

    def traverse_pre_rec_help(self, node, order_list):
        if node is None:
            return
        order_list.append(node.data)
        if node.left:
            self.traverse_pre_rec_help(node.left, order_list)
        if node.right:
            self.traverse_pre_rec_help(node.right, order_list)

    def traverse_pre_rec(self):
        order = []
        if self.root is None:
            return order
        else:
            self.traverse_pre_rec_help(self.root, order)
            return order

    def traverse_in_iter(self):
        order = []
        stack = []

        if self.root is None:
            return order
        else:
            node = self.root

        while True:
            while node is not None:
                stack.append(node)
                node = node.left
            if stack == []:
                break
            else:
                node = stack.pop()
                order.append(node.data)
                node = node.right
        return order

    def traverse_in_rec_help(self, node, order_list):
        if node is None:
            return
        if node.left:
            self.traverse_in_rec_help(node.left, order_list)
        order_list.append(node.data)
        if node.right:
            self.traverse_in_rec_help(node.right, order_list)

    def traverse_in_rec(self):
        order = []
        if self.root is None:
            return order
        else:
            self.traverse_in_rec_help(self.root, order)
            return order

    def traverse_post_iter(self):
        order = []
        stack = []
        # local helper for our stack
        peek = lambda l: l[-1] if len(l) > 0 else None

        if self.root is None:
            return order
        else:
            node = self.root

        while True:
            while node:
                # push right child then root onto stack
                if node.right:
                    stack.append(node.right)
                # add node and set it as nodes's left child
                stack.append(node)
                node = node.left

            node = stack.pop()
            # if popped has right child and is not processed,
            # make sure right child is processed before root
            if (node.right) and (peek(stack) == node.right):
                stack.pop() # remove right child from stack
                stack.append(node) # push node back on
                node = node.right
            else:
                order.append(node.data)
                node = None

            if len(stack) <= 0:
                break
        return order

    def traverse_post_rec_help(self, node, order_list):
        if node is None:
            return
        if node.left:
            self.traverse_post_rec_help(node.left, order_list)
        if node.right:
            self.traverse_post_rec_help(node.right, order_list)
        order_list.append(node.data)

    def traverse_post_rec(self):
        order = []
        if self.root is None:
            return order
        else:
            self.traverse_post_rec_help(self.root, order)
            return order


# Driver program to test above function
""" Constructed binary tree is
            1
          /   \
         2     3
       /  \
      4    5

(a) Inorder (Left, Root, Right) : 4 2 5 1 3
(b) Preorder (Root, Left, Right) : 1 2 4 5 3
(c) Postorder (Left, Right, Root) : 4 5 2 3 1
(d) Level Order Traversal : 1 2 3 4 5
"""

n = TreeNode(1)
n.left = TreeNode(2)
n.right = TreeNode(3)
n.left.left = TreeNode(4)
n.left.right = TreeNode(5)
bst = BST(n)
