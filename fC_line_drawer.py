# -------------------------#
import pygame
import random
import time
import numpy as np
import csv
# -------------------------#

NAME = "./data/points"

screen = pygame.display.set_mode((800, 600))

color = (255, 255, 255)
radius = 2
running = True
drawn = False

points_collector = []
lines_collector = []

cr = csv.reader(open(NAME + ".csv", "rb"))

# -------------------------#

for row in cr:
    print row
    points_collector = []
    for cell in row:
        cell = tuple(eval(cell))
        print cell, type(cell)
        points_collector.append(cell)
    print points_collector, len(points_collector)
    lines_collector.append(points_collector)
    print "line", len(lines_collector)

# -------------------------#

while running:
    e = pygame.event.wait()
    if e.type == pygame.QUIT:
        running = False
        print "exit"
        pygame.image.save(screen, NAME + ".jpg")
    if not drawn:
        for line in lines_collector:
            color = (random.randrange(256), random.randrange(256), random.randrange(256))
            for point in line:
                pygame.draw.circle(screen, color, point, radius)
        drawn = True
    pygame.display.flip()

pygame.quit()

# -------------------------#