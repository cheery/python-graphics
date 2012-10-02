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
