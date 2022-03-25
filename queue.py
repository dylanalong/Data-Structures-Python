from pickle import NONE

class Node:
    def __init__(self, data):
        self.data = data
        self.next = NONE

class Queue:
    def __init__(self):
        self.head = NONE
        self.size = 0

    def add(self, data):
        new_node = Node(data)

        if self.head is NONE:
            self.head = new_node
        else:
            tail = self.head
            while tail.next != NONE:
                tail = tail.next
            tail.next = new_node
        self.size += 1

    def remove(self):
        dq_node = self.head
        dq_data = self.head.data
        self.head = self.head.next
        del dq_node
        self.size -= 1
        return dq_data

    def peek(self):
        return self.head.data

    def is_empty(self):
        return self.size == 0

if __name__ == '__main__':
    q = Queue()
    q.add('Madison')
    q.add('Dylan')
    head = q.peek()
    empty = q.is_empty()
    dq = q.remove()
    print(dq)