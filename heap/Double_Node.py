from Node import Node

class DNode(Node):
    '''
    ' Constructor. Creates a node with an element, a previous node, and a next
    '   node. No paramteres are required but all can be specified.
    '''
    def __init__(self, key, element = None, prev_node = None, next_node = None):
        super().__init__(element, next_node)
        self._prev = prev_node                            # previous node reference
        self._key = key
        # ADDITION key value
    #------------------------------- accessors -------------------------------
    '''
    ' Returns a reference to the previous node
    '''
    def get_previous(self):
        return self._prev

    #------------------------------- mutators -------------------------------
    '''
    ' Sets the previous node and returns the old "previous node" that this
    '   node used to point to
    '''
    def set_previous(self, new_previous):
        old_prev = self._prev
        self._prev = new_previous
        return old_prev
