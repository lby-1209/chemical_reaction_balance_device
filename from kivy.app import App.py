from kivy.app import App
from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('main')

class MainScreen(Screen):
    pass

class HelloApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name = 'main'))
        return sm

if __name__ == '__main__':
    HelloApp().run()