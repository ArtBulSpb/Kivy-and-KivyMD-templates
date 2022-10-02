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
from kivymd.uix.label import MDLabel

# В переменной KV создаём вёрстку
KV = """
MyBL:
        orientation: "vertical"
        size_hint: (0.98, 0.98)
        pos_hint: {"center_x": 0.5, "center_y":0.5}
        padding: 10
        spacing: 10
        
        BoxLayout:
                orientation: "horizontal"
                pos_hint: {"center_x": 0.5, "center_y":0.5}
                MDTextField:
                        id: text_field_md
                        theme_text_color: "Custom"
                        text_color: root.text_primary_color 
                        hint_text: root.placeholder
                        size_hint_x:None
                        width: 400
                        #pos_hint: {"center_x": 0.5, "center_y": 0.5}
                        color: root.text_primary_color 
                        cursor_color: root.text_secondary_color
                        height: "60dp"
                        font_family: 'Roboto'
                        # font_size: '20sp'
                        mode: "round"
                        max_text_length: 100
                        helper_text: root.placeholder
                        on_focus: 
                                self.hint_text = "" if self.hint_text==root.placeholder else self.hint_text #Очищаем поле ввода если в него переведён фокус
                                text_color_focus: root.text_primary_color                        
                        #on_text: root.label_change(self.text) #Передаём введенные данные в Label обуквенно
                        on_text_validate: 
                                text_holder = self.hint_text #Для понимания синтаксиса работы нескольких функций по событию.Их нужно располагать одну под другой 
                                root.label_change(self.text) #Передаём введенные данные в Label после нажатия Enter 
                        foreground_color: root.text_secondary_color if self.text==root.placeholder else root.text_primary_color
                        
                MDFillRoundFlatButton:
                        text:"X"
                        line_color: 0, 0, 0, 0.3
                        md_bg_color : 153/255, 50/255, 204/255, 1
                        #pos_hint: {"center_x": .95, "center_y": .5} #Параметры в {} определяют центр кнопки
                        on_press: 
                                root.callback_txt_input_data("")
                                                                

        # TextInput:
        #         id: txt_input_data
        #         text:root.placeholder 
        #         multiline: False
        #         cursor_color: root.text_secondary_color
        #         font_family: 'Roboto'
        #         font_size: '20sp'
        #         size_hint: 1, None
        #         #height: '100dp'
        #         on_focus: self.text = "" if self.text==root.placeholder else self.text #Очищаем поле ввода если в него переведён фокус                        
        #         #on_text: root.label_change(self.text) #Передаём введенные данные в Label обуквенно
        #         on_text_validate: 
        #                 text_holder = self.text #Для понимания синтаксиса работы нескольких функций по событию.Их нужно располагать одну под другой 
        #                 root.label_change(self.text) #Передаём введенные данные в Label после нажатия Enter 
        #         #width: 300
        #         foreground_color: root.text_secondary_color if self.text==root.placeholder else root.text_primary_color
        #         #background_normal: './assets/imgs/transparent.png'
        #         #background_active: './assets/imgs/transparent.png'    
    
        MDLabel: #вывод
                font_size:"30sp"
                #theme_text_color: [root.text_primary_color, root.text_secondary_color, '#9932CC', '#9932CC', '#9932CC', '#9932CC']
                theme_text_color: "Secondary" #"Primary"#, "Secondary", "Hint", "Error", "ContrastParentBackground"]
                text_color: root.text_primary_color
                text:root.data_label
                halign: "center"
                
        MDFillRoundFlatButton:
                text: root.button1_text
                line_color: 0, 0, 0, 0.3
                md_bg_color : 153/255, 50/255, 204/255, 1
                pos_hint: {"center_x": .5, "center_y": .5} #Параметры в {} определяют центр кнопки
                #size_hint: (1,0.5)
                on_press: 
                        self.md_bg_color = '#9932CC'
                        root.label_change(self.text)
                        root.callback_txt_input_data(self.text)
                
        MDFillRoundFlatButton:
                text: root.button2_text
                line_color: 0, 0, 0, 0.3
                md_bg_color : 153/255, 50/255, 204/255, 1
                pos_hint: {"center_x": .5, "center_y": .5} #Параметры в {} определяют центр кнопки
                #size_hint: (1,0.5)
                on_press: 
                        self.md_bg_color = '#9932CC'
                        root.label_change(self.text)
                        root.callback_txt_input_data(self.text)
                
        MDFillRoundFlatButton:
                text: root.button3_text
                line_color: 0, 0, 0, 0.3
                md_bg_color : 153/255, 50/255, 204/255, 1
                pos_hint: {"center_x": .5, "center_y": .5} #Параметры в {} определяют центр кнопки
                #size_hint: (1,0.5)
                on_press: 
                        self.md_bg_color = '#9932CC'
                        root.label_change(self.text)
                        root.callback_txt_input_data(self.text)
        
        MDFillRoundFlatButton:
                text: root.button5_text
                line_color: 0, 0, 0, 0.3
                md_bg_color : 153/255, 50/255, 204/255, 1
                pos_hint: {"center_x": .5, "center_y": .5} #Параметры в {} определяют центр кнопки
                #size_hint: (1,0.5)
                on_press: 
                        self.md_bg_color = '#9932CC'
                        root.label_change(self.text)
                        root.callback_txt_input_data(self.text)
                #radius: [10.1] #Не работает скругление кнопки. Нужно делать кастомное.
                # border: 30,30,30,30
        
        MDFillRoundFlatButton:
                text: root.button6_text
                #icon: "language-python"
                line_color: 0, 0, 0, 0.3
                pos_hint: {"center_x": .5, "center_y": .5} #Параметры в {} определяют центр кнопки
                on_press: 
                        self.md_bg_color = '#9932CC'
                        root.label_change(self.text)
                        root.callback_txt_input_data(self.text)
                        
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
    placeholder = "Введите текст для поиска здесь:\n"
    text_secondary_color = (0, 0, 0, 0.5)
    text_primary_color = (0, 0, 0, 1)
    button1_text = "поиск по названию 1"
    button2_text = "поиск по названию 2"
    button3_text = "поиск по названию 3"
    button4_text = "поиск по названию 4"
    button5_text = "поиск по названию 5"
    button6_text = "поиск по названию 6"

    def label_change(self, new_text):
        self.data_label = new_text

    def callback_txt_input_data(self, text):
        # self.ids.txt_input_data.text = text
        self.ids.text_field_md.text = text

    def callback(self):
        print("poisk")

    def clear(self):
        self.ids.text_field_md.helper_text = ""


class MyApp(MDApp):
    running = True

    def build(self):
        return Builder.load_string(KV)

    def on_stop(self):
        self_running = False


MyApp().run()
