from sys import path
from collections import defaultdict
from collections import deque


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.weights = {}

    def addNode(self,value):
        if not value in self.nodes:
            self.nodes.add(value)    
    
    def addEdge(self, fromn, ton, weight):
        self.edges[fromn].append(ton)
        self.weights[(fromn, ton)] = weight
        

    def cost_path(self, path):
        cost = 0
        for i in range(0, len(path)-1, 1):
            listweights = [path[i], path[i+1]]
            cost += self.weights[tuple(listweights)]
        return cost

    def countPaths(self, s, d):
 
        v = [False] * len(self.nodes)
        pc = [0]
        self.countPaths_iterate(s, d, v, pc)
        return pc[0]
 

    def countPaths_iterate(self, s, d,
                       v, pc):
        v[int(s)] = True
 
        if (s == d):
            pc[0] += 1
 
        else:
 
            i = 0
            while i < len(self.edges[s]):
                if (not v[int(self.edges[s][i])]):
                    self.countPaths_iterate(self.edges[s][i], d,
                                        v, pc)
                i += 1
 
        v[int(s)] = False


    def get_paths(self,s, d, desc=True):
        v = [False] * len(self.nodes)
        path = []
        paths = {}
        self.show_paths_iterate(s, d, v, path, paths)

        paths = sorted(paths.items(), key=lambda item: item[1], reverse=desc)
        return paths


    
    def show_paths_iterate(self, s, d, v, path, paths):
 
        v[int(s)]= True
        path.append(s)

        if s == d:
            pth = []
            for p in path:
                pth.append(p)
            paths[tuple(pth)] = self.cost_path(pth)
        else:
            for i in self.edges[s]:
                if v[int(i)]== False:
                    self.show_paths_iterate(i, d, v, path,paths)
                     
        path.pop()
        v[int(s)]= False
        

    
    def vertex_with_maxpaths_from_source(self, source):

        nodes = sorted(self.nodes)
        max_paths =  -1 
        vertice_max_paths = 0

        for i in range(1, len(self.nodes)):
            np = self.countPaths('0', nodes[i])
            if np > max_paths:
                vertice_max_paths = nodes[i]
        
        return vertice_max_paths

    
    def add_reachable(self, v, v_n, weight):
        self.addNode(v_n)
        self.addEdge(v, v_n, 1)
        return v, v_n, weight


def read_data(graph, data):
    values = data.replace('},{', ';')
    data = values[1:-1].split(';')
    for d in data:
        nodes_weight = d.split(',')
        node1  = nodes_weight[0].strip()
        node2  = nodes_weight[1].strip()
        weight = nodes_weight[2].strip()
        graph.addNode(node1)
        graph.addNode(node2)
        graph.addEdge(node1, node2, int(weight))
    return graph


graph = Graph()
data = "{0, 1, 2},{0, 2, 4},{0, 4, -2},{0, 5, 1},{0, 6, 5},{2, 3, 3},{2, 4, 2},{3, 8, -4},{4, 3, 5},{4, 8, 1},{4, 7, 2},{5, 7, -1},{5, 8, -3},{6, 7, 6},{7, 8, 2}"

graph = read_data(graph, data)

print(graph.nodes)
print(graph.edges)
print(graph.weights)


more_reachable= graph.vertex_with_maxpaths_from_source('0')
print(more_reachable)

paths = graph.get_paths('0', more_reachable, True)

for path in paths:
    print("The path:", path[0], "cost:", path[1])


new_vertice = '9'
print(graph.add_reachable(more_reachable, new_vertice, 0))


print(graph.vertex_with_maxpaths_from_source('0'))



import unittest

class My_tests(unittest.TestCase):

    data = "{0, 1, 2},{0, 2, 4},{0, 4, -2},{0, 5, 1},{0, 6, 5},{2, 3, 3},{2, 4, 2},{3, 8, -4},{4, 3, 5},{4, 8, 1},{4, 7, 2},{5, 7, -1},{5, 8, -3},{6, 7, 6},{7, 8, 2}"
    

    def test_adding_input(self):
        graph = Graph()
        graph = read_data(graph, data)        
        self.assertEqual(False, len(graph.nodes) == 7);

    def test_adding_input2(self):
        graph = Graph()
        graph = read_data(graph, data)     
        self.assertEqual(True, len(graph.nodes) == 9);

    def test_check_adjacency(self):
        graph = Graph()
        graph = read_data(graph, data)     
        self.assertEqual(True, '6' in graph.edges['0']);

    def test_check_weight(self):
        graph = Graph()
        graph = read_data(graph, data)     
        self.assertFalse(graph.weights[('0', '6')] != 5);

    def test_check_weight2(self):
        graph = Graph()
        graph = read_data(graph, data)     
        self.assertTrue(graph.weights[('0', '6')] == 5);

    def test_check_weight2(self):
        graph = Graph()
        graph = read_data(graph, data)     
        self.assertTrue(graph.weights[('0', '6')] == 5);

    def test_check_max_cost_paths(self):
        graph = Graph()
        graph = read_data(graph, data)
        paths = graph.get_paths('0', '8', True)
        max_cost = max([path[1] for path in paths])             
        self.assertEqual(True, max_cost == paths[0][1]);        

if __name__ == '__main__':    
    unittest.main(argv=['first-arg-is-ignored'], exit=False)