from sdl.util import Point, Rect, Color, Surface, load_bitmap
from bitmapfont import Font
from patch9 import Patch9
import json, os

def load_font(directory):
    metadata = json.load(open(os.path.join(directory, 'metadata.json')))
    surface = load_bitmap(os.path.join(directory, 'bitmap.png'))
    return Font(surface, metadata)

#def loadfont(directory):
#
#def defaultfont():
#    root = os.path.dirname(__file__)
#    surface = load(os.path.join(root, 'defaultfont/bitmap.png'))
#    metadata = json.load(open(os.path.join(root, 'defaultfont/metadata.json')))
#    return font(surface, metadata)
