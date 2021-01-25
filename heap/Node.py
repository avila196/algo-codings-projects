'''
' Class for nodes which will construct a singly linked list.
'''
class Node:
    '''
    ' Constructor. Creates a node with an element and a next
    '   node. No paramteres are required but all can be specified.
    '''
    def __init__(self, element = None, next_node = None, next_priority = None):
        self._element = element                           # user's element
        self._next = next_node                            # next node reference
        self._nextP = next_priority
        # ADDITION^ to keep track of the parent singly linked list of priority numbers
    #------------------------------- accessors -------------------------------
    '''
    ' Returns the data element contained within this node
    '''
    def get_element(self):
        return self._element

    '''
    ' Returns a reference to the next node
    '''
    def get_next(self):
        return self._next

    #------------------------------- mutators -------------------------------
    '''
    ' Sets the data element contained within this code and returns the
    '   data element that was previously stored there
    '''
    def set_element(self, new_element):
        if self._element == None:
            element = self._element
            self._element = new_element
            return element

    '''
    ' Sets the next node and returns the old "next node" that this
    '   node used to point to
    '''
    def set_next(self, new_next):
        old_next = self._next
        self._next = new_next
        return old_next
