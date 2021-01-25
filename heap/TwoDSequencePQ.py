class TwoDSequencePQ(object):
    def __init__(self):
        
        self._queue = []
        self._len = 0


    def length(self, p):
        # Number of elements in the queue number p
        return len(self._queue[p])


    def __len__(self):
        return self._len


    def is_empty(self):
        return len(self) == 0


    def add(self, key, value):
        # Validates the key
        if (key < 0):
            raise KeyError
        priority = key
        # Finds number of lists in queue 
        max_priority = len(self._queue) - 1
        
        if priority > max_priority:
            # Number of new lists
            n_lists = priority - max_priority
            # Make n_lists new lists and append to queue
            for i in range(n_lists):
                self._queue.append([])

        #Here, before appending it to the current priority, we need to compare the element
        #to find its correct position inside the given list
        added = False
        for i,elem in enumerate(self._queue[priority]):
            #If our value is less than the current value, we insert it there and we break
            if value < elem[1]:
                self._queue[priority].insert(i,(key,value))
                added = True
                break
        #If the loop ends and 'added' is False, we just append it to the end of the list
        if not added:
            self._queue[priority].append((key, value))
        self._len += 1

    def _min(self):
        # Finds first non-empty queue
        for priority, list in enumerate(self._queue):
            if list:  # list is not empty
                # Return first element and its key
                return priority, list[0]



    #Min function can just return element
    def min(self):
        _, element = self._min()
        return element



    def remove_min(self):
        # Get min
        priority, element = self._min()
        # Remove min
        del self._queue[priority][0]
        # Decrement _len
        self._len -= 1
        # Return element
        return element

