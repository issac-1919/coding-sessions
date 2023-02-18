class graph():
    def __init__(self, edges):
        self.edges = edges
        self.network_graph = {}
        for org, dest in self.edges:
            """ 
            ('karen', 'brock'),
            ('karen', 'elen') 
            karen -> brock -> elen
            """
            if org in self.network_graph:
                self.network_graph[org].append(dest)
            else:
                self.network_graph[org] = [dest]
        print(self.network_graph)
    
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