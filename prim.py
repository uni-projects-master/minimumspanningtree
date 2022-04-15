import random


class vertex:
    def __init__(self, name):
        INF = 99999
        self.Name = str(name)
        self.Value = INF
        self.Parent = None


class Graph:
    def __init__(self, n_ver, n_edges):
        self.vertecies = []
        self.num_edges = n_edges
        self.edges = {}
        for v in range(1, n_ver+1):
            new_vertex = vertex(name=v)
            self.vertecies.append(new_vertex)

    def add_edges(self, list_edges):
        keys = []
        weights = []
        for i in list_edges:
            edge = i.split()
            keys.append(str(edge[0]) + ' ' + str(edge[1]))
            weights.append(int(edge[2]))
            keys.append(str(edge[1]) + ' ' + str(edge[0]))
            weights.append(int(edge[2]))

        for k in range(len(keys)):
            self.edges[keys[k]] = weights[k]

    def get_graph(self):
        print(self.edges)

    def find_vertex(self, v):
        for i in self.vertecies:
            if i.Name == v:
                return i

    def find_adj(self, v):
        adj_ls = []
        for i in self.edges:
            edge_key = i.split(' ')
            if edge_key[0] == v.Name:
                new_adj = self.find_vertex(edge_key[1])
                adj_ls.append(new_adj)
        return adj_ls


class minHeap:

    # Constructor to initialize a heap
    def __init__(self):
        self.Heap = []
        self.Size = 0

    def extractHeapify(self, idx):
        smallest = idx
        left = 2*idx + 1
        right = 2*idx + 2
        if left < self.Size and self.Heap[left].Value < self.Heap[smallest].Value:
            smallest = left
        if right < self.Size and self.Heap[right].Value < self.Heap[smallest].Value:
            smallest = right
        if smallest != idx:
            self.Heap[idx], self.Heap[smallest] = self.Heap[smallest], self.Heap[idx]
            self.extractHeapify(smallest)

    def extractMin(self):
        if self.isEmpty():
            return
        root = self.Heap[0]
        self.Heap[0] = self.Heap[self.Size - 1]
        self.Size -= 1
        self.extractHeapify(0)
        return root

    def insertHeapify(self, idx):
        parent = int(((idx - 1) / 2))
        if self.Heap[idx].Value < self.Heap[parent].Value:
            self.Heap[idx], self.Heap[parent] = self.Heap[parent], self.Heap[idx]
            self.insertHeapify(parent)

    def insert(self, v):
        self.Size += 1
        self.Heap.append(v)
        self.insertHeapify(self.Size - 1)
        return

    def updateKey(self, v):
        self.Heap.remove(v)
        print(v.Name, "deleted from list")
        self.print_Heap()
        self.Size -= 1
        self.insert(v)

    def isEmpty(self):
        return True if self.Size == 0 else False

    def isInMinHeap(self, v):
        if v in self.Heap:
            return True
        return False

    def print_Heap(self):
        for i in self.Heap:
            print("Name: ", i.Name, ", Value: ", i.Value)


def prim(G):
    Q = minHeap()
    A = []
    start = random.choice(G.vertecies)
    start.Value = 0
    for ver in G.vertecies:
        Q.insert(ver)
    while not Q.isEmpty():
        u = Q.extractMin()
        A.append(u)
        u_adj = g.find_adj(u)
        for v in u_adj:
            current_edge = v.Name + ' ' + u.Name
            if Q.isInMinHeap(v) and g.edges[current_edge] < v.Value:
                v.Value = g.edges[current_edge]
                v.Parent = u
                Q.updateKey(v)
    print("SOLUTION: ", len(A))
    print(A[0].Name, A[0].Value)
    for i in range(1, len(A)):
        #parent = A[i].Parent
        print(A[i].Name, ",", A[i].Value)





if __name__ == '__main__':
    f = open('mst_dataset/input_random_03_10.txt', 'r')

    line = f.readline().split()
    edge_list = f.read().splitlines()
    g = Graph(int(line[0]), int(line[1]))
    g.add_edges(edge_list)
    #random start point
    prim(g)


    #adjacency_list = adjList(int(line[0]) + 1, edge_list)
    #print(line[0])
    #adj_list = adjList(int(line[0]))
    #adj_list.add_edge(edge_list)
    #print("edge list: ", edge_list)
    #adj_list.print_alist()
    #adjacency_list.print_alist()
    # g.get_graph()
    #adj_list.print_alist()

