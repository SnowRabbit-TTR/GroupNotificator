import os
os.environ["KIVY_AUDIO"] = "sdl2"

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox

from kivy.properties import StringProperty, ListProperty
from kivy.config import Config
from kivy.lang import Builder
from kivy.resources import resource_add_path

from kivy.core.audio import SoundLoader
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.clock import Clock

from observer import Observer

Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'resizable', False)

resource_add_path('./fonts')
LabelBase.register(DEFAULT_FONT, 'ImpressBT.ttf')
sound = SoundLoader.load('./sound/chime.wav')


kv = """
<MainPanel>:

    BoxLayout:
        orientation: "vertical"
        size: root.size
        color: 0,1,0,1
        

        BoxLayout:  # explain info
            size_hint_y: 0.1
            orientation: "horizontal"
            canvas.before:
                Color:
                    rgba: 0.1, 0.1, 0.1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size
                Color:
                    rgba: 1, 1, 1, 1
                Line:
                    rectangle: self.x,self.y,self.width,self.height
            Label:
                size_hint_x: 1/17
            Label:
                size_hint_x: 3.5/17
                font_size: 18
                text: "Group"
            Label:
                size_hint_x: 2.5/17
                font_size: 18
                text: "District"
            Label:
                size_hint_x: 2/17
                font_size: 18
                text: "Toons"
            Label:
                size_hint_x: 3/17
                font_size: 18
                text: "Last Activity"
            Label:
                size_hint_x: 4/17
                font_size: 18
                text: "Owner"
        
        
        ScrollView:  # Group Info
            BoxLayout:
                orientation: "vertical"
                size_hont_y: 0.5
                canvas.before:
                    Color:
                        rgba: 0.2, 0.2, 0.2, 1
                    Rectangle:
                        pos: self.pos
                        size: self.size

                BoxLayout:  # 1st Group
                    orientation: "horizontal"
                    canvas.after:
                        Color:
                            rgba: 1, 1, 1, 1
                        Line:
                            rectangle: self.x,self.y,self.width,self.height
                    Image:
                        size_hint_x: 1/17
                        source: root.lamp_list[0]
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 3.5/17
                        font_size: root.info_font_size
                        text: root.group_list[0].group_name
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 2.5/17
                        font_size: root.info_font_size
                        text: root.group_list[0].district
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 2/17
                        font_size: root.info_font_size
                        text: root.group_list[0].people
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 3/17
                        font_size: root.info_font_size
                        text: root.group_list[0].last_activity
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 4/17
                        font_size: root.info_font_size
                        text: root.group_list[0].owner
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height

                BoxLayout:  # 2nd Group
                    orientation: "horizontal"
                    canvas.after:
                        Color:
                            rgba: 1, 1, 1, 1
                        Line:
                            rectangle: self.x,self.y,self.width,self.height
                    Image:
                        size_hint_x: 1/17
                        source: root.lamp_list[1]
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 3.5/17
                        font_size: root.info_font_size
                        text: root.group_list[1].group_name
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 2.5/17
                        font_size: root.info_font_size
                        text: root.group_list[1].district
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 2/17
                        font_size: root.info_font_size
                        text: root.group_list[1].people
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 3/17
                        font_size: root.info_font_size
                        text: root.group_list[1].last_activity
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 4/17
                        font_size: root.info_font_size
                        text: root.group_list[1].owner
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                
                BoxLayout:  # 3rd Group
                    orientation: "horizontal"
                    canvas.after:
                        Color:
                            rgba: 1, 1, 1, 1
                        Line:
                            rectangle: self.x,self.y,self.width,self.height
                    Image:
                        size_hint_x: 1/17
                        source: root.lamp_list[2]
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 3.5/17
                        font_size: root.info_font_size
                        text: root.group_list[2].group_name
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 2.5/17
                        font_size: root.info_font_size
                        text: root.group_list[2].district
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 2/17
                        font_size: root.info_font_size
                        text: root.group_list[2].people
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 3/17
                        font_size: root.info_font_size
                        text: root.group_list[2].last_activity
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 4/17
                        font_size: root.info_font_size
                        text: root.group_list[2].owner
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                
                BoxLayout:  # 4th Group
                    orientation: "horizontal"
                    canvas.after:
                        Color:
                            rgba: 1, 1, 1, 1
                        Line:
                            rectangle: self.x,self.y,self.width,self.height
                    Image:
                        size_hint_x: 1/17
                        source: root.lamp_list[3]
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 3.5/17
                        font_size: root.info_font_size
                        text: root.group_list[3].group_name
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 2.5/17
                        font_size: root.info_font_size
                        text: root.group_list[3].district
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 2/17
                        font_size: root.info_font_size
                        text: root.group_list[3].people
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 3/17
                        font_size: root.info_font_size
                        text: root.group_list[3].last_activity
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 4/17
                        font_size: root.info_font_size
                        text: root.group_list[3].owner
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                
                BoxLayout:  # 5th Group
                    orientation: "horizontal"
                    canvas.after:
                        Color:
                            rgba: 1, 1, 1, 1
                        Line:
                            rectangle: self.x,self.y,self.width,self.height
                    Image:
                        size_hint_x: 1/17
                        source: root.lamp_list[4]
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 3.5/17
                        font_size: root.info_font_size
                        text: root.group_list[4].group_name
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 2.5/17
                        font_size: root.info_font_size
                        text: root.group_list[4].district
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 2/17
                        font_size: root.info_font_size
                        text: root.group_list[4].people
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 3/17
                        font_size: root.info_font_size
                        text: root.group_list[4].last_activity
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 4/17
                        font_size: root.info_font_size
                        text: root.group_list[4].owner
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                
                BoxLayout:  # 6th Group
                    orientation: "horizontal"
                    canvas.after:
                        Color:
                            rgba: 1, 1, 1, 1
                        Line:
                            rectangle: self.x,self.y,self.width,self.height
                    Image:
                        size_hint_x: 1/17
                        source: root.lamp_list[5]
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 3.5/17
                        font_size: root.info_font_size
                        text: root.group_list[5].group_name
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 2.5/17
                        font_size: root.info_font_size
                        text: root.group_list[5].district
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 2/17
                        font_size: root.info_font_size
                        text: root.group_list[5].people
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 3/17
                        font_size: root.info_font_size
                        text: root.group_list[5].last_activity
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 4/17
                        font_size: root.info_font_size
                        text: root.group_list[5].owner
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                
                BoxLayout:  # 7th Group
                    orientation: "horizontal"
                    canvas.after:
                        Color:
                            rgba: 1, 1, 1, 1
                        Line:
                            rectangle: self.x,self.y,self.width,self.height
                    Image:
                        size_hint_x: 1/17
                        source: root.lamp_list[6]
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 3.5/17
                        font_size: root.info_font_size
                        text: root.group_list[6].group_name
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 2.5/17
                        font_size: root.info_font_size
                        text: root.group_list[6].district
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 2/17
                        font_size: root.info_font_size
                        text: root.group_list[6].people
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 3/17
                        font_size: root.info_font_size
                        text: root.group_list[6].last_activity
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 4/17
                        font_size: root.info_font_size
                        text: root.group_list[6].owner
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                
                BoxLayout:  # 8th Group
                    orientation: "horizontal"
                    canvas.after:
                        Color:
                            rgba: 1, 1, 1, 1
                        Line:
                            rectangle: self.x,self.y,self.width,self.height
                    Image:
                        size_hint_x: 1/17
                        source: root.lamp_list[7]
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 3.5/17
                        font_size: root.info_font_size
                        text: root.group_list[7].group_name
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 2.5/17
                        font_size: root.info_font_size
                        text: root.group_list[7].district
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 2/17
                        font_size: root.info_font_size
                        text: root.group_list[7].people
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 3/17
                        font_size: root.info_font_size
                        text: root.group_list[7].last_activity
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height
                    Label:
                        size_hint_x: 4/17
                        font_size: root.info_font_size
                        text: root.group_list[7].owner
                        canvas.before:
                            Color:
                                rgba: 0.15, 0.15, 0.15, 1
                            Line:
                                rectangle: self.x,self.y,self.width,self.height


        Label:
            size_hint_y: 0.1
            font_size: 18
            text: "Notifications"
            canvas.before:
                Color:
                    rgba: 0.1, 0.1, 0.1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size
                Color:
                    rgba: 1, 1, 1, 1
                Line:
                    rectangle: self.x,self.y,self.width,self.height
        
        
        GridLayout:  # Checkbox Panel
            size_hint_y: 0.3
            rows: 2
            cols: 5
            canvas.before:
                Color:
                    rgba: 0.2, 0.2, 0.2, 1
                Rectangle:
                    pos: self.pos
                    size: self.size
                Color:
                    rgba: 1, 1, 1, 1
                Line:
                    rectangle: self.x,self.y,self.width,self.height
            
            BoxLayout:
                orientation: "vertical"
                canvas.before:
                    Color:
                        rgba: 0.5, 0.5, 0.5, 1
                    Line:
                        rectangle: self.x,self.y,self.width,self.height
                Label:
                    text: "DA Office A"
                    font_size: root.checkbox_font_size
                CheckBox:
                    id: da_a
                    on_press: root.on_checkbox_press("da_a")
            
            BoxLayout:
                orientation: "vertical"
                canvas.before:
                    Color:
                        rgba: 0.5, 0.5, 0.5, 1
                    Line:
                        rectangle: self.x,self.y,self.width,self.height
                Label:
                    text: "DA Office B"
                    font_size: root.checkbox_font_size
                CheckBox:
                    id: da_b
                    on_press: root.on_checkbox_press("da_b")

            BoxLayout:
                orientation: "vertical"
                canvas.before:
                    Color:
                        rgba: 0.5, 0.5, 0.5, 1
                    Line:
                        rectangle: self.x,self.y,self.width,self.height
                Label:
                    text: "DA Office C"
                    font_size: root.checkbox_font_size
                CheckBox:
                    id: da_c
                    on_press: root.on_checkbox_press("da_c")

            BoxLayout:
                orientation: "vertical"
                canvas.before:
                    Color:
                        rgba: 0.5, 0.5, 0.5, 1
                    Line:
                        rectangle: self.x,self.y,self.width,self.height
                Label:
                    text: "DA Office D"
                    font_size: root.checkbox_font_size
                CheckBox:
                    id: da_d
                    on_press: root.on_checkbox_press("da_d")

            BoxLayout:
                orientation: "vertical"
                canvas.before:
                    Color:
                        rgba: 0.5, 0.5, 0.5, 1
                    Line:
                        rectangle: self.x,self.y,self.width,self.height
                Label:
                    text: "CJ"
                    font_size: root.checkbox_font_size
                CheckBox:
                    id: cj
                    on_press: root.on_checkbox_press("cj")

            BoxLayout:
                orientation: "vertical"
                canvas.before:
                    Color:
                        rgba: 0.5, 0.5, 0.5, 1
                    Line:
                        rectangle: self.x,self.y,self.width,self.height
                Label:
                    text: "Front 3 Golf Course"
                    font_size: root.checkbox_font_size
                CheckBox:
                    id: golf_front
                    on_press: root.on_checkbox_press("golf_front")

            BoxLayout:
                orientation: "vertical"
                canvas.before:
                    Color:
                        rgba: 0.5, 0.5, 0.5, 1
                    Line:
                        rectangle: self.x,self.y,self.width,self.height
                Label:
                    text: "Middle 6 Golf Course"
                    font_size: root.checkbox_font_size
                CheckBox:
                    id: golf_middle
                    on_press: root.on_checkbox_press("golf_middle")

            BoxLayout:
                orientation: "vertical"
                canvas.before:
                    Color:
                        rgba: 0.5, 0.5, 0.5, 1
                    Line:
                        rectangle: self.x,self.y,self.width,self.height
                Label:
                    text: "Back 9 Golf Course"
                    font_size: root.checkbox_font_size
                CheckBox:
                    id: golf_back
                    on_press: root.on_checkbox_press("golf_back")

            BoxLayout:
                orientation: "vertical"
                canvas.before:
                    Color:
                        rgba: 0.5, 0.5, 0.5, 1
                    Line:
                        rectangle: self.x,self.y,self.width,self.height
                Label:
                    text: "CEO"
                    font_size: root.checkbox_font_size
                CheckBox:
                    id: ceo
                    on_press: root.on_checkbox_press("ceo")

            BoxLayout:
                orientation: "vertical"
                canvas.before:
                    Color:
                        rgba: 0.5, 0.5, 0.5, 1
                    Line:
                        rectangle: self.x,self.y,self.width,self.height
                Label:
                    text: "SOS Shopping VP"
                    font_size: root.checkbox_font_size
                CheckBox:
                    id: shopping_vp
                    on_press: root.on_checkbox_press("shopping_vp")
"""
Builder.load_string(kv)


class MainPanel(Widget):

    show_num = Observer.show_num
    group_list = ListProperty([])
    created_group_id_list = ListProperty([])
    lamp_list = ListProperty([])
    blinker_lamp = StringProperty()

    max_notice_num = 4
    info_font_size = 20
    checkbox_font_size = 16


    def __init__(self, **kwargs):
        self.blinker = False
        self.ob = Observer()
        self.group_list = self.ob.get_observing_group_list()
        self.created_group_id_list = []
        self.lamp_list = [""] * self.show_num
        self.set_lamp_list()
        super(MainPanel, self).__init__(**kwargs)
        Clock.schedule_interval(self.observing, 15)
        Clock.schedule_interval(self.set_blinker, 0.5)


    def set_lamp_list(self):
        for i in range(len(self.group_list)):
            g = self.group_list[i]
            if g.group_type == 0:
                self.lamp_list[i] = "./image/empty.png"
            else:
                if g.isfull == True:
                    self.lamp_list[i] = "./image/full.png"
                elif g.group_id in self.created_group_id_list:
                    self.lamp_list[i] = self.blinker_lamp
                else:
                    self.lamp_list[i] = "./image/available.png"


    def observing(self, dt):
        try:
            self.ob.renew()
        except:
            pass
        self.group_list = self.ob.get_observing_group_list()
        created = self.ob.get_created_attention_group_dict()

        if len(created) != 0:
            sound.play()
        
        for key in created:
            if len(self.created_group_id_list) > self.max_notice_num:
                self.created_group_id_list.pop(0)
            self.created_group_id_list.append(key)
            

    def set_blinker(self, dt):
        self.blinker = not self.blinker
        if self.blinker:
            self.blinker_lamp = "./image/available.png"
        else:
            self.blinker_lamp = "./image/empty.png"
        self.set_lamp_list()


    def on_checkbox_press(self, group_kind):
        is_checked = False
        group_name = ""
        if group_kind == "da_a":
            group_name = "DA Office A"
            is_checked = self.ids.da_a.active
        elif group_kind == "da_b":
            group_name = "DA Office B"
            is_checked = self.ids.da_b.active
        elif group_kind == "da_c":
            group_name = "DA Office C"
            is_checked = self.ids.da_c.active
        elif group_kind == "da_d":
            group_name = "DA Office D"
            is_checked = self.ids.da_d.active
        elif group_kind == "cj":
            group_name = "CJ"
            is_checked = self.ids.cj.active
        elif group_kind == "golf_front":
            group_name = "Front 3 Golf Course"
            is_checked = self.ids.golf_front.active
        elif group_kind == "golf_middle":
            group_name = "Middle 6 Golf Course"
            is_checked = self.ids.golf_middle.active
        elif group_kind == "golf_back":
            group_name = "Back 9 Golf Course"
            is_checked = self.ids.golf_back.active
        elif group_kind == "ceo":
            group_name = "CEO"
            is_checked = self.ids.ceo.active
        elif group_kind == "shopping_vp":
            group_name = "SOS Shopping VP"
            is_checked = self.ids.shopping_vp.active
        
        if is_checked == True:
            self.ob.observing_groups.append(group_name)
        else:
            self.ob.observing_groups.remove(group_name)
    
        self.group_list = self.ob.get_observing_group_list()
        self.set_lamp_list()


class GroupnotificatorApp(App):
    
    def build(self):
        self.title = 'Group Notificator (Beta)'
        self.icon = './image/icon.ico'
        return MainPanel()


if __name__ == '__main__':
    GroupnotificatorApp().run()
