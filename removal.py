from elements.player import Player

class Removal:
  #Removes objects when touched
  #player get the position of the player from the Player function
  #rock creates a rock
  #gem makes a gem

  def __init__(self):
    self._player = Player.set_position
    self._rock = 'o'
    self._gem = '*'
  
  def remove(self):
    if self._player == self._gem:
      self._gem -= 1
    elif self._player == self._rock:
      self._rock -= 1
    else:
      pass

  
