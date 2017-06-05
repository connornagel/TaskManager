import kivy
from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.button import Button


class TaskManager(App):
    def build(self):
        return Button(text='Button1')


class Button(Button):
    pass


taskManager = TaskManager()

taskManager.run()
