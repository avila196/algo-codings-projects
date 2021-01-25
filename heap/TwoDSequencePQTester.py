'''
' Tester code for Question 05 (TwoDSequencePQ) of the Final Project.
'''

from TwoDSequencePQ import TwoDSequencePQ

#7.1) Test the LinkedHeapPQ constructor
print("------------------------------------------------------------")
print("7.1) Test the LinkedHeapPQ constructor")
print("------------------------------------------------------------")

pq = TwoDSequencePQ()

print("len:      0\t= " + str(len(pq)))
print("is_empty: True\t= " + str(pq.is_empty()))

input()

#7.2) Test accessing an empty LinkedHeapPQ
print("------------------------------------------------------------")
print("7.2) Test accessing an empty LinkedHeapPQ")
print("------------------------------------------------------------")

try:
    print("None:\t= " + str(pq.min()))
except:
    print("None:\t= None (via exception)")

try:
    print("None:\t= " + str(pq.remove_min()))
except:
    print("None:\t= None (via exception)")

input()

#7.3) Test the LinkedHeapPQ add method with ints as keys
print("------------------------------------------------------------")
print("7.3) Test the LinkedHeapPQ add method with ints keys")
print("------------------------------------------------------------")

pq.add(5, 10)

print("len:      1\t\t\t    = " + str(len(pq)))
print("is_empty: False\t\t\t    = " + str(pq.is_empty()))
print("min:      (5, 10)\t\t    = " + str(pq.min()))
print()

pq.add(2, 1)

print("len:      2\t\t\t    = " + str(len(pq)))
print("is_empty: False\t\t\t    = " + str(pq.is_empty()))
print("min:      (2, 1)\t\t    = " + str(pq.min()))
print()

pq.add(23, "My Password is Taco")

print("len:      3\t\t\t    = " + str(len(pq)))
print("is_empty: False\t\t\t    = " + str(pq.is_empty()))
print("min:      (2, 1)\t\t    = " + str(pq.min()))
print()

pq.add(10, "Balkava")

print("len:      4\t\t\t    = " + str(len(pq)))
print("is_empty: False\t\t\t    = " + str(pq.is_empty()))
print("min:      (2, 1)\t\t    = " + str(pq.min()))
print()

pq.add(0, "Should be second")

print("len:      5\t\t\t    = " + str(len(pq)))
print("is_empty: False\t\t\t    = " + str(pq.is_empty()))
print("min:      (0, 'Should be second')   = " + str(pq.min()))
print()

pq.add(123, "Last")

print("len:      6\t\t\t    = " + str(len(pq)))
print("is_empty: False\t\t\t    = " + str(pq.is_empty()))
print("min:      (0, 'Should be second')   = " + str(pq.min()))
input()

pq.add(14, "Weird, right?")

print("len:      7\t\t\t    = " + str(len(pq)))
print("is_empty: False\t\t\t    = " + str(pq.is_empty()))
print("min:      (0, 'Should be second')   = " + str(pq.min()))
print()

pq.add(0, "Should be first")

print("len:      8\t\t\t    = " + str(len(pq)))
print("is_empty: False\t\t\t    = " + str(pq.is_empty()))
print("min:      (0, 'Should be <either>') = " + str(pq.min()))
print()

pq.add(47, 555.55)

print("len:      9\t\t\t    = " + str(len(pq)))
print("is_empty: False\t\t\t    = " + str(pq.is_empty()))
print("min:      (0, 'Should be <either>') = " + str(pq.min()))
print()

pq.add(1, ["A", "list", "of", "stuff"])

print("len:      10\t\t\t    = " + str(len(pq)))
print("is_empty: False\t\t\t    = " + str(pq.is_empty()))
print("min:      (0, 'Should be <either>') = " + str(pq.min()))
print()

pq.add(15, "¡Top!")

print("len:      11\t\t\t    = " + str(len(pq)))
print("is_empty: False\t\t\t    = " + str(pq.is_empty()))
print("min:      (0, 'Should be <either>') = " + str(pq.min()))
print()

input()

#7.4) Test the LinkedHeapPQ min and remove_min methods
print("------------------------------------------------------------")
print("7.4) Test the LinkedHeapPQ min and remove_min methods")
print("------------------------------------------------------------")

print("remove_min: (0, 'Should be <either>')\t= " + str(pq.remove_min()))
print("len:        10\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))
print()

print("min:        (0, 'Should be <either>')\t= " + str(pq.min()))
print("remove_min: (0, 'Should be <either>')\t= " + str(pq.remove_min()))
print("len:        9\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))
print()

print("min:        (1, ['A', 'list', 'of', 'stuff'])\n\t  = " + str(pq.min()))
print("remove_min: (1, ['A', 'list', 'of', 'stuff'])\n\t  = " + str(pq.remove_min()))
print("len:        8\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))
print()

print("min:        (2, 1)\t\t\t= " + str(pq.min()))
print("remove_min: (2, 1)\t\t\t= " + str(pq.remove_min()))
print("len:        7\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))
print()

print("min:        (5, 10)\t\t\t= " + str(pq.min()))
print("remove_min: (5, 10)\t\t\t= " + str(pq.remove_min()))
print("len:        6\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))
input()

print("min:        (10, 'Baklava')\t= " + str(pq.min()))
print("remove_min: (10, 'Baklava')\t= " + str(pq.remove_min()))
print("len:        5\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))
print()

print("min:        (14, Weird, right?')\t\t= " + str(pq.min()))
print("remove_min: (14, Weird, right?')\t\t= " + str(pq.remove_min()))
print("len:        4\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))
print()

print("min:        (15, '¡Top!')\t\t\t= " + str(pq.min()))
print("remove_min: (15, '¡Top!')\t\t\t= " + str(pq.remove_min()))
print("len:        3\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))
print()

print("min:        (23, 'My Password is Taco')\t= " + str(pq.min()))
print("remove_min: (23, 'My Password is Taco')\t= " + str(pq.remove_min()))
print("len:        2\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))
print()

print("min:        (47, 555.55)\t\t= " + str(pq.min()))
print("remove_min: (47, 555.55)\t\t= " + str(pq.remove_min()))
print("len:        1\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))
print()

print("min:        (123, 'Last')\t\t= " + str(pq.min()))
print("remove_min: (123, 'Last')\t\t= " + str(pq.remove_min()))
print("len:        0\t\t\t\t= " + str(len(pq)))
print("is_empty:   True\t\t\t= " + str(pq.is_empty()))

input()

#7.5) Test the various key types that shouldn't be allowed
print("------------------------------------------------------------")
print("7.5) Test the various key types that shouldn't be allowed")
print("------------------------------------------------------------")

try:
    pq.add(3.5, "Uh oh")
except:
    print("Float key value failed. (Exception)")
else:
    if len(pq) == 0:
        print("Float key value failed. (Not allowed)")
    else:
        print("FLOAT KEY VALUE ALLOWED!")
        pq.remove_min()

try:
    pq.add("3", "Uh oh")
except:
    print("String key value of an integer failed. (Exception)")
else:
    if len(pq) == 0:
        print("String key value of an integer failed. (Not allowed)")
    else:
        print("STRING KEY VALUE OF AN INTEGER ALLOWED!")
        pq.remove_min()
        
try:
    pq.add("Uh oh", "Uh oh")
except:
    print("String key value failed. (Exception)")
else:
    if len(pq) == 0:
        print("String key value failed. (Not allowed)")
    else:
        print("STRING KEY VALUE ALLOWED!")
        pq.remove_min()

try:
    pq.add(-5, "¡Top!")
except:
    print("Negative key value failed. (Exception)")
else:
    if len(pq) == 0:
        print("Negative key value failed. (Not allowed)")
    else:
        print("NEGATIVE KEY VALUE ALLOWED!")
        pq.remove_min()
