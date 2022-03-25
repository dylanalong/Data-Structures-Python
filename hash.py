from pickle import NONE

__all__ = ['get_value', 'add']

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = NONE

class Hash:
    def __init__(self, initial_capacity):
        self.capacity = initial_capacity
        self.buckets = [NONE] * initial_capacity

    def hash_function(self, key):
        return self.capacity % key
     
    def get_value(self, key):
        index = self.hash_function(key)
        node = self.buckets[index]
        while node != NONE and node.key != key:
            node = node.next
        if node is NONE:
            return NONE
        else:
            return node.value

    def add(self, key, value):
        index = self.hash_function(key)
        new_node = Node(key, value)
        tail = self.buckets[index]
        if tail is NONE:
            self.buckets[index] = new_node
        else:
            while tail.next != NONE:
                tail = tail.next
            tail.next = new_node

if __name__ == '__main__':
    h = Hash(10)
    h.add(9, 'Madison')
    h.add(7, 'Dylan')
    h.add(9, 'Bonnie')
    test = h.hash_function(35)
    value = h.get_value(9)