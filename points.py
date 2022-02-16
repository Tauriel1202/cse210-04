#Determines points
#One class

class Point:
    
    
    def __init__(self, x, y):
        
        self._x = x
        self._y = y

    def add(self, other):
        
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return Point(x, y)

    def equals(self, other):
        
        return self._x == other.get_x() and self._y == other.get_y()

    def get_x(self):
        
        return self._x

    def get_y(self):
        
        return self._y

    def scale(self, factor):
        
        return Point(self._x * factor, self._y * factor)
