import math
import random

from pygame import Vector2
from Settings import*


class Bird:
    """ Describe bird - one flying element"""
    def __init__(self):
        """Initialize bird with position(self.pos: pygame.Vectro2) and velocity(self.pos: pygame.Vectro2)"""
        self.pos = Vector2(random.uniform(0,WIDTH), random.uniform(0,HEIGHT))
        self.vel = Vector2(random.uniform(-MAX_VEL, MAX_VEL), random.uniform(-MAX_VEL, MAX_VEL))

    def get_pos(self):
        """
        Return position of the bird
        
        param: self

        return: self.pos

        """
        return self.pos

    def get_vel(self):
        """
        Return velocity of the bird
        
        param: self

        return: self.vel

        """
        return self.vel
    
    def get_color(self):
        """
        Return color of the bird

        param: self

        return: color of bird

        """
        red = int(self.vel.x * self.vel.x) * 10
        if red > 255: red = 254
        green = int(self.vel.y * self.vel.y) * 10
        if green > 255: green = 254
        return red, green, 50

    def push(self, Force):
        """
        Change direction of the vector of the velocity
        
        param: self

        return: None

        """
        self.vel += Force
        self.vel += Vector2(random.uniform(-0.05*MAX_VEL, 0.05*MAX_VEL), random.uniform(-0.05*MAX_VEL, 0.05*MAX_VEL))
        if math.sqrt(self.vel.x * self.vel.x + self.vel.y * self.vel.y) >= MAX_VEL:
            self.vel.scale_to_length(MAX_VEL)

    def move(self):
        """
        Change position of the bird
        
        param: self

        return: None

        """
        self.pos += self.vel

        if self.pos.x < 0:
            self.pos = Vector2(WIDTH, self.pos.y)
        if self.pos.x > WIDTH:
            self.pos = Vector2(0, self.pos.y)
        if self.pos.y < 0:
            self.pos = Vector2(self.pos.x, HEIGHT)
        if self.pos.y > HEIGHT:
            self.pos = Vector2(self.pos.x, 0)
        

                
