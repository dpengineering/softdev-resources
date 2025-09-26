import os
os.environ['DISPLAY'] = ":0.0"
import pygame
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.clock import Clock
from kivy.config import Config
from pidev.MixPanel import MixPanel
from pidev.kivy.PassCodeScreen import PassCodeScreen
from pidev.kivy.PauseScreen import PauseScreen
from pidev.kivy.AdminScreen import AdminScreen
from pidev.kivy.DPEAButton import DPEAButton
from datetime import datetime
# Todo: uncomment when working on joystick: from joystick import JoystickScreen

time = datetime

MIXPANEL_TOKEN = "x"
MIXPANEL = MixPanel("Project Name", MIXPANEL_TOKEN)

SCREEN_MANAGER = ScreenManager()

# Todo: Add global variables for your different screens:
MAIN_SCREEN_NAME = 'main'

###### code from DPi_Stepper_Startup # Todo: Uncomment this AFTER you have completed the main screen and have connected it to the Raspberry Pi
#from dpeaDPi.DPiComputer import DPiComputer
#from dpeaDPi.DPiStepper import *
from time import sleep

##### Motor Setup:

# Stepper: # Todo: Uncomment these AFTER you have completed the main screen and have connected it to the Raspberry Pi
#dpiStepper = DPiStepper()
#dpiStepper.setBoardNumber(0)
#if not dpiStepper.initialize():
    #print("Communication with the DPiStepper board failed.")

# Servo: # Todo: Uncomment these AFTER you have completed the main screen and have connected it to the Raspberry Pi
#dpiComputer = DPiComputer()
#dpiComputer.initialize()

#####

class MotorButtonsGUI(App):
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

class MainScreen(Screen):
    """
    Class to handle the main screen and its associated touch events
    """
    # Global variables
    btn_x = 100
    btn_y = 100
    pressed_var = False # used in motor_pressed
    motor_scheduled = False # used in schedule_motor
    percent_100_speed = 10 # a max revolutions per second

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)

    servo_scheduled = False
    def schedule_servo_motor(self):
        pass # remove when function is created
        """
        This function should act like a switch to schedule the servo motor.
        Variables used/altered:
            self.servo_scheduled
            self.ids.servo_motor_script_button.text
        It results in a call being placed to check_switch_for_servo_motor
        Called by a Kivy button
        """
        #if """ Condition Statement """:
            #
            # Todo: Use the kivy clock to schedule self.check_switch_for_servo_motor on an interval of 0.05s:
            # Clock.schedule_interval(self.check_switch_for_servo_motor, 0.05)
            #
        #else:
            #
            # Todo: Unschedule self.check_switch_for_servo_motor:
            # Clock.unschedule(self.check_switch_for_servo_motor)
            #

    def check_switch_for_servo_motor(self, dt=0):
        pass  # remove when function is created
        """
        This function reads a switch and activates the servo motor bsed on that input.
        Variables used/altered:
            dpiComputer
        It results in the servo motor being to either 180° or 0°.
        Called by schedule_servo_motor
        """
        #if """ Condition reading the switch """:
            # Todo: Write the servo one direction
        #else:
            # Todo: Write the servo the other direction

    def spin_motor(self, dt = None):
        pass  # remove when function is created
        """
        This function spins the stepper motor at a constant speed that varies based on a slider
        Variables used/altered:
            self.ids.position.value
            self.motor_on
            dpiStepper
            self.set_motor_speed_by_revs_per_sec()
            percent_100_speed
            steps
        It results in the stepper motor spinning at a constant speed
        """
        # Some default values
        microstepping = 8
        wait_to_finish_moving_flg = False # allows the motor to spin continuously
        stepper_num = 0 # the stepper that you would like to control
        steps = 320000 # steps control how smooth the motor spins

        # Todo: Get the value (-100 to 100) from a slider named "position"
        #
        # Todo: Check if the slider is zero or if the button controlling to motor is off
        #if """ Condition to check whether motor isn't, or shouldn't be, running """ :
            # Todo: If so, decelerate, stop, and disable
            #return
        # Todo: if motor was disabled from being at zero or off, enable the motor
        #elif """ Motor was disabled """:
            # Todo: Enable motor
        self.set_motor_speed_by_revs_per_sec((abs(""" Replace with Slider Value """) / self.percent_100_speed), stepper_num) # calculates and set what the speed should be in according to the slider value
        #
        # Todo: Add a check for if the number is negative, and if so make it positive
        #
        # Todo: Activate the Stepper

    def motor_script(self):
        pass  # remove when function is created
        """
        This function should do the following:
            1. Print the value of get_position_in_units to a label on the kivy screen
               15 turns revolutions clockwise at 1 revolution / sec.
            2. Then prints the value of get_position_in_units to a label on the kivy screen
            3. Stops 10 seconds then turns clockwise for 10 revolutions at 5 rev / sec.
            4. Then prints the value of get_position_in_units to a label on the kivy screen
            5. Stops for 8 seconds.
            6. Then goes home and stops for 30 seconds.
            7. Then prints the value of get_position_in_units to a label on the kivy screen
            8. Then turns counterclockwise for 100 revolutions at 8 rev / sec.
            9. Then prints the value of get_position_in_units to a label on the kivy screen
            10. Then stops for 10 seconds and then goes home and then prints the value of get_position_in_units to a label on the kivy screen
        Called by the motor_script_button
        """

    def set_motor_speed_by_revs_per_sec(self, revs_per_sec, stepper_num=0):
        pass  # remove when function is created
        """ This is a helper function that sets the speed of a stepper motor by a specified revolutions per second"""
        microstepping = 8
        speed_steps_per_second = (200 * microstepping) * revs_per_sec
        accel_steps_per_second_per_second = speed_steps_per_second
        dpiStepper.setSpeedInStepsPerSecond(stepper_num, speed_steps_per_second)
        dpiStepper.setAccelerationInStepsPerSecondPerSecond(stepper_num, accel_steps_per_second_per_second)

    def counter_pressed(self):
        pass  # remove when function is created
        """
        This function increases the displayed count for the counter button by one
        Variables used/altered:
            self.ids.counter_button.text
        Called by counter_button
        """
        #

    def motor_pressed(self, dt=0):
        pass  # remove when function is created
        """
        This function should act like a switch to activate the stepper motor.
        Variables used/altered:
            self.pressed_var
            self.ids.power_button.color & .text
        It results in a call being placed to check_switch_for_servo_motor
        Called by a Kivy button
        """
        #
        if """ Condition to check if the motor should be turned on/off """:
            #
            #
            self.schedule_motor(True)
        else:
            #
            #
            self.schedule_motor(False)

    def schedule_motor(self, motor_on=False):
        pass  # remove when function is created
        """
        This function should use the kivy clock to schedule the stepper motor on.
        Variables used/altered:
            self.motor_scheduled
            self.motor_on
            dpiStepper
        It results in a call being placed to check_switch_for_servo_motor
        Called by a Kivy button
        """
        #
        #if """ Condition to check if the motor is not scheduled already and should be turned on """:
            #
            # Todo: Use the kivy clock to schedule self.spin_motor on an interval of 0.001s
        #elif """ Condition to check if the motor is scheduled and should be turned off """:
            #
            #
            #
            # Todo: unschedule self.spin_motor

    def switch_screen(self):
        pass  # remove when function is created
        # Switch screens to Joystick Screen

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

# These statements are required when adding a new screen:
# (at top of file) add a global variable for the new name of your screen: NEW_SCREEN_NAME = 'new'
# Builder.load_file('new.kv')
# SCREEN_MANAGER.add_widget(MainScreen(name=NEW_SCREEN_NAME))
# The 'new' from 'new.kv' should match what is in NEW_SCREEN_NAME

Builder.load_file('main.kv')
SCREEN_MANAGER.add_widget(MainScreen(name=MAIN_SCREEN_NAME))
# Todo: when working on joystick, make sure to add the widget of JoystickScreen with a name of JOYSTICK_SCREEN_NAME to the SCREEN_MANAGER
SCREEN_MANAGER.add_widget(PassCodeScreen(name='passCode'))
SCREEN_MANAGER.add_widget(AdminScreen(name='admin'))
SCREEN_MANAGER.add_widget(PauseScreen(name='pauseScene'))
PassCodeScreen.set_admin_events_screen('admin')
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
    # Makes the window auto full screen
    Config.set('graphics', 'fullscreen', 'auto')
    Config.set('graphics', 'window_state', 'maximized')
    Config.write()
    MotorButtonsGUI().run()

