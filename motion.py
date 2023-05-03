import pygame
import math

WIDTH = 1000
HEIGHT = 1000
AU = 149e9                                                                     # In meters
DAY = 8640                                                                     # Seconds in a day, acts as a timescale
SCALE = 300 / AU                                                               # How many pixels per AU
G = 6.67e-11                                                                   # In N*m/kg

class Body:
    
    def __init__(self, x, y, color, mass):
        #   Converting pixels to AU scale, defining color, mass and velocity
        self.x = x * AU
        self.y = y * AU
        self.color = color
        self.mass = mass
        self.orbit = []
        self.x_vel = 0
        self.y_vel = 0

        # Fits x and y into scale and prints on the screen
    def draw(self, win):
        x = self.x * SCALE + (WIDTH / 2)
        y = self.y * SCALE + (HEIGHT / 2)
        
        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * SCALE + WIDTH / 2
                y = y * SCALE + HEIGHT / 2
                updated_points.append((x, y))
                
            pygame.draw.lines(win, self.color, False, updated_points, 2)
        
        pygame.draw.circle(win, self.color, (x, y), 10)
        

    def attraction(self, other):
        #   Defines the distance per the hypotenuse formula
        distance_x = other.x - self.x
        distance_y = other.y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
        
        #   Calculates the atrraction force per Newton's Law of Universal Gravitation
        force = G * self.mass * other.mass / distance ** 2
        theta = math.atan2(distance_y, distance_x)
        #   Converts the force into x and y axis
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        
        return force_x, force_y
    
    def movement(self, objects):
        total_fx = 0
        total_fy = 0
        #   Cycles through all objects and defines their attraction to each other
        for object in objects:
            if self == object:
                continue
            fx, fy = self.attraction(object)
            total_fx += fx
            total_fy += fy
        
        #   Calculates speed
        self.x_vel += total_fx / self.mass * DAY
        self.y_vel += total_fy / self.mass * DAY

        #   Gets the position after movement and adds coordinates to orbit list
        self.x += self.x_vel * DAY
        self.y += self.y_vel * DAY
        self.orbit.append((self.x, self.y))