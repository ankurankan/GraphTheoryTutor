import bdb


class Node:
    def __init__(self, data):
        self.data = data
    next = None
    prev = None


class LinkedList:
    def __init__(self, li):
        self.head = Node(li[0])
        curr_node = self.head
        for elem_index in range(1, len(li)):
            temp_node = Node(li[elem_index])
            curr_node.next = temp_node
            curr_node = temp_node


class Visualize(bdb.Bdb):
    #Experimenting with bdb module
    pass


if __name__ == '__main__':
    code = """node = head\nwhile node != None:\n\tnode = node.next"""
    Visualize(code)