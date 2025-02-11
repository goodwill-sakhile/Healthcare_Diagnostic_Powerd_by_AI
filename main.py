from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
root = Builder.load_string("""
<MainBox>:
    md_bg_color:47/float(255), 79/float(255), 79/float(255), 1
""")
class MainBox(MDBoxLayout):
    pass
class MainApp(MDApp):
    def build(self):
        root = MainBox()
        return root
if __name__ == "__main__":
    MainApp().run()
