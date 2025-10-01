from kivy.animation import Animation
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.clock import Clock

from pidev.kivy.ImageButton import ImageButton
from pidev.Joystick import Joystick

import pygame

try:
    joy = Joystick(0, False)
except pygame.error as e:
    print("No joystick connected, please connect and try again.")


class JoystickScreen(Screen):
    def on_enter(self):
        # TODO: Schedule joy_update to run every 0.05 seconds
        print("Call to on_enter from JoystickScreen")

    def on_leave(self):
        # TODO: Unschedule joy_update so it stops running
        print("Call to on_leave from JoystickScreen")

    def joy_update(self, dt=None):
        # TODO: Find the Joystick source code in your pidev folder or below
        #  Joystick source code: https://github.com/dpengineering/RaspberryPiCommon/blob/master/pidev/Joystick.py
        # TODO: Get joystick x and y values
        # TODO: Update x and y labels with joystick values
        # TODO: Move ImageButton based on joystick input
        # TODO: Call update_buttons_clicked()
        print("Call to joy_update from JoystickScreen")

    def update_buttons_clicked(self):
        # TODO: Find which buttons are pressed (0–9)
        # TODO: Update corresponding label
        #       (show pressed numbers or 'No Buttons Pressed')

        print("Call to check_buttons_clicked from JoystickScreen")

    def switch_screen_main(self):
        # TODO: Animate the ImageButton before switching back to main screen
        print("Call to switch_screen_main from JoystickScreen")
