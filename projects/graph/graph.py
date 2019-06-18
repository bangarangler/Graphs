# """
# Simple graph implementation
# """
# from util import Stack, Queue  # These may come in handy

# class Graph:
    # """Represent a graph as a dictionary of vertices mapping labels to edges."""
    # def __init__(self):
        # self.vertices = {}
    # def add_vertex(self, vertex):
        # """
        # Add a vertex to the graph.
        # """
        # if vertex in self.vertices:
            # raise ValueError('Given vertex already exists.')
        # self.vertices[vertex] = set()
    # def add_edge(self, v1, v2):
        # """
        # Add a directed edge to the graph.
        # """
        # if v1 in self.vertices and v2 in self.vertices:
            # self.vertices[v1].add(v2)
        # else:
            # raise ValueError('Given vertices must exist!')
    # def traverse(self, start, Data, on, off):
        # ans = []
        # visited = set()
        # data = Data(start)
        # while data.size() > 0:
            # v = getattr(data, off)()
            # if v not in visited:
                # ans.append(str(v))
                # visited.add(v)
                # for sv in self.vertices[v]:
                    # if sv not in visited:
                        # getattr(data, on)(sv)
        # return ', '.join(ans)
    # def bft(self, starting_vertex):
        # """
        # Print each vertex in breadth-first order
        # beginning from starting_vertex.
        # """
        # print('BFT: ', self.traverse(starting_vertex, Queue, 'enqueue', 'dequeue'))
    # def dft(self, starting_vertex):
        # """
        # Print each vertex in depth-first order
        # beginning from starting_vertex.
        # """
        # print('DFT: ', self.traverse(starting_vertex, Stack, 'push', 'pop'))
    # def dft_recursive(self, starting_vertex):
        # """
        # Print each vertex in depth-first order
        # beginning from starting_vertex.
        # This should be done using recursion.
        # """
        # def traverse(v, visited = set(), ans = []):
            # if v not in visited:
                # ans.append(str(v))
                # visited.add(v)
                # for sv in self.vertices[v]:
                    # if sv not in visited:
                        # traverse(sv, visited, ans)
            # return ans
        # print('DFT: ', ', '.join(traverse(starting_vertex)), ' (recursive)')
    # def search(self, start, dest, Data, on, off):
        # data = Data([start])
        # visited = set()
        # while data.size() > 0:
            # path = getattr(data, off)()
            # v = path[-1]
            # if v == dest:
                # return path
            # if v not in visited:
                # visited.add(v)
                # for sv in self.vertices[v]:
                    # if sv not in visited:
                        # getattr(data, on)(path + [sv])
    # def bfs(self, starting_vertex, destination_vertex):
        # """
        # Return a list containing the shortest path from
        # starting_vertex to destination_vertex in
        # breadth-first order.
        # """
        # return self.search(starting_vertex, destination_vertex, Queue, 'enqueue', 'dequeue')
    # def dfs(self, starting_vertex, destination_vertex):
        # """
        # Return a list containing a path from
        # starting_vertex to destination_vertex in
        # depth-first order.
        # """
        # return self.search(starting_vertex, destination_vertex, Stack, 'push', 'pop')


# if __name__ == '__main__':
    # graph = Graph()  # Instantiate your graph
    # # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    # graph.add_vertex(1)
    # graph.add_vertex(2)
    # graph.add_vertex(3)
    # graph.add_vertex(4)
    # graph.add_vertex(5)
    # graph.add_vertex(6)
    # graph.add_vertex(7)
    # graph.add_edge(5, 3)
    # graph.add_edge(6, 3)
    # graph.add_edge(7, 1)
    # graph.add_edge(4, 7)
    # graph.add_edge(1, 2)
    # graph.add_edge(7, 6)
    # graph.add_edge(2, 4)
    # graph.add_edge(3, 5)
    # graph.add_edge(2, 3)
    # graph.add_edge(4, 6)

    # '''
    # Should print:
        # {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    # '''
    # print(graph.vertices)

    # '''
    # Valid BFT paths:
        # 1, 2, 3, 4, 5, 6, 7 *
        # 1, 2, 3, 4, 5, 7, 6
        # 1, 2, 3, 4, 6, 7, 5
        # 1, 2, 3, 4, 6, 5, 7
        # 1, 2, 3, 4, 7, 6, 5
        # 1, 2, 3, 4, 7, 5, 6
        # 1, 2, 4, 3, 5, 6, 7
        # 1, 2, 4, 3, 5, 7, 6
        # 1, 2, 4, 3, 6, 7, 5
        # 1, 2, 4, 3, 6, 5, 7
        # 1, 2, 4, 3, 7, 6, 5
        # 1, 2, 4, 3, 7, 5, 6
    # '''
    # graph.bft(1)

    # '''
    # Valid DFT paths:
        # 1, 2, 3, 5, 4, 6, 7
        # 1, 2, 3, 5, 4, 7, 6
        # 1, 2, 4, 7, 6, 3, 5 *
        # 1, 2, 4, 6, 3, 5, 7
    # '''
    # # graph.dft(1)

    # '''
    # Valid DFT recursive paths:
        # 1, 2, 3, 5, 4, 6, 7  *
        # 1, 2, 3, 5, 4, 7, 6
        # 1, 2, 4, 7, 6, 3, 5
        # 1, 2, 4, 6, 3, 5, 7
    # '''
    # graph.dft_recursive(1)
    # # graph.add_vertex(8)
    # # graph.add_edge(2, 8)
    # # graph.add_edge(7, 8)
    # # graph.dft_recursive(1)

    # '''
    # Valid BFS path:
        # [1, 2, 4, 6] *
    # '''
    # # print('BFS: ', graph.bfs(1, 6))

    # '''
    # Valid DFS paths:
        # [1, 2, 4, 6]
        # [1, 2, 4, 7, 6] *
    # '''
    # # print('DFS: ', graph.dfs(1, 6))

# """
# Simple graph implementation
# """

from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = dict()

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('These vertices do not exist')

    def add_edge_u(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError('These vertices do not exist')

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        visited = set()
        queue = Queue()
        queue.enqueue(starting_vertex)
        while queue.size() > 0:
            vertex = queue.dequeue()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
                for neighbor in self.vertices[vertex]:
                    queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = set()
        stack = Stack()
        stack.push(starting_vertex)
        while stack.size() > 0:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
                for neighbor in self.vertices[vertex]:
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=False):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if not visited:
            visited = set()

        visited.add(starting_vertex)
        print(starting_vertex)
        for vertex in self.vertices[starting_vertex]:
            self.dft_recursive(
                vertex, visited) if vertex not in visited else None

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        if starting_vertex == destination_vertex:
            return [starting_vertex]

        visited = set()
        queue = Queue()
        queue.enqueue([starting_vertex])
        while queue.size() > 0:
            path = queue.dequeue()
            vertex = path[-1]
            if vertex not in visited:
                for neighbor in self.vertices[vertex]:
                    path_new = path[:]
                    path_new.append(neighbor)
                    queue.enqueue(path_new)
                    if neighbor == destination_vertex:
                        return path_new
                visited.add(vertex)
        return []

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        if starting_vertex == destination_vertex:
            return [starting_vertex]

        visited = set()
        stack = Stack()
        stack.push([starting_vertex])
        while stack.size() > 0:
            path = stack.pop()
            vertex = path[-1]
            if vertex not in visited:
                for neighbor in self.vertices[vertex]:
                    path_new = path[:]
                    path_new.append(neighbor)
                    stack.push(path_new)
                    if neighbor == destination_vertex:
                        return path_new
                visited.add(vertex)
        return []


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
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

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
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
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
