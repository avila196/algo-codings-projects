class MyTree():
    def __init__(self, data):
        # Initialize this node, and store data in it
        self.data = data
        self.left = None
        self.right = None
        self.height = 0
    
    def getLeft(self):
        # Return the left child of this node, or None
        return self.left
    
    def getRight(self):
        # Return the right child of this node, or None
        return self.right
    
    def getData(self):
        # Return the data contained in this node
        return self.data

    def insert(self, data):
        # Insert data into the tree, descending from this node
        # Ensure the tree remains complete - every level is filled save for the last, and each node is as far left as possible
        # Return this node after data has been inserted
        #Here, the idea is to start a level order traversal until we find the farthest left possible
        #node to insert the new data. To do this level traversal, we can use a queue to add
        #all the nodes to visit for the levels, in order from left to right
        #We start creating the queue
        queue = []
        queue.append(self)
        #Now we loop through the elements of it to find the place to add the data
        while len(queue) > 0:
            #First, we dequeue the first value
            node = queue.pop(0)
            #Then, we check for the left child of the current node
            if node.left is None:
                #If None, we add the current data here and break the loop
                node.left = MyTree(data)
                break
            else:
                #If not None, we add its left child to the queue
                queue.append(node.left)
            #We do the same for the right child
            if node.right is None:
                #If None, we add the current data here and break the loop
                node.right = MyTree(data)
                break
            else:
                #If not None, we add its right child to the queue
                queue.append(node.right)
        #Finally, we return the current root
        return self
        

    def getHeight(self):
        # Return the height of this node
        #The height of the current node is given as the max height between both paths for 
        #left and right child.
        if self.left is None and self.right is None:
            return 0
        elif self.left is None:
            return self.right.getHeight()+1
        elif self.right is None:
            return self.left.getHeight()+1
        else:
            #If both childs exist, we return the max height between its children
            return max(self.left.getHeight()+1,self.right.getHeight()+1)

class MyBST(MyTree):
    def __init__(self, data):
        # Initialize this node, and store data in it
        super().__init__(data)
        pass

    def insert(self, data):
        # Insert data into the tree, descending from this node
        # Ensure that the tree remains a valid Binary Search Tree
        # Return this node after data has been inserted
        #To insert into a binary tree, we need to loop until we find the right place to place
        #the new data. To do this, we start at the root and we loop through the childs
        #comparing the data.
        node = self
        while True:
            #First, we compare the data against the node data
            if data < node.data:
                #If the data is less than the node data, we need to go to the left
                #Now, if the left child is None, we add it there. If not, we loop again
                #considering the left child as the node to compare
                if node.left is None:
                    node.left = MyTree(data)
                    break
                else:
                    node = node.left
            else:
                #If not, if greater or equal, we need to go to the right
                #Now, if the right child is None, we add it there. If not, we loop again
                #considering the right child as the node to compare
                if node.right is None:
                    node.right = MyTree(data)
                    break
                else:
                    node = node.right
        #Finally, we return the current root
        return self
            

    def __contains__(self, data):
        # Returns true if data is in this node or a node descending from it
        #To search for a value, we look inside the tree and we compare the data against the
        #starting root. Then, if less, we go to the left and we compare, if not, we go to
        #the right and compare. If we get to a Node that doesn't exist, it means the data
        #doesn't exist
        #We start looking at the root
        node = self
        while True:
            #We compare the data of the node with the data we're looking for
            #If the current node is None, we return False directly
            if node is None:
                return False
            #Now, if not None and both data are equal, then return True
            if data == node.data:
                return True
            else:
                #If not equal, we need to go to left or right to look inside the next node
                #on the next loop
                if data < node.data:
                    node = node.left
                else:
                    node = node.right

class MyAVL(MyBST):
    def __init__(self, data):
        # Initialize this node, and store data in it
        super().__init__(data)

    def getBalanceFactor(self):
        # Return the balance factor of this node
        #To find the balance factor, we consider its left and right child
        #To do this, we check for the heights of childs to get the respective balance
        if self.left is None and self.right is None:
            return 0
        elif self.left is None:
            return -(self.right.getHeight()+1)
        elif self.right is None:
            return self.left.getHeight()+1
        else:
            #If both childs exist, we return the difference of left height and right height
            return self.left.getHeight()-self.right.getHeight()

    def insert(self, data):
        # Insert data into the tree, descending from this node
        # Ensure that the tree remains a valid AVL tree
        # Return the node in this node's position after data has been inserted
        #First of all, we do a normal insert as a BST.
        #First, we compare the data against the node data
        if data < self.data:
            #If the data is less than the node data, we need to go to the left
            #Now, if the left child is None, we add it there. If not, we loop again
            #considering the left child as the node to compare
            if self.left is None:
                self.left = MyAVL(data)
            else:
                self.left = self.left.insert(data)
        else:
            #If not, if greater or equal, we need to go to the right
            #Now, if the right child is None, we add it there. If not, we loop again
            #considering the right child as the node to compare
            if self.right is None:
                self.right = MyAVL(data)
            else:
                self.right = self.right.insert(data)
        
        #Then, we update the height of the previous root using its childs heights
        if self.left is None:
            self.height = self.right.getHeight()+1
        elif self.right is None:
            self.height = self.left.getHeight()+1
        else:
            #If both childs exist, we return the max height between its children
            self.height = max(self.left.getHeight()+1,self.right.getHeight()+1)
        
        #Now, is time to balance our tree following the AVL implementation.
        #To do this, we first need to get the balance factor, and this is the one
        #that tells us if we need to right-balance the tree or left-balance the tree
        #To do this, we first ask for the balance using the getBalance method
        balance = self.getBalanceFactor()
        
        #Then, we have 4 cases in order to balance the tree
        #If balance is positive and key is less than left, we right rotate our tree
        if balance > 1 and self.left is not None and data < self.left.data: 
            return self.rightRotate() 
  
        #If balance is negative and our key is greater than right, we left rotate our tree
        if balance < -1 and self.right is not None and data >= self.right.data: 
            return self.leftRotate() 
  
        #If balance is positive and key is greater than left, we first left rotate
        #the left of root and then we right rotate the whole tree
        if balance > 1 and self.left is not None and data >= self.left.data: 
            self.left = self.left.leftRotate() 
            return self.rightRotate() 
  
        #If balance is negative and key is less than right, we first right rotate
        #the right of root and then we left rotate the whole tree
        if balance < -1 and self.right is not None and data < self.right.data: 
            self.right = self.right.rightRotate() 
            return self.leftRotate() 
  
        #Finally, if there was no need to balance the tree, we just return the old root
        return self 

    def leftRotate(self):
        # Perform a left rotation on this node and return the new node in its spot
        #First, we get the one at the left of the node which would be the new root
        #for the subtree and also the right of the new root
        root = self.right 
        temp = root.left 
  
        #Now, we rotate
        root.left = self
        self.right = temp
  
        #Finally, we update the heights and we return the new root
        #Update the height for current node
        if self.left is None and self.right is None:
            self.height = 0
        elif self.left is None:
            self.height = self.right.getHeight()+1
        elif self.right is None:
            self.height = self.left.getHeight()+1
        else:
            #If both childs exist, we return the max height between its children
            self.height = max(self.left.getHeight()+1,self.right.getHeight()+1)
            
        #Update the height for new root node
        if root.left is None and root.right is None:
            root.height = 0
        elif root.left is None:
            root.height = root.right.getHeight()+1
        elif root.right is None:
            root.height = root.left.getHeight()+1
        else:
            #If both childs exist, we return the max height between its children
            root.height = max(root.left.getHeight()+1,root.right.getHeight()+1)
 
        return root

    def rightRotate(self):
        # Perform a right rotation on this node and return the new node in its spot
        #First, we get the one at the left of the node which would be the new root
        #for the subtree and also the right of the new root
        root = self.left 
        temp = root.right
  
        #Now, we rotate
        root.right = self
        self.left = temp
  
        #Finally, we update the heights and we return the new root
        #Update the height for current node
        if self.left is None and self.right is None:
            self.height = 0
        elif self.left is None:
            self.height = self.right.getHeight()+1
        elif self.right is None:
            self.height = self.left.getHeight()+1
        else:
            #If both childs exist, we return the max height between its children
            self.height = max(self.left.getHeight()+1,self.right.getHeight()+1)
            
        #Update the height for new root node
        if root.left is None and root.right is None:
            root.height = 0
        elif root.left is None:
            root.height = root.right.getHeight()+1
        elif root.right is None:
            root.height = root.left.getHeight()+1
        else:
            #If both childs exist, we return the max height between its children
            root.height = max(root.left.getHeight()+1,root.right.getHeight()+1)
 
        return root