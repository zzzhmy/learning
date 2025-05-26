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
#深度优先搜索-----穷举每条路径，可以走通就进栈，走不通则出栈，走过的节点标记为2.。。 但不能找出最优路径。
dirs=[
    lambda x,y:(x+1,y),
    lambda x,y:(x-1,y),
    lambda x,y:(x,y+1),
    lambda x,y:(x,y-1)
]
def maze_path(x1,y1,x2,y2):
    '''
    :param x1: 起点坐标
    :param y1: 起点坐标
    :param x2: 终点坐标
    :param y2: 终点坐标
    :return:
    '''
    stack=[]
    stack.append((x1,y1))
    while(len(stack)>0):
        curNode=stack[-1] #当前节点
        #判断是否到终点
        if curNode[0]==x2 and curNode[1]==y2:
            for p in stack:
                print(p)
            return True
        #四个方向 x-1\x+1\y-1\y+1
        for dir in dirs:
            nextNode=dir(curNode[0],curNode[1])
            #如果下一个节点能走
            if maze[nextNode[0]][nextNode[1]]==0:
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] == 2 #如果这条路走过了，则标记为2
                break
        else:
            maze[nextNode[0]][nextNode[1]] == 2
            stack.pop()
    else:
        print('No way')
        return False

maze_path(1,1,8,8)




