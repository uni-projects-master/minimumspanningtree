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


if __name__ == '__main__':
	f = open('mst_dataset/input_random_13_80.txt', 'r')

	line = f.readline().split()
	g = Graph(int(line[0]), int(line[1]))
	edges = f.read().splitlines()
	g.add_edges(edges)

	union_find_kruskal(g)
