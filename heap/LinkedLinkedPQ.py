from Node import Node

class LinkedLinkedPQ(object):
    def __init__(self):
        self._head = None
        # Let's also store length
        self._len = 0


    # Same as before, x.length() is for priority, x.__len__() aka len(x) is for total
    def length(self, key):
        myLen = 0
        headNode = self._head
        while headNode._element != key:
            headNode = headNode._nextP
        headNode = headNode._next
        while headNode is not None:
            myLen += 1
            headNode = headNode._next
        return myLen


    def __len__(self):
        return self._len


    def is_empty(self):
        return self._head is None


    def add(self, key, value):
        #If no head, we add it to the head        
        if self._head == None:
            self._head = Node((key,value))
        elif key < self._head._element[0]:
            #If the current priority is less, we set it as the new head and the old head
            #as the nextP attribute
            newHead = Node((key,value), None, self._head)
            self._head = newHead
        else:
            #First, we need to get to the correct head for its priority. This means we loop
            #as long as the key for the head is less than the current key
            curr_node = self._head
            parent = None
            while curr_node is not None:
                if key <= curr_node._element[0]:
                    break
                parent = curr_node
                curr_node = curr_node._nextP
            
            #Now, we have some cases:
            #1. If curr_node is None, we just add it after the parent
            if curr_node is None:
                newNode = Node((key,value))
                parent._nextP = newNode
            #2. The key is the same (same priority), so we add it given its value
            elif key == curr_node._element[0]:
                #We loop as long as we get to the correct place
                curr_node_priority = curr_node
                parent_priority = None
                while curr_node_priority is not None:
                    if value <= curr_node_priority._element[1]:
                        break
                    parent_priority = curr_node_priority
                    curr_node_priority = curr_node_priority._next
                    
                #Then, we add it prev to the current node for the same priority
                newNode = Node((key,value),curr_node_priority)
                if parent_priority is not None:
                    parent_priority._next = newNode
                else:
                    if parent is not None:
                        parent._nextP = newNode
                    else:
                        self._head = newNode
                    newNode._nextP = curr_node_priority._nextP
            #3. The key doesn't exist yet, so we just add it after the current node
            else:
                newNode = Node((key,value),None,curr_node)
                parent._nextP = newNode
        self._len += 1


    def min(self):
        #The min value is always placed at the head, so we just return its value
        if self.is_empty():
            return None
        # Can return the tuple right away
        return self._head._element



    def remove_min(self):
        return_value = self.min()
        #To remove the min, we set the head either to the next node with the same priority
        #and if not any of the same priority, to he head of the next priority
        if self._head._next is not None:
            self._head._next._nextP = self._head._nextP #Updates the reference to the next priority head
            self._head = self._head._next
        else:
            self._head = self._head._nextP
        self._len -= 1
        return return_value




