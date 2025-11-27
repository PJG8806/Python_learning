import math

def triang(down_size,height_size):
    return down_size * height_size * 0.5

def circle(radius):
    return (radius ** 2)  * math.pi

def cuboid(width1, whidth2, height):
    return ((width1 * height) + (whidth2 * height) + (width1 * whidth2)) * 2