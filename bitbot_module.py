from microbit import *

ANALOG_MAX = 1023

# Converting values into a valid int between
# 0-1023 for valid analog signals
def to_analog(value):
    global ANALOG_MAX
    analog_val = value * ANALOG_MAX
    return analog_val

# Checking that the user has entered a valid
# speed before we can set the motors to that
# speed. Raises an error if invalid speed is entered
def check_speed(speed):
    if speed < 0 or speed > 1:
        raise ValueError('Invalid speed value for motors')
        
# Class for controlling Bit:bot motors    
class Motors:
    # accelerate() moves the Bit:bot forward at a speed
    # set by the user. The speed must be between 0 - 1
    def accelerate(self, speed):
        # Checking that the user has entered a valid
        # speed before we can set the motors to that
        # speed
        check_speed(speed)
        
        analog_val = to_analog(speed)
        pin0.write_analog(analog_val)
        pin1.write_analog(analog_val)
    
    # Halting to a complete stop
    def stop(self):
        pin0.write_digital(0)
        pin1.write_digital(0)
        
    # spin_left() spins the Bit:bot left at a certain speed
    def spin_left(self, speed):
        check_speed(speed)
        analog_val = to_analog(speed)
        
        pin0.write_analog(0)
        pin1.write_digital(analog_val)
        
    # spin_right() spins the Bit:bot right at a certain speed
    def spin_right(self, speed):
        check_speed(speed)
        analog_val = to_analog(speed)
        
        pin0.write_analog(analog_val)
        pin1.write_digital(0)