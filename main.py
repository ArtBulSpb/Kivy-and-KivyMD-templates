#__version__ = “1.0.3”

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

# В переменной KV создаём вёрстку
KV = """
MyBL:
        orientation: "vertical"
        size_hint: (0.95, 0.95)
        pos_hint: {"center_x": 0.5, "center_y":0.5}
        Label: #вывод
                font_size:"30sp"
                text:root.data_label
        Button:
                text: "поиск по названию 1"
                bold: True
                background_color:'#9932CC'
                size_hint: (1,0.5)
                on_press: root.callback()
        Button:
                text: "поиск по названию 2"
                bold: True
                background_color:'#9932CC'
                size_hint: (1,0.5)
                on_press: root.callback()
        Button:
                text: "поиск по названию 3"
                bold: True
                background_color:'#9932CC'
                size_hint: (1,0.5)
                on_press: root.callback()
                
"""


class MyBL(BoxLayout):
    data_label = StringProperty("Приветствую!")

    def callback(self):
        print("poisk")


class MyApp(App):
    running = True

    def build(self):
        return Builder.load_string(KV)

    def on_stop(self):
        self_running = False


MyApp().run()
