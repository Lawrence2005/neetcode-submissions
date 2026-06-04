class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.nextN = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cMap = {}

        self.lr, self.mr = Node(0, 0), Node(0, 0) # least recent, most recent
        self.lr.nextN = self.mr
        self.mr.prev = self.lr

    def get(self, key: int) -> int:
        if key not in self.cMap:
            return -1

        self.cMap[key].prev.nextN = self.cMap[key].nextN
        self.cMap[key].nextN.prev = self.cMap[key].prev

        self.cMap[key].prev = self.mr.prev
        self.cMap[key].nextN = self.mr

        self.mr.prev.nextN = self.cMap[key]
        self.mr.prev = self.cMap[key]

        return self.cMap[key].val

    def put(self, key: int, value: int) -> None:
        if key not in self.cMap:
            if len(self.cMap) == self.cap:
                del self.cMap[self.lr.nextN.key]

                self.lr.nextN.nextN.prev = self.lr
                self.lr.nextN = self.lr.nextN.nextN
            
            newNode = Node(key, value)
            self.cMap[key] = newNode
        else:
            self.cMap[key].prev.nextN = self.cMap[key].nextN
            self.cMap[key].nextN.prev = self.cMap[key].prev
            self.cMap[key].val = value
        
        self.cMap[key].nextN = self.mr
        self.cMap[key].prev = self.mr.prev

        self.mr.prev.nextN = self.cMap[key]
        self.mr.prev = self.cMap[key]

        return