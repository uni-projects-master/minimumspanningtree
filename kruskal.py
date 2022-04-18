from collections import deque
import os
import gc
from time import perf_counter_ns
import matplotlib.pyplot as plt


class UnweightedGraph:
    # Constructor
    def __init__(self, edges, n):
        # A list of lists to represent an adjacency list
        self.adjList = [[] for _ in range(n)]

        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

    def add_edge(self, edge):
        nodes = edge.split()
        self.adjList[int(nodes[0])].append(int(nodes[1]))
        self.adjList[int(nodes[1])].append(int(nodes[0]))

    def get_unweighted_graph(self):
        print(self.adjList)


class DisjointedSet:

    def __init__(self, num_vertex):
        self.num_vertex = num_vertex
        # create a list to contain all the verteces in the union find
        self.vertices = [*range(1, self.num_vertex, 1)]
        self.parent = {}
        # at the initial state each node is the father of itself
        for v in self.vertices:
            self.parent[v] = v

    def find(self, item):
        # recursevely search the parent of the parent
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])

    def union(self, set1, set2):
        # update the data structure
        root1 = self.find(set1)
        root2 = self.find(set2)
        self.parent[root1] = root2

    def get_disjointed_set(self):
        print('Vertices: ', self.vertices)
        print('Parents: ', self.parent)


class Graph:
    def __init__(self, n_ver, n_edges):
        self.num_vertex = n_ver
        self.num_edges = n_edges
        self.vertex_list = []
        self.edges = {}
        for k in range(self.num_vertex):
            self.vertex_list.append(str(k))

    def add_edges(self, list_edges):
        keys = []
        weights = []
        for e in list_edges:
            edge = e.split()
            keys.append(str(edge[0]) + ' ' + str(edge[1]))
            weights.append(int(edge[2]))

        for k in range(len(keys)):
            self.edges[keys[k]] = weights[k]

    def get_graph(self):
        print(self.edges)


def BFS_cycle_detection(graph, src, n):
    # to keep track of whether a vertex is discovered or not
    discovered = [False] * n
    # mark the source vertex as discovered
    discovered[src] = True
    # create a queue for doing BFS
    q = deque()
    # enqueue source vertex and its parent info
    q.append((src, -1))

    # loop till queue is empty
    while q:
        # dequeue front node and print it
        (v, parent) = q.popleft()
        for u in graph.adjList[v]:
            if not discovered[u]:
                # mark it as discovered
                discovered[u] = True
                q.append((u, v))

            # `u` is discovered, and `u` is not a parent
            elif u != parent:
                # we found a cross-edge, i.e., the cycle is found
                return True

    # no cross-edges were found in the graph
    return False


def naive_kruskal(g):
    # create the list with the final solution
    A = []
    A_weights = 0
    # create an unweighted copy of the graph, used for BFS cycle detection
    unweighted_g = UnweightedGraph([], g.num_vertex + 1)

    # sort the graph by weight of the edges and iterate through it
    sorted_g = {k: v for k, v in sorted(g.edges.items(), key=lambda item: item[1])}
    for key in sorted_g:
        # split the key in order to obtain the node from which we start the BFS cycle detection
        nodes = key.split()
        unweighted_g.add_edge(key)

        # check wheter the added edge createsa cycle
        if not BFS_cycle_detection(unweighted_g, int(nodes[0]), g.num_vertex + 1):
            # we have not detected a cycle, hence the edge can be added to the solution
            A.append(key)
            A_weights += sorted_g[key]

    return A_weights


def union_find_kruskal(g):
    # create the list that will contain the solution
    A = []
    A_weights = 0
    # create the disjointed set to handle the cycle detection
    U = DisjointedSet(g.num_vertex+1)
    # sort the graph by the weight of the nodes and iterate through it
    sorted_g = {k: v for k, v in sorted(g.edges.items(), key=lambda item: item[1])}
    for key in sorted_g:
        # separate the nodes in the key
        nodes = key.split()
        # check if the nodes are already in the same set
        if U.find(int(nodes[0])) != U.find(int(nodes[1])):
            # they are not in the same set, add the edge to the solution and union of the sets of v and w
            A.append(key)
            A_weights += sorted_g[key]
            U.union(int(nodes[0]), int(nodes[1]))
    return A_weights


def measure_run_times(g, num_calls, num_instances):
    sum_times = 0.0
    for k in range(num_instances):
        gc.disable()
        start_time = perf_counter_ns()
        for j in range(num_calls):
            naive_kruskal(g)
        end_time = perf_counter_ns()
        gc.enable()
        sum_times += (end_time - start_time) / num_calls
    avg_time = int(round(sum_times / num_instances))
    # return average time in nanoseconds
    return avg_time


if __name__ == '__main__':

    dir_name = 'mst_dataset'
    num_calls = 100000
    num_instances = 4
    graph_sizes = []
    run_times = []

    directory = os.fsencode(dir_name)
    for file in sorted(os.listdir(directory)):
        filename = os.fsdecode(file)

        if filename.endswith('.txt'):
            f = open(dir_name + '/' + filename)
            line = f.readline().split()
            g = Graph(int(line[0]), int(line[1]))
            edges = f.read().splitlines()
            g.add_edges(edges)
            f.close()
            graph_sizes.append(g.num_vertex)
            run_times.append(measure_run_times(g, num_calls, num_instances))

    with open('results/kruskal_naive_results.txt', 'w+') as f:
        f.write("Sizes\tTimes")
        for i in range(len(graph_sizes)):
            f.write("%s\t%s\n" % (graph_sizes[i], run_times[i]))

    plt.plot(graph_sizes, run_times)
    plt.legend(['Measured times'])
    plt.xlabel('Number of vertices')
    plt.ylabel('Run times (ns)')
    plt.show()
