
from utils.point import Point
from utils.color import Color

class Element:
    
    def __init__(self):
        self._text = "O"
        self._font_size = 15
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)
        self._color = Color(255,255,100)


    def get_color(self):
        return self._color

    def set_color(self,color):
        self._color = color

    def get_font_size(self):
        return self._font_size

    def get_position(self):
        return self._position
    
    def get_text(self):
        return self._text

    def get_velocity(self):
        return self._velocity
    
    def set_position(self, position):
        self._position = position
    
    def set_font_size(self, font_size):
        self._font_size = font_size
    
    def set_text(self, text):
        self._text = text

    def set_velocity(self, velocity):
        self._velocity = velocity
