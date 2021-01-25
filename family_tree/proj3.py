from person import Person
import json
from json import JSONEncoder

#Custom class to serialize a Person to JSON
class PersonEncoder(JSONEncoder):
	def default(self, person):
		return person.__dict__
	
#Main class for the Family Tree
class DynasticDescent:
	#Constructor of the class
	def __init__(self):
		self.tree = {} #Initialize an empty Dictionary
	
	#Function that loads the tree from a JSON formatted file
	def loadTree(self,filename):
		#First, we open the file to read
		with open(filename,'r') as json_file:
			#Now, we create the dictionary with it using the method load() from the json module
			json_dict = json.load(json_file)
			#Then, using the tree laoded from JSON, we create all the Person objects for the family tree
			for name in json_dict:
				#We first get the parents and children from the json dictionary
				parents = json_dict[name]["parents"]
				children = json_dict[name]["children"]
				#Then, we create the Person object and we add it to the tree
				person = Person(name,parents,children)
				self.tree[name] = person
				
	#Function that stores the tree to a JSON formetted file
	def saveTree(self,filename):
		#First, we open the file to write
		with open(filename,'w') as json_file:
			#Now, we write the tree dictionary into the file using the method dump() from json module
			json.dump(self.tree,json_file,cls=PersonEncoder)
			
	#Function that looks for the ancestors of degree n
	def ancestors(self,n):
		#We start looping through all the members of the tree and initializing an empty List of ancestors
		lst_ancest = []
		for member in self.tree:
			person = self.tree[member]
			#Now, for the current member, we call for its ancestors using the recursive helper function
			self._ancestors(n,person,lst_ancest)
		#Once all ancestors were found, we return them
		return lst_ancest
	
	#Recursive helper function that looks for the ancestors of the needed degree
	def _ancestors(self,n,person,lst_ancest):
		#First, if the given degree is 0, we got to the ancestor needed
		if n == 0:
			#We append it to the List if not there yet
			if person.name not in lst_ancest:
				lst_ancest.append(person.name)
		else:
			#If not 0, we recursively call for the ancestors of its parents
			for parent in person.parents:
				#We call for its parent ancestors (using the Person object for parent retrieved from the tree with
				#its name) with n-1 for the next degree to consider
				if parent in self.tree:
					self._ancestors(n-1,self.tree[parent],lst_ancest)
	
	#Function that looks for the children of degree n
	def children(self,n):
		#We start looping through all the members of the tree and initializing an empty List of children
		lst_children = []
		for member in self.tree:
			person = self.tree[member]
			#Now, for the current member, we call for its children using the recursive helper function
			self._children(n,person,lst_children)
		#Once all ancestors were found, we return them
		return lst_children
	
	#Recursive helper function that looks for the children of the needed degree
	def _children(self,n,person,lst_children):
		#First, if the given degree is 0, we got to the children needed
		if n == 0:
			#We append it to the List if not there yet
			if person.name not in lst_children:
				lst_children.append(person.name)
		else:
			#If not 0, we recursively call for the children of its children
			for child in person.children:
				#We call for its child children (using the Person object for child retrieved from the tree with
				#its name) with n-1 for the next degree to consider
				if child in self.tree:
					self._children(n-1,self.tree[child],lst_children)
	
	#Function that returns the siblings of a current person
	def siblings(self,name):
		if name not in self.tree:
			return []
		#First, we look for the person with the given name
		person = self.tree[name]
		#Now, we loop through its parents to find its siblings
		sib = []
		for parent in person.parents:
			if parent in self.tree:
				#Fir each parent, we loop through its children and those are siblings
				for child in self.tree[parent].children:
					if child != name:
						sib.append(child)
		return sib
	
	#Function that adds a new person to the tree
	def addPerson(self,name):
		#First, we check that the given person is not on the family tree yet
		if name not in self.tree:
			#If not present, we just add it
			self.tree[name] = Person(name)
			return True
		return False
			
	#Function that relates two persons as parent and child
	def relatePeople(self,parent,child):
		#We first check if the assignment is valid, meaning the given child doesn't
		#have two parents yet
		if child not in self.tree or parent not in self.tree or len(self.tree[child].parents) > 2:
			return False
		#If valid, we make the relation
		self.tree[parent].addChild(child)
		self.tree[child].addParent(parent)
		return True


#Main function for the main application
def main():
	#First, we create the Tree Object (DynasticDescent)
	family = DynasticDescent()
	#Menu for choices
	while True:
		print("\n--- FAMILY TREE ---")
		print("1. Add Person")
		print("2. Relate People")
		print("3. Find Siblings of Person")
		print("4. Get Ancestors of given degree")
		print("5. Get Children of given degree")
		print("6. Load Tree")
		print("7. Save File")
		print("8. Quit")
		choice = int(input(">> Choice: "))
		#Handle choices
		if choice == 1:
			name = input("Enter name of person: ")
			added = family.addPerson(name)
			if added:
				print("Person added")
			else:
				print("Person existed already")
		elif choice == 2:
			parent = input("Enter parent name: ")
			child = input("Enter child name: ")
			added = family.relatePeople(parent,child)
			if added:
				print("Relation added")
			else:
				print("Relation not added correctly")
		elif choice == 3:
			name = input("Enter name of person: ")
			siblings = family.siblings(name)
			print("Siblings: "+str(siblings))
		elif choice == 4:
			degree = int(input("Enter degree: "))
			ancestors = family.ancestors(degree)
			print("Ancestors of degree "+str(degree)+": "+str(ancestors))
		elif choice == 5:
			degree = int(input("Enter degree: "))
			children = family.children(degree)
			print("Children of degree "+str(degree)+": "+str(children))
		elif choice == 6:
			filename = input("Enter file name to load: ")
			family.loadTree(filename)
			print("File loaded")
		elif choice == 7:
			filename = input("Enter file name to save: ")
			family.saveTree(filename)
			print("File saved")
		elif choice == 8:
			break
		else:
			print("Invalid choice")
		
if __name__ == "__main__":
	main()