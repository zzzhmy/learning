class BiTreeNode:
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None

a=BiTreeNode('A')
b=BiTreeNode('B')
c=BiTreeNode('C')
d=BiTreeNode('D')
e=BiTreeNode('2')
f=BiTreeNode('5')
g=BiTreeNode('7')

a.rchild=b
a.lchild=c
c.lchild=d
c.rchild=e
b.lchild=f
b.rchild=g
root=a

newroots=[]
def pre_order(root):
            #newroot.append(root.val)
    if root:
        newroot=root
        newroots.append(newroot.data)
        print(newroot.data)
        pre_order(root.rchild)
        pre_order(root.lchild)
    #return newroots

    # if root:
    #     newroots.append(root.data)
    #     lroot=root.rchild
    #     pre_order(lroot)
    #     rroot=root.lchild
    #     pre_order(rroot)
    que = []
    que.append(root)
    while len(que) > 0:
        node = que[0]
        que=que[1:]
        print(node.data)
        #newroots.append(node.data)
        if node.rchild:
            que.append(node.rchild)
        if node.lchild:
            que.append(node.lchild)
    #return newroots

pre_order(root)


