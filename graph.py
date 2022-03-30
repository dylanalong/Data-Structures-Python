from my_queue import Queue
from pickle import NONE

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.marked = False
        self.adj_list = []

def breadth_first_search(root):
    q = Queue()
    root.marked = True
    q.add(root)

    while q.is_empty() == False:
        r = q.remove()
        print(r.data)

        for node in r.adj_list:
            if node.marked == False:
                node.marked = True
                q.add(node)

if __name__ == '__main__':
    graph = []
    for i in range(6):
        graph.append(Node(i))
    graph[0].adj_list = [graph[1], graph[4], graph[5]]
    graph[1].adj_list = [graph[3], graph[4]]
    graph[2].adj_list = [graph[1]]
    graph[3].adj_list = [graph[2], graph[4]]

    breadth_first_search(graph[0])