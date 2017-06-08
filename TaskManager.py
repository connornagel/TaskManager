import kivy
from kivy.app import App
from kivy.uix.button import Label, Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.adapters.listadapter import ListAdapter

class TaskManager(App):
    def build(self):
        return ThisBoxlayout()

class ThisBoxlayout(BoxLayout):
    def build(self):
        return Button(text='First Button')


class Button(Button):
    pass


taskManager = TaskManager()

taskManager.run()


