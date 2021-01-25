#NEEDS WORK TEST CODE PART 2.7 ERRORS
#Prints true form
#make into correct heap



from Double_Node import DNode

class LinkedHeapPQ(object):
    def __init__(self):
        self._head = None
        self._tail = None
        self._len = 0



    # Better to use None as the default priority
    def length(self, key = None):
        myLen = 0
        if key == None:
            myLen = self._len
        else:
            headNode = self._head
            # No need for parentheses around while condition
            while headNode._key != key:
                headNode = headNode._next
            while headNode is not None:
                myLen += 1
                headNode = headNode._next
                if headNode is None:
                    break
                if headNode._key != key:
                    break
        return myLen



    # Then the __len__ magic method has to have only 1 argument, so
    def __len__(self):
        # Call with no arguments
        return self.length(None)



    def is_empty(self):
        if self._head is None:
            return True
        return False



    def add(self, key, value):
        
        # Use tuple (key, value) instead of _Item object
        item = (key, value)
        newNode = DNode(key, item)
        self._len += 1
        
        if self._head == None:
            self._head = newNode
            self._tail = newNode
        elif key < self._head._key:
            newNode._next = self._head
            self._head._prev = newNode
            self._head = newNode
        elif key > self._tail._key:
            newNode._prev = self._tail
            self._tail._next = newNode
            self._tail = newNode
        else:
            curr_node = self._head
            while curr_node._next is not None:
                #Here, if the key is equal, we need to check for the element then
                if key > curr_node._next._key or (key == curr_node._next._key and value > curr_node._next._element[1]):
                    curr_node = curr_node._next
                else:
                    break
            next_node = curr_node._next
            
            curr_node._next = newNode
            newNode._prev = curr_node
            newNode._next = next_node
            next_node._prev = newNode



    def min(self):
        #The min value is always placed in the head, so we just return the element of head
        if self.is_empty():
            return None
        # Or even better, since we want to return the tuple itself, just return it directly
        return self._head._element



    def remove_min(self):
        element = self.min()
        self._head = self._head._next
        if self._head is None:
            self._tail = None
        else:
            self._head._prev = None
        self._len -= 1
        return element

