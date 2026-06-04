class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cMap = {}
        self.cap = capacity

        self.lr, self.mr = Node(0, 0), Node(0, 0)  # least recent, most recent
        self.lr.next = self.mr
        self.mr.prev = self.lr

    def get(self, key: int) -> int:
        if key not in self.cMap:
            return -1

        self.cMap[key].prev.next = self.cMap[key].next
        self.cMap[key].next.prev = self.cMap[key].prev

        self.cMap[key].prev = self.mr.prev
        self.cMap[key].next = self.mr
        
        self.mr.prev.next = self.cMap[key]
        self.mr.prev = self.cMap[key]

        return self.cMap[key].val

    def put(self, key: int, value: int) -> None:
        if key not in self.cMap:
            if len(self.cMap) == self.cap:
                del self.cMap[self.lr.next.key]

                self.lr.next.next.prev = self.lr
                self.lr.next = self.lr.next.next
            
            newNode = Node(key, value)
            self.cMap[key] = newNode
        else:
            self.cMap[key].prev.next = self.cMap[key].next
            self.cMap[key].next.prev = self.cMap[key].prev
            self.cMap[key].val = value
        
        self.cMap[key].next = self.mr
        self.cMap[key].prev = self.mr.prev

        self.mr.prev.next = self.cMap[key]
        self.mr.prev = self.cMap[key]

        return
            