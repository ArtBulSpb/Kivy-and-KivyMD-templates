from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

# В переменной KV создаём вёрстку
KV = """
MyBL:
        Label: #вывод
                font_size:"30sp"
                text:root.data_label
"""


class MyBL(BoxLayout):
    data_label = StringProperty("Приветствую")


class MyApp(App):
    running = True

    def build(self):
        return Builder.load_string(KV)

    def on_stop(self):
        self_running = False


MyApp().run()
