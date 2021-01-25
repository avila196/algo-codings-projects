'''
' Tester code for Question 10 (LinkedLinkedPQ) of the Final Project.
'''

from LinkedLinkedPQ import LinkedLinkedPQ

#10.1) Test the LinkedLinkedPQ constructor
print("------------------------------------------------------------")
print("10.1) Test the LinkedLinkedPQ constructor")
print("------------------------------------------------------------")

pq = LinkedLinkedPQ()

print("len:      0\t= " + str(len(pq)))
print("is_empty: True\t= " + str(pq.is_empty()))

input()

#10.2) Test accessing an empty LinkedLinkedPQ
print("------------------------------------------------------------")
print("10.2) Test accessing an empty LinkedLinkedPQ")
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

#10.3) Test the LinkedLinkedPQ add method with ints as keys
print("------------------------------------------------------------")
print("10.3) Test the LinkedLinkedPQ add method with ints keys")
print("------------------------------------------------------------")

pq.add(5, 10)

print("len:      1\t\t\t= " + str(len(pq)))
print("is_empty: False\t\t\t= " + str(pq.is_empty()))
print("min:      (5, 10)\t\t= " + str(pq.min()))
print()

pq.add(2, 1)

print("len:      2\t\t\t= " + str(len(pq)))
print("is_empty: False\t\t\t= " + str(pq.is_empty()))
print("min:      (2, 1)\t\t= " + str(pq.min()))
print()

pq.add(23, "My Password is Taco")

print("len:      3\t\t\t= " + str(len(pq)))
print("is_empty: False\t\t\t= " + str(pq.is_empty()))
print("min:      (2, 1)\t\t= " + str(pq.min()))
print()

pq.add(-10, "Balkava")

print("len:      4\t\t\t= " + str(len(pq)))
print("is_empty: False\t\t\t= " + str(pq.is_empty()))
print("min:      (-10, 'Baklava')\t= " + str(pq.min()))
print()

pq.add(0, "Should be second")

print("len:      5\t\t\t= " + str(len(pq)))
print("is_empty: False\t\t\t= " + str(pq.is_empty()))
print("min:      (-10, 'Baklava')\t= " + str(pq.min()))
print()

pq.add(123, "Last")

print("len:      6\t\t\t= " + str(len(pq)))
print("is_empty: False\t\t\t= " + str(pq.is_empty()))
print("min:      (-10, 'Baklava')\t= " + str(pq.min()))
input()

pq.add(-5, "Weird, right?")

print("len:      7\t\t\t= " + str(len(pq)))
print("is_empty: False\t\t\t= " + str(pq.is_empty()))
print("min:      (-10, 'Baklava')\t= " + str(pq.min()))
print()

pq.add(0, "Should be first")

print("len:      8\t\t\t= " + str(len(pq)))
print("is_empty: False\t\t\t= " + str(pq.is_empty()))
print("min:      (-10, 'Baklava')\t= " + str(pq.min()))
print()

pq.add(47, 555.55)

print("len:      9\t\t\t= " + str(len(pq)))
print("is_empty: False\t\t\t= " + str(pq.is_empty()))
print("min:      (-10, 'Baklava')\t= " + str(pq.min()))
print()

pq.add(1, ["A", "list", "of", "stuff"])

print("len:      10\t\t\t= " + str(len(pq)))
print("is_empty: False\t\t\t= " + str(pq.is_empty()))
print("min:      (-10, 'Baklava')\t= " + str(pq.min()))
print()

pq.add(-15, "¡Top!")

print("len:      11\t\t\t= " + str(len(pq)))
print("is_empty: False\t\t\t= " + str(pq.is_empty()))
print("min:      (-15, '¡Top!')\t= " + str(pq.min()))
print()

input()

#10.4) Test the LinkedLinkedPQ min and remove_min methods
print("------------------------------------------------------------")
print("10.4) Test the LinkedLinkedPQ min and remove_min methods")
print("------------------------------------------------------------")


print("remove_min: (-15, '¡Top!')\t\t= " + str(pq.remove_min()))
print("len:        10\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))
print()

print("min:        (-10, 'Baklava')\t\t= " + str(pq.min()))
print("remove_min: (-10, 'Baklava')\t\t= " + str(pq.remove_min()))
print("len:        9\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))
print()

print("min:        (-5, 'Weird, right?')\t= " + str(pq.min()))
print("remove_min: (-5, 'Weird, right?')\t= " + str(pq.remove_min()))
print("len:        8\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))
print()

print("min:        (0, 'Should be <either>')\t= " + str(pq.min()))
print("remove_min: (0, 'Should be <either>')\t= " + str(pq.remove_min()))
print("len:        7\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))
print()

print("min:        (0, 'Should be <either>')\t= " + str(pq.min()))
print("remove_min: (0, 'Should be <either>')\t= " + str(pq.remove_min()))
print("len:        6\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))
input()

print("min:        (1, ['A', 'list', 'of', 'stuff'])\n\t  = " + str(pq.min()))
print("remove_min: (1, ['A', 'list', 'of', 'stuff'])\n\t  = " + str(pq.remove_min()))
print("len:        5\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))
print()

print("min:        (2, 1)\t\t\t= " + str(pq.min()))
print("remove_min: (2, 1)\t\t\t= " + str(pq.remove_min()))
print("len:        4\t\t\t\t= " + str(len(pq)))
print("is_empty:   False\t\t\t= " + str(pq.is_empty()))
print()

print("min:        (5, 10)\t\t\t= " + str(pq.min()))
print("remove_min: (5, 10)\t\t\t= " + str(pq.remove_min()))
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

#10.5) Test the LinkedLinkedPQ add method with floats as keys
print("------------------------------------------------------------")
print("10.5) Test the LinkedLinkedPQ add method floats as keys")
print("------------------------------------------------------------")

pq.add(5, 10)
pq.add(2.15, 1)
pq.add(23.5, "My Password is Taco")
pq.add(-10.4, "Balkava")
pq.add(0.6, "Should be second")
pq.add(123.467, "Last")
pq.add(-4.9, "Weird, right?")
pq.add(0.6, "Should be first")
pq.add(47, 555.55)
pq.add(1.0000007, ["A", "list", "of", "stuff"])
pq.add(-14.55, "¡Top!")

print("len:      11\t\t\t= " + str(len(pq)))
print("is_empty: False\t\t\t= " + str(pq.is_empty()))
print("min:      (-14.55, '¡Top!')\t= " + str(pq.min()))
print()

print("remove_min: (-14.55, '¡Top!')\t\t  = " + str(pq.remove_min()))
print("remove_min: (-10.4, 'Balkava')\t\t  = " + str(pq.remove_min()))
print("remove_min: (-4.9, 'Weird, right?')\t  = " + str(pq.remove_min()))
print("remove_min: (0.6, 'Should be <either>')\t  = " + str(pq.remove_min()))
print("remove_min: (0.6, 'Should be <either>')\t  = " + str(pq.remove_min()))
print("remove_min: (1.0000007, ['A', 'list', 'of', 'stuff'])\n\t  = " + str(pq.remove_min()))
print("remove_min: (2.15, 1)\t\t\t  = " + str(pq.remove_min()))
print("remove_min: (5, 10)\t\t\t  = " + str(pq.remove_min()))
print("remove_min: (23.5, 'My Password is Taco') = " + str(pq.remove_min()))
print("remove_min: (47, 555.55)\t\t  = " + str(pq.remove_min()))
print("remove_min: (123, 'Last')\t\t  = " + str(pq.remove_min()))
print()

print("len:      11\t= " + str(len(pq)))
print("is_empty: False\t= " + str(pq.is_empty()))

try:
    print("min:      None\t= " + str(pq.min()))
except:
    print("min:      None\t= None (via exception)")

input()

#10.6) Test the LinkedLinkedPQ add method with strings as keys
print("------------------------------------------------------------")
print("10.6) Test the LinkedLinkedPQ add method strings as keys")
print("------------------------------------------------------------")

pq.add("balkava", 10)
pq.add("apescat!", 1)
pq.add("zoo", "My Password is Taco")
pq.add("!2", "Balkava")
pq.add("Apescat!", "Second")
pq.add("æÞëşɔαէ‼֍Ὡ☺☻☼♠♣♥♦", "Last")
pq.add("2.7", "Weird, right?")
pq.add("Apescat!", "First")
pq.add("åpescat!", 555.55)
pq.add("apes", ["A", "list", "of", "stuff"])
pq.add("!!", "¡Top!")

print("len:      11\t\t\t= " + str(len(pq)))
print("is_empty: False\t\t\t= " + str(pq.is_empty()))
print("min:      (-14.55, '¡Top!')\t= " + str(pq.min()))
print()

print("remove_min: ('!!', '¡Top!')\t\t  = " + str(pq.remove_min()))
print("remove_min: (!2, 'Balkava')\t\t  = " + str(pq.remove_min()))
print("remove_min: ('2.7', 'Weird, right?')\t  = " + str(pq.remove_min()))
print("remove_min: ('Apescat!', '<either>')\t  = " + str(pq.remove_min()))
print("remove_min: ('Apescat!', '<either>')\t  = " + str(pq.remove_min()))
print("remove_min: ('apes', ['A', 'list', 'of', 'stuff'])\n\t  = " + str(pq.remove_min()))
print("remove_min: ('apescat!', 1)\t\t  = " + str(pq.remove_min()))
print("remove_min: ('baklava', 10)\t\t  = " + str(pq.remove_min()))
print("remove_min: ('zoo', 'My Password is Taco') = " + str(pq.remove_min()))
print("remove_min: ('åpescat!', 555.55)\t  = " + str(pq.remove_min()))
print("remove_min: ('æÞëşɔαէ‼֍Ὡ☺☻☼♠♣♥♦', 'Last')  = " + str(pq.remove_min()))
print()

print("len:      11\t= " + str(len(pq)))
print("is_empty: False\t= " + str(pq.is_empty()))

try:
    print("min:      None\t= " + str(pq.min()))
except:
    print("min:      None\t= None (via exception)")

input()
