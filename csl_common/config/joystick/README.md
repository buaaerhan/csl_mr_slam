Tue Nov 8 10:56:22 EET 2016, Nikos Koukis

Files of this directory configure the *teleop_twist_joy* node to be used with
different robot types and  for different overall configuration (max speed, axes
for rotating, moving the robot forward etc.).

Files may be used either in simulations (e.g. for controlling a robot in
Gazebo) or for real-time experiments, i.e. controlling the actual robot

NOTES:

- You should always have the enable_button pressed ("X" is commonly used) if
    you are to move the robot.

- Joystick: Logitech Wireless Gamepad F710
  + Have Mode "off"
  + Joystick is not identified by the odroid-XU3 - Use a wired joystick instead
