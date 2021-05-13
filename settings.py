class Settings:
  """A class to store all settings for Alien Invasion."""
  def __init__(self):
    """Initialize the game's settings."""
    # Screen settings
    self.screen_width = 1200
    self.screen_height = 800
    self.bg_color = (180, 200, 230)
    self.bullets_allowed = 6
   
    #Bullet Settings
    self.bullet_speed = 5.0
    self.bullet_width = 600
    self.bullet_height = 20
    self.bullet_color = (230, 230, 230)

    #Ship settings
    self.ship_speed = 10.0
    self.ship_limit = 3

    #Alien settings
    self.alien_speed = 10.0
    self.fleet_drop_speed = 10
    #fleet _direction of 1 represents rights; -1 represents left.
    self.fleet_direction = 1