import pygame
import math


class Shockwave:
    # Function for initializing the shockwave object with its parameters
    def __init__(self, sx, sy, duration, size, max_size, width, color, color2, shadow, damage, original_damage):
        self.x = sx
        self.y = sy
        self.duration = duration
        self.size = size
        self.max_size = max_size
        self.width = width
        self.color = color
        self.color2 = color2
        self.shadow = shadow
        self.d = damage
        self.od = original_damage

    # This function is run each frame and increases the size of the shockwave but decreases the width
    def expand(self):
        self.size += (self.max_size-self.size)/(10 * self.duration)
        if self.size/self.max_size < 0.8:
            self.width -= 0.03
        else:
            self.width -= 0.1

    # This function draws the shockwave (and its shadow) on the screen
    def blit(self, s):
        pygame.draw.circle(s, self.color2, (self.x - self.shadow, self.y + self.shadow), self.size, int(self.width))
        pygame.draw.circle(s, self.color, (self.x, self.y), self.size, int(self.width))


# Creating the list of all the shockwave objects
shockwaves = []


# ---------------- Particle Class, this is used for the dust particles that appear behind the player when the player moves
class Particle:
    # Function for initializing the particle object with its parameters
    def __init__(self, px, py, x_vel, y_vel, color, color2, size, decay, gravity, bounciness):
        self.x = px
        self.y = py
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.color = color
        self.color2 = color2
        self.size = size
        self.decay = decay
        self.gravity = gravity
        self.bounciness = bounciness

    # Function for drawing the particle on the screen
    def blit(self, s):
        pygame.draw.circle(s, self.color2, (self.x - self.size / 4, self.y + self.size / 4), self.size)
        pygame.draw.circle(s, self.color, (self.x, self.y), self.size)

    # Function that is called every frame for moving the particle and detecting collisions with the tiles
    # This function takes a second parameter called "blocks", which is just a list of all the tile rects
    def move(self, blocks):
        self.x += self.x_vel
        self.y += self.y_vel
        self.y_vel += self.gravity
        self.size -= self.decay

        for bl in blocks:
            if bl.collidepoint(self.x, self.y):
                if math.fabs(self.y - bl.top) < (self.y_vel + 10):
                    if self.y_vel > 0:
                        self.y = bl.top
                        self.y_vel *= -self.bounciness
                if math.fabs(self.x - bl.left) < (self.x_vel + 10):
                    self.x = bl.left
                    self.x_vel *= -self.bounciness
                if math.fabs(self.x - bl.right) < (self.x_vel + 10):
                    self.x = bl.right
                    self.x_vel *= -self.bounciness
