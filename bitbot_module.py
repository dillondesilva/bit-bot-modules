from microbit import *

# Converting values into a valid int between
# 0-1023 for valid analog signals
def to_analog(value):
    analog_val = value * 1023
    return analog_val
    
class Motors:
    # accelerate() moves the bit:bot forward at a speed
    # set by the user. The speed must be between 0 - 1
    def accelerate(self, speed):
        # Checking that the user has entered a valid
        # speed before we can set the motors to that
        # speed
        if speed < 0 or speed > 1:
            raise ValueError('Invalid speed value for motors')
        
        analog_val = to_analog(speed)
        pin0.write_analog(analog_val)
        pin1.write_analog(analog_val)
    
    # Halting to a complete stop
    def stop(self):
        pin0.write_digital(0)
        pin1.write_digital(0)
        