class Node:
    def __init__(self, char) -> None:
        self.char = char
        self.is_word = False
        self.children = [None]*26

class Trie:
    def __init__(self) -> None:
        self.root = Node(None)

    def add_word(self, word):
        curr_node = self.root
        for char in word:
            if curr_node.children[ord(char) - ord('a')] is None:
                curr_node.children[ord(char) - ord('a')] = Node(char)
            curr_node = curr_node.children[ord(char) - ord('a')]

        curr_node.is_word = True

    def search(self, word):
        curr_node = self.root
        for char in word:
            if curr_node.children[ord(char) - ord('a')] is None:
                return False
            curr_node = curr_node.children[ord(char) - ord('a')]
        return True

if __name__ == '__main__':
    t = Trie()
    t.add_word("car")
    t.add_word("cat")
    t.add_word("boat")
    t.add_word("boot")
    t.add_word("boots")
    print("hello")