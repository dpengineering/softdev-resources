# Todo: Uncomment this AFTER completing the main screen and connecting to a Raspberry Pi
# from kivy.uix.screenmanager import Screen
# from pidev.Joystick import Joystick
# import pygame
#
# try:
#     joy = Joystick(0, False)
# except pygame.error as e:
#     print("No joystick connected, please connect and try again.")
#     exit(1)
#
# JOYSTICK_SCREEN_NAME  = "joystick"
# MAIN_SCREEN_NAME = "main"
#
# # Todo: Add the joystick screen here
# # Todo: Load the joystick.kv file here
#
# # Todo: Do this AFTER completing the main screen and connecting to a Raspberry Pi
# class JoystickScreen(Screen):
#     # these are variables to keep the size consistent across different buttons
#     btn_x = 100
#     btn_y = 100
#
#     def __init__(self, **kwargs):
#         # this line useful if we want to add attributes but still keep all Screen attributes
#         super(JoystickScreen, self).__init__(**kwargs)
#         # you can make x and y values be instance attributes like this, so they are accessible anywhere in the program
#         self.x_val = 0
#         self.y_val = 0
#         # Todo: Use the kivy clock to schedule joy_update to run every .1 seconds
#
#     def joy_update(self, dt=None):
#         pass # remove when function is created
#         """
#         This function is scheduled to run on an interval to update information about the joystick and display it to the screen
#         Variables used/altered:
#             self.x_val
#             self.y_val
#             self.ids.x.text
#             self.ids.y.text
#         """
#         # dt for clock scheduling
#         self.check_buttons_clicked()
#         if SCREEN_MANAGER.current == JOYSTICK_SCREEN_NAME:  # Only update if active screen is joystick screen
#             self.x_val, self.y_val = joy.get_both_axes()
#             # Todo: update kivy labels to reflect the current x/y movement of the joystick
#
#     def check_buttons_clicked(self):
#         pass # remove when function is created
#         """
#         This function is ran on an interval and constantly checks if any buttons on the joystick are being pressed
#         Variables used/altered:
#             self.buttons_pressed
#             self.ids.buttons_pressed_text.text
#         It results in a label being updated on the joystick screen to display which buttons are being pressed
#         Called by joy_update
#         """
#         self.buttons_pressed = ""
#         for num in range(10):
#             pass # remove when function is created
#             # Todo: check to see if each buttons has been pressed
#             # Todo: If so, add their number to a string
#         # Todo: Use the newly created string to update the buttons_pressed kivy label
#
#     @staticmethod
#     def switch_screen_main(self):
#         # Todo: switch to main screen
#         self.parent.current =