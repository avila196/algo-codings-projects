from graph import Graph


class CityRoadMap(Graph):
    """
    This class represent a Graph with City Vertices and Road Edges.
    """

    def __init__(self, cities=None, roads=None):
        """
        Construct a CityRoadMap Graph
        using Cities and Roads stored in lists
        """
        if cities is None or roads is None:
            super().__init__()
        else:
            super().__init__(cities, roads)

    def get_neighboring_cities(self, city):
        """
        Return the City neighbors of the City Vertex as a list
        """
        
        # Add code here
        city_list = super().get_neighbors(city)
        return city_list

    def get_roads_str(self):
        """
        Create string of Cities and
        Roads with distances and direction
        """
        roads_str = ""

        # Add code here
        cities = super().get_vertices()
        for city in cities:
            roads = super().get_neighbors(city)
            roads_str += "[ " + city.get_name() + " ]:\n"
            for road in roads:
                roads_str += "  "+road.__str__()+"\n"
            roads_str += "\n"
                
        return roads_str

    def get_cities_str(self):
        """
        Create string of Cities with GPS coordinates and population
        """
        
        cities_str = ""
        
        cities = super().get_vertices()
        for city in cities:
            cities_str += city.__str__() + "\n"
            

        # Add code here

        return cities_str
