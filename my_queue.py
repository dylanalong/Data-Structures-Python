class Queue:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = new_node
        self.size += 1

    def remove(self):
        dq_node = self.head
        self.head = self.head.next
        self.size -= 1
        return dq_node

    def peek(self):
        return self.head.data

    def is_empty(self):
        return self.size == 0