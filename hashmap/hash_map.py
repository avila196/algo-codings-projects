#Imports needed
from unordered_list import UnorderedList

#Class that represents a HashMap
class HashMap:
    #Initializer of the HashMap
    def __init__(self, table_size = 11, can_rehash=False):
        #We init tha array with unordered lists for all positions
        self.table_size = table_size
        self.table = [UnorderedList() for i in range(table_size)]
        #Also, we init a variable representing the real number of entries and store can_rehash
        self.num_keys = 0
        self.can_rehash = can_rehash
        
    def get_table_size(self):
        # Returns the size of the table
        return self.table_size

    def get_num_keys(self):
        # Returns the number of key-value pairs in the table
        return self.num_keys

    def get_load_factor(self):
        # Returns the load factor
        m = self.table_size
        n = self.num_keys
        loadfactor = n/m
        return loadfactor

    def insert(self, key, value):
        # method should insert the given key-value pair into the table
        # Modify your insert() method so that after  completing  the  insertion, if the hash map supports rehashing and the load factor is at least 1/2, then rehashing should occur
        location = key % self.table_size
        #We check if, at current location, the key already exists
        if key in self:
            #If so, we raise an error
            raise ValueError("Key already mapped.")
        else:
            #If not, we add it to the list at current location
            self.table[location].add(key, value)
            self.num_keys += 1
        #Finally, if rehashing is enabled, we check for conditions to do it
        if self.can_rehash and self.get_load_factor() >= 0.5:
            #To reshash, we first find the next prime number such that x >= 2*size
            prime = 2*self.table_size
            while True:
                #We check if current value is prime
                is_prime = True
                for i in range(2,prime//2+1): #from 2 to prime/2
                    if prime % i == 0:
                        is_prime = False
                        break
                #If prime, we stop. If not, we increase it by 1
                if is_prime:
                    break
                else:
                    prime += 1
            #Now, we create a new table with this size
            newMap = HashMap(prime)
            #Now, we copy and rehash every value into new table
            for l in self.table:
                node = l.getHead()
                while node is not None:
                    newMap.insert(node.getKey(), node.getValue())
                    node = node.getNext()
            #Finally, we set the array from newMap as the array of this map
            self.table = newMap.table
            self.table_size = prime

    def update(self, key, value):
        # This method should change the value currently associated with the given key to be the new value
        if key not in self:
            #If the key does not exist, we raise an error
            raise ValueError("Key not mapped.")
        else:
            #If it does, we update its value. We first find it and we change the value at its Node
            location = key % self.table_size
            node = self.table[location].search(key)
            node.setValue(value)
        
    def delete(self, key):
        # This method should delete the key-value pair associated with the given key
        if key in self:
            #If it does exist, we remove it from the list it belongs
            location = key % self.table_size
            l = self.table[location]
            l.remove(key) 
            self.num_keys -= 1

    def find(self, key):
        # Returns the value associated with the key passed in as argument. Returns none if not found.
        location = key % self.table_size
        node = self.table[location].search(key)
        if node is not None:
            node = node.getValue()
        return node

    def print_keys(self):
        #TODO: Here, this method needs to traverse the List, from i = 0 to i = size-1, and
        #it should print every key of every existing node there. If the List is empty, it should
        #print just "None"
        print(self.table) #change this print by the needed one
        

    def __contains__(self, key):
        # This method should return True if key is mapped in the hash table and False if not
        location = key % self.table_size
        return self.table[location].search(key) is not None

if __name__ == "__main__":
    h = HashMap()
    h.insert(3, 8)
    h.insert(14, 15)
    h.insert(50, 20)
    h.insert(27, -5)
    h.insert(36, 40)
    print("=== Printing keys ===")
    h.print_keys()
    print("=== Done printing keys ===")
    print("h.get_num_keys():", h.get_num_keys())
    print("h.find(3):", h.find(3))
    print("h.find(36):", h.find(36))
    print("h.find(20):", h.find(20))
    print("3 in h:", 3 in h)
    print("36 in h:", 36 in h)
    print("40 in h:", 40 in h)  # value doesn't work
    h.delete(3)
    h.delete(36)
    h.delete(80)  # unsuccessful
    print("=== Performed three deletions (two successful) ===")
    h.print_keys()
    print("=== By default, rehashing is disabled ===")
    h.insert(11, 1)
    h.insert(22, 1)
    h.insert(33, 1)
    h.print_keys()
    print("h.get_num_keys():", h.get_num_keys())
    print("Load factor (rounded):", round(h.get_load_factor(),2))
    print("\n=== Let's try a hash table that supports rehashing ===")
    h = HashMap(5, True)
    h.insert(15, "values can be any type, by the way")
    h.insert(20, "but the keys have to be integers")
    print("===== Before insertion that causes rehash =====")
    h.print_keys()
    h.insert(26, 48)  # triggers rehashing, AFTER being inserted
    print("===== After rehashing =====")
    h.print_keys()
    print("h.get_num_keys():", h.get_num_keys())
    print("Load factor (rounded):", round(h.get_load_factor(),2))
