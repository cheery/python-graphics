from sdl.util import Point, Rect

def borders(surface):
    _, (width, height) = surface.rect
    y0 = 0
    y1 = 0
    x0 = 0
    x1 = 0
    i = 0
    while i < height:
        r,g,b,a = surface.at((0,i))
        if a > 0:
            y0 = i
            break
        i += 1
    while i < height:
        r,g,b,a = surface.at((0,i))
        if a == 0:
            y1 = i
            break
        i += 1
    i = 0
    while i < width:
        r,g,b,a = surface.at((i,0))
        if a > 0:
            x0 = i
            break
        i += 1
    while i < width:
        r,g,b,a = surface.at((i,0))
        if a == 0:
            x1 = i
            break
        i += 1
    return [1, x0, x1, width], [1, y0, y1, height]

class Patch9(object):
    def __init__(self, surface):
        self.surface = surface
        self.subsurfaces = []
        h, v = borders(surface)
        for y in range(3):
            row = []
            for x in range(3):
                area = (h[x], v[y]), (h[x+1]-h[x], v[y+1]-v[y])
                row.append(surface.subsurface(area))
            self.subsurfaces.append(row)
        self.padding = h[1]-h[0], v[1]-v[0], h[3]-h[2], v[3]-v[2]

    @property
    def rect(self):
        return Rect(Point(0,0), self.surface.rect.size - Point(1,1))

    def paint(self, target, rect):
        left, top, right, bottom = self.padding
        (h0, v0), (w, h) = rect
        (h3, v3) = (h0 + w), (v0 + h)
        h = [h0, h0+left, h3-right, h3] 
        v = [v0, v0+top, v3-bottom, v3]
        for y, row in enumerate(self.subsurfaces):
            for x, surface in enumerate(row):
                sector = (h[x], v[y]), (h[x+1]-h[x], v[y+1]-v[y])
                surface.paint(target, sector)
        return target

    def recolor(self, color):
        return Patch9(color.tint(self.surface.copy()))
