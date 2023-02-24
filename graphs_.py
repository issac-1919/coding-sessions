class und_graph:
    def __init__(self):
        self.graph = {}
    
    def display_graph(self):
        return self.graph
    
    def add_pair(self, beg, end, w=1):
        if self.graph.get(beg):
            if self.graph[beg].count([w, end]) == 0:
                self.graph[beg].append([w, end])
        else:
            self.graph[beg] = [[w, end]]
    
    def remove_pair(self, beg, end):
        if self.graph.get(beg):
            for _ in self.graph.get(beg):
                if _[1] == end:
                    self.graph[beg].remove(_)

def tester():
    undiGraph = und_graph()
    undiGraph.add_pair('tenali', 'vijayawada')
    undiGraph.add_pair('tenali', 'guntur')
    undiGraph.add_pair('vijayawada', 'guntur')
    undiGraph.add_pair('vijayawada', 'tenali')
    return print(undiGraph.display_graph())