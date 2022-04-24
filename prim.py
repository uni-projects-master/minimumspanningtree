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
        self.vertices = []
        self.num_edges = n_edges
        self.num_vertex = n_ver
        self.edges = {}
        # CREATE OBJECT VERTEX AND ADD TO VERTICES
        for v in range(1, n_ver+1):
            new_vertex = vertex(name=v)
            self.vertices.append(new_vertex)

    def add_edges(self, list_edges):
        keys = []
        weights = []
        for i in list_edges:
            edge = i.split()
            if edge[0] != edge[1]:
                # SINCE GRAPH IS UNDIRECTED, ADD EDGE IN TWO WAYS
                keys.append(str(edge[0]) + ' ' + str(edge[1]))
                weights.append(int(edge[2]))
                keys.append(str(edge[1]) + ' ' + str(edge[0]))
                weights.append(int(edge[2]))


        for k in range(len(keys)):
            self.edges[keys[k]] = weights[k]

    def get_graph(self):
        print(self.edges)

    def find_vertex(self, v):
        for i in self.vertices:
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
    # CHOOSE A STARTING POINT AT RANDOM
    start = random.choice(G.vertices)
    start.Value = 0
    # INITIALIZE HEAP FOR PRIM WITH NODE VALUES = INFINITY
    Q = minHeap()
    for ver in G.vertices:
        Q.insert(ver)
    # WHILE EVERY VERTEX IS NOT INCLUDED IN THE TREE
    while not Q.isEmpty():
        # EXTRACT NODE WITH MINIMUM VALUE AND FIND ITS ADJACENTS
        u = Q.extractMin()
        u_adj = G.find_adj(u)
        for v in u_adj:
            current_edge = v.Name + ' ' + u.Name
            # IF EDGE (u,v) HAS A LOWER COST UPADTE THE VALUE OF v
            if Q.isInMinHeap(v) and G.edges[current_edge] < v.Value:
                v.Value = G.edges[current_edge]
                v.Parent = u
                Q.updateKey(v)
    # COMPUTING WEIGHT OF THE TREE
    A_weight = 0
    for ver in G.vertices:
        # IF VERTEX IS NOT THE ROOT
        if ver.Parent is not None:
            ver_parent = ver.Parent
            tree_edge = ver.Name + ' ' + ver_parent.Name
            A_weight += G.edges[tree_edge]

    return A_weight


if __name__ == '__main__':

    f = open('mst_dataset/input_random_13_80.txt', 'r')

    line = f.readline().split()
    edge_list = f.read().splitlines()
    g = Graph(int(line[0]), int(line[1]))
    g.add_edges(edge_list)
    A_w = prim(g)
    print(A_w)
