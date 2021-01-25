from vertex import Vertex
from edge import Edge
from graphTree import GraphTree
from queue_list import Queue
from mst import MST
from shortestPathTree import ShortestPathTree
import sys

class Graph:    
    """
    This class represents a Graph, which has Vertices and Edges.    
    The Vertices are stored in a Python list: vertices
    The Edges are stored in vertex adjacency lists, which are
    kept in a dictionary where the key is the Vertex name and
    the adjacency list is the value.  The list contains the Edges.
    An additional dictionary is kept to retrieve the index 
    for a Vertex using the Vertex name as the key    
    """ 
    def __init__(self, vertices=None, edges=None):        
        """
        Creates a new, empty graph
        Instance variables:
           self.vertices: Python list
           self.neighbors_dict: Python dictionary of adj_lists
           self.vert_dict: Python dictionary of vertex indices
        """ 
               
        self.vertices = vertices 
        self.neighbors_dict = {}
        self.vert_dict = {}

        if vertices is not None:
        
            # Traverse vertices list to create two dictionaries:
            # self.neighbors_dict and self.vert_dict
            # where the key is the name of the vertex

            for index in range(len(self.vertices)):
                self.vert_dict[vertices[index].get_name()] = index
                self.neighbors_dict[vertices[index].get_name()] = []
            
            self.create_adj_lists(edges)

    def create_adj_lists(self, edges):
        """
        Using given edges, create an adjacency list for each vertex
        """
        
        for edge in edges:
            self.add_edge(edge) 
        
    def add_edge(self, edge): 
        """
        Adds a new edge to the graph 
        """
        
        name = edge.from_vertex.get_name()
        adj_list = self.neighbors_dict[name]
        adj_list.append(edge)
        
    def get_edge(self, from_vert, to_vert): 
        """
        Returns the edge in the graph having the supplied vertices
        """
        
        adj_list = self.get_neighbors(from_vert)
        
        for edge in adj_list:
            if edge.to_vertex.get_name() == to_vert.get_name():
                return edge
        return None
    
    def get_neighbors(self, vertex):
        """
        Return the adjacency list for vertex
        """
        
        return self.neighbors_dict[vertex.get_name()] 
    
    def get_vertices(self): 
        """
        Returns the list of all vertices in the graph. 
        """
        
        return self.vertices 
           
    def get_size(self):
        """
        Return the number of vertices in the graph
        """
        
        return len(self.vertices)
        
    def add_vertex(self, vertex):
        """
        Adds a vertex to the graph
        """
        
        self.vertices.append(vertex)
        self.vert_dict[vertex.get_name()] = len(self.vertices) - 1
        self.neighbors_dict[vertex.get_name()] = []
        
    def get_vertex(self, name):
        """
        Returns the vertex in the graph having the supplied name.
        """
        
        for vert in self.vertices:
            if vert.get_name() == name:
                return vert
        return None
        
    def get_vert_index(self, vertex):
        """
        Returns the index of the given vertex in the vertices list
        """
        
        return self.vert_dict[vertex.name]
            
    def __contains__(self, vertex): 
        """
        Determines if the given vertex is in the graph, 
        returning True or False.
        """
        
        for vert in self.vertices:
            if vert.get_name() == vertex.get_name():
                return True
        return False
        
    def get_degree(self, vertex):
        """
        Return the number of adjacent vertices
        """
        
        return len(self.get_neighbors(vertex))

    def df_search(self, vertex):
        """
        Returns the tree resulting in a depth-first-search 
        of the graph starting from the supplied vertex
        """
        
        # Create the search_order list for storing the
        # vertices visited during the traversal
        
        search_order = []
        
        # Create the parents list: initialize all vertices to None
        
        parents = [None] * len(self.vertices)
        
        # Create a vertex visited list: initialize to False
        
        has_visited = [False] * len(self.vertices)
 
        # Recursively search for the next vertex
        
        self.dfs(vertex, parents, search_order, has_visited)

        # Return the depth first search spanning tree
        
        return GraphTree(vertex, search_order, parents, self.vertices)
    
    def dfs(self, vertex, parents, search_order, has_visited):
        """
        Add the vertex to the search order list and 
        Find the next vertex to add 
        """
        
        # Add the vertex to the search_order list 
        # and update the has_visited list
        
        search_order.append(vertex)
        index = self.get_vert_index(vertex)
        has_visited[index] = True

        # Traverse the adjacency list for the vertex
        # To find the adjacent vertices
        
        adj_list = self.get_neighbors(vertex)
        for edge in adj_list:
        
            # Use recursion to go deeper when the other
            # end of the edge has not yet been visited
            
            neighbor = edge.to_vertex
            index = self.get_vert_index(neighbor)
            if not has_visited[index]:
            
                # The parent of neighbor is the vertex
                
                parents[index] = vertex

                # Recursive search
                
                self.dfs(neighbor, parents, search_order, has_visited)
    
    def bf_search(self, vertex):
        """
        Returns the tree resulting in a breadth-first-search 
        of the graph starting from the supplied vertex
        """
        
        # Create the search_order list for storing the 
        # vertices visited during the traversal
        
        search_order = []
        
        # Create the parents list: initialize all vertices to None
        
        parents = [None] * len(self.vertices)
    
        # Create a vertex visited list: initialize to False
        
        has_visited = [False] * len(self.vertices)

        # Create a queue for holding the vertices visited 
        # with traversal and add the vertex to the queue
        
        bfs_queue = Queue()
        bfs_queue.enqueue(vertex)
        
        # Retrieve the index for the vertex 
        # and mark it as been visited
        
        index = self.get_vert_index(vertex)
        has_visited[index] = True
        
        # Loop until each vertex added to the queue is gone
        
        while not bfs_queue.is_empty():
            
            # Add each vertex to the search_order as it is dequeued
            
            vert = bfs_queue.dequeue() 
            search_order.append(vert)
            
            # Traverse the edge adjacency list for this vertex
            # finding all adjacent vertices to this vertex
            
            for edge in self.get_neighbors(vert):
            
                # Place the found adjacent vertex on the queue 
                # if it has not been visited and update the
                # parent and has_visited lists
                
                index = self.get_vert_index(edge.to_vertex)
                if not has_visited[index]:
                
                    bfs_queue.enqueue(edge.to_vertex)
                    parents[index] = vert
                    has_visited[index] = True

        # Return the BFS spanning tree
        
        return GraphTree(vertex, search_order, parents, self.vertices)

    def get_min_spanning_tree(self, root):
        """
        Return MST rooted at a specified vertex 
        """
        
        # Create a cost list to store the weight of an edge,
        # that will be added to the MST
        
        # sys.maxsize is the largest possible number:
        # This simulates initializing the cost elements to infinity
        
        cost = [sys.maxsize] * len(self.vertices)
        
        # Create the parents list: initialize all vertices to None
        
        parents = [None] * len(self.vertices)
          
        # Cost for starting vertex is zero
        
        index = self.get_vert_index(root)
        cost[index] = 0 
        
        # Total weight of the MST
        
        total_weight = 0             

        # Create the search_order list to hold the vertices
        # as they are discovered for the MST
        
        search_order = []

        # Create the edges list to hold the edges
        # as they are discovered for the MST
        
        edges = []

        # Loop finding each best vertex for the MST based on cost
        # Until the search_order list has all the vertices
        # One vertex is added on each round
        
        while len(search_order) < self.get_size():
           
            current_min_cost = sys.maxsize

            # Loop through each vertex which is not already
            # added to the search_order list, and find the
            # smallest cost vertex to add to the list
               
            for i in range(self.get_size()):
               if (self.vertices[i] not in search_order and
                            (cost[i] < current_min_cost)):
                    current_min_cost = cost[i]
                    min_cost_index = i

            # Store the edges as they are discovered in edges list
            # If this new vertex is not the source_vertex
            # Create an edge to the found smallest cost vertex
            
            if current_min_cost != 0:
                edge = Edge(parents[min_cost_index],
                            self.vertices[min_cost_index], 
                            current_min_cost)
                edges.append(edge)

            # Add a new vertex to search_order and
            # the cost to the total weight

            search_order.append(self.vertices[min_cost_index])
            total_weight += cost[min_cost_index]

            # Adjust the cost list values for each vertex
            # that is adjacent to the minimum cost vertex
            # being added to search_order list
            
            # Traverse each edge in this new vertex's adjacency list
            
            adj_list = self.get_neighbors(self.vertices[min_cost_index])
            for edge in adj_list:

                # Get the index of the vertex on the other side of edge
                
                index = self.get_vert_index(edge.to_vertex)
                
                # If this vertex is not in the search_order and the 
                # cost is greater than the weight of the edge between 
                # the vertexes: Then lower its cost to the weight of 
                # the edge and add the new vertex as the parent of 
                # the vertex on the other side of the edge
                
                if (edge.to_vertex not in search_order and
                            (cost[index] > edge.get_weight())):
                    cost[index] = edge.get_weight()
                    parents[index] = self.vertices[min_cost_index]

        # Return the minimum spanning tree
        
        return MST(root, search_order, parents, self.vertices, 
                   edges, total_weight)

    def get_shortest_path(self, source_vertex):
        """
        Return the tree representing the single source shortest path         
        """
        
        # Create a cost list to store the cost of the path 
        # from a vertex to the source_vertex
        
        # sys.maxsize is the largest possible number:
        # This simulates initializing the cost elements to infinity
        
        cost = [sys.maxsize] * len(self.vertices)

        # Cost for source_vertex is zero
        
        index = self.get_vert_index(source_vertex)
        cost[index] = 0

        # Create the parents list: initialize all vertices to None
        
        parents = [None] * len(self.vertices)
        
        # search_order stores the vertices whose path found so far
        
        search_order = []

        # Create the edges list to hold the edges
        # as they are discovered for the path
        
        edges = []

        # Expand the search_order list
        
        while len(search_order) < self.get_size():

            # Initialize the minimum cost to the largest number
            
            current_min_cost = sys.maxsize

            # Loop through each vertex which is not already
            # added to the search_order list, and find the
            # smallest cost vertex to add to the list

            for i in range(self.get_size()):
                if (self.vertices[i] not in search_order and
                            (cost[i] < current_min_cost)):
                    current_min_cost = cost[i]
                    min_cost_index = i

            # If this new vertex is not the source_vertex
            # Create an edge to the found vertex
            
            if current_min_cost != 0:
                edge = Edge(parents[min_cost_index],
                            self.vertices[min_cost_index], 
                            current_min_cost)
                edges.append(edge)

            # Add the new vertex to the search_order list
            
            search_order.append(self.vertices[min_cost_index])

            # Adjust the cost list values for each vertex
            # that is adjacent to the minimum cost vertex
            # being added to search_order list

            # Traverse each edge in this new vertex's adjacency list
            
            adj_list = self.get_neighbors(self.vertices[min_cost_index])
            for edge in adj_list:

                # Get the index of the vertex on the other side of the edge
                
                index = self.get_vert_index(edge.to_vertex)
                
                # If this vertex is not in the search_order 
                # and the cost is greater than the cost of the new vertex's 
                # cost plus the weight of the edge between the vertexes
                # Then lower its cost to the cost of the new vertex plus
                # the weight of the edge and add the new vertex as the
                # parent of the vertex on the other side of the edge
                
                if (edge.to_vertex not in search_order and
                    (cost[index] > (cost[min_cost_index] + edge.get_weight()))):
                
                    cost[index] = cost[min_cost_index] + edge.get_weight()
                    parents[index] = self.vertices[min_cost_index]

        # Return the shortest path tree
        
        return ShortestPathTree(source_vertex, search_order, 
                                parents, self.vertices, edges, cost)
