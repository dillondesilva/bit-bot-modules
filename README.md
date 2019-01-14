# Bit:bot Module
## An easy to use module to interact with Bit:bot and bootstrap projects

### Why use Bit:bot Module?
Using this module allows you to quickly bootstrap projects and save you the trouble of writing functions to perform simple tasks
on Bit:bot

### Installation

For now, clone this repository and then import it as you would for any other python project. Hopefully, it'll be available for installation
on pip soon

### Usage

#### Motors()

To initialise motors, do
```
motors = Motors()
```

To accelerate motors forwards, call accelerate(speed)
- accelerate(speed) takes one argument, speed, which is a value between 0 and 1 controlling how fast you want the motors to be (0 is no speed and 1 is full speed)
```
# Accelerate motors at half speed
motors.accelerate(0.5)
```

To reverse motors, call reverse(speed)
- reverse(speed) takes one argument, speed, which is a value between 0 and 1 controlling how fast you want the motors to be (0 is no speed and 1 is full speed)
```
# Reverse motors at full speed
motors.reverse(1)
```

To spin left on axis, call spin_left(speed)
```
# Spin left at 30% speed
motors.spin_left(0.3)
```

To spin right on axis, call spin_right(speed)
```
# Spin right at 70% speed
motors.spin_right(0.7)
```
