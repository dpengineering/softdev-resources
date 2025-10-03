import os

from kivy.animation import Animation
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from pidev.MixPanel import MixPanel
from pidev.kivy.PassCodeScreen import PassCodeScreen
from pidev.kivy.PauseScreen import PauseScreen
from pidev.kivy.AdminScreen import AdminScreen
from pidev.kivy import DPEAButton
from datetime import datetime

time = datetime

MIXPANEL_TOKEN = "x"
MIXPANEL = MixPanel("Project Name", MIXPANEL_TOKEN)

SCREEN_MANAGER = ScreenManager()

PassCodeScreen.set_admin_events_screen('admin') # Required when using the Admin & Passcode Screens

Window.fullscreen = 'auto'

class ButtonExamplesGUI(App):
    """
    Class to handle running the GUI Application
    """

    def build(self):
        """
        Build the application
        :return: Kivy Screen Manager instance
        """
        return SCREEN_MANAGER


Window.clearcolor = (1, 1, 1, 1)  # White


class ButtonExamplesScreen(Screen):
    """
    Class to handle the ButtonExamples screen and its associated touch events
    """

    def pressed(self):
        """
        Function called on button touch event for button examples
        :return: None
        """
        print("Callback from ButtonExamples.pressed()")

    on_left = True  # button_9 starts on the left
    def button_9_action(self):
        """
        Function called on button with id: button_9
        """
        if self.on_left:
            anim = Animation(x=750, duration=1)
            self.on_left = False
        else:
            anim = Animation(x=25, duration=1)
            self.on_left = True
        anim.start(self.ids.button_9)

    visible = True  # button_10 starts visible
    def button_10_action(self):
        """
        Function called on button with id: button_10
        """
        if self.visible:
            anim = Animation(opacity=0, duration=0.25, t="in_bounce")
            self.visible = False
        else:
            anim = Animation(opacity=100, duration=0.25)
            self.visible = True
        anim.start(self.ids.button_10)


    def admin_action(self):
        """
        Hidden admin button touch event. Transitions to passCodeScreen.
        This method is called from pidev/kivy/PassCodeScreen.kv
        :return: None
        """
        SCREEN_MANAGER.current = 'passCode'

"""
Widget additions
"""

Builder.load_file('button_examples.kv')
SCREEN_MANAGER.add_widget(ButtonExamplesScreen(name='button_examples'))
SCREEN_MANAGER.add_widget(PassCodeScreen(name='passCode'))
SCREEN_MANAGER.add_widget(PauseScreen(name='pauseScene'))
SCREEN_MANAGER.add_widget(AdminScreen(name='admin'))

"""
MixPanel
"""


def send_event(event_name):
    """
    Send an event to MixPanel without properties
    :param event_name: Name of the event
    :return: None
    """
    global MIXPANEL

    MIXPANEL.set_event_name(event_name)
    MIXPANEL.send_event()


if __name__ == "__main__":
    ButtonExamplesGUI().run()
