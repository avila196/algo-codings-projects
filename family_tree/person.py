
#Class that represents a Person
class Person:
	#Constructor of the Person
	def __init__(self,name,parents=None,children=None):
		self.name = name
		#If parents is None, we create a new List
		if parents is None:
			self.parents = []
		else:
			self.parents = parents
		#If children is None, we create a new List
		if children is None:
			self.children = []
		else:
			self.children= children
	
	#Add a parent
	def addParent(self,parent):
		#We only add it if the parent isn't there and it has less than 2 already
		if parent not in self.parents and len(self.parents) < 2:
			self.parents.append(parent)
	
	#Add a child
	def addChild(self,child):
		self.children.append(child)
