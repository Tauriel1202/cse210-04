#Player Movement
#One class

from points import Point


class Player:
    
    def __init__(self):
        self._text = "#"
        self._font_size = 15
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)
        self._y_axis = 0 #the playes moves on X only
    

    def get_font_size(self):
        return self._font_size

    def get_position(self):
        return self._position
    
    def get_text(self):
        return self._text

    def get_velocity(self):
        return self._velocity
    
    def get_y_asix(self):
        return self._y_axis

    def move_next(self, max_x):
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        self._position = Point(x, self._y_axis)
    
    def set_position(self, position):
        self._position = position
    
    def set_font_size(self, font_size):
        self._font_size = font_size
    
    def set_text(self, text):
        self._text = text

    def set_velocity(self, velocity):
        self._velocity = velocity

    def set_y_axis(self,y_axis):
        self._y_axis = y_axis