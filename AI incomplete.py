from collections import defaultdict
class Graph:
    def __init__(self,graph):
        self.graph = defaultdict(list)

    def addedge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def pri(self):
        print(self.graph)

    def bfs(self,start,goal):
        op = [start]
        cl = []
        while op:
            t = op.pop(0)
            if t == goal:
                cl.append(t)
                print(op,'\t',cl)
                print("goal found")
                break
            for i in self.graph[t]:
                #print(i)
                if i not in cl and i not in op and i!=t:
                    op.append(i)
            cl.append(t)
            print(op,'\t',cl)

    def dfs(self,start,goal):
        op = [start]
        cl = []
        while op:
            t = op.pop(0)
            temp = []
            if t == goal:
                cl.append(t)
                print(op,'\t', cl)
                print("goal found")
                break
            for i in self.graph[t]:
                if i not in op+cl+temp and i!=t:
                    temp.append(i)
            cl.append(t)
            op = temp+op
            print(op,'\t',cl)

    def bidir(self, start, goal):
        f_op, b_op, f_cl, b_cl = [], [], [], []
        f_op.append(start)
        b_op.append(goal)
        print(f_op, b_op, f_cl, b_cl, sep='\t')
        while f_op and b_op:
            p = f_op.pop(0)
            q = b_op.pop(0)
            if p==q: print('Goal found'); return
            if p not in f_cl: f_cl.append(p)
            if q not in b_cl: b_cl.append(q)

            for i in self.graph[p]:
                if i not in f_cl: f_op.append(i)
            for i in self.graph[q]:
                if i not in b_cl: b_op.append(i)
            print(f_op, b_op, f_cl, b_cl, sep='\t')

            for i in f_op:
                if i in b_op: print("Goal found"); return
        print('Goal not found')
        
if __name__ == "__main__":
    n = int(input("enter edges"))
    g = Graph(n)
    for i in range(n):
        u,v = input('Enter edge: ').split()
        g.addedge(u,v)
    g.pri()
    #g.bfs('a','e')
    #g.dfs('a','e')
    g.bidir('a','e')

DFID prog

from collections import defaultdict
class Graph:
    def __init__(self):
        self.g=defaultdict(list)
    def addEdge(self,u,v):
        self.g[u].append([v,0])
        self.g[v].append([u,0])
    def dfs(self, start, goal, i):
        opened,closed=[],[]
        opened.append([start,0])
        while opened:
            u,v=opened.pop()
            closed.append(u)
            if u==goal:print(u,' ',opened,' ', closed);return 1
            if v<i :
                for j in self.g[u]:
                    j[1]=v+1
                    if j[0] not in closed:opened.append(j)
            print(u,' ',opened,' ', closed)
        return 0
    def dfid(self, start, goal):
        i=x=0
        while x!=1:
            print('DFID with depth = ',i)
            x=self.dfs(start, goal, i)
            i+=1
        print('Goal found')
g=Graph()
n=int(input('No.of edges : '))
for _ in range(n):                              # Enter  Space seperated edge nodes
    u,v=input('Enter Edge nodes : ').split()
    g.addEdge(u,v)
start,goal=input('Enter start and goal nodes : ').split()
g.dfid(start,goal)

class Waterjug:
    def __init__(self, bjmax, sjmax, target):
        self.bjmax = bjmax
        self.sjmax = sjmax
        self.goal = target

    def bfs(self):
        print('BFS approach')
        op,cl = [], []
        op.append((0,0))
        print(op, cl, sep='\t')
        while op:
            p = op.pop(0)
            cl.append(p)

            if self.goal in p:
                #print(op, cl, sep='\t')
                print(p)
                print('Goal found');return

            if p[1]==0 and (p[0],self.sjmax) not in cl:
                op.append((p[0],self.sjmax))

            if p[0]==self.bjmax and (0,p[1]) not in cl:
                op.append((0,p[1]))
                
            if p[0]+p[1]<=self.bjmax and (p[0]+p[1],0) not in cl:
                op.append((p[0]+p[1],0))

            if p[0]+p[1]>self.bjmax:
                temp = self.bjmax-p[0]
                temp = (p[0]+temp,p[1]-temp)
                if temp not in op+cl: op.append(temp)

            if p[0]==0 and (self.bjmax,p[1]) not in cl:
                op.append((self.bjmax,p[1]))

            if p[1]==self.sjmax and (p[0],0) not in cl:
                op.append((p[0],0))

            if p[0]-p[1]>=0 and p[0]-p[1]<=self.sjmax:
                if (p[0]-p[1],p[1]) not in cl: op.append((p[0]-p[1],p[1]))

            #print(op, cl, sep='\t')
            print(p)
        print('Goal not possible')

    def dfs(self):
        op,cl = [],[]
        op.append((0,0))
        while op:
            p = op.pop(0)
            cl.append(p)
            temp = []
            if self.goal in p:
                print(p)
                print('Goal found'); return

            if p[1]==0 and (p[0],self.sjmax) not in cl:
                temp.append((p[0],self.sjmax))

            if p[0]==self.bjmax and (0,p[1]) not in cl:
                temp.append((0,p[1]))

            if p[0]+p[1]<=self.bjmax and (p[0]+p[1],0) not in cl:
                temp.append((p[0]+p[1],0))

            if p[0]+p[1]>self.bjmax:
                t = self.bjmax-p[0]
                t = (p[0]+ t,p[1]-t)
                if t not in op+cl+temp: temp.append(t)

            if p[0]==0 and (self.bjmax,p[1]) not in cl:
                temp.append((self.bjmax,p[1]))

            if p[1]==self.sjmax and (p[0],0) not in cl:
                temp.append((p[0],0))

            if p[0]-p[1]>=0 and p[0]-p[1]<=self.sjmax:
                if (p[0]-p[1],p[1]) not in cl: temp.append((p[0]-p[1],p[1]))

            op = temp+op
            print(p)
        print('Goal not possible')

bjmax,sjmax,target=map(int,input("Enter values").split())
w=Waterjug(bjmax,sjmax,target)
w.bfs()
w.dfs()

class Graph:
    def __init__(self):
        self.g = defaultdict(list)
        self.h = {}

    def addh(self, v, value):
        self.h[v]=value

    def addedge(self,u,v):
        self.g[u].append(v)
        self.g[v].append(u)

    def bfs(self,start,goal):
        op,cl = [], []
        op.append(start)
        while op:
            t = op.pop(0)
            cl.append(t)
            if t==goal: print(op,cl,sep='\t'); print("Goal found"); return
            for i in self.g[t]:
                if i not in cl:
                    op.append(i)
            op.sort(key = lambda x: self.h[x])
            print(op,cl,sep='\t')
        print('Goal not found')

    def hill(self,start,goal):
        op,cl = [],[]
        op.append(start)
        while op:
            t = op.pop(0)
            cl.append(t)
            li = []
            if t == goal: print(op,cl,sep='\t');print("Goal found"); return
            for i in self.g[t]:
                if i not in cl+op:
                    li.append(i)
            op = li+op
            op.sort(key = lambda x: self.h[x])
            print(op,cl,sep='\t')
        print('Goal not found')

    def beam(self, start, goal, w):
        not_found = True
        if goal not in self.h: print('not possible'); return
        w_op, op, cl = [], [], []
        if start==goal: print('Goal found'); not_found= False; return
        cl.append(start)
        print(op, w_op, cl)
        for i in self.g[start]:
            op.append(i)
        op.sort(key = lambda x: self.h[x])
        w_op = op[:w]
        print(op,w_op,cl,sep='\t')
        while not_found:
            op.clear()
            while w_op:
                p = w_op.pop(0)
                cl.append(p)
                if p == goal: print(op, w_op, cl, sep='\t');print('Goal found');return
                for v in self.g[p]:
                    if v not in cl:op.append(v)
            op.sort(key = lambda x: self.h[x])
            w_op = op[:w]
            print(op,w_op,cl,sep='\t')
            if all(i in cl for i in w_op): print('goal not found'); return

if __name__ == '__main__':
    g = Graph()
    n = int(input('no.of nodes???'))
    m = int(input('no.of edges???'))
    for i in range(m):
        u,v = input().split()
        g.addedge(u,v)
    for i in range(n):
        li = list(map(str,input().split()))
        g.addh(li[0],int(li[1]))

    #g.bfs('a','e')
    #g.hill('a','e')
    #g.beam('a','e',2)
