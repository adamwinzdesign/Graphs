"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id in self.verticies:
            raise Exception(f'A vertex with vertex id: {vertex_id} already exists!')
        else:
            self.verticies[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.verticies and v2 in self.verticies:
            self.verticies[v1].add(v2)
        else:
            raise IndexError('At least one of the given verticies does not exist in this graph!')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.verticies[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        if starting_vertex not in self.verticies:
            raise Exception('Could not locate starting vertex!')
        visited = {}
        verticies_to_visit = Queue()
        current = starting_vertex

        while current != None:
            if current in visited:
                if verticies_to_visit.size() is 0:
                    current = None
                    break
                current = verticies_to_visit.dequeue()
                continue
            visited[current] = self.vertices[current]
            neighbors = self.get_neighbors(current)
            if len(neighbors) == 0:
                if verticies_to_visit.size() == 0:
                    current = None
                    break
                current = verticies_to_visit.dequeue()
            else:
                for vert in neighbors:
                    if vert in visited:
                        continue
                    verticies_to_visit.dequeue(vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = {}
        vertices_to_visit = Stack()
        if starting_vertex not in self.verticies:
            raise Exception(f'There is not a vertex with id: {starting_vertex} in the graph!')
        else:
            continue
        current = starting_vertex
        while current != None:
            if current in visited:
                if vertices_to_visit.size == 0:
                    current = Nonebreak
                current = vertices_to_visit.pop()
                continue
            visited[current] = self.vertices[current]
            neighbors = self.get_neighbors(current)
            if len(neighbors) == 0:
                if vertices_to_visit.size() == 0:
                    current = None
                    break
                current = vertices_to_visit.pop()
            else:
                for vert in neighbors:
                    if vert in visited:
                        continue
                    vertices_to_visit.push(vert)
                if vertices_to_visit.size() == 0:
                    current = None
                    break
                current = vertices_to_visit.pop()

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
       visited = {}
       def traverse(vertex, values=[]):
           if vertex not in visited:
               visited[vertex] = True
               values.append(vertex)
            for vert in self.vertices[vertex]:
                if v not in visited:
                    visited[vert] = True
                    values.append(vert)
                    traverse(vert)
            return values
        order_list = traverse(starting_vertex)
        for node in order_list:
            print(node)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        if starting_vertex not in self.verticies:
            raise Exception(f'There is no vertex with id: {starting_vertex} in the graph!')
        if destination_vertex not in self.vertices:
            raise Exception(f'There is no vertex with id: {destination_vertex} in the graph!')
        visited = {}
        distance = {}
        previous = {}
        vertices_to_visit = Queue()
        visited[starting_vertex] = True
        distance[starting_vertex] = 0
        vertices_to_visit.enqueue(starting_vertex)

        while vertices_to_visit.size() != 0:
            current = vertices_to_visit.dequeue()
            if len(self.vertices[current]) == 0:
                continue
            for vert in self.vertices[current]:
                if v not in visited:
                    visited[vert] = True
                    distance[vert] = distance[current] + 1
                    previous[vert] = current
                    vertices_to_visit.enqueue(vert)
                    if vert == destination_vertex:
                        break
        short_path = []
        current = destination_vertex
        short_path.append(current)
        while current in prev:
            short_path.insert(0, previous[current])
            current = previous[current]
        return short_path

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
