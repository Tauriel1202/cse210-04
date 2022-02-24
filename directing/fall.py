
import random
from elements.element import Element
from utils.color import Color
from utils.keyboard_service import KeyboardService
from utils.point import Point
from utils.video_service import GenericVideoService


class Fall:

    def __init__(self,keyboard,video,player):
        self._elements = []
        self._width = video.get_width()
        self._enemies = ['O','X','&','8','D','S'] 
        self._video = video
        self._keyboard = keyboard
        self._player = player
        self._points = 10
        self._score  = Element()

    def set_enemies(self,enemies):
        if len(enemies) < 2:
            raise Exception("You need to pass more enemies")
        self._enemies = enemies

    def _kind_of_enemy(self):
        key = random.randint(0,len(self._enemies) -1)
        return self._enemies[key]


    def start_fall(self):
        self._video.open_window()
        self._populate_fall()
        while self._video.is_window_open():
            self._get_inputs()
            self._do_updates()
            self._fall()
            self._do_outputs()
        self._video.close_window()
    
    def _populate_fall(self):
        max_enemies = int(self._width  / self._video.get_cell_size())
        for enemy in range(max_enemies):
            y= random.randint(0,int(self._video.get_height()/2))
            #if first and second:
            element  = Element()
            position = Point(enemy*(self._video.get_cell_size()),y)
            element.get_color().random()
            element.set_position(position)
            element.set_text(self._kind_of_enemy())
            if random.choice([True,False]):
                self._elements.append(element)
        
    def _get_inputs(self):
        velocity = self._keyboard.get_direction()
        self._player.set_velocity(velocity)

    def _do_updates(self):
        max_x = self._video.get_width()
        max_y = self._video.get_height()
        self._player.move_next(max_x)
        self._score.set_color(Color(255,255,255))
        self._score.set_position(Point(15,0))
        self._score.set_text(f"Score:{self._points}")
        if len(self._elements)<= 10:
            self._populate_fall()

    def _do_outputs(self):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video.clear_buffer()
        enemies = [None] * len(self._elements)
        for i in range(0,len(self._elements)):
            enemies[i] = self._elements[i]

        enemies.append(self._player)
        enemies.append(self._score)
        self._video.draw_actors(enemies)
        self._video.flush_buffer()

    def _fall(self):
        for i in range(0,len(self._elements)):
            #transform element
            down = random.choice([False,True,False])
            if down:  
                y_axys = random.choice([2,4,6])
                point = Point(0,y_axys)
                try:
                    if self._player.get_position().in_zone(self._elements[i].get_position(),10):
                        if self._elements[i].get_text() == 'X':
                            self._points += 1
                            print("X")
                            self._elements.pop(i)
                        else:
                            self._points -= 1
                            self._elements.pop(i)
                            print("O")
                
                    if(self._elements[i].get_position().get_y() >= self._video.get_height()):
                        point = Point(0,-self._video.get_height()) 
                        self._elements[i].set_text(self._kind_of_enemy())                 
                    position = point.add(self._elements[i].get_position())
                    self._elements[i].set_position(position)
                except IndexError:
                    print(":(")
                
                
