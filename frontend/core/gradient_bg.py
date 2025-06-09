# core/gradient_background.py

from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Line, Color


class GradientBackground(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Use actual widget dimensions instead of Window (in case it's resized later)
        self.bind(size=self._redraw_gradient, pos=self._redraw_gradient)

    def _redraw_gradient(self, *args):
        self.canvas.clear()

        width = int(self.width)
        height = int(self.height)

        # Define start and end colors (white → light pink)
        start_color = (1, 1, 1)
        end_color = (1, 0.9, 0.95)

        for x in range(width):
            t = x / width  # interpolation ratio from 0 → 1

            # Interpolate each channel separately
            r = start_color[0] * (1 - t) + end_color[0] * t
            g = start_color[1] * (1 - t) + end_color[1] * t
            b = start_color[2] * (1 - t) + end_color[2] * t

            # Add the color and draw a vertical line
            with self.canvas:
                Color(rgba=(r, g, b, 1))
                Line(points=[x, 0, x, height], width=1)
