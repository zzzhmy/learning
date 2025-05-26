from collections import deque
maze=[[1,1,1,1,1,1,1,1,1,1],
      [1,0,0,1,0,0,0,1,0,1],
      [1,0,0,1,0,0,0,1,0,1],
      [1,0,0,0,0,1,1,0,0,1],
      [1,1,1,1,1,0,0,0,0,1],
      [1,0,0,0,1,0,0,0,0,1],
      [1,0,1,0,0,0,1,0,0,1],
      [1,0,1,1,1,0,1,1,0,1],
      [1,1,0,0,0,0,0,0,0,1],
      [1,1,1,1,1,1,1,1,1,1]]
#广度优先搜索-----流水式
dirs=[
    lambda x,y:(x+1,y),
    lambda x,y:(x-1,y),
    lambda x,y:(x,y+1),
    lambda x,y:(x,y-1)
]

def print_r(path):
    curNode =path[-1]
    realpath=[]
    while curNode[2] != -1:
        realpath.append(curNode[0],curNode[1])
        curNode=path[curNode[2]]

    realpath.append(curNode[0],curNode[1]) #起点
    realpath.reverse() #倒序,改为从头到终点
    for node in realpath:
        print(node)

def maze_path_queue(x1,y1,x2,y2):
    queue=deque()
    queue.append(x1,y1,-1)
    path=[]
    while len(queue)>0:
        curNode=queue.popleft()
        path.append(curNode)
        if curNode[0]==x2 and curNode[1]==y2:
            print_r(path)
            return True
        for dir in dirs:
            nextNode=dir(curNode[0],curNode[1])
            if maze[nextNode[0]][nextNode[1]]==0:
                queue.append((nextNode[0],nextNode[1],len(path)-1))
                maze[nextNode[0],nextNode[1]]=2 #标记已经走过
    else:
        print('no way')
        return False


