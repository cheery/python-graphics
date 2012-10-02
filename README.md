Python Graphics Module (Unstable)
=================================

This is an initiative about improving aesthetics of graphics programming on open source platforms.

`graphics` is supposed to be simpler to understand and use than what pygame is. It's also named to what it is. The current implementation is inefficient and slow, and wrapped around to pygame.

Here's demonstration of the current state, it is available in examples/simple.py

    import pygame
    import graphics
    import sys
    from graphics import Color, Surface

    font = graphics.load_font('proggy-tiny')

    greeting = font("Hello world.")
    background = Color(0x10, 0x30, 0x20)

    def animation_frame(screen):
        background.paint(screen, screen.rect)
        greeting.paint(screen, greeting.rect.move(
            screen.rect.center - greeting.rect.center
        ))

    def dispatch(event):
        if event.type == pygame.QUIT or event.type == pygame.KEYUP:
            sys.exit(0)

    pygame.display.init()
    screen = Surface(pygame.display.set_mode((320, 240)))
    while 1:
        for event in pygame.event.get():
            dispatch(event)
        animation_frame(screen)
        pygame.display.flip()

Design Goals
------------

 * Cut cords of pygame and sdl, provide something better.
 * Support multiple rendering engines, simple, complex and domain-specific ones.
 * Support multiple programming languages, do not depend on python.
 * Separate rectangles and vectors from the graphics module and make a standard out of them.

Module Reference
----------------

The `graphics` is a collection of traits that are given to several objects. Trait is a collection of methods, and object implements the trait if it has all of these methods. The module looks thin purposefully, and contains only few methods and classes. Here's what you see when you import the
module and dir it in interactive prompt:

    >>> import graphics
    >>> print '\n'.join(dir(graphics))
    Color
    Font
    Patch9
    Point
    Rect
    Surface
    __builtins__
    __doc__
    __file__
    __name__
    __package__
    __path__
    __warningregistry__
    bitmapfont
    json
    load_bitmap
    load_font
    os
    patch9
    sdl
    >>> 

As you see, there's only few modules, and even then this is still bit cluttered. The pieces that belong to this module are:

    Color(r,g,b,a)
    Font(surface, metadata)
    Patch9(surface)
    Point(x,y)
    Rect(position, size)
    Surface
    load_bitmap(path)
    load_font(path)

`Point`, `Rect` and `Color` are utility objects, that are supposed to be vectors with few methods and properties. They are convenience tools. `load_bitmap` and `load_font` do exactly what they say.

    point = Point(x,y)
    point.x
    point.y
    x, y = point
    point + point
    point - point
    point * number

    rect = Rect(position, size)
    rect.position
    rect.size
    position, size = rect
    rect = rect.move(offset)
    rect = rect.pad(left, top, right, bottom)
    rect = rect.inset(left, top, right, bottom)
    rect.center

    color = Color(r, g, b, a=255)
    color.r
    color.g
    color.b
    color.a
    r, g, b, a = color

`Color`, `Surface`, `Patch9` and `Font` are drawable. Each of them can be painted to a surface and it's easy to remember how to use them. The paint function returns the target surface, although it doesn't copy anything.

    rect = obj.rect
    target = obj.paint(target, rect)

`Surface`, `Patch9` and `Font` are recolorable. Their color can be changed to another.

    colorful_obj = obj.recolor(color)

`Surface` has special methods that aren't in any other object. That happens because it is a bitmap of sort.

    surface = Surface.empty((width, height))
    color = surface.at((x,y))
    subsurface = surface.subsurface(rect)
    copied_surface = surface.copy()
