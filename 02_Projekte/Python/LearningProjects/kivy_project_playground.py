from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivy.graphics import Color

class Playground(MDApp):
    screen = Screen()

    b = MDLabel(
        text = "Home", pos_hint={'center_x': 0.6,
                                 'center_y': 1},
                theme_text_color = "Custom",
                text_color = (1, 0, 0, 1),
                font_style = 'Caption'
    )

    screen.add_widget(b)



if __name__ == "__main__":
        Playground().run()