
class graph:
    """Requires edges to create a graph, creates a graph upon calling the constructor"""
    def __init__(self, edges):
        self.edges = edges
        self.network_graph = {}
        for org, dest in self.edges:
            if org in self.network_graph:
                self.network_graph[org].append(dest)
            else:
                self.network_graph[org] = [dest]
    
    def get_paths(self, start, end, path=[]):
        if start == end:
            return [path]
        for edge in self.network_graph:
            adj_nodes = self.network_graph[edge].values()
            if end in adj_nodes:
                path = path + [end]
            else:
                current_node = ''
        
    
    def display_graph(self):
        return "{}".format(self.network_graph)
    
    def total_distance(self):
        pass
    def shortest_path(self):
        pass
    def bfs(self):
        queue = []
        visited = []
    def dfs(self):
        stack = []
        visited = []
    def cycles(self):
        pass
    def topo_sorting(self):
        pass
    def mst(self):
        pass
    def connectivity(self):
        pass
    def maximum_flow(self):
        pass

def tester1():
    user_network = [
        ('samuel','elen'),
        ('elen','brock'),
        ('sandra', 'brock'),
        ('elen', 'sandra'),
        ('sandra', 'samuel'),
        ('brock', 'sandra')
    ]
    graph_ob = graph(user_network)
    graph_ob.display_graph()
    
    org = "samuel"
    dest = "brock"
    return(print(f"Path from {org} to {dest}:", graph_ob.get_paths(org, dest)))