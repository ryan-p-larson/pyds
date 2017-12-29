# Ryan Larson
#
#
# binheap.py

class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.size = 0

    def __repr__(self):
        return str(self.heapList)

    def size(self):
        return self.size

    def is_empty(self):
        return self.heapList == [0]

    def perc_up(self, i):
        """Restore the heap property of our data structure.

        Args:
            i (int): Index of item to percolate up.
        """
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                self.heapList[i], self.heapList[i//2] = self.heapList[i//2], self.heapList[i]
            i = i // 2

    def insert(self, k):
        """Adds a new item to the end of our heap, maintaining tree property.

        Args:
            k (int): Element to add to heap
        """
        self.heapList.append(k)
        self.size += 1
        self.perc_up(self.size)


    def min_child(self, i):
        """For an element i; left_child[i] is at 2i, right_child is at 2i+1
        """
        # first check if we even have element
        if i*2+1 > self.size:
            return i*2
        # Otherwise return the smaller of the two children
        else:
            return i*2 if (self.heapList[i*2]<self.heapList[i*2+1]) else i*2+1

    def perc_down(self, i):
        """"""
        while (i * 2) <= self.size:
            # min child index
            mc = self.min_child(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    def delete_min(self):
        if self.is_empty():
            return

        # hold the smallest value in our heap
        res = self.heapList[1]

        # take the last node added and move it into the root index
        self.heapList[1] = self.heapList[self.size]
        # account for the change
        self.size -= 1

        # get rid of the duplicate last value
        self.heapList.pop()

        # restore heap property
        self.perc_down(1)

        return res

    def build_heap(self, items):
        i = len(items) // 2
        self.size = len(items)
        self.heapList = [0] + items[:]

        while i > 0:
            self.perc_down(i)
            i -= 1
