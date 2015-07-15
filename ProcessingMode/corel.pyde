# imports

import csv

# bezier calculating functions

def calculate(first, my, last, t):
    x1 = (my[0] - first[0] * t ** 2 - last[0] * (1 - t) ** 2) / (2 * t * (1 - t))
    y1 = (my[1] - first[1] * t ** 2 - last[1] * (1 - t) ** 2) / (2 * t * (1 - t))
    return x1, y1

def bezier(first, middle, last):
    tlist = range(0, 100 + 1, 1)   # 1000
    pointslist = []
    for t in tlist:
        t /= 100.0   # 1000
        xt = int(first[0] * t ** 2 + middle[0] * 2 * t * (1 - t) + last[0] * (1 - t) ** 2)
        yt = int(first[1] * t ** 2 + middle[1] * 2 * t * (1 - t) + last[1] * (1 - t) ** 2)
        pointslist.append((xt, yt))
    return pointslist

# GLOBAL variables

points = []   # all points of one line
lines = []   # all lines list
llines = []   # lines list loaded from csv
curves = []   # list of bezier curves
drawn = False   # draw now?
load = True   # load csv?
r = random(255)
g = random(255)
b = random(255)

# saving and loading functions

def tocsv(lines_array, name = "lines"):
    c = csv.writer(open(name + ".csv", "wb"))
    for ent in lines_array:
        c.writerow(ent)
    print len(lines_array), "lines saved"

def csvloader(name = "lines"):
    loaded_lines = []
    cr = csv.reader(open(name + ".csv", "rb"))
    for row in cr:
        points_collector = []
        for cell in row:
            cell = tuple(eval(cell))
            points_collector.append(cell)
        loaded_lines.append(points_collector)
    print "loaded lines", len(loaded_lines)
    return loaded_lines

# main programm setup

def setup():
    global llines
    size(800, 600)
    background(255, 255, 255)
    noStroke()
    textSize(20)
    fill(255, 255, 255)
    # load lines from csv
    llines = csvloader("curves")   # "lines" or "points0" for lines or tests

# events

def mousePressed():
    global points
    global drawn
    drawn = True
    points = []
    x = mouseX
    y = mouseY
    point = (x, y)
    fill(255, 0, 0)
    ellipse(x, y, 3, 3)
    points.append(point)
    
def mouseDragged(): 
    global points
    x = mouseX
    y = mouseY
    point = (x, y)
    fill(200, 200, 200)
    ellipse(x, y, 3, 3)
    points.append(point)

def mouseReleased():
    global points
    global lines
    global drawn
    global curves
    lines.append(points)
    tocsv(lines, "lines")
    middle = calculate(points[0], points[len(points)/2], points[-1], 0.5)
    curve = bezier(points[0], middle, points[-1])
    curves.append(curve)
    tocsv(curves, "curves")
    save("curves.png")
    drawn = False

def draw():
    global llines
    global lines
    global drawn
    global r, g, b
    global load
    global curves
    # to change color of lines
    if keyPressed:
        if keyCode == UP or keyCode == DOWN:
            r = random(255)
            g = random(255)
            b = random(255)
    # background cleaning
    if not drawn:
        background(255, 255, 255)
    # cleaning box with points and lines counter
    fill(255, 255, 255) 
    rect(0, 0, 300, 30)
    # drawing text
    fill(0, 0, 0) 
    text("Points: " + str(len(points))+ " | Lines: " + str(len(lines)), 10, 25)
    # drawing loaded lines
    if load:        
        for l in llines:
            for p in l:
                fill(190, 190, 190)
                ellipse(p[0], p[1], 2, 2)
    # drawing points
    if not drawn:
        for curve in curves:
            fill(r, g, b)
            for point in curve:
                ellipse(point[0], point[1], 3, 3)
# end
