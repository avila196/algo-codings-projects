from Double_Node import DNode

class BinaryNode(DNode):

    def __init__(self,priority,element,parent=None,left=None,right=None):
        #We call the super constructor using the priority as well
        super().__init__(priority,element,left,right)
        self._parent=parent
        #Here, we add the priority as well as a variable of the object
        self._priority = priority
    
    def get_priority(self):
        return self._priority
    
    def get_element(self):
        return self._element

    def get_parent(self):
        return self._parent

    def get_left(self):
        return self._prev

    def get_right(self):
        return self._next

    def set_parent(self,new_parent):
        old_parent=self._parent
        self._parent=new_parent
        return old_parent

    def set_right(self,new_right):
        super().set_next(new_right)

    def set_left(self,new_left):
        super().set_previous(new_left)
