import pygame

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __iter__(self):
        return iter((self.x, self.y))

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Point(self.x-other.x, self.y-other.y)

    def __mul__(self, scalar):
        return Point(self.x*scalar, self.y*scalar)

    def __repr__(self):
        return "Point(%r, %r)" % tuple(self)

class Rect(object):
    def __init__(self, position=None, size=None):
        self.position = position if position else Point(0,0)
        self.size = size if size else Point(0,0)

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

    def inside(self, point):
        (x, y) = point - self.position
        (w, h) = self.size
        return 0 <= x < w and 0 <= y < h

    @property
    def center(self):
        return self.position + self.size * 0.5

    @property
    def topleft(self):
        return self.position

    @property
    def bottomright(self):
        return self.position + self.size

    @property
    def topright(self):
        return Point(self.bottomright.x, self.topleft.y)

    @property
    def bottomleft(self):
        return Point(self.topleft.x, self.bottomright.y)

    @property
    def centerleft(self):
        return Point(self.topleft.x, self.center.y)

    @property
    def centerright(self):
        return Point(self.bottomright.x, self.center.y)

    @property
    def bottomcenter(self):
        return Point(self.center.x, self.bottomright.y)

    @property
    def topcenter(self):
        return Point(self.center.x, self.topleft.y)

    def __repr__(self):
        return "Rect(%r, %r)" % tuple(self)

class Color(object):
    def __init__(self, r, g, b, a=255):
        self.r = r
        self.g = g
        self.b = b
        self.a = a
        color = ''.join(map(chr,self))
        self.surface = Surface(pygame.image.frombuffer(color, (1,1), "RGBA"))

    def __iter__(self):
        return iter((self.r, self.g, self.b, self.a))

    @property
    def rect(self):
        return Rect(Point(0,0), Point(16,16))

    def tint(self, target, rect=None):
        rect = rect if rect else target.rect
        return self.paint(target, rect, pygame.BLEND_RGBA_MULT)

    def paint(self, target, rect, special_flags=0):
        self.surface.paint(target, rect, special_flags)
        return target

    def __repr__(self):
        return "Color(%r, %r, %r, %r)" % tuple(self)

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
