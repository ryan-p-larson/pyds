# Ryan Larson
#
#
# trie.py

class TrieNode:
    def __init__(self, data=None):
        self.data = data
        self.children = {}

    def __repr__(self):
        return self.data if self.data else str(self.children)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, data):
        curr = self.root

        # add each letter
        for ch in data.lower():
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        # so we can see word without going up tree
        curr.data = data

    def search_prefix(self, prefix):
        words = []
        root = self.root

        if not prefix:
            return

        # Get prefix nodes
        for ch in prefix:
            if ch in root.children:
                root = root.children[ch]
            else:
                return words

        # get words
        queue = [root]
        while queue:
            curr = queue.pop()
            if curr.data != None:
                words.append(curr.data)

            queue = [curr.children[key] for key in curr.children] + queue
        return words
