import random, pygame

class Snake:

  def __init__(self, cell_size, win_width, win):
    self.x = 200
    self.y = 200
    self.body = []
    self.length = 2
    self.direction = 0
    self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    self.cell_size = cell_size
    self.win = win
    self.win_width = win_width

  def change_direction(self, turn):
    if(turn == "FORWARD"):
      pass
    elif(turn == "RIGHT"):
      if(self.direction == 0):
        self.direction = 2
      elif(self.direction == 2):
        self.direction = 1
      elif(self.direction == 1):
        self.direction = 3
      elif(self.direction == 3):
        self.direction = 0
    elif(turn == "LEFT"):
      if(self.direction == 0):
        self.direction = 3
      elif(self.direction == 3):
        self.direction = 1
      elif(self.direction == 1):
        self.direction = 2
      elif(self.direction == 2):
        self.direction = 0

  def move(self):
    if self.direction == 0:
      self.y -= self.cell_size
    elif self.direction == 1:
        self.y += self.cell_size
    elif self.direction == 2:
        self.x += self.cell_size
    elif self.direction == 3:
        self.x -= self.cell_size

  def update_body(self):
      if len(self.body) > self.length:
          self.body.pop(0)
      self.body.append((self.x, self.y))
  
  def draw(self):
    for x in self.body:
            pygame.draw.rect(self.win, self.color, pygame.Rect(x[0], x[1], self.cell_size, self.cell_size))