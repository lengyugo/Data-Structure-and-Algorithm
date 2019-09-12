"""
   散列表
"""

class HashEntry(object):
    def __init__(self,key,value):
        self.key=key
        self.value=value
class HashTable(object):
    _DELETED=HashEntry(None,None)  #用于删除
    def __init__(self,tablesize):
        self._table=tablesize*[None]
        self._n=0
    def __len__(self):
        return self._n
    def __getitem__(self,key):
        found,j=self._findSlot(key)
        if not found:
            raise KeyError
        return self._table[j].value
    def __setitem__(self,key,value):
        found,j=self._findSlot(key)
        if not found:
            self._table[j]=HashEntry(key,value)
            self._n+=1
            if self._n>len(self._table)//2:
                self._rehash()
        else:
            self._table[j].value=value
    def __delitem__(self,key):
        found,j=self._findSlot(key)
        if found:
            self._table[j]=HashTable._DELETED   # 懒惰删除
    def _rehash(self):
        oldList=self._table
        newsize=2*len(self._table)+1
        self._table=newsize*[None]
        self._n=0
        for entry in oldList:
            if entry is not None and entry is not HashTable._DELETED:
                self[entry.key]=entry.value
                self._n+=1
    def _findSlot(self,key):
        slot=self._hash1(key)
        step=self._hash2(key)
        firstSlot=None
        while True:
            if self._table[slot] is None:
                if firstSlot is None:
                    firstSlot=slot
                return (False,firstSlot)
            elif self._table[slot] is HashTable._DELETED:
                firstSlot=slot
            elif self._table[slot].key==key:
                return (True,slot)
            slot=(slot+step)%len(self._table)
    def _hash1(self,key):
        return abs(hash(key))%len(self._table)
    def _hash2(self,key):
        return 1+abs(hash(key))%(len(self._table)-2)