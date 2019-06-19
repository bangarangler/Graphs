# testData = [[1,3],[2, 3],[3, 6],[5, 6],[5, 7],[4, 5],[4, 8],[8, 9],[11, 8],[10, 1]]

# # answers = [[number, count], [number, count]]
# answers = []
# largest_count = 0

# def findAncestor(arr, number, count=-1):
    # # loop over arrays:
    # base_case = True
    # count += 1
    # for i in range(len(testData)):
        # # find number in place [1]
        # if testData[i][1] == number:
            # base_case = False
            # findAncestor(arr, testData[i][0], count)
    # if base_case == True:
        # global answers
        # global largest_count
        # if count > largest_count:
            # largest_count = count
        # if count > 0:
            # answers.append([number, count])

# def earliest_ancestor(arr, number):
    # global answers
    # global largest_count
    # answers = []
    # largest_count = 0
    # # call findAncestor (arr, number)
    # findAncestor(arr, number)
    # # loop over returned values
    # final_answer = -1
    # # print("potential answers: ", answers)
    # # print("final answer: ", final_answer)
    # for i in range(len(answers)):
        # # print(answers[i])
        # if answers[i][1] == largest_count:
            # if final_answer == -1 or final_answer > answers[i][0]:
                # # print("change final answer")
                # final_answer = answers[i][0]
    # # print("final answer: ", final_answer)
    # return final_answer

from collections import deque
import operator


class Stack():
    def __init__(self):
        self.stack = deque()

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


def earliest_ancestor(ancestors, starting_node):
    graph = dict()
    for tpl in ancestors:
        if tpl[1] not in graph:
            graph[tpl[1]] = set()
        graph[tpl[1]].add(tpl[0])

    def dfs(starting_vertex):
        nonlocal graph
        if starting_vertex not in graph:
            return -1
        distances = dict()

        visited = set()
        stack = Stack()
        stack.push([starting_vertex])
        while stack.size() > 0:
            path = stack.pop()
            vertex = path[-1]
            if vertex not in visited:
                if vertex in graph:
                    for neighbor in graph[vertex]:
                        path_new = path[:]
                        path_new.append(neighbor)
                        stack.push(path_new)
                        if neighbor not in graph:
                            distances[neighbor] = len(path_new)
                            continue
                    visited.add(vertex)
        return min([k for k, v in distances.items() if v ==
                    max([v for k, v in distances.items()])])
    return dfs(starting_node)

testData = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[8,9],[11,8],[10,1]]
print(earliest_ancestor(testData, 5))
