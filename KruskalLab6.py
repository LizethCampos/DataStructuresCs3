class Kruskal:
    def ___init___(self,vertices2):#ver--->vertices 
        self.vertices = vertices2
        self.graph = []
    def Krustal_(self):
        list = [] 
        index_edges = 0
        index_list = 0
        self.graph = sorted(self.graph,key = lambda item : item[2])
        parent = []
        rank = []
        for i in range(self.vertices):
            parent.append(i)
            rank.append(0)
            
        while index_list < self.vertices - 1:
            From,To,Weight = self.graph[index_edges]
            index_edges = index_edges + 1
            x = self.find(parent,From)
            y = self.find(parent,To)
            if x != y:
                index_list = index_list + 1
                list.append([From,To,Weight])
                self.union(parent,rank,x,y)
                
                
    def addEdge(self,u,vertices,weight):
        self.graph.append([u,vertices,weight])
        
        
    def find(self,parent,i):
        if parent[i] == i:
            return i
        return self.find(parent,parent[i])
    
    
    def union(self,parent,ranked,x,y):
        xRoot = self.find(parent,x)
        yRoot = self.find(parent,y)
        if ranked[xRoot] < ranked[yRoot]:
            parent[xRoot] = yRoot
        elif ranked[xRoot] > ranked[yRoot]:
            parent[yRoot] = xRoot
        else:
            parent[yRoot] = xRoot
            ranked[xRoot] += 1
