import pygame, time, os, random

WIN_WIDTH = 500
WIN_HEIGHT = 500
BLOCK_SIZE = 25
SPAWN_POINTS = [x for x in range(500) if x % BLOCK_SIZE == 0]

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Snake")

class Snake():
    def __init__(self, x ,y):
        self.x = x
        self.y = y
        self.direction = 0
        self.length = 0
        self.snake_body = []
        self.dead = False
        self.food_x, self.food_y = random.choice(SPAWN_POINTS), random.choice(SPAWN_POINTS)
    
    def draw(self, win):
        for x in self.snake_body:
            pygame.draw.rect(win, (49, 189, 86), pygame.Rect(x[0], x[1], BLOCK_SIZE, BLOCK_SIZE))

    def change_direction(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction = 0
        elif keys[pygame.K_DOWN]:
            self.direction = 1
        elif keys[pygame.K_RIGHT]:
            self.direction = 2
        elif keys[pygame.K_LEFT]:
            self.direction = 3 
    
    def move(self):
        if self.direction == 0:
            self.y -= BLOCK_SIZE
        elif self.direction == 1:
            self.y += BLOCK_SIZE
        elif self.direction == 2:
            self.x += BLOCK_SIZE
        elif self.direction == 3:
            self.x -= BLOCK_SIZE
        if self.y >= 500:
            self.y = 0
        elif self.y < 0:
            self.y = 500
        elif self.x >= 500:
            self.x = 0
        elif self.x < 0:
            self.x = 500
    
    def update_body(self):
        for x in self.snake_body:
            if (x[0], x[1]) == (self.x, self.y):
                self.dead = True
        if len(self.snake_body) > self.length:
            self.snake_body.pop(0)
        snake_head = (self.x, self.y)
        self.snake_body.append(snake_head)

    def spawn_food(self, win):
        pygame.draw.rect(win, (214, 32, 32), pygame.Rect(self.food_x, self.food_y, BLOCK_SIZE, BLOCK_SIZE))

    def eat_food(self):
        if (self.x, self.y) == (self.food_x, self.food_y):
            self.food_x, self.food_y = random.choice(SPAWN_POINTS), random.choice(SPAWN_POINTS)
            self.length += 1

def draw_window(win, snake):
    win.fill((0, 0, 0))
    snake.draw(win)
    snake.spawn_food(win)
    pygame.display.update()

def main():
    snake = Snake(200, 200)
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if snake.dead == True:
            run = False
        snake.eat_food()
        snake.change_direction()
        snake.update_body()
        draw_window(WIN, snake)
        snake.move()

        
    pygame.quit()

main()
