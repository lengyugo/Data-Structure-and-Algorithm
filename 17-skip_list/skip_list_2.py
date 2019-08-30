import random

class SkipListNode(object):
    def __init__(self,val,high=1):
        self.data = val
        self.deeps = [None] * high

class SkipList(object):

    def __init__(self):

        self.__MAX_LEVEL = 16
        self._high = 1
        self._head = SkipListNode(None,self.__MAX_LEVEL)

    def find(self,val):
        cur = self._head

        for i in range(self._high - 1,-1,-1):
            while cur.deeps[i] and cur.deeps[i].data < val:
                cur = cur.deeps[i]

        if cur.deeps[0] and cur.deeps[0].data == val:
            return cur.deeps[0]
        return None

    def insert(self,val):
        high = self.randomLvel()
        if self._high < high:
            self._high = high

        newNode = SkipListNode(val,high)

        cache = [self._head] * high
        cur = self._head

        for i in range(high-1,-1,-1):
            while cur.deeps[i] and cur.deeps[i].data < val:
                cur = cur.deeps[i]
            cache[i] = cur

        for i in range(high):
            newNode.deeps[i] = cache[i].deeps[i]
            cache[i].deeps[i] = newNode


    def delete(self,val):
        cache = [None] * self._high
        cur = self._head
        for i in range(self._high-1,-1,-1):
            while cur.deeps[i] and cur.deeps[i].data < val:
                cur = cur.deeps[i]
            cache[i] = cur

        if cur.deeps[0] and cur.deeps[0].data == val:
            for i in range(self._high):
                if cache[i].deeps[i] and cache[i].deeps[i].data == val:
                    cache[i].deeps[i] = cache[i].deeps[i].deeps[i]

    def randomLvel(self,p=0.25):
        high = 1
        for _ in range(self.__MAX_LEVEL-1):
            if random.random() < p:
                high += 1
        return high

    def __repr__(self):
        vals = []
        p = self._head
        while p.deeps[0]:
            vals.append(str(p.deeps[0].data))
            p = p.deeps[0]
        return '->'.join(vals)

if __name__ == "__main__":
    s1 = SkipList()
    for i in range(50):
        s1.insert(i)
    print(s1)
    p = s1.find(7)
    print(p.data)
    s1.delete(3)
    print(s1)
    s1.insert(20)
    print(s1)














