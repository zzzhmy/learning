class Queue:
    def __init__(self,size=100):
        self.queue=[0 for _ in range(size)]
        self.rear=0
        self.fronts=0
        self.size=size

    def push(self,element):
        if not self.is_full():
            self.rear =(self.rear+1)%self.size
            self.queue[self.rear]=element
        else:
            raise IndexError('Queue is full.')

    def pop(self):
        if not self.is_empty():
            self.fronts=(self.fronts+1)% self.size
            return self.queue[self.fronts]
        else:
            raise IndexError('Queue is empty.')

    def is_empty(self):
        if self.rear==self.fronts:
            return True

    def is_full(self):
        return (self.rear+1) % self.size==self.fronts

q=  Queue(8)
for i in range(7):
    q.push(i)
print(q.pop())


from collections import deque
q=deque([1,2,3],5) #创建 一个空的双向队列////队长为5，队满了则自动出队
q.append(1) #队尾进队
q.popleft() #队首出队.。队首是删除的一端，也就是早进来的一端

#用于双向队列
q.appendleft(2) #队首进队
q.pop() #队尾出队

def tail(n): #打印了test.txt文件中的后5行
    with open('test.txt','r') as f:
        q1=deque(f,n)
        return q1
for line in tail(5):
    print(line,end='')
