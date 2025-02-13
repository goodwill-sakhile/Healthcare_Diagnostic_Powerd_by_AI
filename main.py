import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from home import HomeScreen
root = Builder.load_string("""
<MainBox>:
    md_bg_color:220/float(255), 220/float(255), 220/float(255), 1
    MDBoxLayout:
        size_hint_x:None
        width:"80dp"
        md_bg_color:47/float(255), 79/float(255), 79/float(255), 1
        orientation:"vertical"
        MDBoxLayout:
            size_hint_y:None
            height:"70dp"
            Widget:
            MDIconButton:
                size_hint:None, None
                size:"40dp", "40dp"
                icon:"home"
                theme_bg_color:"Custom"
                #md_bg_color:220/float(255), 220/float(255), 220/float(255), 1
                theme_icon_color:"Custom"
                icon_color:0, 230/float(255), 150/float(255), 1
            Widget:
        MDBoxLayout:
            size_hint_y:None
            height:"70dp"
            Widget:
            MDIconButton:
                size_hint:None, None
                size:"40dp", "40dp"
                icon:"comment-alert"
                theme_bg_color:"Custom"
                #md_bg_color:220/float(255), 220/float(255), 220/float(255), 1
                theme_icon_color:"Custom"
                icon_color:0, 230/float(255), 150/float(255), 1
            Widget:
        MDBoxLayout:
            size_hint_y:None
            height:"70dp"
            Widget:
            MDIconButton:
                size_hint:None, None
                size:"40dp", "40dp"
                icon:"information-slab-box"
                theme_bg_color:"Custom"
                #md_bg_color:220/float(255), 220/float(255), 220/float(255), 1
                theme_icon_color:"Custom"
                icon_color:0, 230/float(255), 150/float(255), 1
            Widget:
        MDBoxLayout:
            size_hint_y:None
            height:"70dp"
            Widget:
            MDIconButton:
                size_hint:None, None
                size:"40dp", "40dp"
                icon:"logout"
                theme_bg_color:"Custom"
                #md_bg_color:220/float(255), 220/float(255), 220/float(255), 1
                theme_icon_color:"Custom"
                icon_color:0, 230/float(255), 150/float(255), 1
            Widget:
        Widget:
    MDBoxLayout:
        ScreenManager:
            HomeScreen:
""")
class MainBox(MDBoxLayout):
    pass
class MainApp(MDApp):
    def build(self):
        root = MainBox()
        return root
if __name__ == "__main__":
    MainApp().run()
