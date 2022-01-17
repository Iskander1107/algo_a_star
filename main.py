import collections

class SimpleGraph:
    def __init__(self):
        self.edges = {}
    
    def neighbors(self, id):
        return self.edges[id]

class Queue:
    def __init__(self):
        self.elements = collections.deque()
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, x):
        self.elements.append(x)
    
    def get(self):
        return self.elements.popleft()

def breadth_first_search_1(graph, start):
    # печать того, что мы нашли
    frontier = Queue()
    frontier.put(start)
    visited = {}
    visited[start] = True
    
    while not frontier.empty():
        current = frontier.get()
        print("Visiting %r" % current)
        for next in graph.neighbors(current):
            if next not in visited:
                frontier.put(next)
                visited[next] = True
              
class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
    
    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height
    
    def passable(self, id):
        return id not in self.walls
    
    def neighbors(self, id):
        (x, y) = id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x + y) % 2 == 0: results.reverse() # ради эстетики
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results

def draw_grid(x):
    res = [['.'] * x.width for i in range(x.height)]
    for i in x.walls:
        res[i[1]][i[0]] = '#'
    
    for hg in range(x.height):
        for wd in range(x.width):
            print(res[hg][wd], end="")
        print('\n')
        

def main():
    example_graph = SimpleGraph()
    example_graph.edges = {
        'A': ['B'],
        'B': ['A', 'C', 'D'],
        'C': ['A'],
        'D': ['E', 'A'],
        'E': ['B']
    }
    breadth_first_search_1(example_graph, 'A')


    g = SquareGrid(30, 15)
    g.walls = [(0, 0), (5, 2)] # список long, [(21, 0), (21, 2), ...]
    draw_grid(g)



if __name__ == '__main__':
    main()