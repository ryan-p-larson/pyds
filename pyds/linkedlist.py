# Ryan Larson
#
#
# linkedlist.py

class ListNode:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        ascii_data = "({})".format(self.data)
        ascii_tail = "->" if self.next != None else "-x"
        return ascii_data + ascii_tail

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        res = ""
        curr = self.head
        while curr:
            res += str(curr)
            curr = curr.next
        return res

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def reverse(self):
        pass


class DNode:
    def __init__(self, data, prev=None, next_node=None):
        self.data = data
        self.prev = prev
        self.next = next_node

    def __repr__(self):
        s0 = "<->" if self.prev else ":"
        s1 = "({})".format(self.data)
        s2 = "" if self.next else ":"
        return s0 + s1 + s2

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        res = ""
        curr = self.head
        while curr:
            res = res + str(curr)
            curr = curr.next
        return res

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        if self.is_empty():
            return count
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def add_front(self, data):
        # step 1: create node
        node = DNode(data)
        if not self.is_empty():
            node.next = self.head
            self.head.prev = node
        #
        else:
            self.tail = node
        self.head = node

    def add_rear(self, data):
        node = DNode(data)
        if not self.is_empty():
            node.prev = self.tail
            self.tail.next = node
        #
        else:
            self.head = node
        self.tail = node

    def remove_front(self):
        if not self.is_empty():
            temp = self.head
            # check one node
            if (temp.prev == temp.next):
                self.head = None
                self.tail = None
            else:
                self.head = temp.next
                self.head.prev = None

    def remove_rear(self):
        if not self.is_empty():
            temp = self.tail
            if (temp.prev == temp.next):
                self.head = None
                self.tail = None
            else:
                self.tail = temp.prev
                self.tail.next = None
