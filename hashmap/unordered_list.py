# Initial version from section 4.21 of "Problem Solving with Algorithms and Data
# Structures using Python" by Brad Miller and David Ranum.

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def getKey(self):
        return self.key

    def getValue(self):
        return self.value
    
    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext
    
    def __str__(self):
        #String representation of the Node
        return "("+str(self.key)+","+str(self.value)+")"


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, key, value):
        #Add method receives both key and value
        temp = Node(key, value)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self, key):
        #Search method now looks for both key and value on a Node, and if found,
        #it returns the Node, None if not.
        current = self.head
        found = None
        while current != None and not found:
            if current.getKey() == key:
                found = current
            else:
                current = current.getNext()
        return found
    
    def getHead(self):
        #Returns the head node of list
        return self.head

    def remove(self, key):
        #First, we look for the node to remove
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getKey() == key:
                found = True
            else:
                previous = current
                current = current.getNext()
        #If the node is found, we remove it
        if found:
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())

    def __str__(self):
        # Returns a string representation of the List (just keys)
        str_rep = ""
        current = self.head
        while current != None:
            str_rep += str(current.getKey())+" "
            current = current.getNext()
        return str_rep
    
    def __repr__(self):
        return self.__str__()