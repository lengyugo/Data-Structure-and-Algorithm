class DbListNode(object):
    def __init__(self,x,y):
        self.key = x
        self.val = y
        self.next = None
        self.prev = None

class LRUCache():
    def __init__(self,capacity: int):
        self.cap = capacity
        self.hkeys = {}
        self.top = DbListNode(None,-1)
        self.tail = DbListNode(None,-1)
        self.top.next = self.tail
        self.tail.prev = self.top

    def get(self,key: int) -> int:

        if key in self.hkeys.keys():
            cur = self.hkeys[key]

            cur.next.prev = cur.prev
            cur.prev.next = cur.next

            top_node = self.top.next
            self.top.next = cur
            cur.prev = self.top
            cur.next = top_node
            top_node.prev = cur

            return self.hkeys[key].val
        return -1

    def put(self,key:int,value:int) -> None:

        if key in self.hkeys.keys():
            cur = self.hkeys[key]
            cur.val = value

            cur.next.prev = cur.prev
            cur.prev.next = cur.next

            top_node = self.top.next
            self.top.next = cur
            cur.prev = self.top
            cur.next = top_node
            top_node.prev = cur
        else:
            cur = DbListNode(key,value)
            self.hkeys[key] = cur

            top_node = self.top.next
            self.top.next = cur
            cur.prev = self.top
            cur.next = top_node
            top_node.prev = cur

            if len(self.hkeys.keys()) > self.cap:
                self.hkeys.pop(self.tail.prev.key)
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev


    def __repr__(self):
        vals = []
        p = self.top.next
        while p.next:
            vals.append(str(p.val))
            p = p.next
        return '->'.join(vals)

if __name__ == '__main__':
    cache = LRUCache(3)
    cache.put(1,1)
    cache.put(2,2)
    print(cache)
    cache.get(1)
    cache.put(3,3)
    print(cache)
    cache.get(2)
    cache.put(4, 4)
    print(cache)
    cache.get(3)
    print(cache)
    cache.get(4)
    print(cache)