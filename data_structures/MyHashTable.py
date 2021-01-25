# You may not use dicts.

class MyHashTable():
    def __init__(self, size, hash1):
        self.size = size
        self.items = [None] * size
        self.count = 0
        self.hash1 = hash1
    
    def put(self, key, data):
        index = self.hash1(key)
        if self.items[index] is None:
            #Here, we store a tuple representing a (key,data)
            self.items[index] = (key,data)
            self.count += 1
            return True
        return False
    
    def get(self, key):
        index = self.hash1(key)
        if index >= len(self.items):
            return None
        #Once we get the index, we check if the key is the asked one
        if self.items[index][0] == key:
            return self.items[index][1]
        else:
            #If not the key we're looking for, then None
            return None
        
    def __len__(self):
        return self.count

    def __str__(self):
        return str(self.items)

    def isFull(self):
        return self.count == self.size

class MyChainTable(MyHashTable):
    def __init__(self, size, hash1):
        # Create an empty hashtable with the size given, and stores the function hash1
        super().__init__(size,hash1)
        for i in range(0, size):
            self.items[i] = []
    
    def put(self, key, data):
        index = self.hash1(key)
        lst = self.items[index]
        lst.append((key, data))
        self.count += 1
        return True

    def get(self, key):
        index = self.hash1(key)
        lst = self.items[index]
        for p in lst:
            if p[0] == key:
                return p[1]
        return None

    def __len__(self):
        return super().__len__()

    def isFull(self):
        return False

class MyDoubleHashTable(MyHashTable):
    def __init__(self, size, hash1, hash2):
        # Create an empty hashtable with the size given, and stores the functions hash1 and hash2
        super().__init__(size,hash1)
        self.hash2 = hash2
    
    def put(self, key, data):
        if self.isFull():
            return False
        index = self.hash1(key)
        #Here, we use an index i to get the next hash indices when needed
        i = 0
        while self.items[index] is not None:
            #The hash function to use is the next formula that involves both hash1 and hash2
            index = (self.hash1(key) + i * self.hash2(key)) % self.size
            i += 1
        self.items[index] = (key, data)
        self.count += 1
        return True
    
    def get(self, key):
        # Returns the item linked to the key given, or None if element does not exist 
        index = self.hash1(key)
        if index >= len(self.items):
            return None
        item = self.items[index]
        #Here, we use an index i to get the next hash indices when needed
        i = 0
        while item[0] is not key:
            #The hash function to use is the next formula that involves both hash1 and hash2
            index = (self.hash1(key) + i * self.hash2(key)) % self.size
            #If i gets equals to the size, it means the item doesn't exist, so break
            if i == self.size:
                break
            item = self.items[index]
            i += 1
        if item is None:
            return None
        return item[1] if item[0] is key else None
        
    def __len__(self):
        return super().__len__()