import pygame, time, os, random, neat, math

max_length = 1

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
        self.length = 2
        self.snake_body = []
        self.dead = False
        self.food_x, self.food_y = random.choice(SPAWN_POINTS), random.choice(SPAWN_POINTS)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.food_distance = distance(self.x, self.y, self.food_x, self.food_y)
    
    def draw(self, win):
        for x in self.snake_body:
            pygame.draw.rect(win, self.color, pygame.Rect(x[0], x[1], BLOCK_SIZE, BLOCK_SIZE))

    def change_direction(self, direction):
        if direction == 0:
            self.direction = 0
        elif direction == 1:
            self.direction = 1
        elif direction == 2:
            self.direction = 2
        elif direction == 3:
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
    
    def update_body(self):
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
            return True

def draw_window(win, snake):
    snake.draw(win)
    snake.spawn_food(win)

def distance(x1,y1,x2,y2):
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def remove(index):
    snakes.pop(index)
    ge.pop(index)
    nets.pop(index)
    
def detect_colision(index, snake):
    if snake.x < 0:
        ge[index].fitness -= 10
        remove(index)
    elif snake.x > WIN_WIDTH:
        ge[index].fitness -= 10
        remove(index)
    elif snake.y < 0:
        ge[index].fitness -= 10
        remove(index)
    elif snake.y > WIN_HEIGHT:
        ge[index].fitness -= 10
        remove(index)
    for x in snake.snake_body:
        if (x[0], x[1]) == (snake.x, snake.y):
            ge[index].fitness -= 1
            remove(index)

def eval_genomes(genomes, config):

    global snakes, ge, nets, max_length


    snakes = []
    ge = []
    nets = []

    for genome_id, genome in genomes:
        snakes.append(Snake(200,200))
        ge.append(genome)
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        genome.fitness = 0

    clock = pygame.time.Clock()


    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        WIN.fill((0, 0, 0))

        if len(snakes) == 0:
            break

        for i, snake in enumerate(snakes):
            ge[i].fitness -= 0.01
            if(snake.length > max_length):
                max_length = snake.length
            print(max_length)
            if(distance(snake.x, snake.y, snake.food_x, snake.food_y) < snake.food_distance):
                ge[i].fitness += 1
            # else:
            #     ge[i].fitness -= 1
            snake.food_distance = distance(snake.x, snake.y, snake.food_x, snake.food_y)
            draw_window(WIN, snake)
            if(snake.eat_food()):
                ge[i].fitness += 100
            output = nets[i].activate((snake.x, 
                                    snake.y, 
                                    distance(snake.x, snake.y, snake.food_x, snake.food_y)))
            # if snake.direction == 0 and output.index(max(output)) == 1 or snake.direction == 1 and output.index(max(output)) == 0:
            #     ge[i].fitness -= 10
            #     snake.change_direction(snake.direction)
            # elif snake.direction == 2 and output.index(max(output)) == 3 or snake.direction == 3 and output.index(max(output)) == 2:
            #     ge[i].fitness -= 10
            #     snake.change_direction(snake.direction)
            # else:
            snake.change_direction(output.index(max(output)))
            detect_colision(i, snake)
            snake.update_body()
            snake.move()
            pygame.display.update()

        clock.tick(60)
        pygame.display.update()

def run(config_path):
    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path)

    pop = neat.Population(config)
    pop.run(eval_genomes, 1000)


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")
    run(config_path)
