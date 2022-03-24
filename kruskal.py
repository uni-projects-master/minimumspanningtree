import random
from collections import deque


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


# Perform BFS on the graph starting from vertex `src` and
# return true if a cycle is found in the graph
def BFS(graph, src, n):
 
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
 
        # do for every edge (v, u)
        for u in graph.adjList[v]:
            if not discovered[u]:
                # mark it as discovered
                discovered[u] = True
 
                # construct the queue node containing info
                # about vertex and enqueue it
                q.append((u, v))
 
            # `u` is discovered, and `u` is not a parent
            elif u != parent:
                # we found a cross-edge, i.e., the cycle is found
                return True
 
    # no cross-edges were found in the graph
    return False


def kruskal(g):
	# create the list with the final solution
	A = UnweightedGraph([], g.num_vertex+1)
	# sort the graph by weight of the edges
	sorted_g = {k: v for k, v in sorted(g.edges.items(), key=lambda item: item[1])}
	print(sorted_g)
	for key in sorted_g:
		nodes = key.split()
		#if not BFS(A.add_edge(key))
		print('------------------NUOVA ITERAZIONE-------------------')
		print('Arco considerato: ', key)
		
		A.add_edge(key)
		A.get_unweighted_graph()
		if BFS(A, 0, g.num_vertex):
			print('ciclo')
		else:
			print('non ciclo')
		
	return A


if __name__ == '__main__':
	f = open('mst_dataset/test.txt', 'r')

	line = f.readline().split()
	g = Graph(int(line[0]), int(line[1]))
	edges = f.read().splitlines()
	g.add_edges(edges)
	#g.get_graph()
	kruskal(g)

