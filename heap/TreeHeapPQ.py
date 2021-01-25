#new_node = binarNode((key,value))
#new_node = binaryNode(new_item)
#current get_element()[0]
#binary node stores 4 



from Binary_Node import BinaryNode

class TreeHeapPQ(object):
    def __init__(self):
        self._root = None
        self._len = 0


    def __len__(self):
        return self._len



    def is_empty(self):
        if self._root is None:
            return True
        return False



    def add(self, key, value):
        
        #Here, we add the key and value directly into the respective Node object
        self._len += 1
        if self._root is None:
            self._root = BinaryNode(key, (key,value))
        else:
            self._add(key, (key,value), self._root)


    def _add(self, key, item, node):
        #When adding a new value, if the priority is the same, it needs to be
        #stored given the value, in order to find the min value between them
        #First, if keys is directly less or keys are equal but value is less
        if key < node._key or (key == node._key and item[1] < node.get_element()[1]):
            if node._prev is None:
                node._prev = BinaryNode(key, item, node)
            else:
                self._add(key, item, node._prev)
        else:
            if node._next is None:
                node._next = BinaryNode(key, item, node)
            else:
                self._add(key, item, node._next)

    def _min(self):
        if self.is_empty():
            return None
        tempNode = self._root
        parent = None
        while tempNode._prev is not None: 
            parent = tempNode
            tempNode = tempNode._prev
        return parent, tempNode, tempNode.get_element()

    #Min function can just return element
    def min(self):
        element = self._min()
        return element[2]



    def remove_min(self):
        return_parent, return_node, return_value = self._min()
        if self._len == 1:
            self._root = None
        elif return_parent is None:
            self._root = self._root._next
        elif return_node._next is not None:
            return_parent._prev = return_node._next
        else:
            return_parent._prev = None
        self._len -= 1

        return return_value

