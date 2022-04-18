import random

# VERTEX STRUCTURE FOR PRIM'S ALGORITHM
class vertex:
    def __init__(self, name):
        INF = 999999
        # VERTEX NAME
        self.Name = str(name)
        # VERTEX COST
        self.Value = INF
        # VERTEX PARENT
        self.Parent = None


class Graph:
    def __init__(self, n_ver, n_edges):
        self.vertecies = []
        self.num_edges = n_edges
        self.num_vertex = n_ver
        self.edges = {}
        for v in range(1, n_ver+1):
            new_vertex = vertex(name=v)
            self.vertecies.append(new_vertex)

    def add_edges(self, list_edges):
        keys = []
        weights = []
        for i in list_edges:
            edge = i.split()
            if edge[0] != edge[1]:
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
        self.Heap.pop()
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
        self.Size -= 1
        self.insert(v)

    def isEmpty(self):
        return True if self.Size == 0 else False

    def isInMinHeap(self, v):
        if v in self.Heap:
            return True
        return False

    def print_Heap(self):
        print("HEAP: ")
        for i in self.Heap:
            print("Name: ", i.Name, ", Value: ", i.Value)


def prim(G):
    Q = minHeap()
    A = []
    A_weight = 0
    start = random.choice(G.vertecies)
    start.Value = 0
    for ver in G.vertecies:
        Q.insert(ver)

    while not Q.isEmpty():
        u = Q.extractMin()
        A.append(u)
        A_weight += u.Value
        #print(u.Value)
        u_adj = G.find_adj(u)
        for v in u_adj:
            current_edge = v.Name + ' ' + u.Name
            if Q.isInMinHeap(v) and G.edges[current_edge] < v.Value:
                v.Value = G.edges[current_edge]
                v.Parent = u
                Q.updateKey(v)

   # for i in A:
        #A_weight += i.Value

    return A_weight


if __name__ == '__main__':

    f = open('mst_dataset/input_random_13_80.txt', 'r')

    line = f.readline().split()
    edge_list = f.read().splitlines()
    g = Graph(int(line[0]), int(line[1]))
    g.add_edges(edge_list)
    A, A_w = prim(g)
    print(A_w)

