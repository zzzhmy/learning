from collections import deque
class BiTreeNode:
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None

a=BiTreeNode('A')
b=BiTreeNode('B')
c=BiTreeNode('C')
d=BiTreeNode('D')

a.rchild=b
a.lchild=c
c.lchild=d
root=a
print(root.lchild.data)

def pre_order(root): #前序遍历
    if root:
        print(root.data,end=',')
        pre_order(root.lchild)
        pre_order(root.rchild)

def in_order(root): #中序遍历
    if root:
        in_order(root.lchild)
        print(root.data,end=',')
        in_order(root.rchild)

def post_order(root): #后序遍历
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data,end=',')

def level_order(root): #层次遍历
    queue=deque()
    queue.append(root)
    while len(queue)>0:
        node=queue.popleft()
        print(node.data,end=',')
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)



print(pre_order(root))
print(in_order(root))
print(post_order(root))
print(level_order(root))
