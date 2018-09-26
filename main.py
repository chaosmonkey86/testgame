import kivy
kivy.require('1.0.9')
from kivy.lang import Builder
from kivy.uix.gridLayout import GridLayout
from kivy.properties import NumericProperty
from kivy.app import App

class HomeScreen(GridLayout):
    pass

class MainApp(App):
    def build(self):
        return HomeScreen()

if __name__ == '__main__':
    MainApp().run()
