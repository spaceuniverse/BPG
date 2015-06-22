# -------------------------#
import pygame
import random
import time
import numpy as np
import csv
# -------------------------#

NAME = "./data/points"

pygame.font.init()   # pygame.init()
screen = pygame.display.set_mode((800, 600))
mfont = pygame.font.Font(None, 25)

draw_on = False
color = (255, 255, 255)
radius = 2
running = True

points_collector = []
lines_collector = []
lines_counter = 0

# -------------------------#

while running:
    e = pygame.event.wait()
    if e.type == pygame.QUIT:
        running = False
        print "save"
        c = csv.writer(open(NAME + ".csv", "wb"))
        for ent in lines_collector:
            print ent[0], ent[1]
            c.writerow(ent[1])
        print "saved"
        pygame.image.save(screen, NAME + ".jpg")
    if e.type == pygame.MOUSEBUTTONDOWN:
        color = (random.randrange(256), random.randrange(256), random.randrange(256))
        pygame.draw.circle(screen, color, e.pos, radius)
        print "\n", "first point", e.pos
        points_collector = []
        points_collector.append(e.pos)
        draw_on = True
    if e.type == pygame.MOUSEBUTTONUP:
        draw_on = False
        print points_collector, len(points_collector)
        lines_collector.append( (lines_counter, points_collector) )
        lines_counter += 1
        print lines_collector, len(lines_collector)
    if e.type == pygame.MOUSEMOTION:
        if draw_on:
            pygame.draw.circle(screen, color, e.pos, radius)
            print "point", e.pos
            points_collector.append(e.pos)
    label = mfont.render("Lines: " + str(len(lines_collector)), True, (255, 255, 255))
    pygame.draw.rect(screen, (150, 150, 150), (0, 0, 800, 30))
    screen.blit(label, (10, 5))
    pygame.display.flip()

pygame.quit()
# -------------------------#