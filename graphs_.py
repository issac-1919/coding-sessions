class und_graph:
    def __init__(self):
        self.graph = {}
    
    def display_graph(self):
        return self.graph
    
    def display_edge(self, beg):
        return_string = f"{beg}:{self.graph.get(beg)}"
        return return_string
    
    def display_degree(self, beg):
        return f"{beg}: {len(self.graph[beg])}\n"
    
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
    
    def dfs(self, src=-2, dst=-1):
        """DFS
        If no destination means default is -1"""
        if src == dst:
            return []
        stack = []
        visited = []
        if src == -2:
            src = list(self.graph)[0]
        stack.append(src)
        visited.append(src)
        ss = src
        while True:
            # check if there are non isolated nodes
            if len(self.graph[src]) != 0:
                ss = src
                for node in self.graph[src]:
                    if visited.count(node[src]) < 1:
                        if node[1] == dst:
                            visited.append(dst)
                        else:
                            stack.append(node[1])
                            visited.append(node[1])
                            ss = node[1]
                            break
            # checking if all children are visited
            if src == ss:
                stack.pop()
                if len(stack) != 0:
                    src = stack[len(stack) - 1]
            else:
                src = ss
            
            # check if we have reached the starting point
            if len(stack) == 0:
                return visited
            
def tester():
    undiGraph = und_graph()
    undiGraph.add_pair(0, 1)
    undiGraph.add_pair(1, 2)   
    undiGraph.add_pair(2, 3)   
    undiGraph.add_pair(3, 5)   
    undiGraph.add_pair(1, 3)   
    undiGraph.add_pair(3, 4)   

    print(undiGraph.dfs())
    print(undiGraph.display_graph())

def junk():
    undiGraph = und_graph()
    undiGraph.add_pair('tenali', 'vijayawada')
    undiGraph.add_pair('tenali', 'guntur')
    undiGraph.add_pair('vijayawada', 'guntur')
    undiGraph.add_pair('vijayawada', 'tenali')
    undiGraph.add_pair('vijayawada', 'eluru')
    undiGraph.add_pair('eluru', 'repalle')
    undiGraph.add_pair('vijayawada', 'vijayawada')