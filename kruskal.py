import random
import os
import gc
from time import perf_counter_ns
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, n_ver, n_edges):
        self.num_vertex = n_ver
        self.num_edges = n_edges
        #self.vertecies = []
        self.vertex_list = []
        self.edges = {}
        self.visited = [False] * (self.num_vertex)
        self.adjList = [[] for _ in range(self.num_vertex+1)]

        for i in range(1, self.num_vertex+1):
            self.vertex_list.append(str(i))


    def add_edges(self, list_edges, single_mode=False):
        if single_mode:
            self.edges[list_edges] = 0

        else:
        
            keys = []
            weights = []
            for i in list_edges:

                edge = i.split()
                if edge[0] != edge[1]:
                    keys.append(str(edge[0]) + ' ' + str(edge[1]))
                    weights.append(int(edge[2]))

            for k in range(len(keys)):
                self.edges[keys[k]] = weights[k]


    def create_adj_list(self, list_edges):
        nodes = list_edges.split()
        self.adjList[int(nodes[0])].append(int(nodes[1]))
        self.adjList[int(nodes[1])].append(int(nodes[0]))


    def get_graph(self):
        print(self.edges)


    def find_adj(self, v):
        adj_ls = []
        for i in self.edges:
            edge_key = i.split(' ')
            if int(edge_key[0]) == v:
                adj_ls.append(int(edge_key[1]))
            elif int(edge_key[1]) == v:
                adj_ls.append(int(edge_key[0]))
        return adj_ls


    def removekey(self, key):
        del self.edges[key]
        return


    def remove_adj(self, edge):
        nodes = edge.split()
        self.adjList[int(nodes[0])].remove(int(nodes[1]))
        self.adjList[int(nodes[1])].remove(int(nodes[0]))


def isCyclicUtil(gSupport, v, parent):
    gSupport.visited[v] = True
    adj_ls = gSupport.adjList[v]
    for i in adj_ls:
        if gSupport.visited[i] == False:
            if(isCyclicUtil(gSupport, i, v)):
                return True
        elif parent != i:
            return True

    return False


def naive_kruskal(g):
    # create the list with the final solution
    A = []
    
    # sort the graph by weight of the edges and iterate through it
    sorted_g = {k: v for k, v in sorted(g.edges.items(), key=lambda item: item[1])}
    support_graph = Graph(g.num_vertex, g.num_edges)

    for edge in sorted_g:
        support_graph.add_edges(edge, single_mode=True)
        support_graph.create_adj_list(edge)
        single_edge = edge.split()

        support_graph.visited = [False] * (support_graph.num_vertex+1)
        # check wheter the added edge createsa cycle
        if not isCyclicUtil(support_graph, int(single_edge[0]), -1):
            # we have not detected a cycle, hence the edge can be added to the solution
            A.append(edge)
        else:
            support_graph.remove_adj(edge)
            support_graph.removekey(edge)

    # Measuring Tree Weight
    A_weight = 0
    for e in A:
        A_weight += g.edges[e]

    return A_weight


def measure_run_times(g, num_calls, num_instances):
    sum_times = 0.0
    for i in range(num_instances):
        gc.disable()
        start_time = perf_counter_ns()
        for i in range(num_calls):
            print(kruskal(g))
        end_time = perf_counter_ns()
        gc.enable()
        sum_times += (end_time - start_time)/num_calls
    avg_time = int(round(sum_times/num_instances))
    # return average time in nanoseconds
    return avg_time


if __name__ == '__main__':

    dir_name = 'mst_dataset'
    num_calls = 1
    num_instances = 1
    graph_sizes = []
    run_times = []

    directory = os.fsencode(dir_name)
    for file in sorted(os.listdir(directory)):
        filename = os.fsdecode(file)

        if(filename.endswith('.txt')):
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
    plt.ylabel('Run times (ms)')
    plt.show()

