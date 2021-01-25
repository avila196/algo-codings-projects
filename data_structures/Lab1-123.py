class MyQueue:
    def __init__(self, data=None):
        # Initialize this queue, and store data if it exists
        #Here, we need to initialize the Queue with a root node with the given data (if exists)
        if data is not None:
             #If data exists, we initialize the root as a Node with data and no next, and 
             #we can use a size field and set it to 1
            self.root = Node(data)
            self.size = 1
        else:
            #If not, we set the root as None and we set the size as 0
            self.root = None
            self.size = 0
            
    def enqueue(self, data):
        # Add data to the end of the queue
        #Here, we need to loop until we get to the end of the queue and we add the current
        #data there, within a new Node. This loop starts at root and goes until there is 
        #no next.
        if self.root is None:
            #To start, if root is None, we just add it to the root
            self.root = Node(data)
        else:
            #If not, if root exists, we consider it to start our loop
            node = self.root
            while node.next is not None:
                node = node.next
            #When the loop ends, 'node' points to the last Node, so we add a new Node as its
            #next 
            newNode = Node(data)
            node.next = newNode
        #Finally, we increase the size of the Queue
        self.size += 1

    def dequeue(self):
        # Return the data in the element at the beginning of the queue, or None if the queue is empty
        #Here, we return the first element of the Queue and we set the new root as its next.
        #If root doesn't exist, we return None directly
        if self.root is None:
            return None
        else:
            #If not, we store its data and we set the new root as its next
            data = self.root.data
            self.root = self.root.next
            #Finally, we decrease the size and we return data
            self.size -= 1
            return data

    def __len__(self):
        # Return the number of elements in the queue
        #Here, we just return our variable size
        return self.size
        

class MyStack:
    def __init__(self, data=None):
        # Initialize this stack, and store data if it exists
        #Here, we need to initialize the Stack with a root node with the given data (if exists)
        if data is not None:
             #If data exists, we initialize the root as a Node with data and no next, and 
             #we can use a size field and set it to 1
            self.root = Node(data)
            self.size = 1
        else:
            #If not, we set the root as None and we set the size as 0
            self.root = None
            self.size = 0
    
    def push(self, data):
        # Add data to the beginning of the stack
        #Here, we add a new node to the beginning of the Stack. To do this, we create a new
        #node, we set it as the new root and the old root as its next
        newNode = Node(data,self.root)
        self.root = newNode
        #Finally, we increase the size of the Stack
        self.size += 1

    def pop(self):
        # Return the data in the element at the beginning of the stack, or None if the stack is empty
        #Here, we return the first element of the Stack and we set the new root as its next.
        #If root doesn't exist, we return None directly
        if self.root is None:
            return None
        else:
            #If not, we store its data and we set the new root as its next
            data = self.root.data
            self.root = self.root.next
            #Finally, we decrease the size and we return data
            self.size -= 1
            return data

    def __len__(self):
        # Return the number of elements in the stack
        #Here, we just return our variable size
        return self.size


class Node:
    def __init__(self, data, next=None):
        # Initialize this node, insert data, and set the next node if any
        #Here, we set the data and the next node as fields of the Node class
        self.data = data
        self.next = next