#Main game play

import os
import random

from directing.fall import Fall
from elements.player import Player
from utils.keyboard_service import KeyboardService
from utils.video_service import GenericVideoService



def main():
   
    video = GenericVideoService('Greed')
    keyboard = KeyboardService()
    player = Player()
    fall = Fall(keyboard,video,player)
    fall.start_fall()
    

if __name__ == "__main__":
    main()
