class Node:
    def __init__(self,item):
        self.item =item
        self.next =None

a=Node(1)
b=Node(3)
c=Node(2)
a.next=b
b.next=c
print(a.next.next.item)

def create_linklist_head(li):
    head=Node(li[0])
    for element in li[1:]:
        node=Node(element)
        node.next=head
        head=node
    return head

def create_linklist_tail(li):
    head=Node(li[0])
    tail=head
    for element in li[1:]:
        node=Node(element)
        tail.next=node
        tail=node
    return head

def print_linklist(lk):
    while lk:
        print(lk.item,end='')
        lk=lk.next

lk=create_linklist_tail([1,2,3,4])
print_linklist(lk)
