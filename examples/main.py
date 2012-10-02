import pygame, sys
from graphics import Point, Rect, Color, Surface, load_bitmap, load_font, Patch9

box = Patch9(load_bitmap("gui/simple_box.png"))

font = load_font('proggy-tiny')

text = font('hello user.')

background = Color(0x10, 0, 0x50)
front = Color(0xA5, 0x56, 0x94)
red = Color(0xFF, 0x00, 0x00)

redfont = font.recolor(front)

redtext = redfont('hi.')
redbox = box.recolor(front)

def animation_frame(screen):
    background.paint( screen, screen.rect )
    front.paint( screen, front.rect.move(Point(10, 10)) ) 
    box.paint( screen, screen.rect.inset(100, 10, 10, 10) )
    text.paint( screen, text.rect.move(Point(200, 200)) )
    redtext.paint( screen, redtext.rect.move(Point(200, 216)) )
    redbox.paint( screen, redbox.rect.move(Point(200, 230)) )

def dispatch(event):
    if event.type == pygame.QUIT:
        sys.exit(0)

pygame.display.init()
screen = Surface(pygame.display.set_mode((1024, 768)))
while 1:
    for event in pygame.event.get():
        dispatch(event)
    animation_frame(screen)
    pygame.display.flip()
