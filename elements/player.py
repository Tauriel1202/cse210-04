#Player Movement
#One class

from elements.element import Element
from utils.color import Color
from utils.point import Point


class Player(Element):
    
    def __init__(self):
        super().__init__()
        self._text  = "@"
        self._y_axis = 585 #the playes moves on X only
        self._color = Color(100,255,100)

    def get_y_asix(self):
        return self._y_axis

    def move_next(self, max_x):
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        self._position = Point(x, self._y_axis)
    
    def set_y_axis(self,y_axis):
        self._y_axis = y_axis