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

    def check_var_assignment(self, frame):
        variables = frame.f_code.co_varnames
        node_variables = []
        for var in variables:
            if isinstance(frame.f_locals[var], Node):
                node_variables.append(var)
        self.identify_nodes(node_variables)

    def identify_nodes(self, node_variables):
        node_id = self.dict_node_id()
        node_objects = []
        for var in node_variables:
            node_objects.append(node_id[var])
        return node_objects

    def dict_node_id(self):
        node_id = {}
        curr_node = linked_list.head
        node_id[id(curr_node)] = curr_node
        while curr_node:
            curr_node = curr_node.next
            node_id[id(curr_node)] = curr_node
        return node_id

if __name__ == '__main__':
    code = """node = head\nwhile node != None:\n\tnode = node.next"""
    Visualize(code)