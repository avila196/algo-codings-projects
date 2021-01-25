"""
Project #1     Fall 2019
SongLibrary.py - SongLibrary class
"""

from Song import Song
import random
import time


class SongLibrary:
    """
    Intialize your Song library here.
    You can initialize an empty songArray, empty BST and
    other attributes such as size and whether the array is sorted or not

    """
    def __init__(self):
        self.songArray = list()
        self.songBST = None
        self.isSorted = False
        self.size = 0

    """
    load your Song library from a given file. 
    It takes an inputFilename and store the songs in songArray
    """

    def loadLibrary(self, inputFilename):        
        #To load the library of songs from the file, we read the file line by line
        #To do this, we open it normally and then we loop through its lines
        file = open(inputFilename,'r')
        for line in file:
            #Now, for each of the lines, we create the Sobg object
            song = Song(line)
            #Then, we append the current song to the list of songs and increase size
            self.songArray.append(song)
            self.size += 1


    """
    Linear search function.
    It takes a query string and attibute name (can be 'title' or 'artist')
    and return the number of songs fonud in the library.
    Return -1 if no songs is found.
    Note that, Each song name is unique in the database,
    but each artist can have several songs.
    """
    def linearSearch(self, query, attribute):
        found = 0 #Found can be initialized as 0
        #For the linear search, we just loop through the array of songs and we look
        #for the ones that actually have the same query given the attribute searched.
        #To do this, we do a for loop through the songArray
        for song in self.songArray:
            #Now, we check for the respective attribute
            #If we're looking for title and the titles are equal, we found one
            if attribute == 'title' and song.title == query:
                found += 1
            #If we're looking for artist and the artists are equal, we found one
            elif attribute == 'artist' and song.artist == query:
                found += 1
            #If not, we just pass and continue to next loo
            else:
                pass
        #Finally, when the loop ends, if found is still 0, it means there were no
        #matches, so we return -1
        if found == 0:
            return -1
        #If not, we return 'found' directly
        else:
            return found

    """
    Build a BST from your Song library based on the song title. 
    Store the BST in songBST variable
    """

    def buildBST(self):
        #Here, to build the balanced BST, we just loop through the array of Songs
        #and we add them to the Tree
        self.songBST = BST()
        for song in self.songArray:
            self.songBST.add(song)
            
    """
    Implement a search function for a query song (title) in the songBST.
    Return the song information string
    (After you find the song object, call the toString function)
    or None if no such song is found.
    """
    def searchBST(self, query):
        #Here, to perform the search, we just call the method binarySearch
        #from the tree.
        found = self.songBST.binarySearch(query)
        #If it returns None, we return None
        if found is None:
            return None
        #If not, we return the toString from the song
        else:
            return found.toString()

    """
    Return song libary information
    """
    def libraryInfo(self):
        return "Size: " + str(self.size) + ";  isSorted: " + str(self.isSorted)

    """
    Sort the songArray using QuickSort algorithm based on the song title.
    The sorted array should be stored in the same songArray.
    Remember to change the isSorted variable after sorted
    """
    def quickSort(self):
        #For a quickSort, we need to choose a pivot value, in this case it is
        #the last eklement, and we place it on the correct on the array. Then,
        #we place all the smaller ones before that index and all the greater ones
        #after that index. This is done by a a recursive procedure, so we call the
        #quickSort method here that does the recursive calls
        self.qsort(self.songArray,0,len(self.songArray)-1)
        #Then, we make the boolean isSorted as true
        self.isSorted = True
    
    """
    Recursive quickSort method that sorts the songArray base on the song title.
    """
    def qsort(self,array,low,high): 
        #For the quickSort, if low < high indices, it means there's still
        #part of the array to be sorted
        if low < high: 
            #Here, we start placing the pivot (last element, at high index), in the
            #correct position, we move all smaller values before that index and
            #all greater values after that index and we store the index where it
            #occurs. To do this, we use the well known method called 'partition'
            index = self.partition(array,low,high) 
            
            #Then, we sort values before and after the index for the pivot
            self.qsort(array, low, index-1) 
            self.qsort(array, index+1, high)  
        
    """
    Partition helper function to perform the quickSort
    This function chooses the last element as the pivot, places it on the right
    index, places all smaller values before it and greater values after it and
    returns the index where all of that occurs, the correct index on the sorted
    array for the current pivot.
    """
    def partition(self,array,low,high): 
        #We start finding the pivot
        pivot = array[high]
        #Also, we declare the index of the pivot to be found as low-1 to start
        index = low - 1
        
        #Now, we loop through the whole array to place all the smaller values
        #before the pivot final index.
        #To do this, we loop from low to high
        for i in range(low,high,1):
            #If the value at i index has a 'smaller title', we place it on the
            #next index
            if array[i].title <= pivot.title: 
                #We increment the next index value
                index += 1 
                #Then, we do the swap between the value at index and the valye at i
                temp = array[index]
                array[index] = array[i]
                array[i] = temp
        
        #Finally, wthen the loop ends, 'index' is the final index  where all smaller
        #values are before it, so we place pivot on index+1 (swap again) and we
        #return it
        temp = array[index+1]
        array[index+1] = pivot
        array[high] = temp
        return index+1
    
"""
Class that represents a Node for the BST to build to store Songs
"""
class SongNode: 
    """
    Constructor of the Node. It stores the value as the song title,
    value that will be used to perform the add and search on the BST
    """
    def __init__(self, song): 
        self.song = song
        self.value = song.title
        self.left = None
        self.right = None
        self.height = 1

"""
Class that represents a balanced BST
It follows the implementation of an AVL tree in order to self balance when
inserting values
"""
class BST: 
    
    """
    Constructor for the BST
    """
    def __init__(self):
        self.root = None
        
    """
    Add function that adds the given value inside the BST
    """
    def add(self,key):
        #If this is the first value, we create a new root with it
        if self.root is None:
            self.root = SongNode(key)
        #If not, we insert it on teh respective position using a recursive
        #method and we replace the new root (if needed for a new balance)
        else:
            self.root = self.insert(self.root,key)
  
    """
    Recursive function to insert the given value inot the tree
    """
    def insert(self, root, key): 
        # First, we do a normal insert for BST into the tree
        if root is None:
            return SongNode(key)
        if key.title < root.value:
            root.left = self.insert(root.left, key) 
        else: 
            root.right = self.insert(root.right, key) 
  
        #Then, we update the height of the previous root using its childs heights
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right)) 
  
        #Now, is time to balance our tree following the AVL implementation.
        #To do this, we first need to get the balance factor, and this is the one
        #that tells us if we need to right-balance the tree or left-balance the tree
        #To do this, we first ask for the balance using the getBalance method
        balance = self.getBalance(root) 
        
        #Then, we have 4 cases in order to balance the tree
        #If balance is positive and key is less than left, we right rotate our tree
        if balance > 1 and key.title < root.left.value: 
            return self.rightRotate(root) 
  
        #If balance is negative and our key is greater than right, we left rotate our tree
        if balance < -1 and key.title > root.right.value: 
            return self.leftRotate(root) 
  
        #If balance is positive and key is greater than left, we first left rotate
        #the left of root and then we right rotate the whole tree
        if balance > 1 and key.title > root.left.value: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        #If balance is negative and key is less than right, we first right rotate
        #the right of root and then we left rotate the whole tree
        if balance < -1 and key.title < root.right.value: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        #Finally, if there was no need to balance the tree, we just return the old root
        return root 
  
    """
    Method that left rotate the subtree for the given node
    """
    def leftRotate(self, node): 
        
        #First, we get the one at the right of the node which would be the new root
        #for the subtree and also the left of the new root
        root = node.right 
        temp = root.left 
  
        #Now, we rotate
        root.left = node
        node.right = temp
  
        #Finally, we update the heights and we return the new root
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right)) 
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right)) 
        return root
  
    """
    Method that right rotate the subtree for the given node
    """
    def rightRotate(self, node): 
        
        #First, we get the one at the left of the node which would be the new root
        #for the subtree and also the right of the new root
        root = node.left 
        temp = root.right 
  
        #Now, we rotate
        root.right = node
        node.left = temp
  
        #Finally, we update the heights and we return the new root
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right)) 
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))  
        return root
  
    """
    Function to get the balance factor for the given node
    """
    def getBalance(self, node): 
        #If the node is None, then 0
        if node is None: 
            return 0
        #Else, we check for the heights of childs to get the respective balance
        else:
            return self.getHeight(node.left) - self.getHeight(node.right) 
    
    """
    Function to get the height of a given node. If Node, return 0.
    If not, we return its height
    """
    def getHeight(self, root): 
        if not root: 
            return 0
  
        return root.height 
        
    """
    Recursive function to do a binary search on the tree for the given value
    Returns the song object on it if found, None if not
    """
    def binarySearch(self, val, node=0):
        #If node = 0, this is the first call, so we call again using the root as
        #the starting node
        if node == 0:
            return self.binarySearch(val,self.root)
        
        #To perform the search, we first look at the current node. 
        #If the node is None, we return false
        if node is None:
            return None
        #If it's val is the one we're looking for, we return true
        if node.value == val:
            return node.song
        #If not, if value is less, we call again for its left node
        elif val < node.value:
            return self.binarySearch(val,node.left)
        #Else, if greater, we call again for its right node
        else:
            return self.binarySearch(val,node.right)
  
        
# WRITE YOUR OWN TEST UNDER THAT IF YOU NEED
if __name__ == '__main__':
    songLib = SongLibrary()
    songLib.loadLibrary("TenKsongs.csv")
    print(songLib.libraryInfo())
    songLib.buildBST()
    print("Looking for <Mr. Goose> using the BST --> "+songLib.searchBST("Mr. Goose"))
    print("--- sorting --- ")
    songLib.quickSort()
    print(songLib.libraryInfo())
    
    #TO DO: Perform all the tests you need to do and record all the needed times
    #and final perform data :) 
    
    
    
    