import random
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


class Graph:
	def __init__(self, n_ver, n_edges):
		self.num_vertex = n_ver
		self.num_edges = n_edges

		self.vertex_list = []
		for i in range(self.num_vertex):
			self.vertex_list.append(str(i))

	def add_edges(self, list_edges):
		self.edges = {}
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


def kruskal(g):
	# create the list with the final solution
	A = []
	# create an unweighted copy of the graph, used for BFS cycle detection
	unweighted_g = UnweightedGraph([], g.num_vertex+1)

	# sort the graph by weight of the edges and iterate through it
	sorted_g = {k: v for k, v in sorted(g.edges.items(), key=lambda item: item[1])}
	for key in sorted_g:
		# split the key in order to obtain the node from which we start the BFS cycle detection
		nodes = key.split()
		unweighted_g.add_edge(key)

		# check wheter the added edge createsa cycle
		if not BFS_cycle_detection(unweighted_g, int(nodes[0]), g.num_vertex+1):
			# we have not detected a cycle, hence the edge can be added to the solution
			A.append(key)

	return A


def measure_run_times(g, num_calls, num_instances):
	sum_times = 0.0
	print('calcolo i tempi del file')
	for i in range(num_instances):
		gc.disable()
		start_time = perf_counter_ns()
		for i in range(num_calls):
			kruskal(g)
		end_time = perf_counter_ns()
		gc.enable()
		sum_times += (end_time - start_time)/num_calls
	avg_time = int(round(sum_times/num_instances))
	# return average time in nanoseconds
	return avg_time


if __name__ == '__main__':

	dir_name = 'mst_dataset'
	num_calls = 100
	num_instances = 5
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
			print('-------------------FILE CHE STIAMO GUARDANDO' + filename + '-------------------------')
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

