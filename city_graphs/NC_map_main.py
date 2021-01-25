"""
This is the mainline logic for running commands
for a Graph of City and Road objects
"""
import csv
from cityRoadMap import CityRoadMap
from road import Road
from city import City

def main():

    # Constants for file names and records
    
    COMMAND_FILE = "Commands.txt"
    OUTPUT_FILE = "NCRoutesOut.txt"

    # Create an output File writer for writing the processing results
    
    writer = open(OUTPUT_FILE, 'w')

    # Open and Read file containing the commands to be processed
    
    cmd_file = open(COMMAND_FILE, 'r')
    file_lines = csv.reader(cmd_file, delimiter=':')
    commands = list(file_lines)
    cmd_file.close()

    print("Begin NC Routes Program ")

    # Use build_map function to create empty CityRoadMap object, and 
    # return the graph and the output message etring
    # You need to pass this pass to process_cmd

    city_road_map, msg = build_map()

    msg = msg + '\n'

    # Loop for each line in the Command File and process it
    # The command output is placed in the result String
    
    for cmd_line in commands:
        msg += process_cmd(cmd_line, city_road_map)
    writer.write(msg)

    print("End NC Routes Program ")

    writer.close()

def process_cmd(cmd_list, city_road_map):

    cmd = cmd_list[0].strip().lower()

    # Echo the command
    
    result = "Command: " + cmd.upper() + "\n"

    if cmd == "PrintMap".lower():
        map_str = city_road_map.get_roads_str()
        result += map_str
        ## Add in code here
    
    elif cmd == "PrintCities".lower(): 
        cities_str = city_road_map.get_cities_str()
        result += cities_str
        ## Add in code here 
    
    elif cmd == "DFSMap".lower():
        root_name = cmd_list[1].strip()
        dest_name = cmd_list[2].strip()
        result += dfs(city_road_map,root_name,dest_name)
        ## Add in code here 
    
    elif cmd == "BFSMap".lower():
        root_name = cmd_list[1].strip()
        result += bfs(city_road_map,root_name)
    
        ## Add in code here 
    
    elif cmd == "MSTMap".lower(): 
        root_name = cmd_list[1].strip()
        result += mst(city_road_map,root_name)
        ## Add in code here 
    
    elif cmd == "ShortPathMap".lower():
    
        if city_road_map is not None:
            num_args = len(cmd_list)
            root = cmd_list[1].strip()
            dest = None
            if num_args == 3:
                dest = cmd_list[2].strip()
                
            result += shortest_path(city_road_map, root, dest)

    elif cmd == "SortCities".lower():
        result += sort_cities(city_road_map)
        
        ## Add in code here
        
    
    else:
        result += "Unknown command."

    return result

"""
Build CityRoadMap graph object
from the CITY and ROAD records in a file

Note: Do NOT round any values (especially GPS) here, 
      we want them to have their max precision.
      Only do rounding when displaying values
"""
def build_map():

    print("Entering build map")

    CITY_REC = "CITY"
    ROAD_REC = "ROAD"
    NCMAP_FILE = "NCRoadMap.csv"

    # Start message about City and Roads processed

    msg = ""

    # Create lists for holding Graph information and a dictionary
    # that maps the City name to its index in cities. This 
    # city_dict dictionary is filled in while processing the City 
    # records and is used while processing the Road records in 
    # order to retrieve the City-Vertex to pass to the Road constructor

    cities = []
    roads = []
    city_dict = {}
    city_index = 0
    road_index = 0

    # Read in Road Map information from NCMAP_FILE using CSV reader
    #     Loop: Read each line in NCMAP_FILE:
    #     The first field has either CITY or ROAD to distinguish 
    #     the record type
    #     The remaining fields are used to create the 
    #     City or Road objects
    #     Append each city to the cit

    cmd_file = open(NCMAP_FILE, 'r')
    file_lines = csv.reader(cmd_file, delimiter=',')
    lines = list(file_lines)
    cmd_file.close()
    
    for line in lines:
        if line[0] == CITY_REC:
            city = City(line[1], float(line[2]), float(line[3]), int(line[4]))
            cities.append(city)
            city_dict[line[1]] = city
        if line[0] == ROAD_REC:
            from_city = city_dict[line[1]]
            to_city = city_dict[line[2]]
            road = Road(from_city,to_city)
            roads.append(road)
    
    ## Add in much code here

    
    # Add the processing message to the String result to return
    
    msg += "Processed {} Cities and {} Roads \n".format(city_index, road_index)

    # Build a road_map CityRoadMap graph object of the cities and roads
    
    city_road_map = CityRoadMap(cities, roads)

    return city_road_map, msg

"""
Depth first search:
Starting Node : root_name
Destination Node: dest_name
"""
def dfs(city_road_map, root_name, dest_name):
    
    msg = ""
    
    # Retrieve the starting vertex from the root city name

    root = city_road_map.get_vertex(root_name)
    ## Add in code here

    # Call the DFS graph method, which returns a DFS tree 
    # containing the DFS order of the vertices, starting with root

    graph_tree = city_road_map.df_search(root)
    ## Add in code here

    
    # Retrieve the City search order and Number of Cities
    
    cities = graph_tree.get_search_order()
    num_cities = len(cities)
    ## Add in code here

    
    # Output the number of Cities found and root name

    msg = str(num_cities) + " cities are searched in this DFS order"
    msg += " starting from " + root_name + "\n"

    # Loop through the search order list
    # Output each city name: only display 5 cities per line
    
    i = 0
    for j in range(len(cities)):
        if i <= 4 and j != 51:
            msg += cities[j].get_name() + ", "
            i += 1
        else:
            msg += cities[j].get_name() + "\n"
            i = 0
    ## Add in code here
 
    # Output to msg the DFS Path of Roads From Root
    
    msg += "\nRoot is "+root_name+"\n"  
    msg += graph_tree.get_edge_str()
    ## Add in code here
    
    # Retrieve the dest vertex from the dest name
    
    dest = city_road_map.get_vertex(dest_name)
    ## Add in code here

    # Output to msg the DFS Path of Cities From Root to Dest

    msg += graph_tree.get_path_str(dest)+"\n"
    ## Add in code here
    
    return msg

"""
Breadth first search:
Starting Node : root_name
"""
def bfs(city_road_map, root_name):
    
    msg = ""
    
    # Retrieve the starting vertex from the root city name

    root = city_road_map.get_vertex(root_name)
    ## Add in code here
    
    # Call the BFS method, which returns a BFS tree containing
    # the BFS order of the vertices, starting with root
    
    graph_tree = city_road_map.bf_search(root)
    ## Add in code here
    
    # Retrieve the City search order and Number of Cities

    cities = graph_tree.get_search_order()
    num_cities = len(cities)
    ## Add in code here
    
    # Output to msg the number of Cities found and root name

    msg = str(num_cities) + " cities are searched in this BFS order"
    msg += " starting from " + root_name + "\n"

    # Loop through the search order list
    # Output each city name: only display 5 cities per line

    i = 0
    for j in range(len(cities)):
        if i <= 4 and j != 51:
            msg += cities[j].get_name() + " : "
            i += 1
        else:
            msg += cities[j].get_name() + "\n"
            i = 0
    ## Add in code here
    
    
    # Output to msg the parents of the vertices found using BFS order
    # of cities starting with root

    msg += "\nThe parents of cities searched in BFS order:"
    for city in cities[1:]:
        msg += city.get_name() + " has a parent " + graph_tree.get_parent(city).get_name()+"\n"
    msg += "\n"
    ## Add in code here

    
    return msg

"""
Minimum Spanning Tree:
Starting Node : root_name
"""
def mst(city_road_map, root_name):

    msg = ""
    
    # Retrieve the starting vertex from the root city name

    root = city_road_map.get_vertex(root_name)
    ## Add in code here
       
    # Call the MST method, which returns an MST containing
    # the MST order of the vertices, starting with root

    mst = city_road_map.get_min_spanning_tree(root)
    ## Add in code here

    # Output to msg root, total weight and mst edge str
    
    msg += "Root is " + root_name+"\n"
    msg += "Total Weight of MST: " + str(mst.get_total_weight())+"\n"
    msg += mst.get_mst_edge_str()+"\n"
    ## Add in code here
           
    
    return msg

"""
ShortestPath Tree:
Starting Node : root_name
"""
def shortest_path(city_road_map, root_name, dest_name):

    msg = ""
    
    # Retrieve the starting vertex from the root city name

    root = city_road_map.get_vertex(root_name)
    ## Add in code here

    
    # Call the get_shortest_path method, which returns a short path tree
    # containing all the shortest paths from root to each other city

    sp_tree = city_road_map.get_shortest_path(root)
    ## Add in code here

    
    # If destination is None,
    # Output to msg the Shortest Path from root to all Cities

    if dest_name is None:
        msg += "Root is " + root_name + "\n"
        msg += sp_tree.get_all_paths_str() + "\n"
    ## Add in code here

    
    # Else Print the Shortest Path from root to destination city
    
    else:
        dest = city_road_map.get_vertex(dest_name)
        msg += sp_tree.get_path_str(dest)+"\n"
    ## Add in code here

    
    return msg
        
"""
Sort the cities by population and display them
"""
def get_key(city):
    return city.get_pop()

def sort_cities(city_road_map):

    # Message to return

    msg = ""

    
    ## Add in code here

    cities = city_road_map.get_vertices()
    cities.sort(key = get_key)

    # Output to msg each City object information
    
    for city in cities:
        msg += city.__str__()+"\n"
    ## Add in code here

    
    return msg

main() 
