#链式哈希表
class HashTable:
    def __init__(self,size=101):
        self.size=size
        self.T=[LinkList() for i in range(self.size)]

    def h(self,k):
        return k % self.size

    def find(self,k):
        i=self.h(k)
        return T[i].find(k)

    def insert(self,k):
        i=self.h(k)
        if self.find(k):
            print('Duplicated Insert') #已经存在，无需重复插入
        else:
            self.T[i].append(k)

