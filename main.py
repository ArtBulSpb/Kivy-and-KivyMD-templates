
__version__ = '1.0.3'

import kivy as kivy

requirements = kivy

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
        size_hint: (0.98, 0.98)
        pos_hint: {"center_x": 0.5, "center_y":0.5}
        padding: 10
        spacing: 10
                
        Label: #вывод
                font_size:"30sp"
                text:root.data_label
                
        Button:
                text: "поиск по названию 1"
                bold: True
                background_color:'#9932CC'
                size_hint: (1,0.5)
                on_press: root.label_change("поиск по названию 1")
                line_width: 2
                elevation_normal: 8  # длинна тени 
                radius: [20]
                
        Button:
                text: "поиск по названию 2"
                bold: True
                background_color:'#9932CC'
                size_hint: (1,0.5)
                on_press: root.label_change("поиск по названию 2")
                line_width: 2
        Button:
                text: "поиск по названию 3"
                bold: True
                background_color:'#9932CC'
                size_hint: (1,0.5)
                on_press: root.label_change("поиск по названию 3")
                line_width: 2
                
        Button:
                text: "поиск по названию 4"
                bold: True
                background_color:'#9932CC'
                size_hint: (1,0.5)
                on_press: root.label_change("поиск по названию 4")
                radius: [50,]
                # border: 30,30,30,30
                
                
"""


class MyBL(BoxLayout):
    data_label = StringProperty("Приветствую!")

    def label_change(self, new_text):
        self.data_label = new_text
        print(new_text)

    def callback(self):
        print("poisk")


class MyApp(App):
    running = True

    def build(self):
        return Builder.load_string(KV)

    def on_stop(self):
        self_running = False


MyApp().run()
