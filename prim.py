import random


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


def belong_edge(e, X):
	for i in X:
		if e == i:
			return true

def prim(g):
	start = random.choice(g.vertex_list)
	X = [start]
	A = []
	for key in g.edges:
		u = key.split()[0]
		v = key.split()[1]
		if belong_edge(u, X) and !belong_edge(v, X):
			elif belong_edge(v, X) and !belong_edge(u, X):
				# check if this is a light edge
				#if so add vertex to X, add edge to A

if __name__ == '__main__':
	f = open('mst_dataset/input_random_01_10.txt', 'r')

	line = f.readline().split()
	g = Graph(int(line[0]), int(line[1]))
	edges = f.read().splitlines()
	g.add_edges(edges)
	#g.get_graph()
	prim(g)

