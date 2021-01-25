import heapq

class MyHuffman():
    def __init__(self):
        #We can initialize the root node as None
        self.root = None
        
    def build(self, weights):
        # Build a huffman tree from the dictionary of character:value pairs
        #To build the Huffman tree, we need to use a min-heap structure to store all the
        #characters along with their frquencies as Nodes.
        #Let's start adding all the Nodes to the min-heap
        h = []
        for key in weights:
            #We create a node with the given char (key) and frequency (value)
            node = Node(key,weights[key])
            heapq.heappush(h,node)
        #After all values were added, we start looping through the heap to join the pairs
        #of smallest nodes in order to create the Huffman tree
        while len(h) > 1:
            #We first take the 2 min values from the heap
            first = heapq.heappop(h)
            second = heapq.heappop(h)
            #Now, we create a new Node with both of them as childs and the root as the sum
            newNode = Node(None,first.data+second.data,first,second)
            #Then, we push the new node into the heap
            heapq.heappush(h,newNode)
        
        #When the joining ends, the remaining node is the root of the tree
        self.root = h[0]
            
    def encode(self, word):
        # Return the bitstring of word encoded by the rules of your huffman tree
        #To encode a String, we need to loop through the chars of the String to find the
        #bit representation of each of the chars.
        encoded = ''
        for c in word:
            #Here, we can look for the bitstring for the current char using the helper method
            bs = self.findBitstring(c,self.root)
            if bs[0]:
                encoded += bs[1]
            else:
                #If False, it means the char doesn't exist, so None directly
                return None 
        #Finally, we return the encoded string
        return encoded
            
    def findBitstring(self, c, node, bitstring=''):
        #To find the bitstring of the current char, we loop through the tree until we get
        #to the needed char. We can do this recursively.
        #If the node is already the one with the char, we found it, so return the bitstring
        if c == node.value:
            return True, bitstring
        else:
            #If not, we can call the left path first recursively and check for the return
            if node.left is not None:
                found = self.findBitstring(c, node.left, bitstring+"0")
                if found[0]:
                    return True, found[1]
            #Then, we do the same for right child
            if node.right is not None:
                found = self.findBitstring(c, node.right, bitstring+"1")
                if found[0]:
                    return True, found[1]
            #If we get until here with no returns, it means the path doesn't work, then False
            return False, ""
    
    def decode(self, bitstring):
        # Return the word encoded in bitstring, or None if the code is invalid
        #Here, to decode a bitstring, we loop through all the bits and we get pieces
        #of them until we get to a valid char. If the string runs out and no valid chars are
        #found, we return None directly
        decoded = ''
        bs = bitstring
        while len(bs) > 0:
            #Here, we do a 2nd loop to consider portions of the bitstring
            i = 0
            found = False
            while i <= len(bs):
                c = self.findChar(bs[:i])
                #If the current char is valid, then we append it to the decoded string
                #and we break the inner loop after 'cutting' the bitstring
                if c is not None:
                    decoded += c
                    bs = bs[i:]
                    found = True
                    break
                else:
                    #If not, we consider another bit
                    i += 1
            #Once the inner loop ends, we either found a char or we run out of bits to find
            if not found:
                #For this case, there's a bitstring that doesn't exist, so None
                return None
        #If no returns until this point, it means the bitstring was valid, so return decoded
        return decoded
            
        
    def findChar(self, bitstring):
        #Here, to look for a valid char given the bitstring, we just traverse the tree
        #for each of the values on the bitstring. If 0, we go to the left. If 1, to the right
        node = self.root
        for b in bitstring:
            if b == '0':
                node = node.left
            else:
                node = node.right
            #Once we get to the next node, we return None if that node doesn't exist
            if node is None:
                return None
        #Once the loop ends, we return whatever the value of the Node is (None or a valid char)
        return node.value

# This node structure might be useful to you
class Node:
    def __init__(self,value,data,left=None,right=None):
        #Here, we start creating a node with the given values
        self.value = value
        self.data = data
        self.left = left
        self.right = right

    def __lt__(self, other):
        #We compare here the data (frequencies)
        return self.data < other.data
    
    def __le__(self, other):
        #We compare here the data (frequencies)
        return self.data <= other.data

    def __gt__(self, other):
        #We compare here the data (frequencies)
        return self.data > other.data
    
    def __ge__(self, other):
        #We compare here the data (frequencies)
        return self.data >= other.data