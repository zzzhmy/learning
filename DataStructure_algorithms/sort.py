'''冒泡排序
1.列表每两个相邻的数，如果前面比后面大，则交换这两个数。  箭头在无序区从前到后走一遍
2.一趟排序完成后，无序区减少一个数，有序区增加一个数
代码关键：趟数、无序区范围
复杂度：O(n^2)'''
import random
def bubble_sort(li): #冒泡升序
    for i in range(len(li)-1): #第i趟
        exchange=False #改进后的冒泡排序
        for j in range(len(li)-i-1): #j为箭头位置
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
                exchange=True
        print(li)
        if not exchange: #如果在一趟中没有变化，则说明已经排好了，则退出
            return


'''选择排序
每次找最小的，找出来后放在无序区最前面(第一个位置) 
关键： 有序区、无序区、无序区最小数的位置'''

def select_sort_simple(li):
    li_new=[]
    for i in range(len(li)):
        min_val=min(li) #复杂度为O(n)
        li_new.append(min_val)
        li.remove(min_val) #复杂度为O(n)
    print(li_new)
    return li_new

def select_sort(li):
    for i in range(len(li)-1): #第几趟
        min_loc=i #最小数的位置,无序区的第一个位置
        for j in range(i+1,len(li)): #遍历哪些，无序区
            if li[j]<li[min_loc]:
                min_loc=j
        if min_loc !=i:
            li[i],li[min_loc]=li[min_loc],li[i]
        print(li)

'''插入排序
初始时，手里（有序区）只有一张牌，
每次从（无序区）摸一张牌，插入到手里已经有牌的正确位置
复杂度 O(n^2)'''
def insert_sort(li):
    for i in range(1,len(li)): #摸到牌的下标
        tmp=li[i]
        j=i-1 #j为手里的牌的下标，有序区的最后一个
        while j>=0 and li[j]>tmp: #找插入的位置
            li[j+1]=li[j]
            j-= 1 #j的箭头往左移
        li[j+1]=tmp
        print(li)

'''冒泡排序、选择排序、插入排序都为 原地排序，都为O(n^2)'''


'''NB快速排序'''





'''堆排序--二叉树'''
'''二叉树的存储方式：链式存储、顺序存储'''
def sift(li,low,high): #堆的向下调整，复杂度为lg(n)
    '''
    :param li: 列表
    :param low: 堆的根节点的位置
    :param high: 堆的最后一个元素的位置
    :return:
    '''
    i=low
    j=2*i+1
    tmp=li[i] #存起来堆顶
    while j<=high: #只要j位置有数，就一直循环判断
        if j+1<=high and li[j+1]<li[j]: #指向大的那个孩子
            j=j+1
        if li[j]<tmp: #改写为小根堆了
            li[i]=li[j]
            i=j
            j=2*1+1
        else: #tmp更大，把tmp放到i位置(某一级领导的位置）
            li[i]=tmp
            break
    else:
        li[i]=tmp #没有孩子后，把tmp放在叶子节点上

def heap_sort(li): #复杂度为O(n*lgn)
    n=len(li)
    for i in range((n-1-1)//2,-1,-1):#倒着遍历到0
        # i为建堆的时候调整的部分的根的下标
        sift(li,i,n-1)
    #建堆任务完成
    #挨个出数
    for i in range(n-1): #i指向当前堆的最后位置
        li[0],li[i]=li[i],li[0]
        sift(li,0,i-1) #i-1为最新的high

    print(li)


'''TOPK问题求解；现有n个数，设计算法得到前K个大的数'''
def topk(li,k): #用小根堆
    heap=li[0:k]
    for i in range((k-1-1)//2,-1,-1):
        sift(heap,i,k-1)#1.建堆完成
    for i in range(k,len(i)-1): #2.遍历堆中所有的元素
        if li[i]>heap[0]:
            heap[0]=li[i]
            sift(heap,0,k-1)
    for i in range(k-1,-1,-1): #3.出数
        heap[0],heap[i]=heap[i],heap[0]
        sift(heap,0,i-1)
    return heap


'''归并排序'''
def merge(li,low,mid,high): #归并
    '''
    :param li:
    :param low:
    :param mid:
    :param high:
    :return:
    '''
    i=low #第一段的箭头
    j=mid+1 #第二段的箭头
    ltmp=[]
    while i<=mid and j<=high: #只要两端都有数
        if li[i]<li[j]:
            ltmp.append(li[i])
            i+=1
        else:
            ltmp.append(li[j])
            j+=1
    while i<=mid:
        ltmp.append(li[i])
        i+=1
    while j<=high:
        ltmp.append(li[j])
        j+=1
    li[low:high+1]=ltmp

def merge_sort(li,low,high): #归并排序，把左边排好序、把右边排好序，两边合并
    if low<high: #至少两个元素，递归
        mid=(low+high)//2
        merge_sort(li,low,mid)
        merge_sort(li,mid+1,high)
        merge(li,low,mid,high)


'''希尔排序'''
def insert_sort_gap(li,gap): #分组插入排序
    for i in range(gap,len(li)): #摸到牌的下标
        tmp=li[i]
        j=i-gap #j为手里的牌的下标，有序区的最后一个
        while j>=0 and li[j]>tmp: #找插入的位置
            li[j+gap]=li[j]
            j-= gap #j的箭头往左移
        li[j+gap]=tmp
        print(li)
def shell_sort(li):
    d=len(li)//2
    while d>=1:
        insert_sort_gap(li,d)
        d //=2


def count_sort(li,max_count=100):
    count=[0 for _ in range(max_count+1)]
    for val in li:
        count[val] +=1
    li.clear()
    for ind,val in enumerate(count): #有val个ind; #ind为下标、val为值
        for i in range(val):
            li.append(ind)


def bucket_sort(li,n=100,max_num=10000):
    buckets=[[] for _ in range(n)] #创建桶
    for var in li:
        i= min(var // (max_num//n),n-1) #var放几号桶 0~99号桶
        buckets[i].append(var)
        #排号桶内的顺序
        for j in range(len(buckets[i])-1,0,-1):
            if buckets[i][j]<buckets[i][j-1]:
                buckets[i][j],buckets[i][j-1]=buckets[i][j-1],buckets[i][j]
            else:
                break
        sorted_li=[]
    for buc in buckets:
        sorted_li.extend(buc)
    return sorted_li















li= [2,509,1,899,5,7,300,208,4,3,6,8,100,1,8,3,5]
li1=bucket_sort(li)
print(li1)

