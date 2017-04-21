#!/usr/bin/env bash

# Tue Nov 8 10:25:04 EET 2016, Nikos Koukis
# Current configuration file was used during the multi-robot real-time testing for the Pioneer2DX agent
#
# Source this file on both the ubuntu machine and youbot
#########################################################

export MR_USE_MULTIMASTER=1
export MR_IS_MULTIROBOT_GRAPHSLAM=1
export MR_DISABLE_MRPT_VISUALS=0

export MR_ORIGIN_MARKER_ID="mf7"
export MR_ROBOT_MARKER_ID="mf1"
export MR_USE_ODD_ARUCO_MARKERS_FOR_GT=1

export MR_ROBOT_NS="$(hostname)"
export MR_RECORD_TOPICS=0
export MR_ROBOT_DRIVERS_NAME="aria"
export MR_OUTPUT_MESSAGES_TO="screen"
export MR_USE_LASER=1
export MR_LASER_NAME="hokuyo"

# [!] WARNING
# urg_node doesn't seem to work properly with the hokuyo laser scanners available in the Control Systems lab
# It is *strongly* advised to set this to 0
export MR_LASER_USE_URG_NODE_PKG=0 # Use the urg_node ROS pkg instead of the hokuyo_node
# Option only available with the urg_node laserScans package - ignored otherwise
export MR_LASER_SKIP_NUM_MESSAGES="1"

export MR_LASER_PORT="/dev/ttyACM0"
export MR_DRIVERS_PORT="/dev/ttyUSB0"

export MR_USE_ONBOARD_CAMERA=0
export MR_ONBOARD_CAMERA_PORT="dev/video0"

export MR_USE_JOYSTICK=1
export MR_JOYSTICK_PORT="/dev/input/js0"
export MR_JOYSTICK_CONFIG_FNAME="non-holonomic"
export MR_JOYSTICK_FOR="generic"

export MR_COMPUTE_GROUND_TRUTH=0
