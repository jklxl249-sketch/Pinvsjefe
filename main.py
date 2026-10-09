from kivy.app import App
from kivy.uix.button import Button
class PinVsJefeApp(App):
    def build(self):
        return Button(text="PIN VS JEFE\nToca para ganar!", font_size=40)
PinVsJefeApp().run()
