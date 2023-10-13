import random, pygame, math

def distance(x1,y1,x2,y2):
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)

class Snake:

  def __init__(self, cell_size, win_width, win):
    self.x = 200
    self.y = 200
    self.body = []
    self.length = 0
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

  def eyes(self, food):
    output = []
    if self.direction == 0:
      #forward
      output.append(self.y - food.y)
      #right
      output.append(food.x - self.x)
      #left
      output.append(self.x - food.x)
      #forward right
      if food.y <= self.y and food.x >= self.x:
          output.append(distance(food.x, food.y, self.x, self.y))
      else:
         output.append(-distance(food.x, food.y, self.x, self.y))
      #forward left
      if food.y <= self.y and food.x <= self.x:
         output.append(distance(food.x, food.y, self.x, self.y))
      else:
         output.append(-distance(food.x, food.y, self.x, self.y))
      return output
    
    if self.direction == 1:
      #forward
      output.append(food.y - self.y)
      #right
      output.append(food.x - self.x)
      #left
      output.append(self.x - food.x)
      #forward right
      if food.y >= self.y and food.x >= self.x:
         output.append(distance(food.x, food.y, self.x, self.y))
      else:
         output.append(-distance(food.x, food.y, self.x, self.y))
      #forward left
      if food.y >= self.y and food.x <= self.x:
          output.append(distance(food.x, food.y, self.x, self.y))
      else:
         output.append(-distance(food.x, food.y, self.x, self.y))
      return output

    if self.direction == 2:
      #forward
      output.append(food.x - self.x)
      #right
      output.append(food.y - self.y)
      #left
      output.append(self.y - food.y)
      #forward right
      if food.x >= self.x and food.y >= self.y:
          output.append(distance(food.x, food.y, self.x, self.y))
      else:
        output.append(-distance(food.x, food.y, self.x, self.y))
      #forward left
      if food.x >= self.x and food.y <= self.y:
          output.append(distance(food.x, food.y, self.x, self.y))
      else:
        output.append(-distance(food.x, food.y, self.x, self.y))
      return output

    if self.direction == 3:
      #forward
      output.append(self.x - food.x)
      #right
      output.append(self.y - food.y)
      #left
      output.append(food.y - self.y)
      #forward right
      if food.x <= self.x and food.y <= self.y:
          output.append(distance(food.x, food.y, self.x, self.y))
      else:
        output.append(-distance(food.x, food.y, self.x, self.y))
      #forward left
      if food.x <= self.x and food.y >= self.y:
          output.append(distance(food.x, food.y, self.x, self.y))
      else:
        output.append(-distance(food.x, food.y, self.x, self.y))
      return output