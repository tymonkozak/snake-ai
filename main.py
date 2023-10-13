import pygame, neat, math, os
from snake import Snake
from food import Food


WIN_WIDTH = 500
WIN_HEIGHT = 500
CELL_SIZE = 25

highest_score = 0

pygame.init()

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Snake")

def distance(x1,y1,x2,y2):
  return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def check_collision(snake, food):
    if(snake.x == food.x and snake.y == food.y):
        snake.length += 1
        snake.update_body()
        food.replace()
        return True

def check_death(index, snake):
    if((snake.x, snake.y) in snake.body[1:]):
        return True
    if snake.x < 0:
        return True
    elif snake.x >= WIN_WIDTH:
        return True
    elif snake.y < 0:
        return True
    elif snake.y >= WIN_HEIGHT:
        return True

def remove(index):
    snakes.pop(index)
    ge.pop(index)
    nets.pop(index)

def redraw(snake, food):
    snake.draw()
    food.draw()

def draw_text(score):
    font = pygame.font.SysFont(None, 24)
    text = font.render("Current highest score: " + str(score), True, (255, 255, 255))
    WIN.blit(text, (10, 5))

def eval_genomes(genomes, config):

  clock = pygame.time.Clock()

  global snakes, ge, nets, highest_score

  snakes = []
  ge = []
  nets = []

  for genome_id, genome in genomes:
      snakes.append((Snake(CELL_SIZE, WIN_WIDTH, WIN), Food(CELL_SIZE, WIN_WIDTH, WIN)))
      ge.append(genome)
      net = neat.nn.FeedForwardNetwork.create(genome, config)
      nets.append(net)
      genome.fitness = 0

  run = True
  while run and len(snakes) > 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
      
    WIN.fill((0, 0, 0))

    for i, (snake,food) in enumerate(snakes):
        if snake.length > highest_score:
            highest_score = snake.length
        snake.update_body()
        redraw(snake, food)
        output = nets[i].activate(snake.eyes(food))
        output_index = output.index(max(output))
        if(output_index == 0):
            snake.change_direction("FORWARD")
        if(output_index == 1):
            snake.change_direction("RIGHT")
        if(output_index == 2):
            snake.change_direction("LEFT")

        snake.move()

        if check_death(i, snake):
            ge[i].fitness -= 10
            remove(i)
        if check_collision(snake, food):
            ge[i].fitness += 10
            snake.length += 1

    draw_text(highest_score)

    clock.tick(30)
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
