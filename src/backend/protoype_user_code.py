import bdb

############################## Example with manually extracting frames #################################################
# >>> def traverse():
# 	frame_list.append(deepcopy(sys._getframe(0).f_locals))
# 	linked = LinkedList([1,2,3,4,5,6,7,8,9])
# 	frame_list.append(deepcopy(sys._getframe(0).f_locals))
# 	curr = linked.head
# 	frame_list.append(deepcopy(sys._getframe(0).f_locals))
# 	while curr:
# 		frame_list.append(deepcopy(sys._getframe(0).f_locals))
# 		curr = curr.next
# 		frame_list.append(deepcopy(sys._getframe(0).f_locals))
#
# >>> traverse()
# >>> frame_list
# [{},
# {'linked': <__main__.LinkedList object at 0x7f3fe9f60210>},
# {'linked': <__main__.LinkedList object at 0x7f3fe9f60590>, 'curr': <__main__.Node object at 0x7f3fe9f605d0>},
# {'linked': <__main__.LinkedList object at 0x7f3fe9f60810>, 'curr': <__main__.Node object at 0x7f3fe9f60850>},
# {'linked': <__main__.LinkedList object at 0x7f3fe9f60a90>, 'curr': <__main__.Node object at 0x7f3fe9f60b10>},
# {'linked': <__main__.LinkedList object at 0x7f3fe9f60d10>, 'curr': <__main__.Node object at 0x7f3fe9f60d90>},
# {'linked': <__main__.LinkedList object at 0x7f3fe9f60f90>, 'curr': <__main__.Node object at 0x7f3fe9f63090>},
# {'linked': <__main__.LinkedList object at 0x7f3fe9f63250>, 'curr': <__main__.Node object at 0x7f3fe9f63310>},
# {'linked': <__main__.LinkedList object at 0x7f3fe9f634d0>, 'curr': <__main__.Node object at 0x7f3fe9f635d0>},
# {'linked': <__main__.LinkedList object at 0x7f3fe9f63750>, 'curr': <__main__.Node object at 0x7f3fe9f63850>},
# {'linked': <__main__.LinkedList object at 0x7f3fe9f639d0>, 'curr': <__main__.Node object at 0x7f3fe9f63b10>},
# {'linked': <__main__.LinkedList object at 0x7f3fe9f63c50>, 'curr': <__main__.Node object at 0x7f3fe9f63d90>},
# {'linked': <__main__.LinkedList object at 0x7f3fe9f63ed0>, 'curr': <__main__.Node object at 0x7f3fe9f69090>},
# {'linked': <__main__.LinkedList object at 0x7f3fe9f69190>, 'curr': <__main__.Node object at 0x7f3fe9f69310>},
# {'linked': <__main__.LinkedList object at 0x7f3fe9f69410>, 'curr': <__main__.Node object at 0x7f3fe9f695d0>},
# {'linked': <__main__.LinkedList object at 0x7f3fe9f69690>, 'curr': <__main__.Node object at 0x7f3fe9f69850>},
# {'linked': <__main__.LinkedList object at 0x7f3fe9f69910>, 'curr': <__main__.Node object at 0x7f3fe9f69b10>},
# {'linked': <__main__.LinkedList object at 0x7f3fe9f69b90>, 'curr': <__main__.Node object at 0x7f3fe9f69d90>},
# {'linked': <__main__.LinkedList object at 0x7f3fe9f69e10>, 'curr': <__main__.Node object at 0x7f3fe9f5f090>},
# {'linked': <__main__.LinkedList object at 0x7f3fe9f5f0d0>, 'curr': <__main__.Node object at 0x7f3fe9f5f310>},
# {'linked': <__main__.LinkedList object at 0x7f3fe9f5f350>, 'curr': None}]
########################################################################################################################


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

    @staticmethod
    def create_visualization(frame_list):
        trace = {}
        step = 0
        prev_frame = {}
        for frame_var_dict in frame_list:
            if frame_var_dict != prev_frame:
                for var, obj in frame_var_dict.items():
                    if isinstance(obj, Node):
                        state = get_state(G)
                        state.pointers[var] = obj_id[obj]  # obj_id is a dictionary mapping
                                                           # obj to its cytoscape id. id should be unique.
                        trace[step] = state
                        step += 1

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
   
    @staticmethod
    def dict_node_id():
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
