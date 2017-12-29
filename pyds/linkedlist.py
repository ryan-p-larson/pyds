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
    def __init__(self, head):
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
