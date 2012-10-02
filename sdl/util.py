import pygame

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iter__(self):
        return iter((self.x, self.y))

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Point(self.x-other.x, self.y-other.y)

class Rect(object):
    def __init__(self, position, size):
        self.position = position
        self.size = size

    def __iter__(self):
        return iter((self.position, self.size))

    def move(self, point):
        return Rect(self.position + point, self.size)

    def pad(self, left, top, right, bottom):
        lt = Point(left, top)
        rb = Point(right, bottom)
        return Rect(
            self.position - lt,
            self.size + lt + rb
        )
    
    def inset(self, left, top, right, bottom):
        return self.pad(-left, -top, -right, -bottom)

class Color(object):
    def __init__(self, r, g, b, a=255):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __iter__(self):
        return iter((self.r, self.g, self.b, self.a))

    @property
    def rect(self):
        return Rect(Point(0,0), Point(16,16))

    def tint(self, target, rect=None):
        rect = rect if rect else target.rect
        return self.paint(target, rect, pygame.BLEND_RGBA_MULT)

    def paint(self, target, rect, special_flags=0):
        (x, y), (w, h) = rect
        target.internal.fill(tuple(self), (x,y,w,h), special_flags=special_flags)
        return target

class Surface(object):
    def __init__(self, internal):
        self.internal = internal

    @staticmethod
    def empty((width, height)):
        width = max(1, int(width))
        height = max(1, int(height))
        return Surface(pygame.surface.Surface((width, height), pygame.SRCALPHA))

    @property
    def rect(self):
        w, h = self.internal.get_size()
        return Rect(Point(0,0), Point(w,h))

    def tint(self, target, rect=None):
        rect = rect if rect else target.rect
        return self.paint(target, rect, pygame.BLEND_RGBA_MULT)

    def paint(self, target, rect, special_flags=0):
        (x, y), (w, h) = rect
        if w > 0 and h > 0:
            scaled = pygame.transform.scale(self.internal, (w, h))
            target.internal.blit(scaled, (x,y,w,h), special_flags=special_flags)
        return target

    def at(self, (x,y)):
        r, g, b, a = self.internal.get_at((x, y))
        return Color(r, g, b, a)

    def subsurface(self, rect):
        (x, y), (w, h) = rect
        return Surface(self.internal.subsurface((x,y,w,h)))

    def copy(self):
        return Surface(self.internal.copy())

    def recolor(self, color):
        return color.tint(self.copy())

def load_bitmap(filename):
    return Surface(pygame.image.load(filename))
