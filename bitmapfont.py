from sdl.util import Surface

class Font(object):
    def __init__(self, surface, metadata):
        self.surface = surface
        self.metadata = metadata

    def calculate_mathline(self, baseline):
        metrics = self.metadata['+']
        return metrics["height"] / 2 - metrics["vbearing"] + baseline

    def __call__(self, text):
        _, (font_width, font_height) = self.surface.rect
        offsets = [0]
        baseline = 0
        overline = 0
        x = 0
        for character in text:
            metrics = self.metadata.get(character)
            if metrics is None:
                continue
            if metrics["display"]:
                baseline = max(baseline, metrics["vbearing"])
                overline = max(overline, metrics["height"] - metrics["vbearing"])
            x += metrics['advance']
            offsets.append(x)
        surface = Surface.empty((offsets[-1], baseline + overline))
        x = 0
        for character in text:
            metrics = self.metadata.get(character)
            if metrics is None:
                continue
            if metrics["display"]:
                width = metrics["width"]
                height = metrics["height"]
                uv = metrics["uv"]
                glyph = self.surface.subsurface((
                    (uv["s"] * font_width, uv["t"] * font_height),
                    (width, height)
                ))
                glyph.paint(surface, (
                    (x + metrics["hbearing"], baseline - metrics["vbearing"]),
                    (width, height)
                ))
            x += metrics['advance']
        mathline = self.calculate_mathline(baseline)
        surface.offsets = offsets
        surface.baseline = baseline
        surface.mathline = mathline
        return surface

    def recolor(self, color):
        return Font(color.tint(self.surface.copy()), self.metadata)
