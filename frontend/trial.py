from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Line, Color
from kivy.uix.boxlayout import BoxLayout


class Background(BoxLayout):
    def __init__(self):
        super(Background, self).__init__()
        self.width = Window.size[0]
        self.height = Window.size[1]
        self.add_gradient()

    def add_gradient(self):
        alpha_channel_rate = 0
        increase_rate = 1 / self.width

        for sep in range(self.width):
            self.canvas.add(Color(rgba=(0, 1, 0, alpha_channel_rate)))
            self.canvas.add(Line(points=[sep, 0, sep, self.height], width=1))
            alpha_channel_rate += increase_rate


class GradientApp(App):
    def build(self):
        background = Background()
        return background


if __name__ == "__main__":
    GradientApp().run()