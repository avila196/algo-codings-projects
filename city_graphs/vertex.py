class Vertex():
    """
    This class represents the Vertex for a Graph.
    The instance variables are:
        name: str
    """

    def __init__(self, name):
        """
        Create a vertex object with the passed in name 
        """
        
        self.name = name
        
    def get_name(self):
        """
        Return the vertex name
        """
        
        return self.name
                        
    def __str__(self):
        """
        Returns a string representation of this Vertex
        """
        
        return str(self.name)
