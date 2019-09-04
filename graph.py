from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = {}
    
    def __str__(self):
        return self.graph

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        queue = [s]
        self.visited[s] = 0
        while queue:
            s = queue.pop(0)
            for i in self.graph[s]:
                queue.append(i)
                self.visited[i] = self.visited[s] + 1
        print(self.visited)

    def BFS_paths(self, s):
        self.BFS(s)
        visited = {}
        paths = defaultdict(set)
        queue = [s]
        visited[s] = 0
        while queue:
            s = queue.pop(0)
            for i in self.graph[s]:
                queue.append(i)
                visited[i] = visited[s] + 1
                if(visited[i] == self.visited[i]):
                    paths[s].add(i)
        print(paths)

def main():
    g = Graph()
    g.add_edge('1', 'a')
    g.add_edge('2', 'a')
    g.add_edge('2', 'b')
    g.add_edge('2', 'c')
    g.add_edge('a', 'e')
    g.add_edge('b', 'a')
    g.add_edge('b', 'd')
    g.add_edge('b', 'c')
    g.add_edge('c', 'f')
    g.add_edge('d', 'f')
    g.add_edge('d', 'c')
    g.add_edge('e', 'd')
    g.add_edge('3', 'c')

    g.BFS_paths('2')

if __name__ == "__main__":
    main()
