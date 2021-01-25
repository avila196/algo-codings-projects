from comparable import Comparable
from vertex import Vertex

class City(Vertex, Comparable):
    """
    This class represents a city on a graph
    """
    def __init__(self, name, x, y, pop):
        """
	Create a city for a Graph.
	The instance variables are:
	    gps_X: float: Longitide
	    gps_Y: float: Latitide
	    pop: int: Population
	    name: str: Pass to Vertex constructor
	"""

        # Add code here
        super().__init__(name)
        self.x=x
        self.y=y
        self.pop=pop

    def get_X(self):
        """
        Return the City longitude
        """
        return self.x
        # Add code here

    def get_Y(self):
        """
        Return the City latitude
        """
        return self.y
        # Add code here

    def get_pop(self):
        """
        Return the City poulation
        """
        return self.pop
        # Add code here

    def compare(self, other_city):
        """
        Use the City poulations for comparison
        """

        return self if self.pop > other_city.pop else other_city
        # Add code here

    def __str__(self):
        """
        Return a string representation for the City
        """
        # Add code here
        return f'{self.name}: [{self.x}, {self.y}]:({self.pop})'

