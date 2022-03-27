


'''
class adjNode:
    def __init__(self, value):
        self.node = value
        self.next = None

    #def get_next(self, i):
class adjList:
    def __init__(self, n_ver):
        self.num_vertex = n_ver
        self.graph = [None] * self.num_vertex

    # Add edge
    def add_edge(self, edge_ls):
        for i in edge_ls:
            edge = i.split()
            v = int(edge[0])
            w = int(edge[1])
            node = adjNode(w)
            node.next = self.graph[v]
            self.graph[v] = node

            node = adjNode(v)
            node.next = self.graph[w]
            self.graph[w] = node

    def print_alist(self):
        for i in range(1, self.num_vertex):
            #print("Vertex " + str(i) + ":", end="")
            ls = []
            temp = self.graph[i]
            while temp:
                #print(" -> {}".format(temp.node), end="")
                ls.append(temp.node)
                temp = temp.next
            #print(ls)
            print(" \n")


    def find(self, node):
        ls = []
        for i in range(self.num_vertex):
            temp = self.graph[i]
            while temp:
                print("temp:", temp.node)
                #print("node:", node[0])
                if temp.node == int(node[0]):
                    print("**")
                    ls.append(temp.next)
                temp = temp.next
        print(ls)
'''


class vertex:
    def __init__(self, n, v, p, adj):
        self.name = n
        self.value = v
        self.pos = p
        self.adj = adj


class Graph:
    def __init__(self, n_ver, n_edges):
        self.num_vertex = n_ver
        self.num_edges = n_edges
        self.edges = {}
        self.vertecies = []
        for i in range(1, self.num_vertex+1):
            self.vertecies.append(str(i))

    def add_edges(self, list_edges):
        keys = []
        weights = []
        for i in list_edges:
            edge = i.split()
            keys.append(str(edge[0]) + ' ' + str(edge[1]))
            weights.append(int(edge[2]))

        for k in range(len(keys)):
            self.edges[keys[k]] = weights[k]

    def get_graph(self):
        print(self.edges)

    def find_adj(self, vertex):
        ls = []
        for i in self.edges:
            edge_key = i.split()
            if edge_key[0] == vertex:
                ls.append(edge_key[1])
            elif edge_key[1] == vertex:
                ls.append(edge_key[0])
        return ls

class minHeap:
    def __init__(self, node_list):
        self.size = len(node_list)
        rows, cols = len(node_list), 2
        INF = 999999
        self.Heap = [[1 for i in range(cols)] for j in range(rows)]
        self.Pos = []
        for i in range(0, rows):
            #print("vertex name is:", node_list[i])
            self.Heap[i][0] = node_list[i]
            self.Heap[i][1] = INF
           # self.Pos[i][0] = node_list[i]
            self.Pos.append(i)

    def minHeapify(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < self.size and self.Heap[left][1] < self.Heap[smallest][1]:
            smallest = left

        if right < self.size and self.Heap[right][1] < self.Heap[smallest][1]:
            smallest = right

        # The nodes to be swapped in min heap if index is not smallest
        if smallest != index:
            # Swap positions
            #self.Position[self.Heap[smallest]] = index
            #self.Position[self.Heap[index]] = smallest
            # Swap nodes
            temp = self.Heap[smallest]
            self.Heap[smallest] = self.Heap[index]
            self.Heap[index] = temp


            #print("temp:", temp)
            #print("smallest:", )
            # Call function again
            self.minHeapify(smallest)

    def extractMin(self):

        if self.isEmpty():
            return

        #print("before swap:")


        root = self.Heap[0]
        lastNode = self.Heap[self.size - 1]
        #print("root:", self.Heap.index(root))
        #print("lastnode:", self.Heap.index(lastNode))
        self.Heap[0] = lastNode
        self.Heap[self.size - 1] = root
        #print("after swap:")
        #print("root:", self.Heap.index(root))
        #print("lastnode:", self.Heap.index(lastNode))
        # Update position of last node

        # Reduce heap size and heapify root
        self.size -= 1
        self.minHeapify(0)
        return root


    def isEmpty(self):
        return True if self.size == 0 else False

    def print_heap(self):
        print("heap:", self.Heap)
        print("pos:", self.Pos)
        #print(self.size)

    def isInMinHeap(self, vertex):
        #print("size:", self.size)
        #print("position:", self.Heap[vertex][0])
        if self.Heap.index(vertex) < self.size:
            return True
        return False


# implement minHeap (each node has a name and a value) with functions insert and extractMin
def prim(g):
    Q = minHeap(g.vertecies)
    Q.print_heap()

    while not Q.isEmpty():
        # find vertex in adjList
        # iterate through adjacents of u
        u = Q.extractMin()
        u_adj = g.find_adj(u[0])
        #print("u is:", u[0])
        #print("adj list:", u_adj)
        for v in u_adj:
            if not Q.isInMinHeap(v):
                print("yes it is")
                if edge(u,v) < Q.vertex.value:
                    update vertex value in heap





if __name__ == '__main__':
    f = open('mst_dataset/input_random_01_10.txt', 'r')

    line = f.readline().split()
    edge_list = f.read().splitlines()
    g = Graph(int(line[0]), int(line[1]))
    g.add_edges(edge_list)
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

