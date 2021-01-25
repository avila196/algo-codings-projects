import math
from edge import Edge
from comparable import Comparable

"""
Background to Find Direction of Travel:

If you are traveling:

Due East:  you are moving in the positive x direction
Due North: you are moving in the positive y direction
Due West:  you are moving in the negative x direction
Due South: you are moving in the negative y direction

From any point in a plane one can travel 360 degrees.
The 360 degrees can be divided into 4 quadrants of 90 degrees each.
The angles run from 0-90 degrees in a counter-clockwise direction
through each of the four quadrants defined below:
                                            
  a) East to North: called Quadrant I
  b) North to West: called Quadrant II
  c) West to South: called Quadrant III
  d) South to East: called Quadrant IV

The possible directions of travel are
  Quadrant I:   E, ENE, NE, NNE, N
  Quadrant II:  N, NNW, NW, WNW, W
  Quadrant III: W, WSW, SW, SSW, S
  Quadrant IV;  S, SSE, SE, ESE. E
  
The angle slices in these quadrants correspond to traveling in 
one of 16 directions:

Quadrant I (1):   [0.00, 11.25)  : 'E' 
                  [11.25, 33.75) : 'ENE' 
                  [33.75, 56.25) : 'NE'
                  [56.25, 78.75) : 'NNE' 
                  [78.75, 90.0)  : 'N' 
Quadrant II (2):  [0.00, 11.25)  : 'N', 
                  [11.25, 33.75) : 'NNW' 
                  [33.75, 56.25) : 'NW'
                  [56.25, 78.75) : 'WNW'
                  [78.75, 90.0)  : 'W' 
Quadrant III (3): [0.00, 11.25)  : 'W' 
                  [11.25, 33.75) : 'WSW' 
                  [33.75, 56.25) : 'SW'
                  [56.25, 78.75) : 'SSW' 
                  [78.75, 90.0)  : 'S' 
Quadrant IV (4):  [0.00, 11.25)  : 'S'
                  [11.25, 33.75) : 'SSE'
                  [33.75, 56.25) : 'SE'
                  [56.25, 78.75) : 'ESE'
                  [78.75, 90.0)  : 'E'

To determine the quadrant, you need to know the relative 
positions between x1 and x2 and between y1 and y2
  a) Quadrant I:  (x1 <  x2 & y1 <= y2) 
  b) Quadrant II: (x1 >= x2 & y1 <  y2) 
  c) Quadrant III:(x1 >  x2 & y1 >= y2)
  d) Quadrant IV: (x1 >= x2 & y1 >  y2)
  
To find the direction of travel, you need to find an angle
between the line from P1 to P2 and either

  a) a line parallel to the x-axis OR
  b) a line parallel to the y-axis

In order to find the angle A in radians, which is the angle between 
the line from P1 to P2, and the line parallel to either the x-axis for
Quadrants I and III or the y-axis for Quadrants II and IV, you need 
to use:

angle_A = arctan((y2-y1) / (x2-x1))

The Python math library has a function for this

angle_A  = math.atan ((y2-y1) / (x2-x1))
 
This gives the angle in radians. You must convert the angle to degrees.

Use the Python math library function:

angle_A_deg = math.degrees (angle_A)

If the direction is in Quadrants II or IV, then add 90 degrees. 

To compute the distance, use the distance formula
  
distance = SQRT [(x2-x1)**2 + (y2-y1)**2]
    
The Python math library has a function for this

distance = math.sqrt ((x2-x1)**2 + (y2-y1)**2) 
"""
class Road(Edge, Comparable):
    """
    This class represents a Road on a map (Graph) 
    """
    def __init__(self, from_city, to_city):
        """
        Creates a new Road
        New Instance variables:
            self.direction: str
        Set Edge instance variable:
            self weight: float
            This is the distance stored in miles
        Call the method comp_direction to set 
             the direction and weight (in miles)    
        """
        
        super().__init__(from_city, to_city)
        direction, distance = self.comp_direction()
        
        self.direction = direction
        self.weight = distance
        
    def get_direction(self):
        """
        Return the direction set in the constructor
        """
        return self.get_direction()
        # Add code here

    def comp_direction(self):
        """
        Compute and return the direction of the Road
        and the distance between the City vertices
        Note: Do NOT round any values (especially GPS) in this method,
	      we want them to have their max precision.
              Only do rounding when displaying values
        This is called in the constructor
        """
        # Get the points from the GPS coordinates of each City
        # These are in degrees, change to radians
        x1 = self.from_vertex.get_X()
        y1 = self.from_vertex.get_Y()
        x2 = self.to_vertex.get_X()
        y2 = self.to_vertex.get_Y()
        ## Add code here

        # Given the x and y coordinates of P1 and P2,
        # find the quadrant in which the angle exists

        ## Add code here
        quadrant = self.find_quadrant(x1, y1, x2, y2)
        # Given the x and y coordinates of P1 and P2 and the quadrant,
        # find the angle between the x or y axis and the line from P1 to P2.
        # Return the angle in degrees

        ## Add code here
        angle = self.compute_angle(x1, y1, x2, y2, quadrant)
        # Using the angle and quadrant, find the direction
        # This function must use a dictionary

        ## Add code here
        direction = self.compute_direction(angle, quadrant)
        # Find the distance between the points P1 and P2
        # Convert the distance to miles and return it

        ## Add code here
        distance = self.distance(x1,y1,x2,y2)
        dist_miles = distance * 3956
        return direction, dist_miles

    def find_quadrant(self, x1, y1, x2, y2):
        """
        a) Quadrant I:   when x2 >  x1 and y2 >= y1
        b) Quadrant II:  when x2 <= x1 and y2 >  y1
        c) Quadrant III: when x2 <  x1 and y2 <= y1
        d) Quadrant IV:  when x2 >= x1 and y2 <  y1
        """
        if x2 > x1 and y2 >= y1:
            return 1
        elif x2 <= x1 and y2 > y1:
            return 2
        elif x2 < x1 and y2 <= y1:
            return 3
        elif x2 >= x1 and y2 < y1:
            return 4
        else:
            pass
        # Add code here

    def distance(self, x1, y1, x2, y2):
        """
        Use distance formula to find length of line from P1 to P2
        """
        distance = math.sqrt((x2 - x1)**2 + (y2-y1)**2)
        return distance
        # Add code here

    def compute_angle(self, x1, y1, x2, y2, quadrant):
        """
        Use the trig formula: atan = (y2-y1) / (x2-x1)
        Convert radians to degrees
        """
        if x1 == x2:
            angleDeg = 90
        else:
            angleRad = math.atan( (y2 - y1) / (x2 - x1) )
            angleDeg = math.degrees(angleRad)

        if quadrant in [2, 4]:
            angleDeg += 90
        return angleDeg
        # Add code here

    def compute_direction(self, angle, quadrant):
        """
        Create a dictionary for each quadrant that holds the angle slices
        for each direction.  The key is a 2-tuple holding the degrees
        (low, high) of the angle slices, and the value is the direction
        """
        angleToDir2 = {
                (0, 11.25): "N",
                (11.25, 33.75): "NWN",
                (33.75, 56.25): "NW",
                (56.25, 78.75): "WNW",
                (78.75, 90): "W"
            }
        angleToDir1 = {
                (0, 11.25): "E",
                (11.25, 33.75): "ENE",
                (33.75, 56.25): "NE",
                (56.25, 78.75): "NEN",
                (78.75, 90): "N"
            }
        angleToDir3 = {
                (0, 11.25): "W",
                (11.25, 33.75): "WSW",
                (33.75, 56.25): "SW",
                (56.25, 78.75): "SWS",
                (78.75, 90): "S"
            }
        angleToDir4 = {
                (0, 11.25): "S",
                (11.25, 33.75): "SES",
                (33.75, 56.25): "SE",
                (56.25, 78.75): "ESE",
                (78.75, 90): "E"
            }
        if quadrant == 1:
            angleToDir = angleToDir1
        elif quadrant == 2:
            angleToDir = angleToDir2
        elif quadrant == 3:
            angleToDir = angleToDir3
        elif quadrant == 4:
            angleToDir = angleToDir4
        else:
            raise Exception("Illegal argument {} for 'quadrant': must be between 1 and 4 inclusive".format(quadrant))

        for slice in angleToDir:
            if slice[0] <= angle < slice[1]:
                return angleToDir[slice]

        raise Exception("No corresponding direction for {} degrees in quadrant {}".format(angle, quadrant))

        # Add code here


    def __str__(self):
        """
        Return road information as a string
        """
        return str(self.from_vertex) + " to " + str(self.to_vertex) + " traveling " + self.direction + " for " + str(self.weight) + "miles"
        # Add code here
