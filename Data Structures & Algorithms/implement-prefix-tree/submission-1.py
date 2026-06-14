class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.wordEnd = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            cur = cur.children.setdefault(c, Node())
        cur.wordEnd = True 

    def search(self, word: str) -> bool:
        cur = self.root 
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        return cur.wordEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        return True
        