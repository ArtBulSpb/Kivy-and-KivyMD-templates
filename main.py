__version__ = '1.0.3'

import kivy as kivy

requirements = kivy

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.base import runTouchApp
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatIconButton


# В переменной KV создаём вёрстку
KV = """
MyBL:
        orientation: "vertical"
        size_hint: (0.98, 0.98)
        pos_hint: {"center_x": 0.5, "center_y":0.5}
        padding: 10
        spacing: 10
        
        TextInput:
                id: txt_input_data
                text:root.placeholder 
                multiline: False
                cursor_color: root.text_secondary_color
                font_family: 'Roboto'
                font_size: '20sp'
                size_hint: 1, None
                #height: '100dp'
                on_focus: self.text = "" if self.text==root.placeholder else self.text #Очищаем поле ввода если в него переведён фокус                        
                #on_text: root.label_change(self.text) #Передаём введенные данные в Label обуквенно
                on_text_validate: 
                        text_holder = self.text #Для понимания синтаксиса работы нескольких функций по событию.Их нужно располагать одну под другой 
                        root.label_change(self.text) #Передаём введенные данные в Label после нажатия Enter 
                #width: 300
                foreground_color: root.text_secondary_color if self.text==root.placeholder else root.text_primary_color
                #background_normal: './assets/imgs/transparent.png'
                #background_active: './assets/imgs/transparent.png'    
    
        Label: #вывод
                font_size:"30sp"
                text:root.data_label
                
        Button:
                text: root.button1_text
                bold: True
                background_color:'#9932CC'
                size_hint: (1,0.5)
                on_press: root.label_change(root.button1_text)
                 #       print("root.placeholder = ", root.placeholder)
                 #      root.callback_txt_input_data(root.placeholder)
                elevation_normal: 8  # длинна тени 
                radius: [20]
                
        Button:
                text: root.button2_text
                bold: True
                background_color:'#9932CC'
                size_hint: (1,0.5)
                on_press: root.label_change(root.button2_text)
                line_width: 2
        Button:
                text: root.button3_text
                bold: True
                background_color:'#9932CC'
                size_hint: (1,0.5)
                on_press: root.label_change(root.button3_text)
                
        Button:
                text: root.button4_text
                bold: True
                background_color:'#9932CC'
                size_hint: (1,0.5)
                on_press: root.label_change(root.button4_text)
                radius: [50,]
                # border: 30,30,30,30
                
        MDFillRoundFlatButton:
                text: "MDRectangleFlatIconButton"
                #icon: "language-python"
                line_color: 0, 0, 0, 0
                pos_hint: {"center_x": .5, "center_y": .7} #Параметры в {} определяют центр кнопки
            

"""

LogIn = """

<LoginScreen>:
    f_username: username
    f_password: password
    GridLayout:
        rows: 2
        cols: 2
        padding: 10
        spacing: 10
        Label:
            text: "User Name"
        TextInput:
            id: username
        Label:
            text: "Password"
        TextInput:
            id: password
            password: True


"""

class MyBL(BoxLayout):
    data_label = StringProperty("Приветствую!")
    # в переменных окружения формируем всё окружение
    placeholder = "Введите текст:\n"
    text_secondary_color = (0, 0, 0, 0.5)
    text_primary_color = (0, 0, 0, 1)
    button1_text = "поиск по названию 1"
    button2_text = "поиск по названию 2"
    button3_text = "поиск по названию 3"
    button4_text = "поиск по названию 4"

    def label_change(self, new_text):
        self.data_label = new_text

    def callback_txt_input_data(self, text):
        self.ids.txt_input_data.text = text

    def callback(self):
        print("poisk")


class MyApp(MDApp):
    running = True

    def build(self):
        return Builder.load_string(KV)

    def on_stop(self):
        self_running = False


MyApp().run()
