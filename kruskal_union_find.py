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
		self.vertices = [*range(1, self.num_vertex, 1)]
		self.parent = {}
		for v in self.vertices:
			self.parent[v] = v

	def find(self, item):
		if self.parent[item] == item:
			return item
		else:
			return self.find(self.parent[item])

	def union(self, set1, set2):
		root1 = self.find(set1)
		root2 = self.find(set2)
		self.parent[root1] = root2

	def get_disjointed_set(self):
		print('Vertices: ', self.vertices)
		print('Parents: ', self.parent)


def kruskal(g):
	A = []
	U = DisjointedSet(g.num_vertex+1)
	#U.get_disjointed_set()
	sorted_g = {k: v for k, v in sorted(g.edges.items(), key=lambda item: item[1])}
	for key in sorted_g:
		nodes = key.split()
		if U.find(int(nodes[0])) != U.find(int(nodes[1])):
			A.append(key)
			U.union(int(nodes[0]), int(nodes[1]))
	return A


if __name__ == '__main__':
	f = open('mst_dataset/input_random_02_10.txt', 'r')

	line = f.readline().split()
	g = Graph(int(line[0]), int(line[1]))
	edges = f.read().splitlines()
	g.add_edges(edges)
	#g.get_graph()

	print(kruskal(g))
