import random, pygame

class Food:

  def __init__(self, cell_size, win_width, win):
    self.cell_size = cell_size
    self.spawn_points = [x for x in range(win_width) if x % cell_size == 0]
    self.x = random.choice(self.spawn_points)
    self.y = random.choice(self.spawn_points)
    self.win = win

  def replace(self):
    self.x = random.choice(self.spawn_points)
    self.y = random.choice(self.spawn_points)
  
  def draw(self):
    pygame.draw.rect(self.win, (214, 32, 32), pygame.Rect(self.x, self.y, self.cell_size, self.cell_size))
    pass