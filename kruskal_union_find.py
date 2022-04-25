import random
import os
import gc
from time import perf_counter_ns
import matplotlib.pyplot as plt


class Graph:
	def __init__(self, n_ver, n_edges):
		self.num_vertex = n_ver
		self.num_edges = n_edges

		self.vertex_list = []
		for i in range(self.num_vertex):
			self.vertex_list.append(str(i))

	def add_edges(self, list_edges):
		# rapresent the graph as a dictionary
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


class DisjointedSet:
	def __init__(self, num_vertex):
		self.num_vertex = num_vertex
		# create a list to contain all the verteces in the union find
		self.vertices = [*range(1, self.num_vertex, 1)]
		self.parent = {}
		# at the initial state each node is the father of itself
		for v in self.vertices:
			self.parent[v] = [v]

	def find(self, item):
		# iteratevely check who is the father of the node until one is the father of itself
		for key in self.parent:
			if item in self.parent[key]:
				return key

	def union(self, set1, set2):
		# update the data structure 
		root1 = self.find(set1)
		root2 = self.find(set2)

		# if the nodes are already in the same set we do nothing
		if root1 == root2:
			return

		# if the second set is bigger we append to it the first one, then delete it to keep the data structure updated
		if len(self.parent[root1]) < len(self.parent[root2]):
			self.parent[root2].extend(self.parent[root1])
			del self.parent[root1]
		else:
			self.parent[root1].extend(self.parent[root2])
			del self.parent[root2]

	def get_disjointed_set(self):
		print('Vertices: ', self.vertices)
		print('Parents: ', self.parent)


def union_find_kruskal(g):
	# create the list that will contain the solution
	A = []
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
			U.union(int(nodes[0]), int(nodes[1]))

	#Measuring Tree Weight
	A_weight = 0
	for e in A:
		A_weight += g.edges[e]
	return A_weight


def measure_run_times(g, num_calls, num_instances):
	sum_times = 0.0
	print('calcolo i tempi del file')
	for i in range(num_instances):
		gc.disable()
		start_time = perf_counter_ns()
		for i in range(num_calls):
			union_find_kruskal(g)
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
			print('-----------------------file che stiamo guardando '+filename+'------------------------------')
			f = open(dir_name + '/' + filename)
			line = f.readline().split()
			g = Graph(int(line[0]), int(line[1]))
			edges = f.read().splitlines()
			g.add_edges(edges)
			f.close()
			graph_sizes.append(g.num_vertex)
			run_times.append(measure_run_times(g, num_calls, num_instances))

	with open('results/kruskal_union_find_results.txt', 'w+') as f:
		f.write("Sizes\tTimes")
		for i in range(len(graph_sizes)):
			f.write("%s\t%s\n" % (graph_sizes[i], run_times[i]))

	plt.plot(graph_sizes, run_times)
	plt.legend(['Measured times'])
	plt.xlabel('Number of vertices')
	plt.ylabel('Run times (ns)')
	plt.show()
