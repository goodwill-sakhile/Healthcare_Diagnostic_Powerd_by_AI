from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
root = Builder.load_string("""
<HomeScreen>:
    name:"home_screen"
    MDBoxLayout:
        orientation:"vertical"
        spacing:5
        MDBoxLayout:
            size_hint_y:None
            height:"50dp"
        MDBoxLayout:
            spacing:5
            Widget:
            MDBoxLayout:
                radius:10, 10, 10, 10
                size_hint_x:None
                width:"300dp"
                md_bg_color:0, 0, 0, 1
                MDIconButton:
                    icon:"home"
                    icon_size:"100dp"
                    size_hint:None, None
                    size:"100dp", "100dp"
                    theme_icon_color:"Custom"
                    icon_color:1, 255/float(255), 255/float(255), 1
            MDBoxLayout:
                radius:10, 10, 10, 10
                size_hint_x:None
                width:"300dp"
                md_bg_color:0, 0, 0, 1
            Widget
        MDBoxLayout:
            spacing:5
            Widget:
            MDBoxLayout:
                radius:10, 10, 10, 10
                size_hint_x:None
                width:"300dp"
                md_bg_color:0, 0, 0, 1
            MDBoxLayout:
                radius:10, 10, 10, 10
                size_hint_x:None
                width:"300dp"
                md_bg_color:0, 0, 0, 1
            Widget:
        MDBoxLayout:
            size_hint_y:None
            height:"50dp"
""")
class HomeScreen(MDScreen):
    pass
