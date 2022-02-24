class Point:
    """A class that represent a point in the screen. 
    
    Attributes:
        _x (int): x-coordinate
        _y (int): y-coordinate
    """ 
    
    def __init__(self, x, y):

        """Constructs a new Point
            Args:
             x (int): x-coordinate
             y (int): y-coordinate
        """
        self._x = x
        self._y = y

    def add(self, point):
        """Adds the current point and one that is passed as an argument
        Args:
            other (Point): The Point to add.

        Returns:
            Point: A new Point that is the sum.
        """
        x = self._x + point.get_x()
        y = self._y + point.get_y()
        return Point(x, y)

    def equals(self, point):
        """Checks if the point share the same position on the screen

        Args:
            point (Point): The Point to compare.

        Returns: 
            boolean: True if both x and y are equal; false if otherwise.
        """
        return self._x == point.get_x() and self._y == point.get_y()

    def get_x(self):
        """Gets the horizontal distance.
        
        Returns:
            integer: The horizontal distance.
        """
        return self._x

    def get_y(self):
        """Gets the vertical distance.
        
        Returns:
            integer: The vertical distance.
        """
        return self._y

    def scale(self, factor):
        """
        Scales the point by the provided factor.

        Args:
            factor (int): The amount to scale.
            
        Returns:
            Point: A new Point that is scaled.
        """
        return Point(self._x * factor, self._y * factor)

    def in_zone(self,point,radius):
        if(self._x == point.get_x() and self._y == point.get_y()):
            return True
        
        if (self._x in  range(point.get_x() - radius, point.get_x() + radius)) and (self._y in  range(point.get_y() - int(radius/2), point.get_y() + int(radius/2))) :
            
            return True
        return False

        

