import math
import random

import pygame


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


class Snake:
    def __init__(self, cell_size, win_width, win):
        self.x = 200
        self.y = 200
        self.body = []
        self.length = 1
        self.direction = 0
        self.color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        self.cell_size = cell_size
        self.win = win
        self.win_width = win_width
        self.score = 1

    def change_direction(self, turn):
        if turn == "FORWARD":
            pass
        elif turn == "RIGHT":
            if self.direction == 0:
                self.direction = 2
            elif self.direction == 2:
                self.direction = 1
            elif self.direction == 1:
                self.direction = 3
            elif self.direction == 3:
                self.direction = 0
        elif turn == "LEFT":
            if self.direction == 0:
                self.direction = 3
            elif self.direction == 3:
                self.direction = 1
            elif self.direction == 1:
                self.direction = 2
            elif self.direction == 2:
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
            pygame.draw.rect(
                self.win,
                self.color,
                pygame.Rect(x[0], x[1], self.cell_size, self.cell_size),
            )

    def eyes(self, food):
        output = []
        if self.direction == 0:
            # forward
            output.append(self.y - food.y)
            # right
            output.append(food.x - self.x)
            # left
            output.append(self.x - food.x)
            # forward right
            if food.y <= self.y and food.x >= self.x:
                output.append(distance(food.x, food.y, self.x, self.y))
            else:
                output.append(-distance(food.x, food.y, self.x, self.y))
            # forward left
            if food.y <= self.y and food.x <= self.x:
                output.append(distance(food.x, food.y, self.x, self.y))
            else:
                output.append(-distance(food.x, food.y, self.x, self.y))
            # distance to nearest obstacle forward
            nearest_forward = self.y
            for bp in self.body:
                if bp[0] == self.x and bp[1] < self.y:
                    dist = self.y - bp[1]
                    if dist < nearest_forward:
                        nearest_forward = dist
            output.append(nearest_forward - self.cell_size)
            # distance to nearest obstacle right
            nearest_right = self.win_width - self.x
            for bp in self.body:
                if bp[1] == self.y and bp[0] > self.x:
                    dist = bp[0] - self.x
                    if dist < nearest_forward:
                        nearest_right = dist
            output.append(nearest_right - self.cell_size)
            # distance to nearest obstacle left
            nearest_left = self.x
            for bp in self.body:
                if bp[1] == self.y and bp[0] < self.x:
                    dist = self.x - bp[0]
                    if dist < nearest_forward:
                        nearest_left = dist
            output.append(nearest_left - self.cell_size)

            return output

        if self.direction == 1:
            # forward
            output.append(food.y - self.y)
            # right
            output.append(self.x - food.x)
            # left
            output.append(food.x - self.x)
            # forward right
            if food.y >= self.y and food.x >= self.x:
                output.append(distance(food.x, food.y, self.x, self.y))
            else:
                output.append(-distance(food.x, food.y, self.x, self.y))
            # forward left
            if food.y >= self.y and food.x <= self.x:
                output.append(distance(food.x, food.y, self.x, self.y))
            else:
                output.append(-distance(food.x, food.y, self.x, self.y))
            # distance to nearest obstacle forward
            nearest_forward = self.win_width - self.y
            for bp in self.body:
                if bp[0] == self.x and bp[1] > self.y:
                    dist = bp[1] - self.y
                    if dist < nearest_forward:
                        nearest_forward = dist
            output.append(nearest_forward - self.cell_size)
            # distance to nearest obstacle right
            nearest_right = self.win_width - self.x
            for bp in self.body:
                if bp[1] == self.y and bp[0] < self.x:
                    dist = self.x - bp[0]
                    if dist < nearest_forward:
                        nearest_right = dist
            output.append(nearest_right - self.cell_size)
            # distance to nearest obstacle left
            nearest_left = self.x
            for bp in self.body:
                if bp[1] == self.y and bp[0] > self.x:
                    dist = bp[0] - self.x
                    if dist < nearest_forward:
                        nearest_left = dist
            output.append(nearest_left - self.cell_size)

            return output

        if self.direction == 2:
            # forward
            output.append(food.x - self.x)
            # right
            output.append(food.y - self.y)
            # left
            output.append(self.y - food.y)
            # forward right
            if food.x >= self.x and food.y >= self.y:
                output.append(distance(food.x, food.y, self.x, self.y))
            else:
                output.append(-distance(food.x, food.y, self.x, self.y))
            # forward left
            if food.x >= self.x and food.y <= self.y:
                output.append(distance(food.x, food.y, self.x, self.y))
            else:
                output.append(-distance(food.x, food.y, self.x, self.y))
            # nearest obstacle forward
            nearest_forward = self.win_width - self.x
            for bp in self.body:
                if bp[1] == self.y and bp[0] > self.x:
                    dist = bp[0] - self.x
                    if dist < nearest_forward:
                        nearest_forward = dist
            output.append(nearest_forward - self.cell_size)
            # nearest obstacle right
            nearest_right = self.win_width - self.y
            for bp in self.body:
                if bp[0] == self.x and bp[1] > self.y:
                    dist = bp[1] - self.y
                    if dist < nearest_right:
                        nearest_right = dist
            output.append(nearest_right - self.cell_size)
            # nearest obstacle left
            nearest_left = self.y
            for bp in self.body:
                if bp[0] == self.x and bp[1] < self.y:
                    dist = self.y - bp[1]
                    if dist < nearest_left:
                        nearest_left = dist
            output.append(nearest_left - self.cell_size)

            return output

        if self.direction == 3:
            # forward
            output.append(self.x - food.x)
            # right
            output.append(self.y - food.y)
            # left
            output.append(food.y - self.y)
            # forward right
            if food.x <= self.x and food.y <= self.y:
                output.append(distance(food.x, food.y, self.x, self.y))
            else:
                output.append(-distance(food.x, food.y, self.x, self.y))
            # forward left
            if food.x <= self.x and food.y >= self.y:
                output.append(distance(food.x, food.y, self.x, self.y))
            else:
                output.append(-distance(food.x, food.y, self.x, self.y))
            # nearest obstacle forward
            nearest_forward = self.x
            for bp in self.body:
                if bp[1] == self.y and bp[0] < self.x:
                    dist = self.x - bp[0]
                    if dist < nearest_forward:
                        nearest_forward = dist
            output.append(nearest_forward - self.cell_size)
            # nearest obstacle right
            nearest_right = self.win_width - self.y
            for bp in self.body:
                if bp[0] == self.x and bp[1] < self.y:
                    dist = self.y - bp[1]
                    if dist < nearest_right:
                        nearest_right = dist
            output.append(nearest_right - self.cell_size)
            # nearest obstacle left
            nearest_left = self.y
            for bp in self.body:
                if bp[0] == self.x and bp[1] > self.y:
                    dist = bp[1] - self.y
                    if dist < nearest_left:
                        nearest_left = dist
            output.append(nearest_left - self.cell_size)

            return output
